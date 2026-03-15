# Status: active
# Tag: Devel
# Type: Devel
# Category: Programming

Summary: Potluck with different functions for different purposes that can be shared among C programs
Name: orcania
Version: 2.3.3
Release: 1%{?dist}
License: LGPL2.1
URL: https://github.com/babelouest/orcania
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/babelouest/orcania/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
Potluck with different functions for different purposes that can be shared among C programs.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export CFLAGS="-Wno-error=discarded-qualifiers $CFLAGS"

%cmake
%cmake_build

%install

%cmake_install

%files
%doc API.md README.md
%license LICENSE
%{_libdir}/*.so.*
%{_bindir}/base64url
%{_mandir}/man1/base64url.1.gz

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Orcania/*.cmake

%changelog
* Tue Mar 10 2026 Yann Collette <ycollette dot nospam at free.fr> 2.3.3-1
- Initial release
