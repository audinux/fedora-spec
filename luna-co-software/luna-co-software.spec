# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

%global commit0 7d8b31734a0a61e16bac37808a9217bde91c854b

Name: luna-co-software
Version: 0.0.1
Release: 1%{?dist}
Summary: A collection of professional audio VST3/LV2 plugins built with JUCE
License: GPL-2.0-or-later
URL: https://github.com/luna-co-software/plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./luna-co-software-source.sh <TAG>
#        ./luna-co-software-source.sh main

Source0: plugins.tar.gz
Source1: luna-co-software-source.sh

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

%description
This is a multi-band distortion plugin 『Fire』.
It can be used in DAWs which supports AU and Vst3 plugins such
as Ableton Live, Fl Studio, etc.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

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
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n plugins

sed -i -e "s/PLUGIN_NAME \"Spectrum Analyzer\"/PLUGIN_NAME \"Spectrum_Analyzer\"/g" plugins/spectrum-analyzer/CMakeLists.txt
sed -i -e "s/PLUGIN_NAME \"Neural Amp\"/PLUGIN_NAME \"Neural_Amp\"/g" plugins/neural-amp/CMakeLists.txt
sed -i -e "s/PLUGIN_NAME \"4K EQ\"/PLUGIN_NAME \"4K_EQ\"/g" plugins/4k-eq/CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/plugins/spectrum-analyzer/SpectrumAnalyzer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/spectrum-analyzer/SpectrumAnalyzer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/chord-analyzer/ChordAnalyzer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/chord-analyzer/ChordAnalyzer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/neural-amp/NeuralAmp_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/neural-amp/NeuralAmp_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/multi-q/MultiQ_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/multi-q/MultiQ_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/SilkVerb/SilkVerb_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/SilkVerb/SilkVerb_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/convolution-reverb/ConvolutionReverb_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/convolution-reverb/ConvolutionReverb_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/groovemind/GrooveMind_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/groovemind/GrooveMind_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Feb 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
