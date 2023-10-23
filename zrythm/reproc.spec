Name:    libreproc
Version: 14.2.0
Release: 1%{?dist}
Summary: A cross-platform (C99/C++11) process library
License: GPL-2.0-or-later
URL:     https://github.com/DaanDeMeyer/reproc/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DaanDeMeyer/reproc/archive/v14.2.0.tar.gz#/reproc-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
Fully featured LFO for CV-based automation

%package devel
Summary:  libreproc Development Files
Requires: %{name} = %{version}-%{release}

%description devel
libreproc Development Files

%prep
%autosetup -n reproc-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libreproc.so.*

%files devel
%{_includedir}/*
%{_libdir}/libreproc.so
%{_libdir}/cmake/reproc/*
%{_libdir}/pkgconfig/*

%changelog
* Tue Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 14.2.0-1
- Initial build
