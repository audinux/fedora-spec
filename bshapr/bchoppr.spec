# Tag: Jack
# Type: Plugin, LV2
# Category: Audio, Effect

Summary: An audio stream chopping LV2 plugin
Name:    lv2-BChoppr
Version: 1.12.4
Release: 3%{?dist}
License: GPL
URL:     https://github.com/sjaehn/BChoppr

Vendor:       Audinux
Distribution: Audinux

# ./sjaehn-source.sh <project> <tag>
# ./sjaehn-source.sh BChoppr 1.12.4

Source0: BChoppr.tar.gz
Source1: sjaehn-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: cairo-devel

%description
BChoppr cuts the audio input stream into a repeated sequence of up to 16 chops.
Each chop can be leveled up or down (gating). BChoppr is the successor of BSlizr

%prep
%autosetup -n BChoppr

%build

%set_build_flags

%make_build PREFIX=%{_prefix} \
	    LV2DIR=%{_libdir}/lv2 \
	    DESTDIR=%{buildroot} \
	    STRIP=true \
	    CXXFLAGS="$CXXFLAGS -include stdexcept -include array -std=c++11 -fvisibility=hidden -fPIC"

%install

%make_install PREFIX=%{_prefix} \
	      LV2DIR=%{_libdir}/lv2 \
	      DESTDIR=%{buildroot} \
	      STRIP=true \
	      CXXFLAGS="$CXXFLAGS -include stdexcept -include array -std=c++11 -fvisibility=hidden -fPIC"

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu Dec 08 2022 Yann Collette <ycollette dot nospam at free.fr> 1.12.4-3
- updata to 1.12.4-3

* Mon Nov 21 2022 Yann Collette <ycollette dot nospam at free.fr> 1.12.2-3
- updata to 1.12.2-3

* Sat Nov 19 2022 Yann Collette <ycollette dot nospam at free.fr> 1.12.0-3
- updata to 1.12.0-3

* Fri Sep 10 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.10-3
- updata to 1.10.10-3

* Sun Jun 06 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.8-2
- updata to 1.10.8-2

* Sun Apr 18 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.6-2
- updata to 1.10.6-2

* Thu Feb 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.4-2
- updata to 1.10.4-2

* Fri Jan 29 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.2-2
- updata to 1.10.2-2

* Mon Jan 11 2021 Yann Collette <ycollette dot nospam at free.fr> 1.10.0-2
- updata to 1.10.0-2

* Thu Aug 27 2020 Yann Collette <ycollette dot nospam at free.fr> 1.8.0-2
- updata to 1.8.0-2

* Thu Jun 25 2020 Yann Collette <ycollette dot nospam at free.fr> 1.6.4-2
- updata to 1.6.4

* Fri Apr 24 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-2
- fix for Fedora 32

* Thu Apr 2 2020 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- initial release 
