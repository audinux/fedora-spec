# Tag: Tracker, MIDI, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    furnace
Version: 0.5.8
Release: 3%{?dist}
Summary: A multi-system chiptune tracker compatible with DefleMask modules
License: GPLv2
URL:     https://github.com/tildearrow/furnace

Vendor:       Audinux
Distribution: Audinux

# To get the sources, use:
# $ ./source-furnace.sh v0.5.8

Source0: furnace.tar.gz
Source1: source-furnace.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
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
BuildRequires: fmt-devel
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: patchelf

%description
A multi-system chiptune tracker compatible with DefleMask modules

%prep
%autosetup -n %{name}

%build

%cmake -DSYSTEM_FMT=ON -DSYSTEM_LIBSNDFILE=ON -DSYSTEM_RTMIDI=ON -DSYSTEM_ZLIB=ON -DSYSTEM_SDL2=ON
%cmake_build

%install 

%cmake_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/furnace/
%{_datadir}/doc/furnace/papers/*
%{_datadir}/furnace/
%{_datadir}/furnace/demos/*
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Fri Sep 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-3
- use system libs

* Tue Mar 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.8-1
- Initial spec file
