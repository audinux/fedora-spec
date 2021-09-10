# Tag: Jack
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: Beat / envelope shaper LV2 plugin
Name:    lv2-BShapr
Version: 0.13
Release: 2%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BShapr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sjaehn/BShapr/archive/v%{version}.tar.gz#/BShapr-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
B.Shapr is an envelope plugin for time or beat position-dependent effects. 
The user can define up to four different envelope shapes by drawing Bezier curves. 
Each of these envelope shapes can be connected to different target effects, such as amplification, balance, 
stereo width, filters, pitch shift, delay, and distortion effects and can be combined together.

%prep
%autosetup -n BShapr-%{version}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} \
	    LV2DIR=%{_libdir}/lv2 \
	    DESTDIR=%{buildroot} \
	    STRIP=true \
	    CXXFLAGS="$CXXFLAGS -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} \
	      LV2DIR=%{_libdir}/lv2 \
	      DESTDIR=%{buildroot} \
	      STRIP=true \
	      CXXFLAGS="$CXXFLAGS -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Sep 10 2021 Yann Collette <ycollette dot nospam at free.fr> 0.13.0-2
- update to 0.13.0-2 - fix install

* Sun Jun 06 2021 Yann Collette <ycollette dot nospam at free.fr> 0.13.0-1
- update to 0.13.0-1

* Wed Mar 17 2021 Yann Collette <ycollette dot nospam at free.fr> 0.12.0-1
- update to 0.12.0-1

* Mon Mar 15 2021 Yann Collette <ycollette dot nospam at free.fr> 0.11.0-1
- update to 0.11.0-1

* Sun Feb 7 2021 Yann Collette <ycollette dot nospam at free.fr> 0.10.0-1
- update to 0.10.0-1

* Mon May 25 2020 Yann Collette <ycollette dot nospam at free.fr> 0.9.0-1
- update to 0.9.0-1

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 0.8.0-1
- update to 0.8.0-1

* Thu Jan 16 2020 Yann Collette <ycollette dot nospam at free.fr> 0.7.0-1
- update to 0.7.0-1

* Sat Nov 30 2019 Yann Collette <ycollette dot nospam at free.fr> 0.6.0-1
- update to 0.6.0-1

* Sun Oct 13 2019 Yann Collette <ycollette dot nospam at free.fr> 0.4.0-1
- update to 0.4.0-1

* Sat Aug 24 2019 Yann Collette <ycollette dot nospam at free.fr> 0.3.2-1
- initial release 
