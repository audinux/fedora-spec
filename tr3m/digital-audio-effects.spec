# Status: active
# Tag: Jack, Effect, Compressor, Delay, Equalizer, Reverb, Overdrive, Modulation
# Type: Plugin, Standalone, VST3
# Category: Effect, Audio

%global commit0 375e968ca30af10062fd09c18241a270d91a2f88

Name: digital-audio-effects
Version: 0.0.1
Release: 2%{?dist}
Summary: A collection of real-time audio effect algorithms implemented in C++.
License: GPL-3.0-or-later
URL: https://github.com/Tr3m/Digital-Audio-Effects
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./tr3m-source.sh <PROJECT> <TAG>
#        ./tr3m-source.sh Digital-Audio-Effects master

Source0: Digital-Audio-Effects.tar.gz
Source1: tr3m-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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

%description
This a collection of real-time audio effect algorithms implemented in C++.
Each effect class is also demonstrated as an audio plug-in (Built using the JUCE Framework).

The effects implemented are the following:
- Time-Based:
  - Digital Delay
  - Reverb
- Modulation Effects:
  - Flanger
  - Chorus
  - Vibrado
- Distortion:
  - Vaccum Tube
  - Diode
  - Soft Clipper
  - Hard Clipper
  - Asymmetrical Clipping Distortion
- IIR Filters
  - 2nd Order Butterworth Low-Pass Filter
  - 2nd Order Butterworth High-Pass Filter
  - Peaking Filter
- Dynamic Effects:
  - Compressor
  - Limiter
- Utility Classes:
  - Comb Filter
  - Comb Filter (w/ Linear Interpolation)
  - Modulated Comb Filter
  - All-Pass Filter
  - All-Pass Filter (w/ Linear Interpolation)
  - Modulated All-Pass Filter
  - LFO (Low Frequency Oscillator)
  - Envelope Detector

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Digital-Audio-Effects

sed -i -e "s/PRODUCT_NAME \"Digital Delay\"/PRODUCT_NAME \"Digital_Delay\"/g" plugins/Delay/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"IIR Filter\"/PRODUCT_NAME \"IIR_Filter\"/g" plugins/IIRFilter/CMakeLists.txt

%build

FILES="Chorus
Compressor
Delay
Distortion
Flanger
IIRFilter
Limiter
Reverb
Vibrado"

for File in $FILES
do
    cd plugins/$File
    %cmake
    %cmake_build
    cd ../..
done

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/

FILES="./Vibrado/%{__cmake_builddir}/VIBRADO_PLUGIN_artefacts
./IIRFilter/%{__cmake_builddir}/IIR_FILTER_PLUGIN_artefacts
./Reverb/%{__cmake_builddir}/REVERB_PLUGIN_artefacts
./Distortion/%{__cmake_builddir}/DISTORTION_PLUGIN_artefacts
./Chorus/%{__cmake_builddir}/CHORUS_PLUGIN_artefacts
./Limiter/%{__cmake_builddir}/LIMITER_PLUGIN_artefacts
./Compressor/%{__cmake_builddir}/COMPRESSOR_PLUGIN_artefacts
./Delay/%{__cmake_builddir}/DELAY_PLUGIN_artefacts
./Flanger/%{__cmake_builddir}/FLANGER_PLUGIN_artefacts"

cd plugins
for File in $FILES
do
    uppercase_File="${File^}"
    cp -ra $File/Standalone/* %{buildroot}/%{_bindir}/
    cp -ra $File/VST3/* %{buildroot}/%{_libdir}/vst3/
done
cd ..

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Aug 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - remove unused dep

* Sun Sep 15 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
