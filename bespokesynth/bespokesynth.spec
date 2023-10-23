# Tag: Modular
# Type: Standalone
# Category: Audio, Synthesizer

Name:    BespokeSynth
Version: 1.2.0
Release: 8%{?dist}
Summary: A software modular synth
License: GPL-3.0-or-later
URL:     https://github.com/BespokeSynth/BespokeSynth

Vendor:       Audinux
Distribution: Audinux

# ./bespokesynth-sources.sh <tag>
# ./bespokesynth-sources.sh v1.2.0

Source0: BespokeSynth.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: bespokesynth-sources.sh

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: patchelf
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: python3-devel
BuildRequires: pybind11-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libglvnd-devel
BuildRequires: libusbx-devel
BuildRequires: libpng-devel
BuildRequires: jsoncpp-devel
BuildRequires: desktop-file-utils

Requires: youtube-dl
Requires: ffmpeg

%description
Bespoke is a software modular synthesizer. It contains a bunch of modules,
which you can connect together to create sounds.
Bespoke is like a DAW in some ways, but with less of a focus on a global timeline.
Instead, it has a design more optimized for jamming and exploration.

%prep
%autosetup -p1 -n %{name}

sed -i -e "s/\.\.\/\.\.\/MacOSX\/build\/Release\/data/\/usr\/share\/BespokeSynth\/data/g" Source/OpenFrameworksPort.cpp

unzip %{SOURCE1}

# cp %{SOURCE2} libs/JUCE/modules/juce_audio_processors/format_types/

# Manage VST path
sed -i -e "s/lib\/vst/%{_lib}\/vst/g" libs/JUCE/modules/juce_audio_processors/format_types/juce_VSTPluginFormat.cpp
sed -i -e "s/lib\/vst3/%{_lib}\/vst3/g" libs/JUCE/modules/juce_audio_processors/format_types/juce_VST3PluginFormat.cpp
sed -i -e "s/lib\/vst3/%{_lib}\/vst3/g" VST_SDK/VST3_SDK/public.sdk/source/vst/hosting/module_linux.cpp

# Work around with an incompatibility with pybind11
%if 0%{?fedora} >= 37
rm -rf libs/pybind11/include/pybind11/
ln -s /usr/include/pybind11 libs/pybind11/include/pybind11
%endif

%build

%set_build_flags

export CXXFLAGS="$CXXFLAGS -include memory"

%cmake \
    -DBESPOKE_VST2_SDK_LOCATION=`pwd`/VST_SDK/VST2_SDK \
    -DBESPOKE_SYSTEM_PYBIND11=ON \
    -DBESPOKE_SYSTEM_JSONCPP=ON
%cmake_build

%install

%cmake_install

# Install manually some thirdparty libraries
mkdir -p %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/push2/libpush2.so               %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/psmove/libpsmove.so             %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/freeverb/libfreeverb.so         %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/oddsound-mts/liboddsound-mts.so %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/xwax/libxwax.so                 %{buildroot}/%{_libdir}/bespokesynth/
cp %{__cmake_builddir}/libs/nanovg/libnanovg.so             %{buildroot}/%{_libdir}/bespokesynth/

patchelf --set-rpath '$ORIGIN/../%{_lib}/bespokesynth/' %{buildroot}/%{_bindir}/BespokeSynth

# Install desktop file
desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/BespokeSynth.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/BespokeSynth.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/bespokesynth/**
%{_datadir}/applications/*
%{_datadir}/BespokeSynth/*
%{_datadir}/icons/*

%changelog
* Fri Jul 14 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-8
- update to 1.2.0-7

* Wed Jan 05 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-8
- fix default vst search paths

* Tue Nov 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-7
- update to 1.1.0-7

* Thu Sep 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-7
- update to 1.0.0-7 - fix install

* Thu Sep 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-6
- update to 1.0.0-6 - fix install

* Tue Sep 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-5
- update to 1.0.0-5

* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update for fedora 33

* Wed Sep 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to v0.0005-pre

* Wed Aug 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to v0.0004-pre - dc51a8783f71fc5a8f019beb0783d35d9ec5474c

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Fix install

* Tue May 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
