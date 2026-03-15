# Status: active
# Tag: Devel
# Type: Devel
# Category: Programming

Summary: Logging library for C applications
Name: yder
Version: 1.4.20
Release: 1%{?dist}
License: LGPL2.1
URL: https://github.com/babelouest/yder
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/babelouest/yder/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: systemd-devel
BuildRequires: orcania-devel

%description
Logging library written in C.
Simple and easy to use logging library. You can log messages to the console, a file, Syslog, journald or a callback function.
Yder is mono-thread, which mean that you can use only one instance of Yder log at the same time in your program.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

rm -f %{buildroot}/%{_datadir}/doc/yder/examples/.gitignore

%files
%doc API.md README.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Yder/*.cmake
%{_datadir}/doc/yder/examples/*

%changelog
* Tue Mar 10 2026 Yann Collette <ycollette dot nospam at free.fr> 1.4.20-1
- Initial release
