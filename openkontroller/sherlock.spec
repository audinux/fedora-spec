# Tag: Tool, Devel
# Type: Plugin, LV2
# Category: Tool, Plugin

Name: sherlock.lv2
Version: 0.28.0
Release: 3%{?dist}
Summary: An investigative LV2 plugin bundle
URL: https://git.open-music-kontrollers.ch/~hp/sherlock.lv2
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/sherlock.lv2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: sratom-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: glew-devel
BuildRequires: flex
BuildRequires: meson
BuildRequires: cmake

%description
An investigative LV2 plugin bundle

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

%meson -Dlv2libdir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.28.0-3
- update to 0.28.0-3

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-3
- update to 0.26.0-3

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.24.0-3
- update to 0.24.0-3

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.24.0-2
- update to 0.24.0-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to 0.20.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.12.0
- Initial build
