# Status: active
# Tag: Effect
# Type: Plugin, VST
# Category: Audio, Effect

%global commit0 bcef0b855812318133a679728d9db0c6060e8508

Name: mxcomp
Version: 0.1.0
Release: 2%{?dist}
Summary: A digital compression plugin for VST
License: GPL-3.0-or-later
URL: https://github.com/liuanlin-mx/MXComp
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./mxcomp-source.sh <TAG>
#        ./mxcomp-source.sh main

Source0: MXComp.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: mxcomp-source.sh
Patch0: mxcomp-0001-fix-link.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
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
BuildRequires: fftw-devel
BuildRequires: glfw-devel
BuildRequires: chrpath

%description
A digital compression effect.

%prep
%autosetup -p1 -n MXComp

unzip %{SOURCE1}
cp -r ./VST_SDK/VST2_SDK/public.sdk/source pluginterfaces
cp -r ./VST_SDK/VST2_SDK/pluginterfaces/* pluginterfaces

sed -i -e "/net_log.h/d" src/plugin_processor.cpp
sed -i -e "/net_log.h/d" src/plugin_editor.cpp

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 cmake-build-linux_vst_cmake/output/libmx_comp.so %{buildroot}/%{_libdir}/vst/

chrpath --delete %{buildroot}%{_libdir}/vst/libmx_comp.so

%files
%doc README.md
%license LICENSE
%{_libdir}/vst/*

%changelog
* Wed Oct 08 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to 0.1.0-2 - remove unused dep

* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
