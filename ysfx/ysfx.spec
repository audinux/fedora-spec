# Tag: Audio, Tool
# Type: Plugin, VST3
# Category: Audio, Tool

%define commit0 8077347ccf4115567aed81400281dca57acbb0cc

Name: ysfx
Version: 0.0.1
Release: 1%{?dist}
Summary: Hosting library for JSFX
URL: https://github.com/jpcima/ysfx
ExclusiveArch: x86_64 aarch64
License: Apache-2.0

Vendor:       Audinux
Distribution: Audinux

# ./ysfx-source.sh maser

Source0: ysfx.tar.gz
Source1: ysfx-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
This package provides support for audio and MIDI effects developed with the
JSFX language. These effects exist in source code form, and they are compiled
and ran natively by hosting software.
This contains a hosting library, providing a JSFX compiler and runtime.
In addition, there is an audio plugin which can act as a JSFX host in a
digital audio workstation.

%prep

%autosetup -n ysfx

%build

%cmake 
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ysfx_plugin_artefacts/RelWithDebInfo/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_libdir}/vst3/*

%changelog
* Fri Nov 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
