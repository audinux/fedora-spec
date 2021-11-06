# Tag: Sequencer, MIDI
# Type: Plugin, LV2
# Category: Audio, Sequencer

# Global variables for github repository
%global commit0 b20d67550864df05c8969ad689f4ec465e6efbcc
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lv2-screcord-plugin
Version: 0.2
Release: 3%{?dist}
Summary: A simple Lv2 capture plugin
License: GPLv2+
URL:     https://github.com/brummer10/screcord.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: screcord.lv2.tar.gz
Source1: screcord-source.sh

# ./screcord-source.sh <tag>
# ./screcord-source.sh v0.2

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: cairo-devel
BuildRequires: libffi-devel

%description
A simple Lv2 capture plugin

%prep
%autosetup -n screcord.lv2

%build

%set_build_flags

cd Xputty
%make_build -j1
cd ..
%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 STRIP=true install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/sc_record.lv2/*

%changelog
* Tue OCt 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2-3
- fix debug build

* Mon Dec 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2-2
- update to 0.2-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to latest master

* Tue Nov 21 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
