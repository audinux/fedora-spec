# Status: active
# Tag: Jack, Editor
# Type: Standalone
# Category: Audio

Name: qutecsound
Version: 7.2.1
Release: 3%{?dist}
Summary: A csound file editor
URL: https://github.com/CsoundQt/CsoundQt
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# Usage: ./csoundqt-source.sh <TAG>
#        ./csoundqt-source.sh v7.2.1

Source0: CsoundQt.tar.gz
Source1: qutecsound.desktop
Source2: qutecsound.xml
Source3: csoundqt-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: csound7-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

Requires: csound-manual

%description
CsoundQt is a frontend for Csound featuring a highlighting editor with autocomplete,
interactive widgets and integrated help. It is a cross-platform and aims to be a simple
yet powerful and complete development environment for Csound.
It can open files created by MacCsound.
Csound is a musical programming language with a very long history, with roots in the
origins of computer music. It is still being maintained by an active community and despite
its age, is still one of the most powerful tools for sound processing and synthesis.
CsoundQt hopes to bring the power of Csound to a larger group of people,
by reducing Csound''s intial learning curve, and by giving users more immediate control of
their sound. It hopes to be both a simple tool for the beginner, as well as a powerful
tool for experienced users.

%prep
%autosetup -n CsoundQt

%build

%qmake_qt6 CSOUND_LIBRARY_DIR=/usr/%{_lib} CONFIG+=nostrip qcs.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# install qutecsound.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/qutecsound
%{_datadir}/applications/qutecsound.desktop
%{_datadir}/mime/packages/qutecsound.xml
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/

%changelog
* Mon Sep 28 2026 Yann Collette <ycollette.nospam@free.fr> - 7.2.1-3
- update to 7.2.1-3

* Thu Oct 17 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-3
- update to 1.1.3-3

* Mon Jul 29 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-3
- update to 1.1.2-3

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.8.1-3
- fix debug build

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.8.1-2
- update to 0.9.8.1-2

* Mon Nov 11 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-2
- update to 0.9.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.6b-1
- update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.6b-1
- update to 0.9.6b

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9.5b-1
- Initial spec file
