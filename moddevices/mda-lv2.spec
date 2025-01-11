# Status: active
# Tag: Effect
# Type: Plugin, LV2
# Category: Effect

Name: mda-lv2
Version: 1.2.10
Release: 4%{?dist}
Summary: MDA LV2 set of plugins
License: GPL-2.0-or-later
URL: https://gitlab.com/drobilla/mda-lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/drobilla/mda-lv2/-/archive/v%{version}/mda-lv2-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: meson
BuildRequires: lv2lint

%description
MDA LV2 set of plugins synth

%prep
%autosetup -n %{name}-v%{version}

%build

%meson -Dtests=disabled
%meson_build

%install

%meson_install

%files
%doc README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_libdir}/lv2/*

%changelog
* Tue Jan 07 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.10-4
- update to 1.2.10-4 from drobilla

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
