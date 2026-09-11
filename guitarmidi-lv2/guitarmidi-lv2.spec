# Status: active
# Tag: Guitar, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect, MIDI

%global debug_package %{nil}

Name: guitarmidi
Version: 3.0
Release: 3%{?dist}
Summary: A concept for guitar to midi as an lv2 plugin
URL: https://github.com/geraldmwangi/GuitarMidi-LV2
ExclusiveArch: x86_64 aarch64
License: LGPL-2.1-or-later

Vendor:       Audinux
Distribution: Audinux

# Usage: ./guitarmidi-lv2-source.sh <TAG>
#        ./guitarmidi-lv2-source.sh v3.0

Source0: GuitarMidi-LV2.tar.gz
Source1: guitarmidi-lv2-source.sh
Patch0: guitarmidi-lv2-0001-add-missing-include.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: aubio-devel
BuildRequires: zita-resampler-devel
BuildRequires: cairo-devel
BuildRequires: libX11-devel

%description
A concept for guitar to midi as an LV2 plugin. GuitarMidi-LV2 analyses the
signal of a guitar in standard tuning E A D G B E extracts the notes played.
It deploys a bank of elliptic cauer bandpass filters to separate the
polyphonic audio into monophonic frequency segments, which are then
analysed by monophonic pitch detectors.

%prep
%autosetup -p1 -n GuitarMidi-LV2

sed -i -e "s/Git_FOUND/0/g" cmake/setversionfromgit.cmake

%build

export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC -include cstdint"
export LDFLAGS="-fPIC"

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
       -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
       -DCMAKE_INSTALL_PREFIX=%{_libdir}/lv2 \
       -DCMAKE_CXX_FLAGS="-fPIC -include cstdint" \
       -DCMAKE_C_FLAGS="-fPIC" ..

%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Sep 11 2026 Yann Collette <ycollette.nospam@free.fr> - 3.0-3
- update to 3.0-3

* Sun Jun 21 2026 Yann Collette <ycollette.nospam@free.fr> - 2.2-3
- update to 2.2-3

* Thu May 28 2026 Yann Collette <ycollette.nospam@free.fr> - 2.1-3
- update to 2.1-3

* Mon May 18 2026 Yann Collette <ycollette.nospam@free.fr> - 2.0-3
- update to 2.0-3 - update to 460af5c7ca03f27db50d3ddc88f388e5fa94099b

* Sun May 17 2026 Yann Collette <ycollette.nospam@free.fr> - 2.0-2
- update to 2.0-2

* Fri Jul 19 2024 Yann Collette <ycollette.nospam@free.fr> - 1.6-2
- update to 1.6-2

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
