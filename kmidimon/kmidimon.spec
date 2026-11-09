# Status: active
# Tag: MIDI, Alsa
# Type: Standalone
# Category: MIDI, Tool
# GUIToolkit: Qt

%define	desktop_vendor planetccrma

Summary: ALSA MIDI monitor
Name: kmidimon
Version: 1.4.2
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://kmetronome.sourceforge.net/kmidimon/
ExclusiveArch: x86_64 aarch64

Source0: https://sourceforge.net/projects/kmidimon/files/%{version}/kmidimon-%{version}.tar.bz2
Source1: kmidimon.desktop

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Requires: hicolor-icon-theme

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: gettext-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qt5compat-devel
BuildRequires: drumstick-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
MIDI monitor for Linux using ALSA sequencer and KDE user interface.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/Drumstick 2.11/Drumstick 2.10/g" CMakeLists.txt

%build

%cmake -DQT_DEBUG_FIND_PACKAGE=ON
%cmake_build

%install

%cmake_install

desktop-file-install --vendor %{desktop_vendor} \
		     --dir %{buildroot}%{_datadir}/applications    \
		     %{buildroot}/%{_datadir}/applications/net.sourceforge.kmidimon.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS ChangeLog INSTALL.md NEWS.md README.md TODO.md
%license COPYING
%{_bindir}/kmidimon
%{_datadir}/icons/hicolor/*/apps/kmidimon*
%{_mandir}/man1/kmidimon.1.gz
%{_mandir}/ja/man1/kmidimon.1.gz
%{_datadir}/applications/net.sourceforge.kmidimon.desktop
%{_datadir}/applications/planetccrma-net.sourceforge.kmidimon.desktop
%{_datadir}/doc/kmidimon/*
%{_datadir}/kmidimon/standards.ins
%{_datadir}/kmidimon/translations/*
%{_datadir}/metainfo/net.sourceforge.kmidimon.metainfo.xml

%changelog
* Sun Nov 08 2026 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-1
- update to 1.4.2-1

* Fri May 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.5-1
- update to 0.7.5-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Tue Jan 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- added documentation patch to build on fc14

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- updated to version 0.7.1, updated post scripts

* Wed Jul 16 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- tweaked spec file for building on CentOS

* Tue Jul 14 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1
- add proper dependencies for building on fc9

* Fri Feb  1 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- built on CentOS

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-1
- updated to version 0.5.0
- updated desktop categories
- now builds with cmake

* Tue Dec 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-2
- spec file tweaks, build for fc6

* Thu Sep  7 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-1
- updated to 0.4.1

* Fri Aug 19 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3-1
- updated to version 0.3

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1-1
- initial build.
