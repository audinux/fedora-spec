# Tag: MIDI, FM, Tracker
# Type: Standalone
# Category: Audio, Synthesizer, Sequencer

# Global variables for github repository
%global commit0 1a0c8afc1187a0e7aa98074a63a6a360eec04b87
%global gittag0 v1.7.6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: Chiptune tracker for making chiptune-like music on a modern computer.
Name: klystrack
Version: 1.7.6
Release: 4%{?dist}
License: GPL
URL: https://kometbomb.github.io/klystrack/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the source archive:
# ./klystrack-source.sh v1.7.6

Source0: klystrack.tar.gz
Source1: klystrack-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_gfx-devel
BuildRequires: SDL2_image-devel
BuildRequires: desktop-file-utils

%description
Tracker for making C64/NES/Amiga-style chiptunes on a modern platform.
- Sound
  - Additive synthesis with filters (think SID, Atari, NES etc.)
  - Hard sync and ring modulation (like SID)
  - FM synthesis (think Adlib, MSX, OPL2 etc.)
  - Wavetable for samples or custom waveforms to be used in synthesis (think Amiga, SNES)
  - Built-in wave generator and editor
  - Programmable instruments not limited to simple arpeggios
- Sequencer
  - Tracker with free positioning of patterns
  - Pattern transpose
  - Pattern length is not fixed
- Effects: Stereo chorus ; SNES-style multitap echo ; Bit crusher/decimator
- Export: custom format ; Wav ...
- Import: Wav ; ProTracker, FT2 ; C64 SID files ...

%prep
%autosetup -n %{name}

sed -i -e "s/-Werror//g" Makefile
# Allow multiple definition of symbols
sed -i -e "s/LDFLAGS :=/LDFLAGS := -z muldefs/g" Makefile
# Add Fedora compile flags
sed -i -e "s/CFLAGS :=/CFLAGS := \$(MYCFLAGS)/g" Makefile
# Remove stripping for debug package generation
sed -i -e "s/CFLAGS += -O3 -Wall -s/CFLAGS += -O3 -Wall/g"  Makefile
# Clean desktop file
sed -i -e "s/AudioVideo;AudioVideoEditing/Audio/g" linux/klystrack.desktop

%build

%set_build_flags

%make_build MYCFLAGS="$CFLAGS" DESTDIR=%{buildroot} PREFIX=/usr RES_PATH=/usr/share/%{name}/ CFG=release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp bin.release/%{name} %{buildroot}/%{_bindir}/

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack klystrack
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse klystrack
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p icon/256x256.png %{buildroot}/%{_datadir}/icons/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 -p linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
install -m 644 -p linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop

# Adjust the desktop file
sed -i -e "s/Exec=klystrack/Exec=klystrack-jack/g"  %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
sed -i -e "s/Exec=klystrack/Exec=klystrack-pulse/g" %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop

sed -i -e "s/Name=Klystrack/Name=klystrack-jack/g"  %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
sed -i -e "s/Name=klystrack/Name=klystrack-pulse/g" %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop

sed -i -e "s/klystrack.png/klystrack/g" %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
sed -i -e "s/klystrack.png/klystrack/g" %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop

install -m 755 -d %{buildroot}%{_datadir}/%{name}/res
cp -r res/* %{buildroot}%{_datadir}/%{name}/res/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/doc
cp -r doc/* %{buildroot}%{_datadir}/%{name}/doc/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples/instruments/n00bstar-instruments/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples/songs/
cp -r examples/instruments/* %{buildroot}%{_datadir}/%{name}/examples/instruments/
cp -r examples/songs/*       %{buildroot}%{_datadir}/%{name}/examples/songs/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/themes
cp -r themes/* %{buildroot}%{_datadir}/%{name}/themes/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/key
cp -r key/* %{buildroot}%{_datadir}/%{name}/key/

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

desktop-file-install                         \
  --add-category="Audio;AudioVideo"          \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
* Sun Jun 20 2021 Yann Collette <ycollette dot nospam at free.fr> 1.7.6-4
- update to 1.7.6-4 - fix desktop file

* Tue Jun 30 2020 Yann Collette <ycollette dot nospam at free.fr> 1.7.6-3
- update to 1.7.6-3 - fix spec file

* Thu Apr 23 2020 Yann Collette <ycollette dot nospam at free.fr> 1.7.6-2
- update to 1.7.6-2 - fix for Fedora 32

* Wed Jul 17 2019 Yann Collette <ycollette dot nospam at free.fr> 1.7.6-1
- update to 1.7.6-1

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.7.5-1
- update for Fedora 29

* Thu Oct 4 2018 Yann Collette <ycollette dot nospam at free.fr> 1.7.5-1
- update to 1.7.5

* Fri Sep 21 2018 Yann Collette <ycollette dot nospam at free.fr> 1.7.4-1
- Initial release of spec file
