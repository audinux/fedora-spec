# Status: active
# Tag: Effect
# Type: Plugin, LV2
# Category: Effect

# Global variables for github repository
%global commit0 b2df88cb28540856b7ec7d0210809efd7ca6bcd7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: mda-lv2
Version: 0.9.%{shortcommit0}
Release: 4%{?dist}
Summary: MDA LV2 set of plugins from moddevices
License: GPL-2.0-or-later
URL: https://github.com/moddevices/mda-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2

%description
MDA LV2 set of plugins synth from moddevices

%prep
%autosetup -n %{name}-%{commit0}

# For Fedora 29
%if 0%{?fedora} >= 29
  find . -type f -exec sed -i -e "s/env python/env python2/g" {} \;
%endif

%build

%set_build_flags

./waf configure --libdir=%{buildroot}%{_libdir}
./waf

%install
./waf -j1 install

%files
%doc README
%license COPYING
%{_libdir}/lv2/*

%changelog
* Fri May 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-4
- update to last master

* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-3
- fix debug build

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.2
- fix for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- update for Fedora 29

* Sat May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- fix f27 / f28 build

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
