# Tag: Effect, Sampler
# Type: LV2
# Category: Plugin, Audio 

Name: lv2-freeze
Version: 0.2.0
Release: 1%{?dist}
Summary: LV2 plugin that freezes track audio to reduce DSP load
License: GPL-3.0
URL: https://github.com/taylordotfish/freeze
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/taylordotfish/freeze/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: gtk2-devel

%description
Freeze is an LV2 plugin for freezing tracks in a digital audio workstation—that is,
temporarily rendering a track as audio to reduce CPU/DSP load, as tracks with large
chains of CPU-heavy effects can make buffer underruns (xruns) quite common.
Some DAWs like Ardour support track freezing to a certain extent, but Ardour,
for example, cannot freeze MIDI tracks.

%prep
%autosetup -n freeze-%{version}

sed -i -e "s/build\///g" manifest.ttl

%build

%set_build_flags
%make_build

%Install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/freeze.lv2/
cp build/freeze.so %{buildroot}/%{_libdir}/lv2/freeze.lv2/
cp build/freeze_ui.so %{buildroot}/%{_libdir}/lv2/freeze.lv2/
cp freeze.ttl %{buildroot}/%{_libdir}/lv2/freeze.lv2/
cp manifest.ttl %{buildroot}/%{_libdir}/lv2/freeze.lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial development
