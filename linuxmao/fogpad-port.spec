# Tag: Effect, Reverb
# Type: Plugin, LV2, VST3
# Category: Effect, Plugin

Name: fodpad-port
Version: 1.0.0
Release: 1%{?dist}
Summary: A reverb effect in which the reflections can be frozen, filtered, pitch shifted and ultimately disintegrated
URL: https://github.com/linuxmao-org/fogpad-port
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./fogpad-port-source.sh v1.0.0

Source0: fogpad-port.tar.gz
Source1: fogpad-port-source.sh

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: libglvnd-devel

%description
A reverb effect in which the reflections can be frozen,
filtered, pitch shifted and ultimately disintegrated)

%prep

%autosetup -n fogpad-port

%build

%set_build_flags
%make_build BUILD_VST2=true SKIP_STRIPPING=true PREFIX=/usr LIBDIR=/usr/%{_lib}/

%install

%make_install BUILD_VST2=true SKIP_STRIPPING=true PREFIX=/usr LIBDIR=/usr/%{_lib}/

%files
%doc README.md
%license LICENSE
%{_bindir}/fogpad
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Sat Jan 30 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
