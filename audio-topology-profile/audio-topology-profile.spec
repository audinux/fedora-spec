# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: audio-topology-profile
Version: 1.0
Release: 1%{?dist}
Summary: CPU topology aware audio tuning for PipeWire/JACK
License: MIT
BuildArch: noarch

Source0: detect.sh
Source1: build-profile.sh
Source2: irq-affinity.sh
Source3: 10-audio-topology.conf
Source4: audio-topology.service

Requires: systemd
Requires: pipewire
Requires: util-linux

%description
Dynamic low-latency audio tuning profile for PipeWire/JACK.
Automatically adapts CPU affinity based on CPU topology
and RT kernel detection.

%prep

%build

%install

install -m 0755 -d %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 -d %{buildroot}/%{_userunitdir}/pipewire.service.d/
install -m 0755 -d %{buildroot}/%{_unitdir}/

install -m 0755 %{SOURCE0} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE1} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE2} %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 %{SOURCE3} %{buildroot}/%{_userunitdir}/pipewire.service.d/
install -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/

%post
%systemd_post audio-topology.service

%preun
%systemd_preun audio-topology.service

%postun
%systemd_postun_with_restart audio-topology.service

%files
%{_libexecdir}/audio-topology-profile/*
%{_userunitdir}/pipewire.service.d/10-audio-topology.conf
%{_unitdir}/audio-topology.service

%changelog
* Wed May 20 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial version of the spec
