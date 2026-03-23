Name: kernel-audio-tuned
Version: 1.0
Release: 1%{?dist}
Summary: Audio tuned kernel boot entries for Fedora

License: GPLv3
BuildArch: noarch

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

%files
/usr/lib/kernel/install.d/90-audio-tuned.install
%config(noreplace) /etc/sysconfig/kernel-audio-tuned

%changelog
* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- initial version of the spec
