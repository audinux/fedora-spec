# Global variables for github repository
%global commit0 cab6e0dfb2ce20e4ad34b067d1281ec0b193598a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    tap-lv2
Version: 0.9.%{shortcommit0}
Release: 3%{?dist}
Summary: TAP LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL:     https://github.com/portalmod/tap-lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
TAP LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/-Wl,--strip-all//g" Makefile.mk

%ifarch aarch64
sed -i -e "s/-msse -msse2 -mfpmath=sse//g" Makefile.mk
%endif

%build

%set_build_flags

export SPECCFLAGS="$CFLAGS"

%make_build INSTALL_PATH=%{_libdir}/lv2

%install 

%make_install INSTALL_PATH=%{_libdir}/lv2

%files
%doc README.md README CREDITS
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9-3
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
