# Tag: Mixer, Editor
# Type: IDE, Standalone
# Category: DAW

# find out stuff about python
%define pythonbin %(if [ -x /usr/bin/python2 ] ; then echo "python2" ; else echo "python3" ; fi)
%define python_pkgsdir %(echo `%{pythonbin} -c "import sys; print (sys.prefix + '/%{_lib}/python' + sys.version[:3])"`)
%define python_version %(echo `%{pythonbin} -c "import sys; print (sys.version[:3])"`)
%define python_compile_opt %{pythonbin} -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile %{pythonbin} -c "import compileall; compileall.compile_dir('.')"

%define makepdf 0

Summary: ecasound - multitrack audio processing tool
Name:    ecasound
Version: 2.9.3
Release: 1%{?dist}
Epoch:   1
URL:     https://ecasound.seul.org/ecasound/
License: GPL

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Source0: http://ecasound.seul.org/download/ecasound-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: python2
BuildRequires: python2-devel
BuildRequires: python3
BuildRequires: python2-devel
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: hevea
BuildRequires: python3-docutils
BuildRequires: liboil-devel
BuildRequires: texlive
BuildRequires: texlive-latex-bin-bin
BuildRequires: texlive-texlive-scripts-extra
BuildRequires: texlive-metafont-bin
BuildRequires: texlive-comment
BuildRequires: ladspa
BuildRequires: lilv-devel
BuildRequires: liblo-devel

%description
Ecasound is a software package designed for multitrack audio
processing. It can be used for simple tasks like audio playback,
recording and format conversions, as well as for multitrack effect
processing, mixing, recording and signal recycling. Ecasound supports
a wide range of audio inputs, outputs and effect algorithms.
Effects and audio objects can be combined in various ways, and their
parameters can be controlled by operator objects like oscillators
and MIDI-CCs. A versatile console mode user-interface is included
in the package.

%package devel
Summary:  Ecasound - development files
Requires: ecasound >= %{version}-%{release}

%description devel
The ecasound-devel package contains the header files and static libraries
necessary for building apps like ecawave and ecamegapedal that
directly link against ecasound libraries.

%package -n libecasoundc
Summary:  Ecasound - libecasoundc
Requires: ecasound >= %{version}-%{release}

%description -n libecasoundc
Ecasound - libecasoundc package. Provides
C implementation of the Ecasound Control Interface
(ECI). Both static library files and and header
files are included in the package.

%package -n pyecasound
Summary:  Python bindings to ecasound control interface.
Requires: ecasound

%description -n pyecasound
Python bindings to Ecasound Control Interface (ECI).

%package -n rubyecasound
Summary:  Ruby bindings to ecasound control interface.
Requires: ecasound

%description -n rubyecasound
Ruby bindings to Ecasound Control Interface (ECI).

%prep
%autosetup -n ecasound-%{version}

%build

%set_build_flags

# add redhat/fedora optimizations, do not build with -g
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%configure --with-largefile \
	   --enable-shared \
	   --with-python-modules=%{_libdir}/python%{python_version} \
	   CFLAGS="$CFLAGS" \
	   CXXFLAGS="$CXXFLAGS"

%make_build

# build the documentation
%if %makepdf
cd Documentation/users_guide
make ecasound_users_guide.pdf
cd ../programmers_guide/
make docs
%endif

%install
%make_install
( cd pyecasound
  %python_compile_opt
  %python_compile
  mkdir -p %{buildroot}%{python_pkgsdir}/site-packages/
  install *.py *.pyc *.pyo %{buildroot}%{python_pkgsdir}/site-packages/
  rm %{buildroot}%{python_pkgsdir}/site-packages/test{1,2}_stresstest.py
)
# ruby file is installed in the wrong place
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ruby/vendor_ruby/
cp rubyecasound/ecasound.rb $RPM_BUILD_ROOT%{_datadir}/ruby/vendor_ruby/
rm -rf $RPM_BUILD_ROOT%{_usr}/local/share/ruby/

# Fix python / python2
sed -i -e "s/env python$/env python2/g" $RPM_BUILD_ROOT%{_bindir}/ecamonitor

# Cleanup
rm -f %{buildroot}/%{_libdir}/libecasound.la
rm -f %{buildroot}/%{_libdir}/libkvutils.la

%files
%doc NEWS README INSTALL AUTHORS BUGS TODO examples
%license COPYING COPYING.GPL COPYING.LGPL
%if %makepdf
%doc Documentation/users_guide/ecasound_users_guide.pdf
%doc Documentation/users_guide/html_uguide
%endif
%{_mandir}/man1/eca*
%{_mandir}/man5/eca*
%{_bindir}/ecasound
%{_bindir}/ecaconvert
%{_bindir}/ecafixdc
%{_bindir}/ecamonitor
%{_bindir}/ecanormalize
%{_bindir}/ecalength
%{_bindir}/ecaplay
%{_bindir}/ecasignalview
%{_datadir}/ecasound/ecasoundrc
%{_datadir}/ecasound/ecasound.el
%config %{_datadir}/ecasound/generic_oscillators
%config %{_datadir}/ecasound/effect_presets

%files devel
%if %makepdf
%doc Documentation/programmers_guide/ecasound_programmers_guide.*
%doc Documentation/programmers_guide/ecasound_eci_doc.pdf
%doc Documentation/programmers_guide/html_ecidoc/
%endif
%{_bindir}/libecasound-config
%{_includedir}/kvutils
%{_includedir}/libecasound
%{_libdir}/libecasound.a
%{_libdir}/libkvutils.a

%files -n libecasoundc
%{_bindir}/libecasoundc-config
%{_includedir}/libecasoundc
%{_libdir}/libecasoundc.a

%files -n pyecasound
%defattr(644,root,root,755)
%{python_pkgsdir}/site-packages/*.pyo
%{python_pkgsdir}/site-packages/*.pyc
%{python_pkgsdir}/site-packages/*.py

%files -n rubyecasound
%defattr(644,root,root,755)
%{_datadir}/ruby/vendor_ruby/ecasound.rb

%changelog
* Wed Oct 06 2021 Yann Collette <ycollette.nospam@free.fr> - 2.9.3-2
- Fix for Fedora 35

* Thu Apr 01 2021 Yann Collette <ycollette.nospam@free.fr> - 2.9.3-2
- Fix for Fedora 34

* Thu Nov 05 2020 Yann Collette <ycollette.nospam@free.fr> - 2.9.3-1
- update to 2.9.3-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2.9.1-1
- update for Fedora 29

* Mon Nov  9 2015 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.9.1-1
- remove install strip option to fix packaging on fc23

* Thu Feb  6 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.9.1-1
- fix rubyecasound path

* Wed Dec 18 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- removed documentation build, the system can't seem to find hevea.sty
  although it is installed

* Thu Jan 17 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.9.0-1
- updated to 2.9.0
- add lilv, liblo, ladspa build requirements
- adjusted latex requirements

* Thu Dec  2 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.7.2-1
- updated to 2.7.2, added liboil build dependency

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.7.0-1
- updated to 2.7.0

* Fri Feb 20 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.6.0-1
- updated to 2.6.0
- properly build documentation (html & pdf)

* Tue Jun 17 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added gcc 4.3 patch from gentoo ebuild for fc9 build

* Thu Sep 20 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.6.1-1
- updated to 2.4.6.1, added readline-devel build dependency to get
  readline support

* Thu Jun  7 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.5-1
- build on fc7, fix detection of python 2.5

* Thu May 10 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.5-1
- updated to 2.4.5, fixed pyecasound build (lib64 issues)
- spec file cleanup

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added --enable-shared to build on x86_64, deleted --disable-static

* Fri Nov 24 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.4-2
- updated spec file to use %%{?dist}

* Sat May  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.4-1
- updated to 2.4.4

* Wed Nov 30 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.3-1
- updated to 2.4.3

* Fri Aug 19 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.2-2
- updated to 2.4.2
- don't do any stripping (fixes fc3 build), was only needed when
  using automake 1.4 and rh9 uses 1.6 by default
- erase old rh73 conditionals

* Mon May 30 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- changed obsolete tag Serial: to Epoch: and Copyright: to License:

* Fri Apr  8 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.1-1
- updated to 2.4.1, removed support for building with arts

* Tue Mar 22 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.4.0-1
- updated to 2.4.0, added patch to fix arts support (from cvs snapshot)

* Sun Dec 19 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Mon Nov 15 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.5-1
- updated to 2.3.5
- add instruction ordering optimizations to build, ecasound uses
  AM_CFLAGS and AM_CXXFLAGS. Do not compile -g.

* Wed May  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.3-1
- updated to 2.3.3
- forced use of python2 under 7.3 (can't use "import as" in 1.5)

* Fri Dec  5 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.2-1
- updated to 2.3.2, added rubyecasound

* Wed Nov 19 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.1-1
- added missing preset.h include file

* Tue Nov 18 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.1-1
- updated to 2.3.1

* Fri Nov  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.0-2
- added flags for building with alsa > 0.9.8

* Fri Aug 29 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.3.0-1
- updated to 2.3.0, added release tags

* Wed Aug 20 2003 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- added 'AUTHORS' file

* Wed May 21 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.3-2
- rebuilt with --with-largefile option
- added patch for audiofile support

* Tue May  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.3-1
- updated to 2.2.3

* Mon Apr  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.2-1
- under rh9 the "install" macro call in the changelog was triggering
  a "package already defined debuginfo" error
- updated to current cvs so that it can compile with the latest jack
- fixed files lists

* Tue Mar 18 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 2.2.2-1
- updated to 2.2.2

* Sat Feb 15 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated to 2.2.1

* Mon Jan 20 2003 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- added Serial tag to differentiate between 2.2 pre and
  final releases

* Sun Jan 19 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- rebuild 2.2.0 for Planet CCRMA


* Sat Nov 02 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- ported Fernando Lopez-Lezcano's changes to unify this
  spec file with PlanetCCRMA's ecasound package; see
  http://ccrma-www.stanford.edu/planetccrma/software/soundapps.html
- ecasound.el added to package (installed as a data
  file to avoid dependency to emacs/elisp)
- removed unnecessary raw documentation source files
- man files are no longer installed as doc files
- use redhat style mandir location

* Thu Oct 31 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- minor layout changes
- added TODO to the package
- changed to use rpmrc dir variables

* Thu Oct 24 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- added the COPYING files to the package

* Thu Oct 17 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- added the -devel package
- fixed the build procedure to handle static builds

* Wed Oct 16 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- removed all shared libraries and subpackages containing
  them
- ecamonitor binary added to main package

* Sat Oct 05 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- changed libecasoundc versioning back to normal libtool style

* Thu Apr 25 2002 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- libraries put to separate subpackages, interface
  version numbers code to library names
- ecasound-config renamed to libecasound-config
- ecasoundc-config renamed to libecasoundc-config
- plugin install dir changed from prefix/lib/ecasound-plugins
  to prefix/lib/libecasoundX-plugins
- 'contrib' directory removed
- ecasound-plugins subpackage renamed to libecasoundX-plugins

* Mon Oct 01 2001 Kai Vehmanen <kai.vehmanen@wakkanet.fi>
- dropped the hardcoded python module path from configure
  argument list

* Wed Jan 17 2001 Kai Vehmanen <kaiv@wakkanet.fi>
- python subpackage config (thanks to wrobell / PLD Linux!)

* Sat Dec 06 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- contrib and examples directories added to docs
- ecasoundc-config added
- libecasoundc added (C implementation of ECI)
- a new package: pyecasound

* Sat Nov 25 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- ecasignalview added to the package.

* Thu Aug 31 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- Added /etc/ld.so.conf modification script.
- Added DESTDIR to %%install.

* Wed Aug 30 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- 'ecasound-config' script added.

* Sun Aug 20 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- All Qt-related stuff removed.

* Wed Jul 06 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- Added the -plugins package.

* Wed Jun 07 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- ecaconvert added to the package.

* Mon Jun 05 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- Renamed ecatools programs.

* Mon Apr 15 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- Removed dynamic linking to ALSA libraries. You
  can get ALSA support by recompiling the source-RPM
  package.

* Mon Feb 10 2000 Kai Vehmanen <kaiv@wakkanet.fi>
- Added libqtecasound to ecasound-qt.

* Mon Nov 09 1999 Kai Vehmanen <kaiv@wakkanet.fi>
- A complete reorganization. Ecasound distribution is now
  divided to three RPMs: ecasound, ecasound-qt and ecasound-devel.

* Mon Nov 08 1999 Kai Vehmanen <kaiv@wakkanet.fi>
- As Redhat stopped the RHCN project, so these rpms
  are again distributed via Redhat's contrib service
- You can also get these from http://ecasound.seul.org/download

* Sun Aug 15 1999 Kai Vehmanen <kaiv@wakkanet.fi>
- Initial rhcn release.
