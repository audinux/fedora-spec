# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: kernel-audio-tuned
Version: 1.0
Release: 5%{?dist}
Summary: Audio tuned kernel boot entries for Fedora
BuildArch: noarch
License: GPLv3

Source0: 90-audio-tuned.install
Source1: kernel-audio-tuned.sysconfig

%description
Creates additional kernel boot entries with low-latency tuning
parameters (preempt, IRQ threading, etc.) using kernel-install hooks.

%install

install -m 0755 -d %{buildroot}%{_prefix}/lib/kernel/install.d
install -m 0755 -d %{buildroot}%{_sysconfdir}/sysconfig

install -m 0755 %{SOURCE0} %{buildroot}%{_prefix}/lib/kernel/install.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/kernel-audio-tuned

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

%preun
if [ $1 -eq 0 ]; then
    for entry in /boot/loader/entries/*-audio.conf; do
        rm -f "$entry" || :
    done
fi

%files
%{_prefix}/lib/kernel/install.d/90-audio-tuned.install
%config(noreplace) %{_sysconfdir}/sysconfig/kernel-audio-tuned

%changelog
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
