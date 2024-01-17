# Tag: Guitar, Tool
# Type: Plugin, LV2, VST3, CLAP
# Category: Audio, Effect

%define _lto_cflags %{nil}

Name: ChowMultiTool
Version: 1.0.0
Release: 1%{?dist}
Summary: Multi-Tool Audio Plugin
License: GPL-3.0-or-later
URL: https://github.com/Chowdhury-DSP/ChowMultiTool

Vendor:       Audinux
Distribution: Audinux

# to generater code archive:
# ./source_chowmultitool.sh <tag>
# ./source_chowmultitool.sh v1.0.0

Source0: ChowMultiTool.tar.gz
Source1: source_chowmultitool.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: JUCE
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

%package -n vst3-%{name}
Summary: CHOW Multitool plugin (VST3)

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: CHOW Multitool plugin (LV2)

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CHOW Multitool plugin (CLAP)

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n ChowMultiTool

%build
%set_build_flags

%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install cmake-build/ChowMultiTool_artefacts/Release/Standalone/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst3
cp -r cmake-build/ChowMultiTool_artefacts/Release/VST3/*.vst3 %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/lv2
cp -r cmake-build/ChowMultiTool_artefacts/Release/LV2/*.lv2 %{buildroot}%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%doc README.md
%license LICENSE
%{_libdir}/vst3/

%files -n lv2-%{name}
%doc README.md
%license LICENSE
%{_libdir}/lv2/

%files -n clap-%{name}
%doc README.md
%license LICENSE
%{_libdir}/clap/

%changelog
* Sat May 27 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
