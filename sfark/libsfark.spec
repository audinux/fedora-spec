# Tag: Library
# Type: Devel
# Category: Programming

# Global variables for github repository
%global commit0 e558feb824132d71004af82cc3a235566b89bec8
%global gittag0 2.24
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: sfArk library
Name: sfArkLib
Version: 2.24.%{shortcommit0}
Release: 2%{?dist}
License: GPL
URL: https://github.com/raboof/sfArkLib
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/raboof/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  libsfark-0001-fix-install-path.patch

BuildRequires: gcc gcc-c++
BuildRequires: zlib-devel

%description
Library for decompressing sfArk soundfonts.

A simple command-line tool to convert sfArk files to sf2
based on this library can be found at https://github.com/raboof/sfArkXTm

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%set_build_flags

%make_build LIB_PATH=%{_libdir} INC_PATH=%{_includedir}

%install

install -m 755 -d %{buildroot}/%{_libdir}
install -m 755 -d %{buildroot}/%{_includedir}

install -m 644 sfArkLib.h  %{buildroot}/%{_includedir}/
install -m 755 libsfark.so %{buildroot}/%{_libdir}

%files
%doc README.md
%license COPYING
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette dot nospam at free.fr> 2.24-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 2.24-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 2.24-1
- Initial release of spec file for 2.24
