# Status: active
# Tag: Effect, Tool, Devel
# Type: Plugin, Standalone, VST3
# Category: Effect, Programming

Name: protoplug
Version: 0.0.1
Release: 1%{?dist}
Summary: Create audio plugins on-the-fly with Lua
License: MIT
URL: https://github.com/ycollet/protoplug
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./protoplug-source.sh <TAG>
#        ./protoplug-source.sh fixes

Source0: protoplug.tar.gz
Source1: protoplug-source.sh

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: lua-devel

%description
Protoplug is a VST/AU plugin that lets you load and edit Lua scripts as audio effects and instruments.
The scripts can process audio and MIDI, display their own interface, and use external libraries.
Transform any music software into a live coding environment!

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n protoplug

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/protoplug_fx_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/protoplug_gen_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/
cp -ra ProtoplugFiles/* %{buildroot}%{_datadir}/%{name}/

%files -n vst3-%{name}
%doc readme.md
%license license.txt
%{_libdir}/vst3/*
%{_datadir}/%{name}/*

%changelog
* Tue Apr 28 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
