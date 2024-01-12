# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

%global commit0 9ebaddc0f140f107e46ee8f2a75cad97fef8bee9

Name: lv2-loopor
Version: 0.0.1
Release: 1%{?dist}
Summary: Looper plugin for LV2
License: MIT
URL: https://github.com/stevie67/loopor

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/stevie67/loopor/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
Looper plugin for LV2, specifically for the Mod Devices pedal board.

%prep
%autosetup -n loopor-%{commit0}

sed -i -e "s/lib\/lv2/%{_lib}\/lv2/g" loopor-lv2/source/Makefile

%build

%set_build_flags

export CFLAGS="-include cstdio $CFLAGS"
export CXXFLAGS="-include cstdio $CXXFLAGS"

cd loopor-lv2/source
%make_build PREFIX=/usr

%Install

cd loopor-lv2/source
%make_install PREFIX=/usr

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Oct 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial development
