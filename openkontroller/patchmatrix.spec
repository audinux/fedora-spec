# Tag: Jack, Editor
# Type: Standalone
# Category: Session Mngmt, Tool

Name: patchmatrix
Version: 0.26.0
Release: 3%{?dist}
Summary: A JACK patchbay in flow matrix style
URL: https://git.open-music-kontrollers.ch/~hp/patchmatrix
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.open-music-kontrollers.ch/~hp/patchmatrix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: glew-devel
BuildRequires: meson
BuildRequires: cmake

%description
A JACK patchbay in flow matrix style

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
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Nov 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-3
- update to 0.26.0-2

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-3
- update to 0.22.0-2

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-3
- fix debug build

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-2
- update to 0.20.0-2

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.16.0-2
- update to 0.16.0-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- inital release
