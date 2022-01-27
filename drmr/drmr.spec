# Tag: Drum
# Type: LV2
# Category: Synthesizer

# Global variables for github repository
%global commit0 a593de0836790a3437b861cf0eb7acd1b581e512
%global gittag0 lv2unstable
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    drmr
Version: 1.0.0.%{shortcommit0}
Release: 2%{?dist}
Summary: A drum LV2 plugin
License: GPLv2+
URL:     https://github.com/falkTX/drmr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: gtk2-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: expat-devel
BuildRequires: cmake

%description
A drum LV2 plugin

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "/set(CMAKE_C_FLAGS/d" CMakeLists.txt

%build

%cmake -DLV2_INSTALL_DIR:Path=%{_lib}/lv2

%cmake_build

%install

%cmake_install

%files
%{_libdir}/lv2/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
