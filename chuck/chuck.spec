# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

Name:    chuck
Summary: Real-time audio synthesis and graphics/multimedia language
Version: 1.5.0.8
Release: 2%{?dist}
License: GPL
URL:     https://chuck.cs.princeton.edu/

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: https://github.com/ccrma/chuck/archive/refs/tags/chuck-%{version}.tar.gz
# emacs mode from: http://wiki.cs.princeton.edu/index.php/Recent_chuck-mode.el
Source1: chuck-mode.el

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: bison
BuildRequires: flex
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: pulseaudio-libs-devel

%description
ChucK is a general-purpose programming language, intended for
real-time audio synthesis and graphics/multimedia programming.  It
introduces a truly concurrent programming model that embeds timing
directly in the program flow.  Other potentially useful features include
the ability to write/change programs on-the-fly.

%prep
%autosetup -n chuck-chuck-%{version}

%build

%set_build_flags

cd src

# insert rpm optflags in makefiles
sed -i -e "s|-O3|-O3 %{optflags}|g" makefile
    
# build alsa version
%make_build linux-alsa
mv chuck chuck-alsa

# build pulse version
%make_build clean
%make_build linux-pulse
mv chuck chuck-pulse

# build jack version
%make_build clean
%make_build linux-jack
mv chuck chuck-jack

%install

mkdir -p %{buildroot}%{_bindir}

# install alsa version
install -m 755 src/chuck-alsa %{buildroot}%{_bindir}/chuck-alsa

# install alsa version
install -m 755 src/chuck-pulse %{buildroot}%{_bindir}/chuck-pulse

# install jack version
install -m 755 src/chuck-jack %{buildroot}%{_bindir}/chuck-jack

# install emacs mode
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
cp -a %{SOURCE1} %{buildroot}%{_datadir}/emacs/site-lisp/chuck.el
mkdir -p %{buildroot}%{_libdir}/xemacs/site-packages/lisp/chuck/
cp -a %{SOURCE1} %{buildroot}%{_libdir}/xemacs/site-packages/lisp/chuck/chuck.el

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/emacs/site-lisp/*
%{_libdir}/xemacs/site-packages/lisp/chuck/*

%changelog
* Thu Aug 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.8-2
- update to 1.5.0.8-2

* Tue Jul 11 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.7-2
- update to 1.5.0.7-2

* Sat Jul 08 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.6-2
- update to 1.5.0.6-2

* Thu Jul 06 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.5-2
- update to 1.5.0.5-2

* Thu Jun 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.4-2
- update to 1.5.0.4-2

* Sun Jun 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.3-2
- update to 1.5.0.3-2

* Fri May 19 2023 Yann Collette <ycollette.nospam@free.fr> - 1.5.0.0-2
- update to 1.5.0.0-2

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 1.4.2.0-2
- update to 1.4.2.0-2

* Wed Jul 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.4.1.0-2
- update to 1.4.1.0-2

* Thu Nov 05 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0.1-2
- update to 1.4.0.1

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.4.0.0-2
- fix debug build

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.4.0.0-1
- update for Fedora 29
- update to 1.4.0.0

* Wed Oct 12 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.6.0-1.220a
- update to experimental 1.3.6.0 (released for the 220a class)

* Tue Jan 14 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.3.0-1
- update to 1.3.3, add pulse build

* Sun Sep 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.2.0-1
- final 1.3.2.0 release

* Sat Sep 14 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add optflags for proper build on arm

* Thu Aug 29 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.2.0-0.1.beta4
- update to latest beta-4 test release
- add patch for util_thread.h

* Tue Oct  2 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.3-1
- updated to 1.3.1.3

* Sun Sep 16 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.2-1
- updated to 1.3.1.2

* Thu Sep 13 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.1-1
- updated to 1.3.1.1

* Fri Sep  7 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.1.0-1
- updated to 1.3.1.0, now 64 bit native

* Wed Aug 29 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.0.2-1
- updated to 1.3.0.2

* Sat Aug 25 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.3.0.0-1
- updated to 1.3.0.0

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.3-1
- added -lpthread patch to build on fc13/gcc444

* Mon Oct 12 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.3-1
- updated to 1.2.1.3

* Thu Sep  3 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-2
- change build flags on fc11, otherwise segfaults on startup

* Thu Jun 11 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-1
- add gcc44 patch for building on fc11

* Fri Jul 18 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.2-1
- updated to 1.2.1.2 (keep building it with -DAJAY for experimental
  features)

* Wed Jul  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- build fixes for gcc4.3 on fc9

* Mon Oct  8 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1c-1
- unofficial update/fix release

* Thu Oct  4 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1-2
- small bug fix release (no change in main version number)

* Wed Oct  3 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.1.1-1
- updated to 1.2.1.1, updated emacs mode to latest version

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.7-2
- build for fc6

* Fri Sep 22 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.7-1
- updated to 1.2.0.7, redid makefile patch for defining -DAJAY
  (to enable the PRC and Skot objects)

* Tue Jul 25 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.6-3
- keep the old chuck.el file name (not chuck-mode.el)

* Tue Jul 25 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.6-2
- updated to 1.2.0.6, updated emacs mode file

* Wed Jul 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.5-2
- build with additional experimental objects (see patch0), thanks to
  Ge Wang for the tip
- add an alsa only chuck in /usr/bin/chuck-alsa
- install emacs mode for chuck files

* Mon Jul 10 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.2.0.5-1
- initial build.
