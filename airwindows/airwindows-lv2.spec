# Tag: Effect
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    lv2-airwindows
Version: 22.0
Release: 1%{?dist}
Summary: Airwindows plugins (ported to LV2)
License: GPL-3.0-or-later
URL:     https://github.com/hannesbraun/airwindows-lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hannesbraun/airwindows-lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: lv2-devel
BuildRequires: boost-devel

%description
This is an LV2 port of the Airwindows plugins made by Chris Johnson.
Have a look at https://www.airwindows.com for a detailed description of all the plugins.
Find the original source code at https://github.com/airwindows/airwindows.

%prep
%autosetup -n airwindows-lv2-%{version}

%build

%meson
%meson_build

%install 

%meson_install

%files
%doc README.md NOTES.md CONTRIBUTING.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Wed Aug 02 2023 Yann Collette <ycollette.nospam@free.fr> - 22.0-1
- update to 22.0-1

* Sat Jul 22 2023 Yann Collette <ycollette.nospam@free.fr> - 20.0-1
- update to 20.0-1

* Mon Apr 03 2023 Yann Collette <ycollette.nospam@free.fr> - 18.0-1
- update to 18.0-1

* Wed Feb 01 2023 Yann Collette <ycollette.nospam@free.fr> - 16.0-1
- update to 16.0-1

* Fri Nov 18 2022 Yann Collette <ycollette.nospam@free.fr> - 12.0-1
- Initial spec file
