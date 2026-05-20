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
Source1: topology.sh
Source2: build-profile.sh
Source3: irq-affinity.sh
Source4: audio-topology-generator
Source5: audio-topology.service

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
install -m 0755 -d %{buildroot}/%{_unitdir}/
install -m 0755 -d %{buildroot}/%{_systemdgeneratordir}/

install -m 0755 detect.sh        %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 topology.sh      %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 build-profile.sh %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 irq-affinity.sh  %{buildroot}/%{_libexecdir}/audio-topology-profile/
install -m 0755 audio-topology-generator %{buildroot}/%{_systemdgeneratordir}/
install -m 0644 audio-topology.service   %{buildroot}/%{_unitdir}/

%post
%systemd_post audio-topology.service

%preun
%systemd_preun audio-topology.service

%postun
%systemd_postun_with_restart audio-topology.service

%files
%{_libexecdir}/audio-topology-profile/*
%{_systemdgeneratordir}/audio-topology-generator
%{_unitdir}/audio-topology.service

%changelog
* Wed May 20 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial version of the spec
