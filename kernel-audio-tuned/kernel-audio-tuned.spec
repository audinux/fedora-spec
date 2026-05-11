Name: kernel-audio-tuned
Version: 1.0
Release: 4%{?dist}
Summary: Audio tuned kernel boot entries for Fedora
BuildArch: noarch
License: GPLv3

Source0: 90-audio-tuned.install
Source1: kernel-audio-tuned.sysconfig

%description
Creates additional kernel boot entries with low-latency tuning
parameters (preempt, IRQ threading, etc.) using kernel-install hooks.

%install

mkdir -p %{buildroot}/usr/lib/kernel/install.d
mkdir -p %{buildroot}/etc/sysconfig

install -m 0755 %{SOURCE0} %{buildroot}/usr/lib/kernel/install.d/
install -m 0644 %{SOURCE1} %{buildroot}/etc/sysconfig/kernel-audio-tuned

%post
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
/usr/lib/kernel/install.d/90-audio-tuned.install
%config(noreplace) /etc/sysconfig/kernel-audio-tuned

%changelog
* Sun May 10 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-4
- update to 1.0-4 - avoid some errors when there are no kernels to manage

* Tue May 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-3
- update to 1.0-3 - limit the number of audio tuned entries to installonly_limit

* Mon Mar 30 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2 - add %post and %preun section

* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- initial version of the spec
