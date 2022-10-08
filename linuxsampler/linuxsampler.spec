# Tag: Jack, Sfz, Alsa
# Type: Plugin, DSSI, LV2
# Category: Audio, Sampler

Summary: Linux Sampler
Name:    linuxsampler
Version: 2.1.1
Release: 2%{?dist}
License: GPL
URL:     https://www.LinuxSampler.org/

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: https://download.linuxsampler.org/packages/linuxsampler-%{version}.tar.bz2
Patch0: linuxsampler-0001-aarch64-fix.patch

BuildRequires: gcc gcc-c++
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: make
BuildRequires: perl-XML-Parser
BuildRequires: flex
BuildRequires: bison
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: libgig-devel
BuildRequires: alsa-lib-devel
BuildRequires: sqlite-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: dssi-devel
BuildRequires: slv2-devel

%description
LinuxSampler is a work in progress. The goal is to produce a free,
open source pure software audio sampler with professional grade
features, comparable to both hardware and commercial Windows/Mac
software samplers.

%package devel
Summary:  Linux Sampler development files
Requires: %{name} = %{version}-%{release}

%description devel
Libraries and include files for Linux Sampler development

%package dssi
Summary:  Linux Sampler DSSI plugin
Requires: %{name} = %{version}-%{release}

%description dssi
Linuxsampler plugin for the Disposable Soft Synth Interface (DSSI).

%package -n lv2-linuxsampler-plugins
Summary:  Linux Sampler LV2 plugin
Requires: %{name} = %{version}-%{release}

%description -n lv2-linuxsampler-plugins
Linuxsampler plugin for the LV2 plugin standard.

%prep
%setup -n linuxsampler%{!?svn:-%{version}}

%ifarch aarch64
%patch0 -p1
%endif

%set_build_flags
export CXXFLAGS="CXXFLAGS -std=c++14"
if [ -f Makefile.svn ]; then make -f Makefile.svn; fi

%build

%configure CXXFLAGS="$CXXFLAGS -std=c++14"
%make_build

%install
%make_install
# add path to linuxsampler libraries
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/linuxsampler" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/linuxsampler.conf

rm -f %{buildroot}/%{_libdir}/linuxsampler/*.la
rm -f %{buildroot}/%{_libdir}/dssi/linuxsampler.la
rm -f %{buildroot}/%{_libdir}/lv2/linuxsampler.lv2/linuxsampler.la

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/linuxsampler
%{_libdir}/linuxsampler/*.so.*
%{_mandir}/man1/*
/var/lib/linuxsampler/instruments.db
%{_sysconfdir}/ld.so.conf.d/linuxsampler.conf
%{_bindir}/ls_instr_script
%{_bindir}/lscp

%files devel
%{_libdir}/linuxsampler/*.so
%{_libdir}/linuxsampler/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/linuxsampler

%files dssi
%{_libdir}/dssi/linuxsampler.so
%exclude %{_libdir}/dssi/linuxsampler.a

%files -n lv2-linuxsampler-plugins
%{_libdir}/lv2/linuxsampler.lv2/linuxsampler.so
%{_libdir}/lv2/linuxsampler.lv2/linuxsampler.ttl
%{_libdir}/lv2/linuxsampler.lv2/manifest.ttl
%exclude %{_libdir}/lv2/linuxsampler.lv2/linuxsampler.a

%changelog
* Sat Mar 27 2021 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-2
- update to 2.1.1-2 - fixes for Fedora 34

* Thu Nov 5 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-1
- update to 2.1.1

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.0.0-1
- update to 2.0.0

* Wed Dec 10 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-6.svn2680.1
- update to svn 2680, fixes fc21 build problems
- add ls_instr_script lscp to the file list

* Wed May 30 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-6.svn2346.1
- update to svn 2346, fixes fc17 build problems

* Wed Mar  7 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-6.svn2325.1
- update to current svn for bzf support

* Sat Sep 18 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-5
- add /etc/ld.so.conf.d/linuxsampler.conf so that libraries can be
  found by other programs (gigedit is affected, fix thanks to Luis
  Garrido), add ldconfig post(un) scripts, add bison build
  requirement

* Tue May 25 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-3
- remove patch (does not seem to affect linuxsampler but remove it
  anyway), the problem with pitch bend was range being set to 0 in 
  certain instruments - that can be edited with gigedit (right click
  on the instrument to get to the options panel)

* Tue Nov 10 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-2
- added patch to ignore PitchBendRange (defaults to 0, ie: no pitch
  bend so copy code that uses it from previous version)

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-1
- updated to 1.0.0, number of voices is now runtime controllable
- added dssi and lv2 build requirements, linuxsampler can now be a
  plugin in both standards
- create linuxsample-dssi and lv2-linuxsampler-plugins subpackages

* Sun Mar 29 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-3
- changed voices from 64 to 96 and streams from 90 to 110

* Mon Jul  7 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-2
- added patch to build on fc9 with gcc 4.3

* Tue May 13 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-1
- updated to version 0.5.0
- added sqlite-devel build requirement
- add intruments.db to file list, no longer a libdir/linuxsampler/include
  directory

* Wed Jan 17 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-2
- assembler was being mistakenly turned on despite --disable-asm, 
  default now is off and nothing is needed (if disable-asm is used
  asm is turned on!)

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- updated to 0.4.0
- added include and pkgconfig files to file list
- split development files into -devel package

* Wed Apr  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.3-1
- updated to 0.3.3
- assembler optimizations are broken, disable them

* Sun Jul  3 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added gcc4 patch, posted by Andreas Persson in the linuxsampler
  mailing list

* Fri Jul  1 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added sse flags to gig engine build

* Wed Jun 29 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.2-1
- updated to 0.3.2

* Thu May 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.1-1
- updated to official 0.3.1 release (from cvs)

* Thu Jan 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2004.01.20
- initial build.
