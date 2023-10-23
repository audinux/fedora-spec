Summary: Web Framework to build REST APIs, Webservices or any HTTP endpoint in C language.
Name:    ulfius
Version: 2.7.0
Release: 1%{?dist}
License: LGPL-2.1
URL:     https://github.com/babelouest/%{name}

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: gnutls-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: jansson-devel
BuildRequires: zlib-devel
BuildRequires: systemd-devel

%description
Web Framework to build REST APIs, Webservices or any HTTP endpoint in C language.
Can stream large amount of data, integrate JSON data with Jansson,
and create websocket services

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package doc
Summary:  Documentation for %{name}

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md API.md CHANGELOG.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/man/man1/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/doc/ulfius/

%changelog
* Sun Dec 13 2020 Yann Collette <ycollette dot nospam at free.fr> 2.7.0-1
- Initial release of spec file for 2.7.0
