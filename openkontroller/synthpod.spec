# Tag: Tool, Rack
# Type: Plugin, LV2, Standalone
# Category: Tool, Plugin

# Global variables for github repository
%global commit0 c91544db474c552b3cf27a87ddc1d60fbeb171f4
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: synthpod
Version: 0.1.2
Release: 4%{?dist}
Summary: Lightweight Nonlinear LV2 Plugin Container
URL: https://git.open-music-kontrollers.ch/~hp/synthpod
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/synthpod/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: sratom-devel
BuildRequires: nanomsg-devel
BuildRequires: efl-devel
BuildRequires: elementary-devel
BuildRequires: pkgconfig(jack)
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-xrm-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libuv-devel
BuildRequires: meson
BuildRequires: cairo-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: alsa-lib-devel
BuildRequires: libevdev-devel
BuildRequires: serd-devel
BuildRequires: libvterm-devel
BuildRequires: glew-devel

%description
Lightweight Nonlinear LV2 Plugin Container

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

%meson -Dlv2libdir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md API.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-4
- update to last master

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-4
- fix debug build

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-3
- update to last master version - c6cd3720b987f73ed5f412db9607433b3769f1db

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-3
- update to 0.1.0-3

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- fixe for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0
- Initial build
