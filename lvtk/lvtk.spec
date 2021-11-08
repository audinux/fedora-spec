%global debug_package %{nil}

# Global variables for github repository
%global commit0 6bfe981dfb5b27ea199dd4f6801b5305ca0355f9
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lvtk
Version: 2.0.0.%{shortcommit0}
Release: 4%{?dist}
Summary: LV2 Toolkit
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

URL:     https://github.com/lvtk/lvtk
Source0: https://github.com/lvtk/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2
BuildRequires: gtkmm24-devel

%description
This software package contains libraries that wrap the LV2 C API and
extensions into easy to use C++ classes. The original work for this
was mostly done by Lars Luthman in lv2-c++-tools.

%prep
%autosetup -n %{name}-%{commit0}

find . -type f -exec sed -i -e "s/env python/env python2/g" {} \;

%build

%set_build_flags

./waf configure --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot} -v

%files
%doc README AUTHORS ChangeLog
%license COPYING
%{_libdir}/*
%{_includedir}/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-3
- fix debug build

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-2
- update for Fedora 32

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-2
- update for Fedora 32

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update for Fedora 29

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.2.0
- Initial build
