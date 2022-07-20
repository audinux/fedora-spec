%global commit0 6772a77ba6a85be1002b67fa786e52ccc70e9580

Name:    gammou
Version: 0.8.1
Release: 1%{?dist}
Summary: Modular Sound Synthesizer
URL:     https://github.com/aliefhooghe/Gammou
License: BSD3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gammou-source.sh <TAG>
# ./gammou-source.sh master

Source0: Gammou.tar.gz
Source1: gammou-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
Gammou is a polyphonic modular sound synthesizer that be run as VST or standalone.

%prep
%autosetup -n Gammou

%build

cd src
%cmake -DGAMMOU_ENABLE_DESKTOP_APP=ON
%cmake_build

%install

cd src
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/%{name}/*

%changelog
* Wed Jul 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
