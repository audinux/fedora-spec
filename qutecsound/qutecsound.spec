# Tag: Jack, Editor
# Type: Standalone
# Category: Audio

Name:    qutecsound
Version: 0.9.8.1
Release: 3%{?dist}
Summary: A csound file editor
URL:     https://github.com/CsoundQt/CsoundQt
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/CsoundQt/CsoundQt/archive/v%{version}.tar.gz#/CsoundQt-%{version}.tar.gz
Source1: qutecsound.desktop
Source2: qutecsound.xml

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: csound-devel
BuildRequires: csound-manual
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtquickcontrols2-devel

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
%autosetup -n CsoundQt-%{version}

%build

# BUILD OPTIONS:
# CONFIG+=build32    To build floats version
# CONFIG+=pythonqt   To build with PythonQt support
# CONFIG+=rtmidi     To build with RtMidi support
# CONFIG+=record_support
# CONFIG+=debugger
# CONFIG+=html5      To support HTML5 via the <CsHtml5> element in the csd file.
# CSOUND_INCLUDE_DIR
# CSOUND_LIBRARY_DIR

# DEBUG: DEFINES+="Q_NULLPTR=0" is an awful hack ...

%set_build_flags

%qmake_qt5 CSOUND_LIBRARY_DIR=/usr/%{_lib} DEFINES+="Q_NULLPTR=0" CONFIG+=nostrip qcs.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/CsoundQt-d-cs6 %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/templates
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples

cp -r templates/* %{buildroot}%{_datadir}/%{name}/templates/
cp -r doc/*       %{buildroot}%{_datadir}/%{name}/doc/
cp -r examples/*  %{buildroot}%{_datadir}/%{name}/examples/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 644 images/qtcs.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

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
%{_datadir}/%{name}/*

%changelog
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
