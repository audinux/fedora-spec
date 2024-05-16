# Tag: Equalizer
# Type: VST3
# Category: Audio, Effect
# LastSourceUpdate: 2021

Name:    frequalizer
Version: 1.0.0
Release: 2%{?dist}
Summary: Equalizer using JUCE new dsp module
License: GPL-3.0-only
URL:     https://github.com/ffAudio/Frequalizer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./frequalizer-source.sh <TAG>
# ./frequalizer-source.sh c4b1b611c8d818107639c79f974bca6a414d672d

Source0: Frequalizer.tar.gz
Source1: Frequalizer.jucer
Source2: frequalizer-source.sh

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: JUCE61
BuildRequires: xorg-x11-server-Xvfb

%description
This is a JUCE project using the new dsp module for an Equalizer. It features:
 - six individual bands
 - an input and an output analyser
 - solo each band
 - drag frequency and gain directly in the graph

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Frequalizer

%build

%cmake -DCOPY_FOLDER=copy_folder
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/frequalizer_artefacts/VST3/* %{buildroot}%{_libdir}/vst3

%files
%doc README.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Oct 23 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- 1.0.0-2

* Sat Jan 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
