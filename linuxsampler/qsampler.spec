# Tag: Editor
# Type: Standalone
# Category: Audio, Sampler
# GUIToolkit: Qt5

Summary: LinuxSampler GUI front-end
Name:    qsampler
Version: 0.9.6
Release: 2%{?dist}
License: GPL
URL:     https://qsampler.sourceforge.net/qsampler-index.html

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: https://download.sf.net/qsampler/qsampler-%{version}.tar.gz
Source1: qsampler.desktop

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libgig-devel
BuildRequires: liblscp-devel
BuildRequires: qt5-linguist
BuildRequires: desktop-file-utils

Requires: linuxsampler
Requires: hicolor-icon-theme

%description
QSampler is a LinuxSampler GUI front-end application written in C++
around the Qt5 toolkit using Qt Designer. At the moment it just wraps
as a client reference interface for the LinuxSampler Control Protocol
(LSCP).

%prep
%autosetup

%build

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 src/images/qsampler.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 src/images/qsampler.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/metainfo/
install -m 644 src/appdata/org.rncbc.qsampler.metainfo.xml %{buildroot}%{_datadir}/metainfo/

install -m 755 -d %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc ChangeLog README TRANSLATORS
%license LICENSE
%{_bindir}/qsampler
%{_datadir}/icons/hicolor/32x32/apps/qsampler.png
%{_datadir}/icons/hicolor/scalable/apps/qsampler.svg
%{_datadir}/mime/packages/*
%{_datadir}/applications/*
%{_datadir}/metainfo/qsampler.appdata.xml
%{_mandir}/*
%{_datadir}/qsampler/translations/*

%changelog
* Wed Dec 02 2020 Yann Collette <ycollette.nospam@free.fr> 0.6.3-2
- override fedora version

* Mon Aug 3 2020 Yann Collette <ycollette.nospam@free.fr> 0.6.3-1
- update to 0.6.3

* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> 0.4.2-1
- update to 0.4.2

* Fri Jul  1 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- update to latest for fc24 build
- add patch to build with new gcc (from Debian)

* Fri Dec 12 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-1
- update to latest version for fc21 build
- fix location of include file, add new files to list

* Wed May 30 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-2.svn527
- update to latest svn for fc17 build

* Thu Sep 16 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-2.svn507
- update to latest svn for Fedora 13, fixes segfault on startup

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add patch to link with -lX11 for fc13/gcc4.4.4

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-1
- updated to 0.2.2

* Tue Jul  8 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1-1
- updated to 0.2.1
- add qmake to the path (otherwise the default is named qmake-qt4
  and is not found)

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.5-1
- updated to version 0.1.5
- updated desktop categories, ignore original desktop file

* Tue Jul  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.4-1
- updated to 0.1.4

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-2
- build for fc6, spec file tweaks

* Sun Jul 30 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-2
- built with libgig support

* Mon Jun 20 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-1
- updated to 0.1.3
- added Planet CCRMA categories to desktop file, moved icon to proper
  freedesktop location

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.2-1
- updated to 0.1.2

* Thu May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- updated to 0.1.0, made explicit dependency on linuxsampler
- added menu entry

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.4-1 
- initial build.
