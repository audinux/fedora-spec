# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

%define toneversion 1.0

Name: proteus
Version: 0.1
Release: 2%{?dist}
Summary: Guitar amp and pedal capture plugin using neural networks.
License: GPL-2.0-or-later
URL: https://github.com/GuitarML/Proteus

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh Proteus d663c5783b3abc581ee3ab1d65d1552d4c9a9cf9

Source0: Proteus.tar.gz
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
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: xsimd8-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: chrpath
BuildRequires: unzip

%description
Capture your own amps/pedals/plugins with Proteus.
Can capture a drive/tone knob, or snapshot of the sound at
a specific setting. Use the Proteus Capture Utility to quickly
train models in the cloud with Colab. Effective for Amps/PreAmps,
Distortion/Overdrive/Boost pedals (non-time based, no
Reverb/Delay/Flange/Phaser). You can also capture a "rig", or
combination of pedals/amp. This is similar in concept to a Kemper,
Quad Cortex, or ToneX, in a free and open source plugin, with the
ability to capture and share the sound of guitar gear normally
costing hundreds or thousands of dollars.

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
%autosetup -n Proteus

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

install -m 755 -d %{buildroot}%{_libdir}/vst3/Proteus.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/Proteus.lv2/

cp -ra %{__cmake_builddir}/Proteus_artefacts/LV2/Proteus.lv2/* %{buildroot}%{_libdir}/lv2/Proteus.lv2/
cp -ra %{__cmake_builddir}/Proteus_artefacts/VST3/Proteus.vst3/* %{buildroot}%{_libdir}/vst3/Proteus.vst3/

chrpath --delete %{buildroot}%{_libdir}/lv2/Proteus.lv2/libProteus.so
chrpath --delete `find %{buildroot}%{_libdir}/vst3/Proteus.vst3 -name Proteus.so`

install -m 755 -d %{buildroot}%{_datadir}/proteus/tones/
unzip %{SOURCE1}
mv ToneLibrary-%{toneversion}/Proteus/* %{buildroot}%{_datadir}/proteus/tones/

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/proteus/
%{_datadir}/proteus/tones/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Dec 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to 0.1-2 - add presets

* Wed Nov 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
