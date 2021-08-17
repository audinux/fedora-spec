# Global variables for github repository
%global commit0 b8f00a788bdc3205c6b39c743df93339cd261899
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Equalizer
# Type: VST
# Category: Audio, Effect
# LastSourceUpdate: 2021

Name:    frequalizer
Version: 1.0.0
Release: 1%{?dist}
Summary: Equalizer using JUCE new dsp module
License: GPLv3
URL:     https://github.com/ffAudio/Frequalizer

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: JUCE == 5.4.2

%description
This is a JUCE project using the new dsp module for an Equalizer. It features:
 - six individual bands
 - an input and an output analyser
 - solo each band
 - drag frequency and gain directly in the graph

%prep
%autosetup -n Frequalizer-%{commit0}

%build

%set_build_flags

Projucer --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE/modules/
Projucer --resave Frequalizer.jucer

cd Builds/LinuxMakefile

%make_build STRIP=true CPPFLAGS="%{optflags}"

%install 

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -p build/receivemidi %{buildroot}/%{_bindir}/

%files
%doc README.md
%license COPYING.md
%{_bindir}/*

%changelog
* Sat Jan 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- Initial spec file
