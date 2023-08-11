# Global variables for github repository
%global commit0 0983ff7b104dc864af56409de5f7c66b061c5857
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: A library for accessing the MusicBrainz Cover Art Archive
Name:    libcoverart
Version: 1.0.0
Release: 4%{?dist}
License: LGPL
URL:     https://github.com/metabrainz/libcoverart

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/metabrainz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: neon-devel
BuildRequires: jansson-devel
BuildRequires: libxml2-devel

%description
A library for accessing the MusicBrainz Cover Art Archive

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{commit0}

find . -name CMakeLists.txt -exec sed -i -e "s/\-Werror//g" {} \;
find . -name "*.cmake" -exec sed -i -e "s/\-Werror//g" {} \;

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build 

%install

%cmake_install

%files
%doc INSTALL.txt NEWS.txt README.md
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Fri Aug 11 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-4
- update to last master - 0983ff7b104dc864af56409de5f7c66b061c5857

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-3
- fix for fedora 33 + update to last master

* Sat May 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- initial release of the spec file
