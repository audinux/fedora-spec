# Global variables for github repository
%global commit0 250844ade88552f0e481bc911cca7794c1e68a3f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    caps-lv2
Version: 0.9.26.%{shortcommit0}
Release: 1%{?dist}
Summary: Caps LV2 set of plugins from portalmod
License: GPL-2.0-or-later
URL:     https://github.com/moddevices/caps-lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
Caps LV2 set of plugins from portalmod

%prep
%autosetup -n %{name}-%{commit0}

%build

%make_build LV2_DEST=%{buildroot}%{_libdir}/lv2

%install
%make_install LV2_DEST=%{buildroot}%{_libdir}/lv2

%files
%{_libdir}/lv2/*

%changelog
* Sat Mar 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.26
- update to 0.9.26

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update for Fedora 29

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Update to latest master version

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
