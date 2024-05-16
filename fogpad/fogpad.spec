# Tag: Effect, Reverb
# Type: Plugin, VST3
# Category: Plugin

%define commit0 54f8bda9c0ad8e94788144e2d2b6a2bb8c8ca85a

Name: fogpad
Version: 1.0.3
Release: 1%{?dist}
Summary: A VST reverb effect in which the reflections can be frozen, filtered, pitch shifted and ultimately disintegrated.
URL: https://github.com/igorski/fogpad
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

# Usage: ./vst3-source.sh <TAG>
#        ./vst3-source.sh v3.7.10_build_14

Source0: https://github.com/igorski/fogpad/archive/%{commit0}.zip#/%{name}-%{commit0}.zip
Source1: vst3sdk.tar.gz
Source2: vst3-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel

%description
FogPad is a VST/AU plug-in which provides a reverb effect in which
the reflections can be frozen, filtered, pitch shifted and ultimately
disintegrated.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep

%autosetup -n fogpad-%{commit0}

tar xvfz %{SOURCE1}

sed -i -e "/set(steinberg_libs/d" CMakeLists.txt

%build

%cmake -DVST3_SDK_ROOT=vst3sdk
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Mar 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- update to 1.0.3-1

* Wed Dec 07 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
