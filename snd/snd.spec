# Tag: Tool, Audio, Editor
# Type: Standalone
# Category: Tool, Audio

%define pkgver 22.5
%define tarname snd-%{pkgver}
%define snd_date "03/07/2022"

%define	desktop_vendor planetccrma

# configuration options (note: check later --with-rt)
%define config_options --prefix=%{_prefix} --with-alsa --with-jack --with-ladspa --with-doc-dir=%{_datadir}/doc/snd-%{pkgver}

# Tag: Editor, Legacy
# Type: Standalone
# Category: Audio, Tool

Summary: A sound editor (%{pkgver}, %{snd_date})
Name: snd
Version: %{pkgver}
Release: 1%{?dist}
License: LGPL
URL: https://ccrma.stanford.edu/software/snd/

Source:	 https://ccrma.stanford.edu/software/snd/snd-%{pkgver}.tar.gz
Source1: snd.png
Source2: snd.desktop
Patch0:  snd-13-docdir.patch

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Requires: hicolor-icon-theme

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsamplerate-devel
BuildRequires: vorbis-tools
BuildRequires: speex-tools
BuildRequires: gsl-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: liblrdf-devel
# BuildRequires: gamin-devel
BuildRequires: gettext-devel
BuildRequires: libXpm-devel
BuildRequires: libtimidity-devel
BuildRequires: timidity++
BuildRequires: flac
BuildRequires: flac-devel
BuildRequires: mpg123
BuildRequires: mpg123-devel
BuildRequires: gtk3-devel
BuildRequires: gtkglext-devel
BuildRequires: desktop-file-utils

Requires: mpg123
Requires: flac
Requires: timidity++

%description
Snd is a sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd. It can accomodate any
number of sounds each with any number of channels, and can be
customized and extended using s7 scheme. Snd is free (LGPL); the code
is available via anonymous ftp at ccrma-ftp.stanford.edu as
pub/Lisp/%{tarname}.tar.gz.

This package contains snd version %{pkgver}, dated %{snd_date}.

%package gtk
Summary: Gtk version of snd (%{pkgver}, %{snd_date})
Requires: snd == %{version}-%{release}

%description gtk
A version of the Snd editor (%{pkgver} of %{snd_date}) compiled with the gtk
gui.

%package utils
Summary: Sndplay and friends (Snd %{pkgver}, %{snd_date})
# always conflict with the (old) sndplay packages from cm/clm/cmn
Conflicts: sndplay-oss sndplay

%description utils
Command line utilities included with the snd sound editor (%{pkgver} of
%{snd_date}).

%package -n sndlib
Summary: Soundfile and audio handler collection

%description -n sndlib
The sound library is a collection of sound file and audio hardware
handlers written in C and running currently on SGI (either audio
library), Sun, OSS or ALSA (Linux and others), Mac, Mac OSX, HPUX,
LinuxPPC, and Windoze systems. It provides relatively straightforward
access to many sound file headers and data types, and most of the
features of the audio hardware.

%prep
%autosetup -p1 -n snd-%{pkgver}

# change all html href tags to point to the absolute location of
# the html documentation
for i in *.html ; do
    for j in *.html ; do
        %{__perl} -p -i -e "s|href=\"${i}|href=\"file://%{_datadir}/doc/snd-%{pkgver}/${i}|g" ${j}
    done
done

# but also change the directory where the html files are looked up
# by default
%{__perl} -p -i -e "s|/usr/share/doc/snd-10/snd.html|/usr/share/doc/snd-%{pkgver}/snd.html|g" index.scm

%build

# build Gtk version
%configure %{config_options} --with-gtk=yes
%make_build
mv snd snd-gtk
make clean
rm -f config.cache

# build snd utilities
%configure --with-no-gui %{config_options}
# removed sndsine for now
# audinfo is not happy (9/26/2005)
perl -p -i -e 's|LIBS = -ldl |LIBS = -lpthread -ldl |' makefile
%make_build sndplay sndinfo

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 snd.1 %{buildroot}%{_mandir}/man1
install -m 755 snd-gtk %{buildroot}%{_bindir}/snd-gtk
# removed sndsine for now
install -m 755 sndplay sndinfo %{buildroot}%{_bindir}

# scheme source code
mkdir -p %{buildroot}%{_libdir}/snd/scheme
(tar cf - *.scm)|(cd %{buildroot}/%{_libdir}/snd/scheme; %{__tar} xpf -)

# install icon to the proper freedesktop location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

# menu categories
BASE="Application AudioVideo Audio"
XTRA="X-Jack X-Editors"

%{__mkdir} -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{SOURCE2}

#--- a configuration file with the default scheme paths ready to go
mkdir -p %{buildroot}/etc
cat << EOF > %{buildroot}/etc/snd.conf
;; Default snd configuration file
;;
;; add paths to begin of default load path (last in the list is the
;; first in the search order)
(set! *load-path (cons "%{_libdir}/snd/scheme" *load-path))
EOF

# sndinfo conflicts with a utility in csound (from fedora extras), so
# rename it snd-info
mv %{buildroot}%{_bindir}/sndinfo %{buildroot}%{_bindir}/snd-info

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.Snd HISTORY.Snd *.html
%doc pix
%license COPYING
%{_datadir}/icons/hicolor/32x32/apps/snd.png
%{_datadir}/applications/*snd.desktop
%{_mandir}/man1/snd.1*
%{_libdir}/snd/scheme
%config(noreplace) /etc/snd.conf

%files gtk
%{_bindir}/snd-gtk

%files utils
%{_bindir}/sndplay
%{_bindir}/snd-info

%changelog
* Tue Aug 02 2022 Yann Collette <ycollette.nospam@free.fr> - 22.5-1
- update to 22.5-1

* Mon Apr 18 2022 Yann Collette <ycollette.nospam@free.fr> - 22.2-1
- update to 22.2

* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> - 21.2-1
- update to 21.2

* Fri May 1 2020 Yann Collette <ycollette.nospam@free.fr> - 20.3-1
- update to 20.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 17.8-1
- update for Fedora 29

* Fri Nov  3 2017 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 17.8-1
- update to 17.8 of 11/1/2017 for fc26 build

* Fri Jul  1 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 16.6-1
- update to 16.6 of 7/1/2016 for fc24 build

* Wed Nov 11 2015 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 16.0-1
- update to 16.0 of 11/11/2015

* Thu Dec 11 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 15.0-2
- update to 15.0 of 12/10/2014

* Mon Sep 29 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 15.0-1
- update to 15.0 of 09/27/2014

* Tue Dec 17 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 14.2-1
- update to 14.2 of 11/21/2013, build on fc20
- add patch to add -lpthread to linker call

* Mon Jul  1 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 13.8-1
- update to 13.8 of 7/1/2013

* Mon Mar 18 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 13.5-1
- update to snapshot of 03/18/2013, snd 13.5
- rework snd-help patch
- fix 64 bit lib dir in /etc/snd.conf

* Thu Jan  3 2013 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 13.3-1
- update to snapshot of 01/03/2013, snd 13.3
- added libXpm-devel build dependency

* Thu Sep  6 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 13.0-2
- updated to snapshot of 09/06/2012 (with some bugfixes for 64 bits)

* Fri Aug 31 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 13.0-1
- updated to 13.0, snapshot of 08/31/2012

* Wed Jun 27 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.12-1
- updated to latest snapshot of snd-12.12 (06/27/2012)

* Fri Jun  1 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.11-1
- updated to latest snapshot of snd-12.11 (05/01/2012)

* Thu Nov 17 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.6-2
- really updated to the latest snapshot (did not really do that yesterday)

* Wed Nov 16 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.6-1
- updated to 12.6 snapshot (11/16/2011)

* Tue Oct  4 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.5-1
- updated to 12.5 snapshot (04/10/2011)
- add -lpthread to the sndplay sndinfo build

* Wed Jun  1 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 12.2-1
- udpated to 12.2 snapshot (31/5/2011)
- removed --with-midi, change to gtk3-devel for fc15
- remove old Snd.ad file from %%doc

* Tue Jan 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 11.12-1
- updated t0 11.12's snapshot (1/18/2011)

* Fri Jul 09 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 11.7-1
- updated to 11.7's snapshot (7/9/2010)

* Thu May 20 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 11.5-1
- updated to 11.5's current snapshot (5/20/2010)

* Fri Jan 29 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated to today's snapshot, fixes problems with jack and alsa
  playback

* Wed Jan 27 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 11.2-1
- udpated to version 11.2 of 2010.01.27, removed sndrecord, no longer
  a make target
- change default options to not include with-gl when building for gtk,
  this is no longer compatible

* Mon Dec  1 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 10.2-1
- updated to version 10.2

* Thu Nov 27 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- use the proper load-path incantation in /etc/snd.conf

* Wed Nov 26 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 10.1-1
- updated to 10.1, uses s7 instead of guile
- rechecked all build dependencies from scratch

* Wed May  7 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 9.9-1
- updated to version 9.9

* Tue Nov 20 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 9.5-1
- udpated to version 9.5
- change all the href tags in the html documentation for absolute
  references pointing to the doc directory
- add patch that forces help files to be found in docdir (patch1)
- remove reference to dlp scheme directory, no longer exists

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated desktop categories

* Fri Jun 15 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 9.1-1
- build on fc6 with new motif (which is installed in /opt), add
  versioned motif requirement so the right one gets pulled in
  regardless

* Thu Jun  7 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 9.1-1
- updated to version 9.1 of 6/7/2007
- check to see if openmotif is installed in /opt
- removed hack to detect ALSA

* Sun Mar 19 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 8.8-1
- updated to 8.8, renamed sndinfo to snd-info to avoid a conflict
  with the binary of the same name in the csound package (fedora extras)

* Sun Nov 26 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 8.5-1
- updated to snd 8.5
- spec file tweaks, added hicolor-icon-theme runtime requirement,
  moved icon to proper location, added post/postun scripts

* Thu Sep  7 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 8.3-1
- updated to 9/7/2006 snapshot
- add proper build requirements for fc5 (desktop-file-utils, X,
  change fftw3 to fftw)
- removed build_for_ccrma flag
- added build requirements: vorbis-tools, speex-devel, flac-devel

* Mon Sep 26 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.15-1
- updated to current snapshot (7.15+)
- audinfo does not link, remove for now

* Sat Apr  2 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.11-1
- updated to 7.11
- detection of alsa not working, hacked config.h, added -lasound to
  link stage and patch to midi.c to be able to build oss and alsa
  support at the same time

* Sat Jan  7 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.9-1
- updated to 7.9 of 2005.01.07
- start of spec file cleanup, remove almost all build switches,
  nobody uses the customization anyway
- removed sndsine, will not build on fc3

* Fri Aug 26 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.6-1
- updated to version 7.6
- added the with-midi build option

* Tue Jul  6 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.5-1
- updated to version 7.5

* Wed May 19 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.4-1
- updated to version 7.4

* Fri Feb 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.2-1
- updated to version 7.2

* Mon Jan 12 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7.1-1
- updated to version 7.1

* Fri Dec 12 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 7-1
- updated to version 7

* Sun Nov  9 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.12-1
- spec file tweaks
- added defines to use old alsa api

* Mon Sep 29 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.12-1
- updated to 6.12 of 09/29/2003

* Sun Aug 17 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.11-1
- updated to 6.11 of 08/15/2003
- no longer use snd-guile packages (switched to guile 6.4 on all
  supported redhat releases, created a new build option to enable it,
  added Obsoletes tag for 7.3 and 8.0 so that snd-guile is erased by
  the apt dist-upgrade process.
- added release tags

* Thu May 29 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.9-1
- updated to 6.9 of 05/29/2003

* Tue May  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.8-1
- updated to 6.8 of 05/06/2003

* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.7-2
- rebuilt for newer version of fftw

* Sat Mar 22 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.7-1
- updated to 6.7
- changed prefix to use default macros
- do not use links to differentiate between motif and gtk version,
  motif version is now named "snd" and gtk version "snd-gtk"
- do not allow oss and alsa versions of the programs to coexist
- contrib directory for scheme and ruby code is now gone

* Tue Feb 18 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.6-1
- updated to 6.6

* Mon Jan 13 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.5-1
- updated to 6.5

* Sat Dec 14 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.4-1
- updated to 6.4 of 12/14/2002
- changed to proper application group

* Wed Nov 13 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.3-1
- updated to 6.3 of 11/13/2002
- added proper redhat 8.0 menu entry

* Wed Oct 16 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.2-1
- updated to 6.2 of 10/16/2002

* Tue Sep 17 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.1-1
- updated to 6.1 of 09/17/2002

* Mon Aug 26 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.0-2
- made dependency on openmotif explicit, otherwise snd appears to be
  happy with lesstif on redhat 7.2 but fails on startup because of an
  undefined symbol
- updated to snd 6.0 of 08/26/2002

* Wed Aug 14 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 6.0-1
- updated to snd 6.0 of 08/14/2002

* Sun Jul 14 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.12-3
- updated to snd of 07/14/2002

* Sat Jul  6 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.12-2
- another update, fixed postun installs as they were not working with
  rpm updates (they need to check the argument to the script)

* Tue Jul  2 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.12-1
- updated to latest snd

* Sun Jun 16 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.11-1
- naming of packages: snd -> base package; snd-motif, snd-gtk main
  executable, depending on driver either -oss or nothing added;
  -utils, depending on driver either -oss or nothing added

* Fri Jun 14 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- simplified spec file, get dependencies automatically
- no longer supports building alsa 0.5 rpms
- no longer supports building with static gsl libraries
- if building for motif always build with static xm library
- simplify snd-detect-flavor, we don't care about releases anymore
- statically linked motif packages are gone, we have openmotif now

* Mon Mar 25 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.8-1
- updated to 5.8 03/25/2002
- undo the guile change, after some thought I concluded it is not worth it,
  much better to depend on a separate snd-guile package, as before (save
  the current spec file as a keepsake :-)
- define a build_for_ccrma flag to create an rpm stub for ccrma internal
  use (does not contain any scheme code and has a configuration file that
  to the shared version of the snd source).

* Fri Jan 18 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.6-1
- updated to 5.6 01/18/2002

* Mon Dec  3 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.5-1
- updated to 5.5 12/03/2001
- incorporated guile 1.5.0 in the rpm (what used to be separate snd-guile
  package). Currently an ugly hack because configuring and compiling snd
  requires a functional guile, but guile is not installed yet if it is
  going to be part of snd snd rpms. So for now I do a temporary install
  of guile in the final location (by default /usr/lib/snd) while compiling
  snd. The install is removed at the end of the snd compilation process.
- install all scheme files in /usr/lib/snd/scheme, including the contrib
  dir
- create a default /etc/snd.conf that adds all scheme source directories
  to the default search path so that "load-from-path" can use just the
  file names.

* Wed Nov 28 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.4-2
- added menu entry for Mandrake 8.x [thanks to Kevin Cosgrove]
- update to snd-5.4 11/28/2001 (with support for new snd_config_get_id
  in alsa)

* Mon Nov 05 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.4-1
- snd 5.4 10/01/2001
- added contrib/ to documentation
- fixed wrong guile_gtk dependency

* Mon Oct  1 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.3-1
- snd 5.3 10/01/2001
- generate oss, alsa0.5 and alsa0.9 separate packages, simplifies spec file
- added environment control variables for build configuration through scripts

- added conflicts with sndplay-* packages (from the cm/clm/cmn rpms)

* Thu Sep 27 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.2-2
- snd-5.2 09/27/2001
- added man page to files

- removed snd requirement for the snd-utils-* packages
- added package date to description of packages
- added ladspa switch

* Wed Sep  5 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 5.2-1
- snd-5.2
- changed over to guile 1.5, will require snd-guile from now on
- start keeping old spec files for reference
- snd requires gsl >= 0.8, drop references to gsl 0.7
- added xm dependencies
- added menu entry for redhat rpms
- added snd icon

* Thu Jul 26 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- snd-5.1, alsa 0.9
- added autodetect of installed alsa version (%alsa_ver)
- added autodetect of linux flavor
- autobuild oss only or oss/alsa binary packages
- changed naming of packages and executables to reflect the fact that
  the statically linked alsa package also supports the oss api

* Thu Jul 12 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- first try at snd-5, snd-guile-1.6, alsa 0.9

* Wed Apr 02 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for rh7, snd-4.tar.gz, version 4.12, dated 4/2/2001

* Wed Mar 07 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for rh7, snd-4.tar.gz, version 4.11, dated 3/7/2001

* Tue Jan 23 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for rh7, suse7.0 and snd-4.tar.gz, version 4.10, dated 1/23/2001

* Wed Jan 17 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added support for redhat 7 and finished up support for SuSE 7

* Mon Jan 15 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- redid the dependencies stuff yet again
- updated to new snd-4.tar.gz of Jan 15 2001

* Sat Jan 13 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for snd-4.10 of Jan 13 2000, release set to 1
- patched snd-1.h, added ps_fd field to chan_info structure
- redid the dependencies for all packages. I'm now setting the
  dependencies manually and trying to be as general as possible
  so that the packages will run in as many distributions as possible.
  See the detailed explanation and %defines at the beginning of the
  spec file.
- deleted the %{usesndguile} option. I now always prefix the path to
  search for guile with /usr/lib/snd/bin/. The library will be found
  there at compile time but as the requirements are location independent
  it will be also looked for elsewhere at run time. Thus a distribution
  that comes with the latest guile will meet the requirement and the
  rpm will install. If snd-guile is not installed or the version of
  guile in the distribution is less than 1.4 the install will fail.
- added %{build_utils} to enable or not compilation of the command
  line utilities

* Mon Dec 11 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for snd-4.9 of Dec 11 2000, release set to 1
- added %{prefix}, removed ${RPM_BUILD_ROOT} prior to install, remove
  -o and -g from the install lines, thanks to Volker Kuhlmann for the tips
- use wildcards in doc file list, added Snd.ad
- added %{usesndguile} option for enabling the search for a private guile
  library

* Mon Nov 20 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for snd-4.8 of Nov 20 2000, release set to 1
- fixed dependencies, utils packages do not depend on guile-gtk,
  only gtk-* do (thanks to Volker Kuhlmann <kuhlmav@elec.canterbury.ac.nz>)

* Mon Oct 16 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for snd-4.7, release set to 1

* Thu Sep 28 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- compiled for snd-4.6 of Sep 28 2000, release set to 1

* Fri Aug 25 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added statically linked versions of the motif gui packages
- compiled using snd-4.tar.gz Aug 25 2000

* Mon Aug 21 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- changed postun to only erase link to binaries if the package being
  installed is the one that set up the link in the first place
- added alsa version number to naming of packages, that will enable
  us to have packages for alsa 0.5.x and 0.6.x in the same directory

* Wed Aug 16 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- no need to hack configure.in, a simple PATH added to the ./configure
  stage makes sure that the proper guile binary is found...

* Tue Aug 15 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- created subpackages snd-motif-oss snd-motif-alsa snd-gtk-oss
  snd-gtk-alsa snd-utils-oss snd-utils-alsa
- changed configure.in in snd-4.5 to search for guile first in
  /usr/lib/snd/, added -rpath to the linker invocation so that
  it is not necessary to add /usr/lib/snd/lib to /etc/ld.so.conf
- TODO: create a snd-devel package with the include files and sndlib?

* Mon Aug 14 2000 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added a root install directory so that compiling the package
  does not clobber the real filesystem
- changed prefix to represent everything up to bin|lib|whatever
  (so that prefix=/usr installs in /usr/bin, follow redhat convention)
- changed version numbering, 4.5 refers to the version of the program,
  the release number is the rpm package release number, the .tar.gz
  file should be named snd-4.5.tar.gz...

