# Tag: Sf2, Sf3
# Type: Standalone
# Category: Tool

Name:    sftools
Version: 1.0.0
Release: 1%{?dist}
Summary: Tools for sound font files
License: GPLv2
URL:     https://github.com/musescore/sftools

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/musescore/sftools/archive/refs/heads/master.zip#/sftools.zip

BuildRequires: gcc gcc-c++
BuildRequires: libvorbis-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libsndfile-devel
BuildRequires: cmake

%description
Utilities for SoundFont files.
- compress sound font files with ogg vorbis for use with MuseScore
- convert to "C" for embedding

%prep
%autosetup -n sftools-master

%build

%cmake 
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license COPYING.LIB
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Jul 19 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial spec file.
