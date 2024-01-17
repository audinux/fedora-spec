# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# GUIToolkit: GTK3

Name:    ts-m1n3
Version: 1.2
Release: 1%{?dist}
Summary: TS-9 guitar pedal clone using neural networks.
License: GPL-2.0-or-later
URL:     https://github.com/GuitarML/TS-M1N3

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh TS-M1N3 d3e8e0d1f90953464b831493bd9360ee7553a8a7

Source0: TS-M1N3.tar.gz
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
%if 0%{?fedora} >= 38
BuildRequires: xsimd8-devel
%else
BuildRequires: xsimd-devel
%endif
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: chrpath

%description
TS-M1N3 is a guitar plugin clone of the TS-9 Tubescreamer
overdrive pedal. Machine learning was used to train a model
of both the drive and tone knobs for an accurate recreation
of the pedal in all possible configurations. This plugin
uses two conditioned parameters during model training to
recreate the entire device using machine learning, as opposed
to snapshot models at a particular setting. For best results,
use prior to amp -> cabinet -> reverb effects to fully simulate
playing an overdrive pedal through a physical amplifier.
This can be done with the NeuralPi plugin.

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
%autosetup -n TS-M1N3

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

install -m 755 -d %{buildroot}%{_libdir}/vst3/TS-M1N3.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/TS-M1N3.lv2/

cp -ra %{__cmake_builddir}/TS-M1N3_artefacts/LV2/TS-M1N3.lv2/* %{buildroot}%{_libdir}/lv2/TS-M1N3.lv2/
cp -ra %{__cmake_builddir}/TS-M1N3_artefacts/VST3/TS-M1N3.vst3/* %{buildroot}%{_libdir}/vst3/TS-M1N3.vst3/

chrpath --delete %{buildroot}%{_libdir}/lv2/TS-M1N3.lv2/libTS-M1N3.so
chrpath --delete `find %{buildroot}%{_libdir}/vst3/TS-M1N3.vst3 -name TS-M1N3.so`

%files
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Nov 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
