# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

Name:    chameleon
Version: 1.2
Release: 1%{?dist}
Summary: Vintage guitar amp using neural networks.
License: GPLv2+
URL:     https://github.com/GuitarML/Chameleon

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh Chameleon aff99fe483d4d264638f719e1ffa67575bb9f1ea

Source0: Chameleon.tar.gz
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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: xsimd-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: chrpath

%description
Chameleon is a guitar plugin using neural networks to create
three distinct sounds from a vintage style amp head. EQ and
gain were added to allow further modification of the three
core sounds, named Red (high gain), Gold (crunchy), and Green
(crisp and clean). In the same way a real amp head is used
with a cabinet and other effects, this plugin is intended to
be used in the signal chain along with IR's (cab sim), reverb,
and any number of guitar effects.

Chameleon's core sound comes from a neural net inference engine
which allows the plugin to disguise itself as a high end tube
amplifier. The engine uses a stateful LSTM model, which improves
the sound quality of the previous stateless LSTM used in the
SmartAmpPro. It also improves CPU usage compared to the
SmartAmpPro and SmartGuitarAmp.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Chameleon

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

%set_build_flags

%cmake
%cmake_build

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/Chameleon.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/Chameleon.lv2/

cp -ra %{__cmake_builddir}/Chameleon_artefacts/LV2/Chameleon.lv2/* %{buildroot}%{_libdir}/lv2/Chameleon.lv2/
cp -ra %{__cmake_builddir}/Chameleon_artefacts/VST3/Chameleon.vst3/* %{buildroot}%{_libdir}/vst3/Chameleon.vst3/

chrpath --delete %{buildroot}%{_libdir}/lv2/Chameleon.lv2/libChameleon.so
chrpath --delete `find %{buildroot}%{_libdir}/vst3/Chameleon.vst3 -name Chameleon.so`

%files
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Nov 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
