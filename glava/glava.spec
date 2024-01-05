# Tag: Analyzer
# Type: Standalone
# Category: Audio, Tool, Graphic

# Global variables for github repository
%global commit0 094dec9b009268814751d3801fc7a5068381c90b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: glava
Version: 1.6.3
Release: 2%{?dist}
Summary: GLava is an OpenGL audio spectrum visualizer
URL: https://github.com/wacossusca34/glava
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# original tarfile can be found here:
Source0: https://github.com/wacossusca34/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libXrender-devel
BuildRequires: libX11-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: glfw-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel
BuildRequires: libsndfile-devel

%description
GLava is an OpenGL audio spectrum visualizer. Its primary use case is for desktop windows or backgrounds.
Displayed to the left is the radial shader module. Development is active, and reporting issues is encouranged.

%prep
%autosetup -n %{name}-%{commit0}

# disable stripping
sed -i -e "s/strip /true /g" Makefile

%build

%make_build CFLAGS="%{build_cxxflags}"

%install

%make_install INSTALL=unix CFLAGS="%{build_cxxflags}"

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/*
%{_sysconfdir}/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-2
- fix package

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-1
- update to 1.6.3-1

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.8-1
- fix for Fedora 31

* Sun Dec 2 2018 Yann Collette <ycollette.nospam@free.fr> - 1.5.8-1
- initial spec file
