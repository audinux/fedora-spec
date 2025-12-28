# Status: active
# Tag: Guitar, Amp Simul
# Type: Plugin, VST3, LV2
# Category: Audio, Effect
# GUIToolkit: GTK3

%define toneversion 1.0

Name: smartamp
Version: 1.3
Release: 3%{?dist}
Summary: Guitar plugin emulating real hardware with Neural Network
License: GPL-2.0-or-later
URL: https://github.com/GuitarML/SmartGuitarAmp
ExclusiveArch: x86_64 aarch64

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
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: unzip

%description
SmartGuitarAmp is a guitar plugin (VST3) made with JUCE that uses neural network models to emulate real world hardware.

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

%cmake -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"
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
%{_datadir}/smartamp/
%{_datadir}/smartamp/tones/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Aug 23 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3-3
- update to 1.3-3 - remove unused dep

* Fri Dec 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3-2
- update to 1.3-2 - add presets

* Wed Aug 31 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3-1
- update to 1.3-1

* Sun Feb 21 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec file
