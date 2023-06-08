Summary: Collection of SuperCollider plugins
Name:    supercollider-sc3-plugins
Version: 3.13.0
Release: 4%{?dist}
License: GPL
URL:     https://github.com/supercollider/sc3-plugins/

# ./supercollider-sc3-source.sh <tag>
# ./supercollider-sc3-source.sh Version-3.13.0

Source0: sc3-plugins.tar.gz
Source1: supercollider-sc3-source.sh

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Requires: supercollider >= 3.5

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: supercollider-devel
BuildRequires: fftw-devel
BuildRequires: stk-devel

Obsoletes: supercollider-extras < 3.5
Provides:  supercollider-extras = %{version}-%{release}
Obsoletes: supercollider-beastmulchplugins < 3.5
Provides:  supercollider-beastmulchplugins = %{version}-%{release}
Obsoletes: supercollider-bbcut2 < 3.5
Provides:  supercollider-bbcut2 = %{version}-%{release}

%description
Collection of SuperCollider plugins

%prep
%autosetup -n sc3-plugins

sed -i -e "s/lib\/SuperCollider/%{_lib}\/SuperCollider/g" source/CMakeLists.txt

%build

%cmake -DSC_PATH=/usr/include/SuperCollider -DSUPERNOVA=ON

%cmake_build

%install

%cmake_install

%files
%doc README.md DEVELOPING.md
%license license.txt
%{_datadir}/SuperCollider/Extensions/SC3plugins
%{_libdir}/SuperCollider/plugins/*

%changelog
* Fri Feb 24 2023 Yann Collette <ycollette.nospam@free.fr> 3.13.0-4
- update to 3.13.0

* Tue Nov 17 2020 Yann Collette <ycollette.nospam@free.fr> 3.11.1-4
- update to 3.11.1

* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> 3.11.0-4
- fix for fedora 33

* Mon Aug 31 2020 Yann Collette <ycollette.nospam@free.fr> 3.11.0-3
- update to 3.11.9-3

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> 3.7.1-296-g42a1bc6-3
- fix for Fedora 32

* Wed Mar 27 2019 Yann Collette <ycollette.nospam@free.fr> 3.7.1-296-g42a1bc6-2
- fix build

* Mon Mar 25 2019 Yann Collette <ycollette.nospam@free.fr> 3.7.1-296-g42a1bc6-1
- update to Version-3.7.1-296-g42a1bc6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> 3.7.1-1.185-g6983e2d
- update for Fedora 29
- update to Version-3.7.1-270-g5e83bd9

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> 3.7.1-1.185-g6983e2d
- update to version 3.7.1-185-g6983e2d

* Thu Nov 2 2017  Yann Collette <ycollette.nospam@free.fr> 3.7.1-1.147.g04a3dca
- update to version 3.7.1-147-g04a3dca

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> 3.7.1-1.141.g5342a4a
- update to latest git for 3.7.1 release

* Fri Nov 25 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.7.1-1.102.gf1200cd
- update to latest git for 3.7.2 release
- bbcut2 is now part of sc3 plugins
- SSE and X86_64 no longer needed (compiles for mtune=generic with sse and sse2 only)
- always build with supernova

* Mon Aug  3 2015 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.6-0.4.g9367339
- update to latest git for 3.7.0 alpha1 and fc22

* Wed Dec 18 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.6-0.4.g34d0869
- update to latest git for 3.6.6
- change fftlib.h into SC_ffltlib.h

* Thu Jun 27 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.6-0.3.gbd15edb
- update to latest git for 3.6.5

* Mon Apr 22 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.6-0.2.g96a5f32
- update to latest git for 3.6.4
- changed release numbering to use git describe string

* Tue Mar 12 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.6-0.3.20130312
- update to latest git for 3.6.3

* Fri Jan 18 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.3.20130118
- update to new location for the git repository

* Thu Jan 17 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.3.20130117
- update to latest git for 3.6 build
- rework the arch and optimization patch
- fix wrong include file in nova gendy ugens

* Sun Jul 15 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.3.20120626
- strip weird characters from sc source files, causes problems 
  (apparently) with some locales

* Wed Jun 27 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.2.20120626
- updated to current source snapshot (after sc 3.5.3 was released)

* Tue May  8 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.2.git20120508
- update to current git

* Sat May  5 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.2.git20120317
- add obsoletes and provides for supercollider-extras and beastmulchplugins

* Sat Mar 17 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120317
- update to current git (to get latest ATK)

* Wed Feb 29 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120229
- update to current git

* Tue Feb 14 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120214
- update to current git
- remove -DSSE42 build option, only valid for Nehalem processors
- remove -DSSE41=ON build option, a Core Duo chokes on roundsd

* Wed Feb  1 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120201
- update to latest git (20120201)

* Fri Dec 30 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111230
- update to latest git

* Fri Oct 21 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111019
- sc3-plugins is no longer part of the sc3 source tree so split the
  package again... sigh... all plugins are in one package

* Thu Mar 26 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.20090325-0.svn350.1
- udpate to latest svn
- add patch to dynamically link against stk shared library
- symbolic machines moved into tagsystemugens
- bhobUGens is now BhobUGens
- ljpclasses is gone...

* Tue Mar 17 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.20090315-0.svn338.1
- udpate to latest svn

* Mon Nov 10 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.20081105-0.svn289.1
- updated to latest svn
- beqsuite has moved to the main supercollider package
- added supercollider-ladspa-ugens, supercollider-mkfftw-ugens, 
  supercollider-sl-ugens subpackages, supercollider-bat-ugens,
  supercollider-rmeqsuite-ugens packages
- relink JoshPVUgens with the proper libraries (otherwise fails to load
  with unknown symbol warnings)

* Thu Oct  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.20080331-0.svn126.2
- updated stk build dependencies for fedora 9
- added obsoletes for old supercollider-beqsuite packages

* Sat Apr  5 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.20080331-0.svn126.1
- upgraded to current svn (revision 216)
- JoshPVUGens now merged into JoshUGens
- new: MembraneUGens, SymbolicMachines, TagSystemUGens
- removed: ReverbUGens (now part of the core SuperCollider classes)

* Sat Nov 17 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- Headers are now coming from a different location

* Thu Jul 26 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2007.07.26-1.119svn
- updated to revision 119

* Fri Mar  9 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.20070308-1.64svn
- initial build of the sc3-plugins collection, split into multiple
  packages with each collection in a separate package (check out
  collection from svn, use svn checkout date as version, include
  svn revision in the release tag)
- fix missing include in bhobFFT.cpp (patch0)
- do not build bhobFFT plugins or install the FFT class or the PV 
  help files, the plugin fails to link properly:

ldd -r -d bhobFFT.so
undefined symbol: _Z17initPV_ThirdPartyP14InterfaceTable        (./bhobFFT.so)
undefined symbol: _Z12ToComplexApxP6SndBuf      (./bhobFFT.so)
undefined symbol: _Z10ToPolarApxP6SndBuf        (./bhobFFT.so)
        linux-gate.so.1 =>  (0xffffe000)
        libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0xf7f07000)
        libm.so.6 => /lib/libm.so.6 (0xf7ee2000)
        libgcc_s.so.1 => /lib/libgcc_s.so.1 (0xf7ed8000)
        libc.so.6 => /lib/libc.so.6 (0xf7daf000)
        /lib/ld-linux.so.2 (0x56555000)
