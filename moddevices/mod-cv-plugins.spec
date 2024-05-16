# Tag: Effect, Tool
# Type: Plugin, LV2
# Category: Effect, Tool

# Global variables for github repository
%global commit0 5b175482a32094f39eb46d569ffbc718b157a0ee
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: mod-cv-plugins
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Control Voltage Plugins
License: GPL-2.0-or-later
URL: https://github.com/moddevices/mod-cv-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./moddevices-source.sh <PROJECT> <commit0>
# ./moddevices-source.sh mod-cv-plugins 5b175482a32094f39eb46d569ffbc718b157a0ee
Source0: mod-cv-plugins.tar.gz
Source1: moddevices-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
Control Voltage Plugins:
- mod-cv-attenuverter
- mod-cv-clock
- mod-cv-control
- mod-cv-meter
- mod-cv-switch1
- mod-cv-switch2
- mod-cv-switch3
- mod-cv-switch4
- mod-cv-to-audio
- mod-midi-to-cv-mono
- mod-midi-to-cv-poly
- mod-cv-abs
- mod-cv-gate
- mod-cv-random
- mod-cv-range
- mod-cv-round
- mod-cv-slew
- mod-logic-operators
- mod-audio-to-cv(beta)
- mod-cv-change(beta)

%prep
%autosetup -n %{name}

for Files in `find source -name Makefile.mk`
do
    echo "Fixing $Files"
    sed -i -e "s/-Wl,--strip-all//g" $Files
    sed -i -e "s/-Wall/-Wall $\(CFLAGS\)/g" $Files
done

%build

%set_build_flags

%make_build LV2_DESTDIR=%{buildroot}/%{_libdir}/lv2

%install

%make_install LV2_DESTDIR=%{buildroot}/%{_libdir}/lv2

%files
%doc README.md
%{_libdir}/lv2/*

%changelog
* Tue May 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-5b175482-1
- Initial build
