# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3, CLAP, LV2
# Category: Audio, Synthesizer

%global commit0 4a87e08ad9370f2d92fb12bf0a0df69738429da4

Name: gearmulator
Version: 0.0.1
Release: 1%{?dist}
Summary: Emulation of classic VA synths of the late 90s/2000s that are based on Motorola 56300 family DSPs 
License: GPL-3.0-or-later
URL: https://github.com/dsp56300/gearmulator
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gearmulator-source.sh <TAG>
#        ./gearmulator-source.sh main

Source0: gearmulator.tar.gz
Source1: gearmulator-source.sh
Patch0: gearmulator-0001-add-missing-header.patch
Patch1: gearmulator-0002-remove-static-flags.patch

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
BuildRequires: webkit2gtk3-devel

%description

This project emulates various musical devices that used the Motorola 56300 family DSPs.
The supported plugin formats are VST3, CLAP and LV2.
At the moment, the following synthesizers are supported:
- Osirus: Access Virus A,B,C
- OsTIrus: Access Virus TI/TI2/Snow
- Vavra: Waldorf microQ
- Xenia: Waldorf Microwave II/XT
- Nodal Red 2x: Clavia Nord Lead/Rack 2x

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -p1 -n gearmulator

%build

%cmake -Dgearmulator_BUILD_FX_PLUGIN=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_FX_artefacts/Release/VST3/*           %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_artefacts/Release/VST3/*              %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_FX_artefacts/Release/VST3/*           %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_artefacts/Release/VST3/*              %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_FX_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_artefacts/Release/VST3/*    %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_FX_artefacts/Release/VST3/*   %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_artefacts/Release/VST3/*      %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/source/nord/n2x/n2xJucePlugin/n2xJucePlugin_artefacts/Release/VST3/*   %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_FX_artefacts/Release/VST/*           %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_artefacts/Release/VST/*              %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_FX_artefacts/Release/VST/*           %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_artefacts/Release/VST/*              %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_FX_artefacts/Release/VST/*   %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_artefacts/Release/VST/*      %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_FX_artefacts/Release/VST/* %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_artefacts/Release/VST/*    %{buildroot}/%{_libdir}/vst/
cp -ra %{__cmake_builddir}/source/nord/n2x/n2xJucePlugin/n2xJucePlugin_artefacts/Release/VST/*   %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_FX_artefacts/Release/CLAP/*           %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_artefacts/Release/CLAP/*              %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_FX_artefacts/Release/CLAP/*           %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_artefacts/Release/CLAP/*              %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_FX_artefacts/Release/CLAP/*   %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_artefacts/Release/CLAP/*      %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_FX_artefacts/Release/CLAP/* %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_artefacts/Release/CLAP/*    %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/source/nord/n2x/n2xJucePlugin/n2xJucePlugin_artefacts/Release/CLAP/*   %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_FX_artefacts/Release/LV2/*           %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/mqJucePlugin/mqJucePlugin_artefacts/Release/LV2/*              %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_FX_artefacts/Release/LV2/*           %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/xtJucePlugin/xtJucePlugin_artefacts/Release/LV2/*              %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_FX_artefacts/Release/LV2/*   %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/osirusJucePlugin/osirusJucePlugin_artefacts/Release/LV2/*      %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_FX_artefacts/Release/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/osTIrusJucePlugin/osTIrusJucePlugin_artefacts/Release/LV2/*    %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/source/nord/n2x/n2xJucePlugin/n2xJucePlugin_artefacts/Release/LV2/*   %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Aug 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
