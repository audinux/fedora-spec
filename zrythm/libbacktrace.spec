%global debug_package %{nil}

%global commit0 4f57c999716847e45505b3df170150876b545088
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    libbacktrace-devel
Version: 0.0.1
Release: 1%{?dist}
Summary: A C library that may be linked into a C/C++ program to produce symbolic backtraces
License: GPL-2.0-or-later
URL:     https://github.com/ianlancetaylor/libbacktrace

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ianlancetaylor/libbacktrace/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make

%description
A C library that may be linked into a C/C++ program to produce symbolic backtraces

%prep
%autosetup -n libbacktrace-%{commit0}

%build

%set_build_flags
export CFLAGS="-fPIC $CFLAGS"

%configure

%make_build

%install 

%make_install

rm %{buildroot}%{_libdir}/*.la

%files
%doc README.md
%license LICENSE
%{_libdir}/*
%{_includedir}/*

%changelog
* Sat Mar 13 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec
