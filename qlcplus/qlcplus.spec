# Tag: Live, Tool
# Type: Standalone
# Category: Tool

Name: qlcplus
Version: 4.13.0
Release: 1%{?dist}
Summary: Q Light Controller Plus - The free DMX lighting console
URL: http://www.hydrogen-music.org/
ExclusiveArch: x86_64 aarch64
License: Apache-2.0

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mcallegari/qlcplus/archive/refs/tags/QLC+_%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qt3d-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-linguist
BuildRequires: fftw-devel
BuildRequires: libftdi-devel
BuildRequires: systemd-devel
BuildRequires: libmad-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
Q Light Controller Plus (QLC+) is a free and cross-platform software
to control DMX or analog lighting systems like moving heads, dimmers,
scanners etc. This project is a fork of the great QLC project written
by Heikki Junnila that aims to continue the QLC development and to
introduce new features. 

%prep
%autosetup -n qlcplus-QLC-_%{version}

%build

%set_build_flags

export CXXFLAGS="-Wno-error=template-id-cdtor $CXXFLAGS"

./translate.sh qmlui
%qmake_qt5 CONFIG+=qmlui qlc.pro
%make_build

%install

%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/mime/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/qlcplus
%{_datadir}/qlcplus/*
%{_sysconfdir}/udev/rules.d/*

%changelog
* Fri Mar 22 2024 Yann Collette <ycollette.nospam@free.fr> - 4.13.0-1
- initial spec file

* Fri Jan 12 2024 Yann Collette <ycollette.nospam@free.fr> - 4.12.4-1
- initial spec file
