# Tag: Loop, Plugin
# Type: Plugin, LV2
# Category: Audio, Sequencer

# Global variables for github repository
%global commit0 725d67898f01cbf903d7ba1494fe5f2532c03055
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: orbit.lv2
Version: 0.1.0
Release: 4%{?dist}
Summary: LV2 Event Looper
URL: https://git.open-music-kontrollers.ch/~hp/orbit.lv2
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/orbit.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: zlib-devel

%description
LV2 Event Looper

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`

%meson
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-4
- update to 0.1.0-4

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-3
- update to 0.1.0-3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial build
