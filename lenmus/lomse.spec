# Global variables for github repository
%global commit0 4c229e45f214e5cca0678006459e154c05afe382
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lomse
Version: 0.20.0.%{shortcommit0}
Release: 1%{?dist}
Summary: A free open source library for rendering music scores
License: GPL-2.0-or-later
URL:     https://github.com/lenmus/lomse

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lenmus/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  lomse_0001-fix-install.patch

BuildRequires: gcc gcc-c++
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: freetype-devel
BuildRequires: cmake

%description
Lomse objective is provide software developers with a library to add capabilities to any program for rendering, editing and playing back music scores. It is written in C++ and it is free open source and platform independent. Lomse stands for "LenMus Open Music Score Edition Library".

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%cmake -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DWANT_SHARED:BOOL=ON \
       -DLIBDIR=%{_lib} \
       .

%cmake_build

%install

%cmake_install

%files
%doc AUTHORS.md CHANGELOG.md README.md NEWS THANKS CONTRIBUTING.md
%license LICENSE
%{_libdir}/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/fonts/*

%files devel
%{_includedir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.19.0-1
- update for Fedora 29

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.19.0-1
- Initial version
