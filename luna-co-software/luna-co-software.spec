# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

%global commit0 07e149aa68c5633a25c08708fa61d2e912cfb97f

Name: luna-co-software
Version: 0.0.1
Release: 5%{?dist}
Summary: A collection of professional audio VST3/LV2 plugins built with JUCE
License: GPL-3.0-or-later
URL: https://github.com/dusk-audio/dusk-audio-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./luna-co-software-source.sh <TAG>
#        ./luna-co-software-source.sh main

Source0: dusk-audio-plugins.tar.gz
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

Requires: license-%{name}

%description
This is a multi-band distortion plugin 『Fire』.
It can be used in DAWs which supports AU and Vst3 plugins such
as Ableton Live, Fl Studio, etc.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n plugins

sed -i -e "s/PLUGIN_NAME \"Spectrum Analyzer\"/PLUGIN_NAME \"Spectrum_Analyzer\"/g" plugins/spectrum-analyzer/CMakeLists.txt
sed -i -e "s/PLUGIN_NAME \"4K EQ\"/PLUGIN_NAME \"4K_EQ\"/g" plugins/4k-eq/CMakeLists.txt

sed -i -e "s/PRODUCT_NAME \"Spectrum Analyzer\"/PRODUCT_NAME \"Spectrum_Analyzer\"/g" plugins/spectrum-analyzer/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"4K EQ\"/PRODUCT_NAME \"4K_EQ\"/g" plugins/4k-eq/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Tape Echo\"/PRODUCT_NAME \"Tape_Echo\"/g" plugins/tape-echo/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Convolution Reverb\"/PRODUCT_NAME \"Convolution_Reverb\"/g" plugins/convolution-reverb/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Chord Analyzer\"/PRODUCT_NAME \"Chord_Analyzer\"/g" plugins/chord-analyzer/CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/bin/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/Standalone/* %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/plugins/spectrum-analyzer/SpectrumAnalyzer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/spectrum-analyzer/SpectrumAnalyzer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/spectrum-analyzer/SpectrumAnalyzer_artefacts/Standalone/* %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/plugins/chord-analyzer/ChordAnalyzer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/chord-analyzer/ChordAnalyzer_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/plugins/Velvet90/Velvet90_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/Velvet90/Velvet90_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/Velvet90/Velvet90_artefacts/Standalone/* %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/plugins/convolution-reverb/ConvolutionReverb_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/convolution-reverb/ConvolutionReverb_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/convolution-reverb/ConvolutionReverb_artefacts/Standalone/* %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/plugins/groovemind/GrooveMind_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/plugins/groovemind/GrooveMind_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/plugins/groovemind/GrooveMind_artefacts/Standalone/* %{buildroot}%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Feb 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 0.0.1-4 - update to 07e149aa68c5633a25c08708fa61d2e912cfb97f

* Sun Feb 08 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 0.0.1-4 - update to d5c04615c670a36b5429d798cc5fb83cf5f1dc72

* Sat Feb 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3 - update to 776ab4484ea414aa28328b51395e51d4da540a26

* Fri Feb 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - update to af81a3563b3d16b638cb1902e6c1c7e552410c41

* Mon Feb 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
