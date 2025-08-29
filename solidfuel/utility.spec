# Status: active
# Tag: Tool
# Type: Plugin, Standalone, VST3
# Category: Audio, Tool

Name: solid-utility
Version: 1.0.0
Release: 2%{?dist}
Summary: Versatile VST3 Channel Utility for Digital Audio Workstations
License: GPL-3.0-or-later
URL: https://github.com/SolidFuel/Utility
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./solidfuel-source.sh <PROJECT> <TAG>
#        ./solidfuel-source.sh Utility v1.0.0

Source0: Utility.tar.gz
Source1: solidfuel-source.sh

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
Versatile VST3 Channel Utility for Digital Audio Workstations.
solidUtility can :
- swap channels
- mute channels
- do mid-side encoding and decoding
- phase invert
- remove DC offset
- and more!

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Utility

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Source/solidUtility_artefacts/Release/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Fri Aug 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2 - remove unused dep

* Mon Jul 21 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
