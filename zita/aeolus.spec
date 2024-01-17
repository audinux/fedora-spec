# Tag: Organ, Jack, Alsa
# Type: Standalone
# Category: Audio, Synthesizer

%define aeolus_ver 0.10.4
%define stops_ver  0.4.0

%define desktop_vendor planetccrma

Name:    aeolus
Summary: A synthesized pipe organ
Version: %{aeolus_ver}%{?aeolus_rel:.%{aeolus_rel}}
Release: 1%{?dist}
License: GPL
URL:     http://www.kokkinizita.net/linuxaudio/aeolus/index.html

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/aeolus-%{aeolus_ver}%{?aeolus_rel:-%{aeolus_rel}}.tar.bz2
Source1: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/stops-%{stops_ver}.tar.bz2
Source2: aeolus.desktop

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Obsoletes: aeolus-stops <= 0.4.0-1
Provides:  aeolus-stops = 0.4.0-1

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: readline-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: desktop-file-utils

%description
Aeolus is a synthesised (i.e. not sampled) pipe organ emulator that
should be good enough to make an organist enjoy playing it. It is a
software synthesiser optimised for this job, with possibly hundreds of
controls for each stop, that enable the user to "voice" his
instrument. Main features of the default instrument: three manuals and
one pedal, five different temperaments, variable tuning, IDI control
of course, stereo, surround or Ambisonics output, flexible audio
controls including a large church reverb.

%prep
%autosetup -n aeolus-%{aeolus_ver}

cd source
# change the default stops directory to point to the installed stops
sed -i -e "s|\".stops\", \"stops\"|\".stops\", \"%{_datadir}/aeolus/stops\"|g" mainwin.cc
# don't ldconfig during build
sed -i -e "s|ldconfig|# ldconfig|g" Makefile
# tweak build flags
sed -i -e "s|-O3|%{optflags}|g" Makefile
sed -i -e "s|-march=native||" Makefile

%build

cd source

%set_build_flags
%make_build PREFIX=/usr LIBDI=%{_libdir}

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/aeolus

cd source
%make_install PREFIX=/usr LIBDIR=%{_libdir}

# install the stops
(cd %{buildroot}%{_datadir}/aeolus; %{__tar} xjf %{SOURCE1}; %{__mv} stops-* stops)
rm -f %{buildroot}%{_datadir}/aeolus/stops/Makefile
# make sure they are readable
find %{buildroot}%{_datadir}/aeolus/stops -type f -exec chmod 644 {} \;

# set reasonable default startup options:
# jack driver, point to stops, store presets in user home directory
mkdir -p %{buildroot}%{_sysconfdir}
cat << EOF > %{buildroot}%{_sysconfdir}/aeolus.conf
# Aeolus default options
-J -S %{_datadir}/aeolus/stops -u
EOF

# desktop file categories
BASE="Application AudioVideo Audio"
XTRA="X-MIDI X-Jack X-Synthesis Midi"

mkdir -p %{buildroot}%{_datadir}/applications

desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{SOURCE2}

%files
%doc AUTHORS INSTALL
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_sysconfdir}/*
%{_datadir}/aeolus/stops
%{_datadir}/applications/%{desktop_vendor}-aeolus.desktop

%changelog
* Wed May 11 2022 Yann Collette <ycollette.nospam@free.fr> - 0.10.3-2
- update to 0.10.3-2

* Wed May 04 2022 Yann Collette <ycollette.nospam@free.fr> - 0.10.1-2
- update to 0.10.1-2

* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-2
- fix debug build

* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.8-1
- update to 0.9.8

* Wed Feb 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-1
- update to 0.9.7

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- update for Fedora 29

* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9.5-1
- update to 0.9.5

* Thu Oct 17 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-1
- update to latest for fc19

* Fri Jul 29 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.4-2
- disable creation of debuginfo packages on fc15 until a real fix is found
  the two weird debug dependencies are for the internal aeolus shared
  object files...

* Thu Jul 21 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.4-1
- add -lclxclient to path0 to build on fc15, thanks to Martin Tarenskeen
  for the fix

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.4-1
- updated to 0.8.4, added patch to link against libdl in fc13

* Wed Oct 29 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.2-1
- updated to 0.8.2

* Tue Apr 15 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.1-1
- updated to 0.8.1

* Tue Oct  9 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.6.2-2
- updated desktop categories

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.6.2-1
- updated to version 0.6.6-2 (beta version with MIDI control of stops)
- spec file tweaks

* Sat May 13 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.6-1
- updated to 0.6.6, stops to 0.3.0

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- proper build dependencies for fc5
- patch for gcc 4.1

* Mon Jul 11 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.1-2
- obsolete aeolus-stops and include the stops in the main package

* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Fri Dec  3 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.1-1
- updated to 0.3.1

* Thu Jul 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- changed default stops directory to /usr/share/aeolus/stops
- deleted startup script

* Fri Jul 23 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1-1
- updated to 0.2.1 and stops 0.0.9

* Mon Jun 14 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- updated to 0.2.0

* Tue May 11 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added alsa-lib-devel buildrequires

* Tue May  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- initial build
