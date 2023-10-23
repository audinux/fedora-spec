#
# spec file for package simplesysexxer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 by Edgar Aichinger
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name: SimpleSysexxer
Version: 0.3
Release: 1%{?dist}
Summary: A MIDI SysEx Transfer Tool
License: GPL-2.0-or-later
URL: http://www.christeck.de/

Source: https://sourceforge.net/projects/sysexxer/files/SimpleSysexxer-0.3/%{name}-%{version}.tar.gz
Patch0: simplesysexxer-Qt5Port.patch

BuildRequires: gcc
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(alsa)
BuildRequires: desktop-file-utils

%description
Simple Sysexxer is a small tool that lets you exchange sysex data with your
MIDI devices. The most important idea is to make backups of the memory of
your devices. If you have spent nights over nights to get this killer sound
out of your synth it will be lost as soon as its battery gets low.

Furthermore it is common to share synth sounds and MIDI device settigns over
the internet. You can use Simple Sysexxer to send sysex files found on the
internet to your device. Please note: If the sounds are in MIDI or LIB
format, Simple Sysexxer cannot handle them. Ask the author to provide his
files in sysex format. If you got sysex in MIDI format, try using a
sequencer like Rosegarden or MusE to send it to your device.

All this is not only valid for synthesizers but for guitar amp emulators,
effects processors, MIDI controllers like faderboxes and footpedals as well.

Simple Sysexxer is ALSA only, there's no OSS support.

%global debug_package %{nil}

%prep
%autosetup -p1

%build

%qmake_qt5 SimpleSysexxer.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}
cp bin/simplesysexxer %{buildroot}%{_bindir}/simplesysexxer

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp bin/simplesysexxer.xpm %{buildroot}/%{_datadir}/pixmaps/
cp bin/simplesysexxer.png %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp bin/simplesysexxer.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/simplesysexxer.desktop

# Install mime type
install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 bin/sysex-mime.xml %{buildroot}/%{_datadir}/mime/packages/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/simplesysexxer.desktop

%files
%doc CHANGELOG COPYRIGHT CREDITS GPL-2
%{_bindir}/simplesysexxer
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/mime/*

%changelog
* Fri Jul 14 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3-1
- update to 0.3-3

* Sat Nov  2 2019 Edgar Aichinger <edogawa@aon.at>
- updated to (ancient) version 0.3
- trivial port to Qt5, see simplesysexxer-Qt5Port.patch
- specfile cleanup
* Mon Feb 28 2011 edogawa@aon.at
- fix install path
* Fri Nov 27 2009 edogawa@aon.at
- updated to version 0.2
* Wed Dec  3 2008 edogawa@aon.at
- add openfile patch - version 0.0.1p
* Sat Jul 14 2007 edogawa@aon.at
- initial package, 0.0.1 (tarball has no version info)
- sources from 06/10/18
