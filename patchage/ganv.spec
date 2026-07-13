# Status: active
# Tag: Devel
# Type: Devel
# Category: Programming

Name: ganv
Version: 1.8.2
Release: 1%{?dist}
Summary: An interactive Gtk canvas widget for graph-based interfaces
License: GPL-3.0-or-later
URL: https://github.com/drobilla/ganv
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/drobilla/ganv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: ganv-0001-remove-intl-dep.patch

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: gtkmm2.4-devel
BuildRequires: graphviz-devel
BuildRequires: gobject-introspection-devel
BuildRequires: cairo-devel
BuildRequires: cairo-gobject-devel

%description
An interactive Gtk canvas widget for graph-based interfaces.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%meson
%meson_build

%install

%meson_install

%files
%doc README.md NEWS
%license COPYING
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Ganv-1.0.typelib
%{_datadir}/gir-1.0/Ganv-1.0.gir

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Jun 14 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.10-1
- Initial build
