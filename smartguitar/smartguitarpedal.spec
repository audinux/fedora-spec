# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

Name: smartguitarpedal
Version: 1.5
Release: 1%{?dist}
Summary: Guitar plugin made with JUCE that uses neural network models to emulate real world hardware.
License: GPL-2.0-or-later
URL: https://github.com/GuitarML/SmartGuitarPedal

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh SmartGuitarPedal 1182756365616a9a39f543eb3ab9c77f47c18c13

Source0: SmartGuitarPedal.tar.gz
Source1: source-guitarml.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: eigen3-devel
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
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: xsimd-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: chrpath

%description
Guitar plugin made with JUCE that uses neural
network models to emulate real world hardware.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n SmartGuitarPedal

sed -i -e "/AAX_SDK/d" CMakeLists.txt

%build

%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/SmartPedal.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/SmartPedal.lv2/

cp -ra %{__cmake_builddir}/SmartPedal_artefacts/LV2/SmartPedal.lv2/* %{buildroot}%{_libdir}/lv2/SmartPedal.lv2/
cp -ra %{__cmake_builddir}/SmartPedal_artefacts/VST3/SmartPedal.vst3/* %{buildroot}%{_libdir}/vst3/SmartPedal.vst3/

chrpath --delete %{buildroot}%{_libdir}/lv2/SmartPedal.lv2/libSmartPedal.so
chrpath --delete `find %{buildroot}%{_libdir}/vst3/SmartPedal.vst3 -name SmartPedal.so`

%files
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Nov 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.5-1
- Initial spec file
