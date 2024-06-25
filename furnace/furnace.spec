# Tag: Tracker, MIDI, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: furnace
Version: 0.6.5
Release: 4%{?dist}
Summary: A multi-system chiptune tracker compatible with DefleMask modules
License: GPL-2.0-only
URL: https://github.com/tildearrow/furnace
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-furnace.sh v0.6.5

Source0: furnace.tar.gz
Source1: source-furnace.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: flac-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: mpg123-devel
BuildRequires: speex-devel
BuildRequires: sqlite-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrender-devel
BuildRequires: wayland-devel
BuildRequires: libsndfile-devel
BuildRequires: rtmidi-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libglvnd-devel
BuildRequires: fftw-devel
BuildRequires: fmt-devel
BuildRequires: SDL2-devel
BuildRequires: patchelf
BuildRequires: desktop-file-utils

%description
A multi-system chiptune tracker compatible with DefleMask modules

%prep
%autosetup -n %{name}

%build

# https://github.com/tildearrow/furnace#cmake-options
%cmake -DSYSTEM_FFTW=ON -DSYSTEM_FMT=ON -DSYSTEM_LIBSNDFILE=ON \
       -DSYSTEM_RTMIDI=ON -DSYSTEM_ZLIB=ON -DSYSTEM_SDL2=ON
%cmake_build

%install

%cmake_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/furnace/*
%{_datadir}/furnace/*
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/furnace.xml
%{_datadir}/locale/locale/*

%changelog
* Tue Jun 25 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-4
- Update to 0.6.5-4

* Wed Jun 19 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-4
- Update to 0.6.4-4

* Thu May 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-4
- Update to 0.6.3-4

* Mon Apr 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-4
- Update to 0.6.2-4

* Sat Feb 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-4
- Update to 0.6.1-4

* Wed Oct 04 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6-4
- Update to 0.6-4 - use system fftw

* Mon Oct 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6-3
- Update to 0.6-3

* Fri Sep 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-3
- use system libs

* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-1
- Initial spec file
