# Global variables for github repository
%global commit0 ab1209eded5184aab28726d627efc66dfbdba37f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    midi_matrix.lv2
Version: 0.30.0
Release: 4%{?dist}
Summary: A LV2 Plugin Bundle
License: GPL-2.0-or-later
URL:     https://github.com/OpenMusicKontrollers/midi_matrix.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/OpenMusicKontrollers/midi_matrix.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: glew-devel
BuildRequires: meson
BuildRequires: cmake

%description
A LV2 Plugin Bundle

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

LDFLAGS="${LDFLAGS:-%{build_ldflags}} -z muldefs" ; export LDFLAGS
%meson -Dlv2libdir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.30.0-4
- update to 0.30.0-4 

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.28.0-4
- update to 0.28.0-4 

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-4
- fix debug build 

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-3
- update to 0.26.0-3

* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-3
- fix for Fedora 32

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-2
- update to 0.22.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to latest master

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.18.0
- Initial build
