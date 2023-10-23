# Tag: Jack
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: Sequenced audio slicing effect LV2 plugin (Step sequencer effect).
Name:    lv2-BSlizr
Version: 1.2.16
Release: 3%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BSlizr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sjaehn/BSlizr/archive/%{version}.tar.gz#/BSlizr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
LV2 audio effect plugin for chopping stereo audio input signals.
Each chop can be levelled up or down to get a step sequencer-like effect.

%prep
%autosetup -n BSlizr-%{version}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} \
	    LV2DIR=%{_libdir}/lv2 \
	    DESTDIR=%{buildroot} \
	    STRIP=true \
	    CXXFLAGS="$CXXFLAGS -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} \
	      LV2DIR=%{_libdir}/lv2 \
	      DESTDIR=%{buildroot} \
	      STRIP=true \
	      CXXFLAGS="$CXXFLAGS -include stdexcept -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sat Nov 19 2022 Yann Collette <ycollette dot nospam at free.fr> 1.2.16-3
- update to 1.2.16-3

* Fri Sep 10 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.12-3
- update to 1.2.12-3 - fix install

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.12-2
- update to 1.2.12-2

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.2.10-2
- update to 1.2.10-2

* Sun Jun 14 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.8-2
- update to 1.2.8-2

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.6-2
- fix for Fedora 32

* Sun Apr 12 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.6-1
- update to 1.2.6-1

* Mon Jan 6 2020 Yann Collette <ycollette dot nospam at free.fr> 1.2.4-1
- update to 1.2.4-1

* Mon Nov 25 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.2-1
- update to 1.2.2-1

* Fri Oct 11 2019 Yann Collette <ycollette dot nospam at free.fr> 1.2.0-1
- initial release
