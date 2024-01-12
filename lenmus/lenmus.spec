# Tag: Editor, Tool
# Type: Standalone
# Category: Audio, Tool

Name: lenmus
Version: 6.0.1
Release: 2%{?dist}
Summary: An app to study music theory and train you ear
License: GPL-2.0-or-later
URL: https://github.com/lenmus/lenmus

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lenmus/lenmus/archive/Release_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: FindPortMidi.cmake

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: freetype-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
%if 0%{?fedora} <= 38
BuildRequires: wxGTK3-devel
%else
BuildRequires: wxGTK-devel
%endif
BuildRequires: sqlite-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: fluidsynth-devel
BuildRequires: fluid-soundfont-gm
BuildRequires: desktop-file-utils

%description
LenMus Phonascus, "the teacher of music", is a free program to help you in the study of music theory and ear training.

The LenMus Project is an open project, committed to the principles of
Open Source, free education, and open access to information. It has no comercial
purpose. It is an open workbench for working on all areas related to teaching
music, and music representation and management with computers. It aims at
developing publicly available knowledge, methods and algorithms related to all
these areas and at the same time provides free quality software for music
students, amateurs, and teachers.

Please visit the LenMus website (http://www.lenmus.org) for the latest news
about the project or for further details about releases.

%prep
%autosetup -n %{name}-Release_%{version}

cp %{SOURCE1} cmake-modules/

sed -ie "s/target_link_libraries ( \${LENMUS}/target_link_libraries ( \${LENMUS} jack/g" CMakeLists.txt

%build

%cmake -D_filename:FILEPATH=/usr/include/wx-3.0/wx/version.h \
%if 0%{?fedora} <= 38
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
%else
       -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.2 \
%endif
       -DPortTime_LIBRARY:FILEPATH=/usr/%{_lib}/libportaudio.so \
       -DLENMUS_DOWNLOAD_SOUNDFONT=OFF

%cmake_build

%install

%cmake_install

# install lenmus.desktop properly.
mv %{buildroot}%{_datadir}/applications/org.lenmus.lenmus.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/metainfo/org.lenmus.lenmus.appdata.xml %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS CHANGELOG.md INSTALL README.md NEWS THANKS
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/man/*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 6.0.1-2
- update 6.0.1-2

* Sun Feb 13 2022 Yann Collette <ycollette.nospam@free.fr> - 6.0.0-2
- update 6.0.0-2

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.2-2
- update 5.6.2-2 - fix for fedora 33

* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.2-1
- update 5.6.2-1

* Mon Mar 2 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.0-1
- update 5.6.0-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- update for Fedora 29

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 5.4.1-1
- Initial version
