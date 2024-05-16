# Global variables for github repository
%global commit0 b5e62895c619d4ffc75c9d822c8d85f1ece77e5b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: QuickJS Javascript Engine.
Name:    quickjs
Version: 2021.03.27
Release: 1%{?dist}
License: MIT
URL:     https://github.com/bellard/quickjs
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bellard/quickjs/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: sed

%description
QuickJS Javascript Engine.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/lib\/quickjs/%{_lib}\/quickjs/g" Makefile
sed -i -e "s/usr\/local/usr\//g" Makefile
sed -i -e "s/CFLAGS_OPT=/CFLAGS_OPT+=/g" Makefile
sed -i -e "/prefix=/a CFLAGS_OPT=%{build_cflags}" Makefile
sed -i -e "s/strip/true/g" Makefile

%build

%set_build_flags

%make_build CFLAGS_EXT="$(CFLAGS)"

%install

%make_install

%files
%doc readme.txt Changelog TODO
%license LICENSE
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/quickjs/*.a

%changelog
* Sat May 08 2021 Yann Collette <ycollette dot nospam at free.fr> 2021.03.27-1
- Initial release of spec file for 2021.03.27
