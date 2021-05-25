
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name:    Cadence
Version: 0.9.1
Release: 5%{?dist}
Summary: JACK control center
License: GPLv2+
URL:     https://github.com/falkTX/Cadence

Source0: https://github.com/falkTX/Cadence/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:  cadence_001_fedora_support.patch
Patch1:  cadence_002_add_missing_include.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-qt4-devel
BuildRequires: python3-qt5-devel
BuildRequires: qt-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture

Requires: jack-audio-connection-kit-dbus
Requires: python3-dbus
Requires: python3-qt4
Requires: python3-qt5
Requires: jack_capture
Requires: a2jmidid

%description
Set of tools useful for audio production.
- System checks, manages JACK, calls other tools and make system tweaks.
...

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%set_build_flags

%make_build PREFIX=/usr SKIP_STRIPPING=true

%install 

%make_install PREFIX=/usr SKIP_STRIPPING=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/cadence/*
%{_datadir}/icons/*
%{_sysconfdir}/*

%changelog
* Sat Oct 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- fix debug build

* Thu Jan 3 2019 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - master
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master + qt5

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- added required dependencies to run minimally

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- added Qt5 dependencies

* Sun May 06 2018 Tom Nguyen <tom81094@gmail.com> - master
- update to latest master and fixed fedora patch

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - master
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - master
- Initial build
