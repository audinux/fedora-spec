# Tag: MIDI, Player
# Type: Standalone
# Category: Audio, MIDI, Tool

Name: pianobooster
Version: 1.0.0
Release: 8%{?dist}
Summary: A MIDI file player that teaches you how to play the piano
License: GPL-3.0-or-later
Url: https://github.com/captnfab/PianoBooster

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/captnfab/PianoBooster/archive/v%{version}.tar.gz#/PianoBooster-%{version}.tar.gz
Patch0: pianobooster-0001-fix-dejavu-font-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(ftgl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: hicolor-icon-theme

Requires: dejavu-sans-fonts
Requires: unzip
Requires: hicolor-icon-theme
Requires: %{name} = %{version}-%{release}
Requires: libnotify

Recommends: qt5-qttranslations

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano.

PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.

To run Piano Booster you need a MIDI Piano Keyboard and a MIDI interface
for the PC. If you don't have a MIDI keyboard you can still try out
PianoBooster, using the PC keyboard ('x' is middle C), but a MIDI piano
is really recommended.

%prep
%autosetup -p1 -n PianoBooster-%{version}

%build

%cmake -DUSE_SYSTEM_FONT=ON \
       -DUSE_JACK=ON \
       -DWITH_MAN=ON \
       -DWITH_INTERNAL_FLUIDSYNTH=OFF

%cmake_build

%install

%cmake_install

%files
%doc README.md Changelog.txt doc/faq.md
%license license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/music
%dir %{_datadir}/games/%{name}/translations
%{_datadir}/games/%{name}/music/*.zip
%{_datadir}/games/%{name}/translations/%{name}*.qm
%{_datadir}/games/%{name}/translations/*.json
%{_mandir}/man6/%{name}.6*

%changelog
* Sat Jan 14 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-8
- update to 1.0.0-8 - fix font path - use system fluidsynth

* Sun Dec 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.2b-2
- fix for Fedora 33

* Tue Mar 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.2b-1
- initial specfile

