# Global variables for github repository
%global commit0 a8c25e63f5edb934daa6ba051a95daaae4c0abeb
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    vopa-lv2
Version: 1.0.0
Release: 2%{?dist}
Summary: A LV2 amplifier controlled via MIDI messages
URL:     https://github.com/ycollet/vopa
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/vopa/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
A LV2 amplifier controlled via MIDI messages

%prep
%autosetup -n vopa-%{commit0}

%build

%set_build_flags
%make_build INSTALLDIR=%{buildroot}/%{_libdir}/lv2/

%install

%make_install INSTALLDIR=%{buildroot}/%{_libdir}/lv2/

%files
%{_libdir}/lv2/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
