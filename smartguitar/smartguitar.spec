# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

%define toneversion 1.0

Name:    smartamp
Version: 1.3
Release: 2%{?dist}
Summary: Guitar plugin emulating real hardware with Neural Network
License: GPL-2.0-or-later
URL:     https://github.com/GuitarML/SmartGuitarAmp

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh SmartGuitarAmp v1.3

Source0: SmartGuitarAmp.tar.gz
Source1: https://github.com/GuitarML/ToneLibrary/archive/refs/tags/v%{toneversion}.zip#/tonelib-%{toneversion}.zip
Source2: source-guitarml.sh

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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: unzip

%description
SmartGuitarAmp is a guitar plugin (VST3) made with JUCE that uses neural network models to emulate real world hardware.

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
%autosetup -n SmartGuitarAmp

sed -i -e "/juce_set_aax_sdk_path/d" CMakeLists.txt

%build

%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/SmartAmp.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/SmartAmp.lv2/

cp -ra %{__cmake_builddir}/SmartAmp_artefacts/LV2/SmartAmp.lv2/* %{buildroot}%{_libdir}/lv2/SmartAmp.lv2/
cp -ra %{__cmake_builddir}/SmartAmp_artefacts/VST3/SmartAmp.vst3/* %{buildroot}%{_libdir}/vst3/SmartAmp.vst3/

install -m 755 -d %{buildroot}%{_datadir}/smartamp/tones/
unzip %{SOURCE1}
mv ToneLibrary-%{toneversion}/SmartAmp/* %{buildroot}%{_datadir}/smartamp/tones/

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/smartamp/
%{_datadir}/smartamp/tones/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Dec 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3-2
- update to 1.3-2 - add presets

* Wed Aug 31 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3-1
- update to 1.3-1

* Sun Feb 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
