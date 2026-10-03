# Status: active
# Tag: Tool, AI
# Type: Plugin, VST3, CLAP, LV2, Standalone
# Category: Audio, Tool

%global _cmake_shared_libs %{nil}

Name: tone3000
Version: 0.0.11
Release: 1%{?dist}
Summary: TONE3000 plugin
License: MIT
URL: https://github.com/tone-3000/tone3000-plugin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./tone3000-source.sh <TAG>
#        ./tone3000-source.sh v0.0.11

Source0: tone3000-plugin.tar.gz
Source1: tone3000-source.sh

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
A JUCE-based audio plugin (VST3, CLAP, LV2, Standalone) that loads Neural Amp Modeler (NAM)
captures and impulse responses (IRs) straight from TONE3000. No manual file downloads:
browse the catalog, sign in, and add tones directly into your signal chain.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n tone3000-plugin

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugin/TONE3000_artefacts/Debug/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/plugin/TONE3000_artefacts/Debug/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugin/TONE3000_artefacts/Debug/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/plugin/TONE3000_artefacts/Debug/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/factory-presets/
cp -ra resources/factory-presets/* %{buildroot}/%{_datadir}/%{name}/factory-presets/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md plugin/docs/*
%license LICENSE
%{_datadir}/%{name}/factory-presets/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Oct 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.11-1
- Initial spec file
