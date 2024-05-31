# Tag: Effect
# Type: VST3, LV2, Plugin
# Category: Effect

Name: zl-split
Version: 0.0.1
Release: 1%{?dist}
Summary: Splitter plugin
License: GPL-3.0-only
URL: https://github.com/ZL-Audio/ZLSplit
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLSplit main

Source0: ZLSplit.tar.gz
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
ZLSplit is a splitter plugin.

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
%autosetup -n ZLSplit

sed -i -e "s/ZL Splitte/ZL_Splitte/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/ZLSplit_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/ZLSplit_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri May 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
