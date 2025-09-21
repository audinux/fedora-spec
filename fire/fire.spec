# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name: fire
Version: 1.5.0b
Release: 2%{?dist}
Summary: This is a distortion plugin developed by Wings
License: GPL-2.0-or-later
URL: https://github.com/jerryuhoo/Fire
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./fire-source.sh <TAG>
#        ./fire-source.sh v1.5.0b

Source0: Fire.tar.gz
Source1: fire-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel

%description
This is a multi-band distortion plugin 『Fire』.
It can be used in DAWs which supports AU and Vst3 plugins such
as Ableton Live, Fl Studio, etc.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Fire

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Fire_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE.md
%{_libdir}/vst3/*

%changelog
* Sat Sep 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.5.0b-2
- update to 1.5.0b-2

* Fri Aug 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-2
- update to 1.0.2-2 - remove unused dep

* Sat Jul 05 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Thu May 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- update to 1.0.1-1

* Sun Jan 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- update to 0.9.9-1

* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-1
- Initial spec file
