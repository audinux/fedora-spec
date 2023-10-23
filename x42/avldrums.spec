# Tag: Drum
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name:    lv2-avldrums-x42-plugin
Version: 0.7.2
Release: 3%{?dist}
Summary: Simple Drum Sample Player LV2 Plugin
License: GPL-2.0-or-later
URL:     https://github.com/x42/avldrums.lv2

Vendor:       Audinux
Distribution: Audinux

# ./x42-source.sh <project> <tag>
# ./x42-source.sh avldrums.lv2 v0.7.2

Source0: avldrums.lv2.tar.gz
Source1: x42-source.sh

BuildRequires: gcc gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
avldrums.lv2 is a simple Drum Sample Player Plugin by x42,
dedicated to the https://www.bandshed.net/avldrumkits/

%prep
%autosetup -n avldrums.lv2

%ifarch aarch64
sed -i -e "s|-msse2||g" Makefile
sed -i -e "s|-msse||g" Makefile
sed -i -e "s|-mfpmath=sse||g" Makefile
%endif
#TODO: use OPTIMIZATION flags instead. Check Makefile

%build

%set_build_flags

%make_build PREFIX=/usr LV2DIR=%{_libdir}/lv2 STRIP=true

%install

%make_install PREFIX=/usr LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/avldrums.lv2/*

%changelog
* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-2
- update to 0.7.2-2

* Fri Sep 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-2
- update to 0.7.0-2

* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-2
- update to 0.6.1-2

* Wed Mar 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- update to 0.6.0-2

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-2
- update to 0.5.2-2

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-2
- update to 0.5.1-2

* Sat Jul 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-2
- update to 0.5.0-2

* Thu Jan 14 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-2
- update to 0.4.2

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-2
- fix debug build

* Tue Dec 31 2019 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update to 0.4.1

* Thu Oct 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.4.0
- update to 0.4.0

* Tue Feb 12 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.3
- update to 0.3.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0
- update for Fedora 29
- update to f670fcdd228f3abf291cc8ec8fd14fe09fa1bfaf

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0
- update to 43b28a761ea980d176b66347a6f8a44fb4e84611

* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.2.2
- Initial build
