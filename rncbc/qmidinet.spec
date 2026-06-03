# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Sampler, Tool

#
# spec file for package qmidinet
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
Name: qmidinet
Version: 1.0.2
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://qmidinet.sourceforge.io/

Source0: https://download.sourceforge.net/qmidinet/qmidinet-%{version}.tar.gz

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
QmidiNet is a MIDI network gateway application that sends and receives
MIDI data (ALSA Sequencer and/or JACK MIDI) over the network, using UDP/IP
multicast. Inspired by multimidicast (http://llg.cubic.org/tools) and
designed to be compatible with ipMIDI for Windows (http://nerds.de).

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
* Wed Jun 03 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1 - Fedora version

* Wed Jun  3 2026 Rui Nuno Capela <rncbc@rncbc.org> 1.0.2
- A Mid-Spring'26 Release.

* Mon Mar 31 2025 Rui Nuno Capela <rncbc@rncbc.org> 1.0.1
- An Early Spring'25 Release.

* Wed Jun 19 2024 Rui Nuno Capela <rncbc@rncbc.org> 1.0.0
- An Unthinkable Release.
