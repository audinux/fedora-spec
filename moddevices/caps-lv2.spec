# Status: active
# Tag: Effect
# Type: Plugin, LV2
# Category: Effect

# Global variables for github repository
%global commit0 250844ade88552f0e481bc911cca7794c1e68a3f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: caps-lv2
Version: 0.9.26.%{shortcommit0}
Release: 1%{?dist}
Summary: Caps LV2 set of plugins from moddevices
License: GPL-2.0-or-later
URL: https://github.com/moddevices/caps-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel

%description
Caps LV2 set of plugins from moddevices

%prep
%autosetup -n %{name}-%{commit0}

find . -name Makefile -exec sed -i -e "/strip-all/d" {} \;
find . -name Makefile -exec sed -i -e "/OPTS =/d" {} \;

%build

%set_build_flags

%make_build DESTDIR=%{buildroot} LV2_DEST=%{_libdir}/lv2 STRIP=true

%install
%make_install DESTDIR=%{buildroot} LV2_DEST=%{_libdir}/lv2 STRIP=true

# Change permissions of so files
find %{buildroot}/%{_libdir}/lv2 -name "*.so" -exec chmod a+x {} \;

%files
%doc README.md README
%license COPYING
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
