# Status: active
# Tag: Effect, Synthesizer
# Type: Plugin, VST3, LV2, Standalone
# Category: Audio, Effect, Synthesizer

Name: resonarium
Version: 1.0.0
Release: 1%{?dist}
Summary: An expressive, semi-modular, and comprehensive physical modeling/waveguide synthesizer
License: GPL-3.0-or-later
URL: https://github.com/gabrielsoule/resonarium
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./resonarium-source.sh <tag>
#        ./resonarium-source.sh v1.0.0

Source0: resonarium.tar.gz
Source1: resonarium-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: git
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: freetype-devel
BuildRequires: libcurl-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils

%description
esonarium is a MPE-compatible expressive physical modeling synthesizer.
It is designed to encourage abstract sound design, exploration, and open-ended play.

Many of the presets work best when used in conjunction with a MPE control
device, such as a Ableton Push 3 or a Roli Seaboard.

This software is still in development. The primary focus at present is stability
and performance. Use at your own risk, and expect bugs or crashes.
Some audio samples can be found here.

Resonarium works well in Ableton and Bitwig.
There are reported issues with Logic and FL Studio.

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

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n resonarium

sed -i -e "s|${PLUGIN_NAME} Effect|${PLUGIN_NAME}_Effect|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Resonarium_Effect_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Resonarium_Instrument_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Resonarium_Effect_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Resonarium_Instrument_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Resonarium_Effect_artefacts/Standalone/*  %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Resonarium_Instrument_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Jun 11 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Mon Jun 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.10-1
- Initial spec file
