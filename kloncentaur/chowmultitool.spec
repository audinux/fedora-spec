# Status: active
# Tag: Guitar, Tool
# Type: Plugin, Standalone, LV2, VST3, CLAP
# Category: Audio, Effect

%define _lto_cflags %{nil}

%global commit0 2d77bdcd946f1673a8a1e7be596982842d3d6844
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240624

Name: ChowMultiTool
Version: 1.1.0^git%{date0}.%{shortcommit0}
Release: 1%{?dist}
Summary: Multi-Tool Audio Plugin
License: GPL-3.0-or-later
URL: https://github.com/Chowdhury-DSP/ChowMultiTool
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# to generater code archive:
# Usage: ./source_chowdhurydsp.sh <project> <tag>
#        ./source_chowdhurydsp.sh ChowMultiTool v1.0.0
#        ./source_chowdhurydsp.sh ChowMultiTool main

Source0: ChowMultiTool.tar.gz
Source1: source_chowdhurydsp.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel

%description
ChowMultiTool is a swiss-army-knife sort of plugin, containing a
handful of little effects and other things that I've found useful.

Requires: license-%{name}

%package -n vst3-%{name}
Summary: CHOW Multitool plugin (VST3)
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: CHOW Multitool plugin (LV2)
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CHOW Multitool plugin (CLAP)
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n ChowMultiTool

%build
%set_build_flags

%cmake
%cmake_build

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/vst3
mkdir -p %{buildroot}%{_libdir}/lv2
mkdir -p %{buildroot}%{_libdir}/clap

install %{__cmake_builddir}/ChowMultiTool_artefacts/Standalone/* %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/ChowMultiTool_artefacts/VST3/*.vst3   %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ChowMultiTool_artefacts/LV2/*.lv2     %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/ChowMultiTool_artefacts/CLAP/*.clap   %{buildroot}%{_libdir}/clap/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Dec 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Sat May 27 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
