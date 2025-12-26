# Status: active
# Tag: Vocoder
# Type: Plugin, LV2
# Category: Audio, Synthesizer, Effect

%global commit0 ea36c53c0bcc828eb8ced8dceb55c5cefd50d089

Name: signalview
Version: 0.0.1
Release: 1%{?dist}
Summary: Stereo audio signal analysis with time and frequency domain LV2 plugin
License: GPL-3.0-or-later
URL: https://github.com/TimKrause2/SignalViewLV2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./timkrause2-source.sh <project> <tag>
# ./timkrause2-source.sh SignalViewLV2 main

Source0: SignalViewLV2.tar.gz
Source1: timkrause2-source.sh
Patch0: signalviewlv2-0001-add-CFLAGS.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: unzip
BuildRequires: ncurses
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: glm-devel
BuildRequires: fftw-devel
BuildRequires: libglvnd-devel

%description
SignalView is a LV2 plugin that provides a visual representation of a stereo audio signal.
There is a time domain view, frequency domain view and a sonogram.

%prep
%autosetup -p1 -n SignalViewLV2

%build

%set_build_flags

%make_build STRIP=true
make SignalView.lv2

%install

cd build
unzip SignalView.lv2.zip

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra SignalView.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Dec 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- Initial spec file
