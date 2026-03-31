# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

Name: ultramaster-kr106
Version: 2.4.6.2
Release: 1%{?dist}
Summary: JUCE port of Ultramaster Group's classic 2001 software synth
License: GPL-3.0-or-later
URL: https://github.com/kayrockscreenprinting/ultramaster_kr106
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ultramaster-kr106-source.sh <TAG>
#        ./ultramaster-kr106-source.sh v2.4.6.2

Source0: ultramaster_kr106.tar.gz
Source1: ultramaster-kr106-source.sh

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

%description
A synthesizer plugin emulating the Roland Juno-106, built with JUCE.
6-voice polyphonic with per-voice analog variance, TPT ladder filter with OTA saturation,
BBD chorus emulation, arpeggiator, portamento/unison mode, and 211 factory presets.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ultramaster_kr106

sed -i -e "s|PRODUCT_NAME \"Ultramaster KR-106\"|PRODUCT_NAME \"Ultramaster_KR-106\"|g" CMakeLists.txt
sed -i -e "s|PLUGIN_NAME \"Ultramaster KR-106\"|PLUGIN_NAME \"Ultramaster_KR-106\"|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/KR106_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/KR106_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/KR106_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/KR106_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md AUTHORS CONTRIBUTING.md docs/*
%license LICENSE THIRD_PARTY_LICENSES

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Mar 31 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.6.2-1
- update to 2.4.6.2-1

* Mon Mar 30 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.6-1
- update to 2.4.6-1

* Sun Mar 29 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.5.1-1
- update to 2.4.5.1-1

* Fri Mar 27 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.4-1
- update to 2.4.4-1

* Wed Mar 25 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.3-1
- update to 2.4.3-1

* Tue Mar 24 2026 Yann Collette <ycollette.nospam@free.fr> - 2.4.2-1
- Initial spec file
