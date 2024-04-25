# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Summary: JackDirector is a GNU/Linux app that lets you control Jack Audio Connection Kit's transport play/pause using midi commands
Name: jack-director
Version: 0.1.1
Release: 1%{?dist}
License: GPL-2.0-only
URL: https://toxic.cubicarea.it/#jack-director

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/jack-director/files/JackDirector-%{version}.tar.gz
Patch0: jack-director-0001-fix-return-value.patch

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel

%description
JackDirector is a GNU/Linux app that lets you control Jack Audio Connection Kit's transport play/pause using midi commands (noteon) and let you assign
bpm changes and other commands to midi program changes. This program plays a metronome thru 2 audio outputs exposed in Jack.
Features:
- Control Jack Transport's play/pause using midi notes
- Control Jack Transport's position
- Metronome audio output
- Assign different scenes to different program changes
- Control bpm, mute metronome, song position, stop transport for every scene
- Output a midi clock out for programs allowing external midi sync (eg. wine programs)

To control its behavior you have to provide a configuration file named jack-directorrc.

%prep
%autosetup -p1 -n jack-director-code

sed -i -e "/QMAKE_CFLAGS_RELEASE/d" jack-director.pro

%build

%qmake_qt5
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 jack-director %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/jack-director/
install -m 755 jack-directorrc %{buildroot}/%{_datadir}/jack-director/

%files
%doc README
%license gpl-3.0.txt gpl-2.0.txt
%{_bindir}/*
%{_datadir}/jack-director/

%changelog
* Fri Dec 02 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- initial build.
