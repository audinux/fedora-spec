# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: kernel-audio-tuned
Version: 1.0
Release: 7%{?dist}
Summary: Audio tuned kernel boot entries for Fedora
BuildArch: noarch
License: GPLv3

Source0: 90-audio-tuned.install
Source1: kernel-audio-tuned.sysconfig
Source2: kernel-audio-tuned-grub.cfg

%description
Creates additional kernel boot entries with low-latency tuning
parameters (preempt, IRQ threading, etc.) using kernel-install hooks.

%install

install -m 0755 -d %{buildroot}%{_prefix}/lib/kernel/install.d
install -m 0755 -d %{buildroot}%{_sysconfdir}/sysconfig
install -m 0755 -d %{buildroot}%{_sysconfdir}/default/grub.d

install -m 0755 %{SOURCE0} %{buildroot}%{_prefix}/lib/kernel/install.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/kernel-audio-tuned
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/grub.d/50-kernel-audio-tuned.cfg

%post
# Pre-delete stale audio entries so upgrades regenerate with current options
for entry in /boot/loader/entries/*-audio.conf; do
    rm -f "$entry" || :
done
for k in /lib/modules/*; do
    version=$(basename "$k")
    if [ -f "/boot/vmlinuz-$version" ]; then
        /usr/bin/kernel-install add "$version" "/boot/vmlinuz-$version" || :
    fi
done
# Apply the GRUB timeout drop-in
if [ -f /boot/efi/EFI/fedora/grub.cfg ]; then
    grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg 2>/dev/null || :
elif [ -f /boot/grub2/grub.cfg ]; then
    grub2-mkconfig -o /boot/grub2/grub.cfg 2>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    for entry in /boot/loader/entries/*-audio.conf; do
        rm -f "$entry" || :
    done
    # Remove the GRUB timeout drop-in and restore the previous timeout
    if [ -f /boot/efi/EFI/fedora/grub.cfg ]; then
        grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg 2>/dev/null || :
    elif [ -f /boot/grub2/grub.cfg ]; then
        grub2-mkconfig -o /boot/grub2/grub.cfg 2>/dev/null || :
    fi
fi

%files
%{_prefix}/lib/kernel/install.d/90-audio-tuned.install
%config(noreplace) %{_sysconfdir}/sysconfig/kernel-audio-tuned
%config(noreplace) %{_sysconfdir}/default/grub.d/50-kernel-audio-tuned.cfg

%changelog
* Mon Aug 17 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-7
- install /etc/default/grub.d/50-kernel-audio-tuned.cfg to force a 4-second
  GRUB menu timeout (GRUB_TIMEOUT=4, GRUB_TIMEOUT_STYLE=menu) so the
  audio-tuned entry is selectable at boot; grub2-mkconfig is run in %%post
  (install/upgrade) and %%preun (full removal) to apply/restore the change

* Sat Jun 27 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-6
- 90-audio-tuned.install: skip non-standard kernel flavors (RT, LQX, Xanmod)
  by checking KERNEL_VERSION against KERNEL_AUDIO_TUNED_SKIP_FLAVORS before
  creating audio entries; defaults cover kernel-rt-mao (.rt), kernel-lqx-mao
  (lqx), and kernel-xan-mao (xan); set to "" in sysconfig to include all
- sysconfig: document and default KERNEL_AUDIO_TUNED_SKIP_FLAVORS

* Thu Jun 25 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-5
- 90-audio-tuned.install: fix sed delimiters (/ → |) so options containing
  slashes are handled correctly; move CPU detection into add) branch only;
  fix cleanup_entries to use printf instead of ls; wrap source sysconfig
  with || true so a syntax error cannot abort the hook
- spec: pre-delete *-audio.conf in %%post before regenerating so package
  upgrades with changed options actually update the boot entries; use
  %%{_prefix} and %%{_sysconfdir} macros in %%install and %%files
- sysconfig: add security note for nopti

* Sun May 10 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-4
- update to 1.0-4 - avoid some errors when there are no kernels to manage

* Tue May 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-3
- update to 1.0-3 - limit the number of audio tuned entries to installonly_limit

* Mon Mar 30 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2 - add %post and %preun section

* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- initial version of the spec
