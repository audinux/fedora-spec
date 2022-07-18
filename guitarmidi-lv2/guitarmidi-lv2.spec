Name:    guitarmidi
Version: 1.1
Release: 2%{?dist}
Summary: A concept for guitar to midi as an lv2 plugin
URL:     https://github.com/geraldmwangi/GuitarMidi-LV2
License: LGPLv2+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./guitarmidi-lv2-source.sh <TAG>
# ./guitarmidi-lv2-source.sh 1.1

Source0: GuitarMidi-LV2.tar.gz
Source1: guitarmidi-lv2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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
* Wed Jul 13 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Mon Jul 11 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- initial version of the spec file
