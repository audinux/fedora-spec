# Status: active
# Tag: Distortion
# Type: Plugin, VST3, LV2
# Category: Effect

Name: smallmuffin
Version: 0.1.5
Release: 1%{?dist}
Summary: Vintage Fuzz plugin for Guitar and Bass
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/smallmuffin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./yimrakhee-source.sh <project> <tag>
# ./yimrakhee-source.sh smallmuffin v0.1.5

Source0: smallmuffin.tar.gz
Source1: yimrakhee-source.sh

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
Vintage Fuzz plugin for Guitar and Bass. (GNU GPLv3)
Combines the legendary, massive sustain of the vintage 1970s circuit (V2 "Ram's Head" style)
with modern DSP enhancements, including 2x oversampling and adjustable midrange control.

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
%autosetup -n %{name}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/smallmuffin_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/smallmuffin_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Feb 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-1
- update to 0.1.5-1

* Wed Feb 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
