# Status: active
# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name: xpolymonk
Version: 0.6.0
Release: 1%{?dist}
Summary: A LV2 simple polyphonic sound generator to have some fun with
License: GPL-2.0-or-later
URL: https://github.com/brummer10/XPolyMonk.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh XPolyMonk.lv2 0.6

Source0: XPolyMonk.lv2.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
A LV2 simple polyphonic sound generator to have some fun with

%prep
%autosetup -n XPolyMonk.lv2

%build

%set_build_flags

%make_build STRIP=true

%install

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- Initial spec file
