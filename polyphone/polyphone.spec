# Global variables for github repository
%global commit0 5f5953d6205c8bba820e8693b380952933574359
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: SF2, Sample
# Type: Standalone
# Category: Audio, Tool
# GUIToolkit: Qt5

Name:    polyphone
Version: 2.2.0
Release: 3%{?dist}
Summary: A SF2 sound font editor
URL:     https://polyphone-soundfonts.com/
License: GPLv2+

Source0: https://github.com/davy7125/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  polyphone-0001-add-missing-header.patch

BuildRequires: gcc gcc-c++ sed
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel 
BuildRequires: rtmidi-devel 
BuildRequires: stk-devel 
BuildRequires: qcustomplot-devel 
BuildRequires: libvorbis-devel 
BuildRequires: libogg-devel 
BuildRequires: zlib-devel
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: flac-devel

%description
Polyphone is a free software for editing soundfonts in format sf2.
These files contain a multitude of audio samples put together and configured so
as to form musical instruments that can be used by synthesizers such
as fluidsynth and played using a MIDI keyboard.
The goal of Polyphone is to provide:

* a simple and efficient interface for creating and editing .sf2 files,
  available on Windows, Mac OS X and Linux, tools to facilitate and automate
  the editing of different parameters, making it possible to handle a
  large amount of data.

* Polyphone is licensed under GNU General Public License.
  Anyone may thus access the source code, and is welcome to help
  in the development of the program.

%prep
%autosetup -p1 -n %{name}-%{commit0}

sed -i -e "s/usr\/local/usr\//g" sources/polyphone.pro

%build

cd sources

%qmake_qt5 "DEFINES+=USE_LOCAL_RTMIDI USE_LOCAL_QCUSTOMPLOT" polyphone.pro
%make_build

%install

cd sources

%__install -m 755 -d %{buildroot}/%{_datadir}/applications/
%__install -m 644 contrib/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 bin/polyphone %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
%__install -m 644 contrib/%{name}.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

%__install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
%__install -m 644 resources/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.svg

# TODO: install man pages

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Drumming \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc sources/changelog README.md sources/README
%license LICENSE.txt
%{_bindir}/polyphone
%{_datadir}/applications/polyphone.desktop
%{_datadir}/mime/packages/polyphone.xml
%{_datadir}/icons/hicolor/*

%changelog
* Tue Oct 13 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-3
- fix debug build

* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-2
- fix for fedora 33

* Sat Nov 16 2019 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-1
- update to 2.2.0

* Wed Oct 23 2019 Yann Collette <ycollette.nospam@free.fr> - 2.1.3-1
- update to 2.1.3

* Mon Sep 16 2019 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-1
- update to 2.1.1

* Fri Sep 6 2019 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- update to 2.1.0

* Thu Jan 24 2019 Yann Collette <ycollette.nospam@free.fr> - 2.0.1-2
- fix permission
- update to 2.0.1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-1
- update for Fedora 29

* Wed Nov 15 2017 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-1
- update to 1.9.0

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-1
- Update to 1.8.0

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- Initial spec file 1.6.0
