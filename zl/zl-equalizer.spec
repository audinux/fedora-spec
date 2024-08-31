# Status: active
# Tag: Equalizer
# Type: LV2, VST3, Plugin
# Category: Effect

Name: zl-equalizer
Version: 0.3.5
Release: 2%{?dist}
Summary: Equalizer plugin
License: GPL-3.0-only
URL: https://github.com/ZL-Audio/ZLEqualizer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLEqualizer 0.3.5

Source0: ZLEqualizer.tar.gz
Source1: zl-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: boost-devel
BuildRequires: libatomic

%description
ZLEqualizer is an equalizer plugin.

%package -n license-%{name}
Summary:  License and documentation of %{name}
License:  GPL-3.0-only

%description -n license-%{name}
License and documentation of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ZLEqualizer

sed -i -e "s/ZL Equalizer/ZL_Equalizer/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/ZLEqualizer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ZLEqualizer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Aug 23 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.5-2
- update to 0.3.5-2

* Sat Aug 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-2
- update to 0.3.4-2

* Sun Jul 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-2
- update to 0.3.3-2

* Tue Jun 18 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-2
- update to 0.3.2-2 - tag updated

* Fri Jun 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-1
- update to 0.3.2-1

* Sun Jun 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to 0.3.1-1

* Fri May 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
