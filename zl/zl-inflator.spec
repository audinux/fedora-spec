# Tag: Distortion
# Type: VST3, Plugin
# Category: Effect

Name: zl-inflator
Version: 0.3.0
Release: 1%{?dist}
Summary: Distortion / saturation plugin
License: GPL-3.0-only
URL: https://github.com/ZL-Audio/ZLInflator
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./zl-source.sh <project> <tag>
# ./zl-source.sh ZLInflator 0.3.0

Source0: ZLInflator.tar.gz
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
ZLInflator is a distortion/saturation plugin to increase loudness.

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

%prep
%autosetup -n ZLInflator

sed -i -e "s/ZL Inflator/ZL_Inflator/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/ZLInflator_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri May 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
