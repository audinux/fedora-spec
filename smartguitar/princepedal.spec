# Status: active
# Tag: Guitar, Amp Simul
# Type: Plugin, VST3, LV2
# Category: Audio, Effect
# GUIToolkit: GTK3

Name: princepedal
Version: 1.0
Release: 2%{?dist}
Summary: Prince of Tone style guitar plugin made with neural networks
License: GPL-2.0-or-later
URL: https://github.com/GuitarML/PrincePedal
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./source-guitarml.sh PrincePedal v1.0

Source0: PrincePedal.tar.gz
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
BuildRequires: xsimd-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: chrpath
BuildRequires: unzip

Requires: license-%{name}

%description
The Prince is a plugin of my homebuilt Prince of Tone style pedal,
cloned using neural networks.
The graphics were created from actual photos of my pedal using
a "stop motion" technique (not perfect but it works). The plugin
features three GuitarML neural network models conditioned on the
Gain and Tone knobs, one each for Overdrive, Boost, and Distortion
modes.
The Prince should be used with an impulse response plugin
(such as Pulse) to emulate playing the pedal through an amplifier.
The original Prince of Tone pedal is essentially 1/2 of the highly
sought after King of Tone by AnalogMan. Use two instances of the
Prince for a King of Tone - like experience!

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n PrincePedal

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

install -m 755 -d %{buildroot}%{_libdir}/vst3/Prince.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/Prince.lv2/
install -m 755 -d %{buildroot}%{_bindir}

cp -ra %{__cmake_builddir}/Prince_artefacts/LV2/Prince.lv2/* %{buildroot}%{_libdir}/lv2/Prince.lv2/
cp -ra %{__cmake_builddir}/Prince_artefacts/VST3/Prince.vst3/* %{buildroot}%{_libdir}/vst3/Prince.vst3/
cp -ra %{__cmake_builddir}/Prince_artefacts/Standalone/* %{buildroot}%{_bindir}/

chrpath --delete %{buildroot}%{_libdir}/lv2/Prince.lv2/libPrince.so
chrpath --delete `find %{buildroot}%{_libdir}/vst3/Prince.vst3 -name Prince.so`
chrpath --delete %{buildroot}%{_bindir}/Prince

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Aug 23 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2 - remove unused dep

* Fri Feb 24 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file
