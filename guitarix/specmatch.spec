# Tag: Guitar, Analyzer
# Type: Standalone
# Category: Audio, Tool

%global commit0 5871254109fc953ba83b495c7c6627da73e19852
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: specmatch
Version: 0.44.1
Release: 1%{?dist}
Summary: SpecMatch can be used to adapt the sound produced by a Guitarix setting to another recorded sound.
License: GPL-2.0-or-later
URL: https://github.com/brummer10/guitarix

Vendor:       Audinux
Distribution: Audinux

# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh guitarix v0.44.1
Source0: guitarix.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-numpy
BuildRequires: pkgconfig(jack)

Requires: python3
Requires: pygtk2
Requires: python3-numpy
Requires: python3-matplotlib
Requires: python3-sympy
Requires: python3-scipy

%description
SpecMatch can be used to adapt the sound produced by a Guitarix setting to another recorded sound.

%prep
%autosetup -n guitarix

%build

cd trunk/specmatch
python3 --version
%py3_build

%install

cd trunk/specmatch
%py3_install

%files
%{_bindir}/*
%{_datadir}/*
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}*.egg-info

%changelog
* Mon Jan 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.44.1-1
- Initial build
