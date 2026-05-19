# Status: active
# Tag: Guitar, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect, MIDI

%global debug_package %{nil}

%global commit0 460af5c7ca03f27db50d3ddc88f388e5fa94099b

Name: guitarmidi
Version: 2.0
Release: 3%{?dist}
Summary: A concept for guitar to midi as an lv2 plugin
URL: https://github.com/geraldmwangi/GuitarMidi-LV2
ExclusiveArch: x86_64 aarch64
License: LGPLv2+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./guitarmidi-lv2-source.sh <TAG>
#        ./guitarmidi-lv2-source.sh master

Source0: GuitarMidi-LV2.tar.gz
Source1: guitarmidi-lv2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: aubio-devel

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

export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

mkdir build
cd build

cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
      -DCMAKE_INSTALL_PREFIX=%{buildroot}/%{_libdir}/lv2 \
      -DCMAKE_CXX_FLAGS="-fPIC" \
      -DCMAKE_C_FLAGS="-fPIC" ..

make VERBOSE=1

%install

cd build
make install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
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
