# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, VST3, LV2
# Category: Effect

%global commit0 96809cc6b3b33054815e740065a0bf265c344dd8

Name: luna-co-software
Version: 0.0.1
Release: 10%{?dist}
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
%autosetup -n dusk-audio-plugins

sed -i -e "s/PLUGIN_NAME \"Spectrum Analyzer\"/PLUGIN_NAME \"Spectrum_Analyzer\"/g" plugins/spectrum-analyzer/CMakeLists.txt
sed -i -e "s/PLUGIN_NAME \"4K EQ\"/PLUGIN_NAME \"4K_EQ\"/g" plugins/4k-eq/CMakeLists.txt

sed -i -e "s/PRODUCT_NAME \"Spectrum Analyzer\"/PRODUCT_NAME \"Spectrum_Analyzer\"/g" plugins/spectrum-analyzer/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"4K EQ\"/PRODUCT_NAME \"4K_EQ\"/g" plugins/4k-eq/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Tape Echo\"/PRODUCT_NAME \"Tape_Echo\"/g" plugins/tape-echo/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Convolution Reverb\"/PRODUCT_NAME \"Convolution_Reverb\"/g" plugins/convolution-reverb/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Chord Analyzer\"/PRODUCT_NAME \"Chord_Analyzer\"/g" plugins/chord-analyzer/CMakeLists.txt

%build

%set_build_flags
export CXXFLAGS="-DJUCE_IGNORE_VST3_MISMATCHED_PARAMETER_ID_WARNING $CXXFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra %{__cmake_builddir}/bin/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/LV2/* %{buildroot}%{_libdir}/lv2/

VST3_PLUGIN_LIST=`find %{__cmake_builddir}/plugins -name "VST3" | grep artefacts`
LV2_PLUGIN_LIST=`find %{__cmake_builddir}/plugins -name "LV2" | grep artefacts`

for Files in $VST3_PLUGIN_LIST
do
    cp -ra $Files %{buildroot}%{_libdir}/vst3/
done

for Files in $LV2_PLUGIN_LIST
do
    cp -ra $Files %{buildroot}%{_libdir}/lv2/
done

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun May 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-10
- update to 0.0.1-10 - 96809cc6b3b33054815e740065a0bf265c344dd8

* Thu Apr 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-9
- update to 0.0.1-9 - update to 299764a1e2b40bf86cd3fc10aa9c794710c72505

* Sun Mar 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-8
- update to 0.0.1-8 - update to 5838084a2ab14f56da8be628010ee275d339d7e1

* Sun Mar 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-7
- update to 0.0.1-7 - update to 721f3dd5cb3f32597973f605abddfd79a401fcd2

* Wed Feb 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6
- update to 0.0.1-6 - update to df0f370efde85dbc0a56978ca7a85d92170b1292

* Thu Feb 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 0.0.1-5 - update to 07e149aa68c5633a25c08708fa61d2e912cfb97f

* Sun Feb 08 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 0.0.1-4 - update to d5c04615c670a36b5429d798cc5fb83cf5f1dc72

* Sat Feb 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3 - update to 776ab4484ea414aa28328b51395e51d4da540a26

* Fri Feb 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - update to af81a3563b3d16b638cb1902e6c1c7e552410c41

* Mon Feb 02 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
