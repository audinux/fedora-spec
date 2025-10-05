# Status: active
# Tag: Effect
# Type: Plugin, LV2
# Category: Audio, Effect

Name: lv2-airwindows
Version: 32.0
Release: 1%{?dist}
Summary: Airwindows plugins (ported to LV2)
License: GPL-3.0-or-later
URL: https://github.com/hannesbraun/airwindows-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hannesbraun/airwindows-lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
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
* Sun Oct 05 2025 Yann Collette <ycollette.nospam@free.fr> - 32.0-1
- update to 32.0-1

* Sat Sep 14 2024 Yann Collette <ycollette.nospam@free.fr> - 30.0-1
- update to 30.0-1

* Tue Mar 05 2024 Yann Collette <ycollette.nospam@free.fr> - 28.0-1
- update to 28.0-1

* Tue Dec 05 2023 Yann Collette <ycollette.nospam@free.fr> - 26.2-1
- update to 26.2-1

* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 24.0-1
- update to 24.0-1

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
