%define commit0 59077dc9bd0d4b47b6e6e84c2aa9c4e14bcea908

Name:    fogpad
Version: 0.0.1
Release: 1%{?dist}
Summary: A VST reverb effect in which the reflections can be frozen, filtered, pitch shifted and ultimately disintegrated.
URL:     https://github.com/igorski/fogpad
License: MIT

Vendor:       Audinux
Distribution: Audinux

# Usage: ./vst3-source.sh <TAG>
# ./vst3-source.sh 5cb57b76ee5287868ba6ac6e4d69a1b99f560cdc

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
License:  GPLv3
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
* Wed Dec 07 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
