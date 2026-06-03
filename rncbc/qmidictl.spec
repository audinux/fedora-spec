# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

#
# spec file for package qmidictl
#
# Copyright (C) 2010-2026, rncbc aka Rui Nuno Capela. All rights reserved.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Summary: A MIDI Network Gateway via UDP/IP Multicast
Name: qmidictl
Version: 1.0.3
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://qmidictl.sourceforge.io/

Source0: https://download.sourceforge.net/qmidictl/qmidictl-%{version}.tar.gz

#Packager: rncbc.org

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(alsa)

%description
QmidiCt is a MIDI remote controller application that sends MIDI data over the network, using UDP/IP multicast.
Inspired by multimidicast and designed to be compatible with ipMIDI for Windows.
QmidiCtl was long ago designed for the Maemo enabled handheld devices, namely the late Nokia N900 and promoted
to the Maemo Package repositories.
Nevertheless, QmidiCtl may still be found effective as a regular desktop application and recently as an Android
application as well.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"
%cmake_build

%install

%cmake_install

%files
%doc README ChangeLog
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/man/fr/man1/%{name}.1.gz

%changelog
* Wed Jun 03 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- Initial version of the spec
