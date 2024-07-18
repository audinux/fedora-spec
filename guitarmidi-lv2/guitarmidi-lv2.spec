# Tag: Guitar, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect, MIDI

Name: guitarmidi
Version: 1.5
Release: 2%{?dist}
Summary: A concept for guitar to midi as an lv2 plugin
URL: https://github.com/geraldmwangi/GuitarMidi-LV2
ExclusiveArch: x86_64 aarch64
License: LGPLv2+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./guitarmidi-lv2-source.sh <TAG>
#        ./guitarmidi-lv2-source.sh v1.5

Source0: GuitarMidi-LV2.tar.gz
Source1: guitarmidi-lv2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: aubio-devel
BuildRequires: pango-devel

%description
A concept for guitar to midi as an lv2 plugin. GuitarMidi-LV2 analyses the
signal of a guitar in standard tuning E A D g b e extracts the notes played.
It deploys a bank of elliptic cauer bandpass filters to separate the
polyphonic audio into monophonic frequency segments, which are then
analysed by monophonic pitch detectors.

%prep
%autosetup -n GuitarMidi-LV2

sed -i -e "s/Git_FOUND/0/g" cmake/setversionfromgit.cmake

%build

%cmake
%cmake_build

%install

%cmake_install
install -d 755 %{buildroot}/%{_libdir}/lv2
mv %{buildroot}/%{_prefix}/guitarmidi.lv2 %{buildroot}/%{_libdir}/lv2/guitarmidi.lv2

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Thu Jul 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1.5-2
- update to 1.5-2

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.4-2
- update to 1.4-2

* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3-2
- update to 1.3-2

* Wed Jul 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Mon Jul 11 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- initial version of the spec file
