# Tag: Audio, Effect, Tool
# Type: Standalone, Plugin, VST
# Category: Tool, Audio, Effect

Name: sparta
Version: 1.7.0
Release: 1%{?dist}
Summary: A collection of spatial audio related VST plug-ins developed using JUCE and the Spatial_Audio_Framework
License: GPL-3.0-or-later
URL: https://leomccormack.github.io/sparta-site/

Vendor:       Audinux
Distribution: Audinux

# Usage: ./sparta-source.sh <TAG>
#        ./sparta-source.sh v1.7.0

Source0: SPARTA.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: sparta-source.sh

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
BuildRequires: webkit2gtk3-devel
BuildRequires: lapack-devel
BuildRequires: openblas-devel
BuildRequires: chrpath

%description
Spatial Audio Real-Time Applications (SPARTA) [1].
A collection of VST audio plug-ins for spatial audio
production, reproduction and visualisation

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n SPARTA

# SPARTA/SDKs/VST2_SDK
unzip %{SOURCE1}

mv VST_SDK/VST2_SDK SDKs/

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="-include utility -fPIC $CXXFLAGS" \
       -DSAF_PERFORMANCE_LIB=SAF_USE_OPEN_BLAS_AND_LAPACKE \
       -DCMAKE_SKIP_RPATH=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_array2sh_/sparta_array2sh_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_panner_/sparta_panner_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_ambiRoomSim_/sparta_ambiRoomSim_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_ambiENC_/sparta_ambiENC_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_rotator_/sparta_rotator_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_beamformer_/sparta_beamformer_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_matrixConv_/sparta_matrixconv_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_pitchShifter_/sparta_pitchShifter_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_ambiDRC_/sparta_ambiDRC_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_decorrelator_/sparta_decorrelator_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/audio_plugins/_SPARTA_multiConv_/sparta_multiconv_artefacts/Release/VST/* %{buildroot}%{_libdir}/vst/

%files
%doc README.md
%license LICENSE

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Mon Jan 29 2024 Yann Collette <ycollette.nospam@free.fr> - 1.7.0-1
- update to 1.7.0-1

* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 1.6.2-1
- Initial spec file
