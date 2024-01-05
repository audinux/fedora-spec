# Tag: Guitar, Jack
# Type: Standalone
# Category: Audio, Tool

# Global variables for github repository
%global commit0 792d453da0f3a599408008f0f1107823939d730d
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: gxtuner
Version: 3.0.%{shortcommit0}
Release: 3%{?dist}
Summary: A tuner for jack, with full jack session managment support
License: GPL-2.0-or-later
URL: https://github.com/brummer10/gxtuner

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildReauires: make
BuildRequires: gtk3-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: fftw-devel
BuildRequires: zita-resampler-devel

%description
A tuner for jack, with full jack session managment support

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

export CPPFLAGS="-D__cplusplus -std=c++11 $CXXFLAGS"

%make_build STRIP=true

%install

%make_install STRIP=true

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.0-3
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.0-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 3.0-2
- update to latest master

* Mon Dec 25 2017 Yann Collette <ycollette.nospam@free.fr> - 3.0-1
- Initial build
