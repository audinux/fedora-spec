# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

Name: pluginval
Version: 1.0.4
Release: 1%{?dist}
Summary: Cross platform plugin testing and validation tool
License: GPL-3.0-or-later
URL: https://github.com/Tracktion/pluginval
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./pluginval-source.sh <TAG>
#        ./pluginval-source.sh v1.0.4

Source0: pluginval.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: pluginval-source.sh
Patch0: pluginval-0001-remove-static-libstdc.patch

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
BuildRequires: ladspa-devel

%description
pluginval is a cross-platform plugin validator and tester application.
It is designed to be used by both plugin and host developers to ensure
stability and compatibility between plugins and hosts.

If you are a plugin user looking to report a problem with a plugin to
the developers, you can use pluginval to create a detailed log which
can drastically improve the time to fix issues. Please follow the
instructions here to get started: Testing plugins with pluginval

Highlights:
* Test VST/AU/VST3 plugins
* Compatible with macOS/Windows/Linux
* Run in GUI or headless mode
* Validation is performed in a separate process to avoid crashing

%prep
%autosetup -p1 -n pluginval

unzip %{SOURCE1}

%build

CWD=`pwd`

export VST2_SDK_DIR="$CWD/VST_SDK/VST2_SDK/"

%cmake -DPLUGINVAL_ENABLE_RTCHECK=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/pluginval_artefacts/pluginval  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc/
cp -ra docs/*  %{buildroot}/%{_datadir}/%{name}/doc/

%files
%doc README.md CHANGELIST.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/doc/*

%changelog
* Fri Jan 30 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.4-1
- Initial spec file
