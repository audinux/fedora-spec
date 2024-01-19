# Tag: Library
# Type: Devel
# Category: Programming

%global debug_package %{nil}

Name: ztoolkit
Version: 0.1.2
Release: 1%{?dist}
Summary: GUI toolkit for LV2 plugins
License: GPL-2.0-or-later
URL: https://github.com/alex-tee/ztoolkit

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/alex-tee/ztoolkit/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: cairo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel
BuildRequires: librsvg2-devel

%description
A GUI toolkit for LV2 plugins

%prep
%autosetup -n %{name}-%{version}

%build

%meson -Denable_rsvg=true
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/*
%{_includedir}/*

%changelog
* Sun Sep 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- update to 0.1.2-1

* Tue Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- Initial build
