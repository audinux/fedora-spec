# Status: active
# Tag: Modular
# Type: Standalone
# Category: Audio, Synthesizer

%global commit0 f435799ad6ca15a892b628e0198153012fcd337b

Name: BespokeSynth-weekly
Version: 1.3.10
Release: 14%{?dist}
Summary: A software modular synth
License: GPL-3.0-or-later
URL: https://github.com/BespokeSynth/BespokeSynth
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./bespokesynth-sources.sh <tag>
# ./bespokesynth-sources.sh main

Source0: BespokeSynth.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: bespokesynth-sources.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: patchelf
BuildRequires: mold
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: jsoncpp-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libcurl-devel
BuildRequires: libglvnd-devel
BuildRequires: libpng-devel
BuildRequires: libusbx-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pulseaudio-libs-devel
BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: youtube-dl
Requires: (ffmpeg or ffmpeg-free)

Obsoletes: BespokeSynth < 1.3.9

%description
Bespoke is a software modular synthesizer. It contains a bunch of modules,
which you can connect together to create sounds.
Bespoke is like a DAW in some ways, but with less of a focus on a global timeline.
Instead, it has a design more optimized for jamming and exploration.

%prep
%autosetup -p1 -n BespokeSynth

sed -i -e "s/\.\.\/\.\.\/MacOSX\/build\/Release\/data/\/usr\/share\/BespokeSynth\/data/g" Source/OpenFrameworksPort.cpp

unzip %{SOURCE1}

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
    -DBESPOKE_SYSTEM_JSONCPP=ON \
    -DCMAKE_EXE_LINKER_FLAGS="-fuse-ld=mold"

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
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.bespokesynth.BespokeSynth.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/bespokesynth/*
%{_datadir}/applications/*
%{_datadir}/BespokeSynth/*
%{_datadir}/icons/*
%{_datadir}/metainfo/com.bespokesynth.BespokeSynth.metainfo.xml

%changelog
* Wed Feb 18 2026 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-14
- Update to 1.3.10-14 - f435799ad6ca15a892b628e0198153012fcd337b

* Tue Feb 03 2026 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-13
- Update to 1.3.10-13 - edd1d9e45325dab68e225a98256a74ac1ceaf220

* Thu Dec 25 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-12
- Update to 1.3.10-12 - 7df1d9236514772a7ab8a038846c8ef0515bfec1

* Wed Dec 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-11
- Update to 1.3.10-11 - 7df1d9236514772a7ab8a038846c8ef0515bfec1

* Fri Oct 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-10
- Update to 1.3.10-10 - 70aeb62b446c5c33d0386816027726f8419868e1

* Sat Aug 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-9
- Update to 1.3.10-9 - d6f17871eb52eb90db96cf4921ce577cab067061

* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-8
- Update to 1.3.10-8 - 772675272cbcb5fd57a0db8a31557cf3f3f36c21

* Tue Jul 22 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-7
- Update to 1.3.10-7 - 75a0040ca3c96ba93079560c47a42ba5de97a827

* Sun Jun 15 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-6
- Update to 1.3.10-6 - 734b62bcf67f622532db1b7fdc3a9609e6ea54ff

* Fri May 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-5
- Update to 1.3.10-5 - 11b88e396cc9c090cebfe2dcd81e0bcd40777bf6 

* Mon May 26 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-3
- Update to 1.3.10-3 - 0878b6c68a1d1ef883b78e0b00b1aa4c3cfaa9a1

* Mon Mar 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-2
- Update to 1.3.10-2 - 9e7f57e4dd2180451a9ea568f76f925f5d02f8ea

* Sun Dec 22 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-1
- Update to 1.3.10-1 - 1d0f0429d9b56f1b120b0b95f0a173cc02787e53

* Sun Dec 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.10-3
- Update to 1.2.10-3 - update to bc9dd72176ec469e20f978d1cae31503593ebe86

* Thu Nov 28 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.10-2
- Update to 1.2.10-2 - update to 09738d3fa21cf54326e7a75efe8dd2bc4183d47e 

* Sat Nov 02 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.10-1
- Update to 1.2.10-1 - fix requires 

* Thu Sep 05 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.9-1
- Initial spec file
