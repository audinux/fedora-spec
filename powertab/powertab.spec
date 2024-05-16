# Tag: DAW, Editor, Player
# Type: Standalone
# Category: Audio, DAW

Name: powertabeditor
Version: 0.0.1
Release: 1%{?dist}
Summary: View and edit guitar powertab tablature.
URL: https://github.com/powertab/powertabeditor
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/powertab/powertabeditor/archive/refs/tags/2.0.0-alpha18.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: alsa-lib-devel
BuildRequires: doctest-devel
BuildRequires: minizip-devel
BuildRequires: json-devel
BuildRequires: pugixml-devel
BuildRequires: rtmidi-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Power Tab Editor is an easy to use cross-platform guitar tablature editor and viewer.
It is an open source, community-driven successor to the original Power Tab Editor 1.7.

A variety of file formats are supported, including .pt2, .ptb, .gp3, .gp4, .gp5, .gpx, and .gp

%prep
%autosetup -n powertabeditor-2.0.0-alpha18

sed -i -e "1i #include <zlib.h>" source/formats/gp7/gp7exporter.cpp
sed -i -e "s/zipOpenNewFileInZip64/zipOpenNewFileInZip_64/g" source/formats/gp7/gp7exporter.cpp

sed -i -e "1i #include <functional>" source/app/viewoptions.cpp

%build

%set_build_flags
export CFLAGS="-fpermissive $CFLAGS"
export CXXFLAGS="-fpermissive $CXXFLAGS"

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications//powertabeditor.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications//powertabeditor.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/powertabeditor.metainfo.xml

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/metainfo/*
%{_datadir}/mime/*
%{_datadir}/powertab/

%changelog
* Fri Jul 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
