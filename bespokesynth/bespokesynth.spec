# Tag: Modular
# Type: Standalone
# Category: Audio, Synthesizer

%define _lto_cflags %{nil}

Name:    BespokeSynth
Version: 1.0.0
Release: 5%{?dist}
Summary: A software modular synth
License: GPLv2+
URL:     https://github.com/awwbees/BespokeSynth

Source0: https://github.com/awwbees/BespokeSynth/archive/refs/tags/v1.0.0.tar.gz#/%{name}-%{version}.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: JUCE5
BuildRequires: python2-devel
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
BuildRequires: xorg-x11-server-Xvfb

%description
A Software modular synth 

%prep
%autosetup -n %{name}-%{version}

tar xvfj %{SOURCE1}

sed -i -e "s/\.\.\/\.\.\/MacOSX\/build\/Release\/data/\/usr\/share\/BespokeSynth\/data/g" Source/OpenFrameworksPort.cpp

# For JUCE >= 6, no need to start an X server
%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

Projucer5 --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE5/modules/
Projucer5 --resave BespokeSynth.jucer

sed -i -e "s/python-config/python2-config/g" Builds/LinuxMakefile/Makefile

%build

export CURRENTDIR=`pwd`
cd Builds/LinuxMakefile
%{make_build} PREFIX=/usr LIBDIR=%{_libdir} CONFIG=Release CPPFLAGS="%{build_cxxflags}" CXXFLAGS="-std=c++14 -I$CURRENTDIR/vst/vstsdk2.4/ -I/usr/include/freetype2" LDFLAGS="-lpython%{python3_version} $LDFLAGS"

%install 

cd Builds/LinuxMakefile
install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 build/BespokeSynth %{buildroot}/%{_bindir}/

cd ../..
install -m 755 -d %{buildroot}/%{_datadir}/BespokeSynth/resource
cp -r Builds/MacOSX/build/Release/resource/* %{buildroot}/%{_datadir}/BespokeSynth/resource

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
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
