# Tag: Equalizer
# Type: VST
# Category: Audio, Effect
# LastSourceUpdate: 2021

# Global variables for github repository
%global commit0 b8f00a788bdc3205c6b39c743df93339cd261899
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    frequalizer
Version: 1.0.0
Release: 1%{?dist}
Summary: Equalizer using JUCE new dsp module
License: GPLv3
URL:     https://github.com/ffAudio/Frequalizer

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: Frequalizer.jucer

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: JUCE5
BuildRequires: xorg-x11-server-Xvfb

%description
This is a JUCE project using the new dsp module for an Equalizer. It features:
 - six individual bands
 - an input and an output analyser
 - solo each band
 - drag frequency and gain directly in the graph

%prep
%autosetup -n Frequalizer-%{commit0}

cp %SOURCE1 .
sed -i -e "s|../../juce|/usr/src/JUCE5/modules|g" Frequalizer.jucer
sed -i -e "s|Frequalizer Free|Frequalizer|g" Frequalizer.jucer

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
export CFLAGS="-I/usr/include/freetype2 $CFLAGS"
export CXXFLAGS="-I/usr/include/freetype2 -include array $CXXFLAGS"

Projucer5 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE5/modules/
Projucer5 --resave Frequalizer.jucer

cd Builds/LinuxMakefile

sed -i -e "s|JucePlugin_Build_VST3=0|JucePlugin_Build_VST3=1|g" Makefile

%make_build CONFIG=Release STRIP=true

%install 

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -p build/Frequalizer %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*

%changelog
* Sat Jan 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- Initial spec file
