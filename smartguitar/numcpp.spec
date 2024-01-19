# Tag: Library
# Type: Devel
# Category: Programming

Summary: C++ implementation of the Python Numpy library
Name: numcpp
Version: 2.4.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/dpilger26/NumCpp

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/dpilger26/NumCpp/archive/refs/tags/Version_%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
C++ implementation of the Python Numpy library.

%prep
%autosetup -n NumCpp-Version_%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_includedir}/NumCpp.hpp
%{_includedir}/NumCpp/
%{_datadir}/NumCpp/
%{_datadir}/NumCpp/cmake/*

%changelog
* Mon Jun 14 2021 Yann Collette <ycollette dot nospam at free.fr> 2.4.2-1
- Initial release of spec file
