# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name:    fire
Version: 0.9.9
Release: 1%{?dist}
Summary: This is a distortion plugin developed by Wings
License: GPLv2+
URL:     https://github.com/jerryuhoo/Fire

Vendor:       Audinux
Distribution: Audinux

# Usage: ./fire-source.sh <TAG>
# ./fire-source.sh v0.9.9

Source0: Fire.tar.gz
Source1: vst3sdk.tar.gz
Source2: fire-source.sh
Source3: vst3-source.sh

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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
This is a multi-band distortion plugin 『Fire』.
It can be used in DAWs which supports AU and Vst3 plugins such
as Ableton Live, Fl Studio, etc.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Fire

tar xvfz %{SOURCE1}

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
* Sun Jan 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- update to 0.9.9-1

* Mon Jul 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-1
- Initial spec file
