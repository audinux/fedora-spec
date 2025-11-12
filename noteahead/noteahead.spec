# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

Summary: A simple MIDI tracker and sequencer
Name: noteahead
Version: 0.15.0
Release: 1%{?dist}
License: GPLv2+
URL: https://github.com/juzzlin/Noteahead
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/juzzlin/Noteahead/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-linguist
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
A simple MIDI tracker and sequencer for Linux focusing on ease of use. There are no audio tracks, only MIDI.
Noteahead is designed to be especially a MIDI tracker so it has/will have features that make MIDI sequencing
as easy as possible, e.g. setting filter cutoff or changing patch on-the-fly without entering cryptic hex
values on a panning column.
Noteahead is still a work in progress and there's a lot of limitations and missing features.
However, I'm already using it for my own music.

%prep
%autosetup -n Noteahead-%{version}

sed -i -e "s/Categories=Audio;/Categories=Audio;AudioVideo/g" data/linux/noteahead.desktop
sed -i -e "/<screenshots>/d" data/linux/noteahead.appdata.xml
sed -i -e "/<\/screenshots>/d" data/linux/noteahead.appdata.xml

%build

%cmake 
%cmake_build

%install

%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/noteahead.appdata.xml

%files
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/metainfo/noteahead.appdata.xml
%{_datadir}/pixmaps/*.png

%changelog
* Tue Nov 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.15.0-1
- update to 0.15.0-1

* Sun Oct 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.14.1-1
- update to 0.14.1-1

* Sat Oct 18 2025 Yann Collette <ycollette.nospam@free.fr> - 0.14.0-1
- update to 0.14.0-1

* Wed Oct 08 2025 Yann Collette <ycollette.nospam@free.fr> - 0.13.0-1
- update to 0.13.0-1

* Thu Sep 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- update to 0.12.0-1

* Mon Jul 21 2025 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- update to 0.10.0-1

* Wed Jun 11 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- update to 0.9.0-1

* Fri May 30 2025 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Sun May 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0-1

* Tue Apr 15 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-1
- initial build
