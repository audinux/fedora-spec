# Tag: OSC, Tool
# Type: Plugin, LV2
# Category: Tool, Audio

# Global variables for github repository
%global commit0 5c048f5c06ddef052bf1ffd2c151e5ff5248fca2
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: eteroj.lv2
Version: 0.10.0
Release: 3%{?dist}
Summary: OSC injection/ejection from/to UDP/TCP/Serial for LV2
URL: https://github.com/OpenMusicKontrollers/eteroj.lv2
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/OpenMusicKontrollers/eteroj.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libuv-devel
BuildRequires: sratom-devel
BuildRequires: meson

%description
OSC injection/ejection from/to UDP/TCP/Serial for LV2

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

%meson
%meson_build

%install

%meson_install

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-3
- update to 0.10.0-3

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-3
- update to 0.8.0-3

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- fix debug build

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- update to 0.6.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to latest master

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.2.0
- Initial build
