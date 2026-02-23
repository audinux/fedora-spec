# Status: active
# Tag: Distortion
# Type: Plugin, VST3, LV2
# Category: Effect

Name: crushfuzz
Version: 0.1.5
Release: 1%{?dist}
Summary: Bitcrusher plugin for Guitar
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/crushfuzz
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./yimrakhee-source.sh <project> <tag>
# ./yimrakhee-source.sh crushfuzz v0.1.5

Source0: crushfuzz.tar.gz
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
Bitcrusher plugin for Guitar.
Destructive digital artifacts with an Analog-style parallel mixing architecture.

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
cp -ra %{__cmake_builddir}/crushfuzz_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/crushfuzz_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Feb 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-1
- update to 0.1.5-1

* Wed Feb 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
