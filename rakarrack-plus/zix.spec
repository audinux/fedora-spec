Name:    zix
Version: 0.4.2
Release: 1%{?dist}
Summary: A lightweight C library of portability wrappers and data structures
License: ISC
URL:     https://github.com/drobilla/zix

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/drobilla/zix/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: lv2-devel
%if 0%{?fedora} >= 38
BuildRequires: python3-sphinxygen
%endif
BuildRequires: doxygen
BuildRequires: python3-sphinx
BuildRequires: glib2-devel

%description
Zix is a lightweight C library of portability wrappers and data structures.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%if 0%{?fedora} >= 38
%package doc
Summary:  Documentation files for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
The %{name}-devel package contains documentation files for %{name}.
%endif

%prep
%autosetup -n %{name}-%{version}

%build

%if 0%{?fedora} >= 38
%meson -Ddocs=enabled
%else
%meson -Ddocs=disabled
%endif
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%if 0%{?fedora} >= 38
%files doc
%{_datadir}/doc/zix-0/*
%endif

%changelog
* Tue Oct 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- Initial spec file
