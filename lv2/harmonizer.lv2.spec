# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Tool

# Global variables for github repository
%global commit0 b16e01c71263bd6254df3096eb16c70864a3d6dd
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: lv2-harmonizer
Version: 0.0.1
Release: 1%{?dist}
Summary: LV2 note detection using aubio
License: GPL-2.0-only
URL: https://github.com/dsheeler/harmonizer.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/dsheeler/harmonizer.lv2/archive/%{commit0}.tar.gz#/harmonizer.lv2-%{shortcommit0}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: aubio-devel

%description
harmonizer.lv2 uses the aubio toolkit for note onset
and pitch detection on audio input and outputs midi

%prep
%autosetup -n harmonizer.lv2-%{commit0}

%build
%set_build_flags
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install
%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/harmonizer.lv2

%changelog
* Sun Jan 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1.1
- Initial build

