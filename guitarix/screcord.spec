# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Sequencer

Name: lv2-screcord-plugin
Version: 0.2
Release: 3%{?dist}
Summary: A simple Lv2 capture plugin
License: GPL-2.0-or-later
URL: https://github.com/brummer10/screcord.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: screcord.lv2.tar.gz
Source1: brummer10-source.sh

# To get the sources:
# ./brummer10-source.sh screcord.lv2 v0.2

BuildRequires: gcc gcc-c++
BuildRequires: make
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
export CXXFLAGS="-Wno-incompatible-pointer-types $CXXFLAGS"
export CFLAGS="-Wno-incompatible-pointer-types $CFLAGS"

cd Xputty
%make_build -j1
cd ..
%make_build INSTALL_DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install INSTALL_DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/sc_record.lv2/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2-3
- fix debug build

* Mon Dec 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.2-2
- update to 0.2-2

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update for Fedora 29

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to latest master

* Tue Nov 21 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
