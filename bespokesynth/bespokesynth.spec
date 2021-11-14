# Tag: Modular
# Type: Standalone
# Category: Audio, Synthesizer

%define _lto_cflags %{nil}

Name:    BespokeSynth
Version: 1.0.999
Release: 7%{?dist}
Summary: A software modular synth
License: GPLv2+
URL:     https://github.com/BespokeSynth/BespokeSynth

Vendor:       Audinux
Distribution: Audinux

# ./bespokesynth-sources.sh <tag>
# ./bespokesynth-sources.sh v1.0.999

Source0: BespokeSynth.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2
Source2: bespokesynth-sources.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: JUCE5
BuildRequires: python3-devel
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
BuildRequires: desktop-file-utils

%description
A Software modular synth 

%prep
%autosetup -n %{name}

tar xvfj %{SOURCE1}

sed -i -e "s/\.\.\/\.\.\/MacOSX\/build\/Release\/data/\/usr\/share\/BespokeSynth\/data/g" Source/OpenFrameworksPort.cpp

%build

%set_build_flags
export CXXFLAGS="-std=c++14 -I$CURRENTDIR/vst/vstsdk2.4/ -I/usr/include/freetype2 $CXXFLAGS"
export LDFLAGS="-lpython%{python3_version} $LDFLAGS"

%cmake
%cmake_build 

%install 

%cmake_install

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
%{_datadir}/*

%changelog
* Sun Nov 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.999-7
- update to 1.0.999-7 - test beta version

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
