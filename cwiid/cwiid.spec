# Tag: Library
# Type: Devel
# Category: Tool, Programming

# The git_commit define will have the complement given by git-hub to the source downloaded
%define git_commit8 fadf11
%define git_commit fadf11e89b579bcc0336a0692ac15c93785f3f82

Name: cwiid
Version: 0.6.00
Release: 36.20100505git%{git_commit8}%{?dist}
Summary: Wiimote interface library
License: GPL-2.0-or-later
URL: https://github.com/abstrakraft/cwiid
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Source0: https://github.com/abstrakraft/cwiid/archive/%{git_commit}.zip#/%{name}-%{version}.zip
Source1: wmgui.desktop

# this patch is in my git-hub fork git://github.com/bogado/cwiid.git
# there is an upstream bug filed by me at http://abstrakraft.org/cwiid/ticket/105
Patch0: 0001-Fix-missing-library-from-wmdemo.patch

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gawk
BuildRequires: bison
BuildRequires: flex
BuildRequires: gtk2-devel
BuildRequires: python2-devel
BuildRequires: bluez-libs-devel
BuildRequires: desktop-file-utils

%description
Cwiid is a library that enables your application to communicate with
a wiimote using a bluetooth connection.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}, bluez-libs-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package python2
Summary: Python binding for %{name}
Requires: %{name} = %{version}-%{release}

%description python2
Python2 binding for %{name}

%package utils
Summary: Wiimote connection test application
Requires: %{name} = %{version}-%{release}
Provides: %{name}-wmgui = %{version}-%{release}
Obsoletes: %{name}-wmgui < 0.6.00-7

%description utils
Applications to test the wiimote connection

%package wminput
Summary: Enables using the wiimote as an input source
# The licence must be GPLv2 instead of GPLv2+ for this package
# since the file wminput/action_enum.txt is GPLv2 as stated
# in the file.
License: GPL-2.0-only
Requires: %{name} = %{version}-%{release}, %{name}-python2

%description wminput
This program allows the user to use the wiimote to emulate normal system
input sources like the mouse and keyboard.

%prep
%autosetup -p1 -n cwiid-%{git_commit}

sed -i -e "s/CFLAGS =/CFLAGS=-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fexceptions -fstack-protector-strong -grecord-gcc-switches -specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1 -specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1 -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -I\/usr\/include\/python2.7 -I. /" defs.mak.in
sed -i -e "s/WARNFLAGS = -Wall -W/WARNFLAGS = -Wall -W -fPIC -Wno-incompatible-pointer-types/g" defs.mak.in

%ifarch aarch64
sed -i -e "s/-m64//g" defs.mak.in
sed -i -e "s/-fcf-protection//g" defs.mak.in
%endif

%build

aclocal
autoconf

%configure --disable-static --docdir="%{_pkgdocdir}" --with-python=python2
%make_build

%install
%make_install LDCONFIG=/bin/true
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# find all directories
find $RPM_BUILD_ROOT%{_sysconfdir} -type f -exec chmod 0644 {} ';'
rm $RPM_BUILD_ROOT/%{_libdir}/*.a
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README COPYING ChangeLog
%exclude %{_pkgdocdir}/Xmodmap
%exclude %{_pkgdocdir}/wminput.list
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files python2
%{python2_sitearch}/*

%files wminput
# Fold-in wminput docs into main-package
%{_pkgdocdir}/Xmodmap
%{_pkgdocdir}/wminput.list
%config(noreplace) %{_sysconfdir}/cwiid/
%{_bindir}/wminput
%{_mandir}/man1/wminput*
%{_libdir}/cwiid

%files utils
%{_bindir}/lswm
%{_bindir}/wmgui
%{_mandir}/man1/wmgui*
%{_datadir}/applications/wmgui.desktop

%changelog
* Tue Nov 5 2019 Yann Collette <ycollette.nospam@free.fr> 0.6.00-36.20100505gitfadf11e
- update for Fedora 31

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-36.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.00-35.20100505gitfadf11e
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-34.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.00-33.20100505gitfadf11e
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-32.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-31.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-30.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-29.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-28.20100505gitfadf11e
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.00-27.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-26.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-25.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-24.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.6.00-23.20100505gitfadf11e
- Add BR: autoconf, automake (FTBFS, RHBZ #992105).
- Reflect docdir changes.
- Fix bogus %%changelog date.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-22.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.00-21.20100505gitfadf11e
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-20.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-19.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-18.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.00-17.20100505gitfadf11e
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-16.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.00-15.20100505gitfadf11e
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu May 06 2010 Victor Bogado <victor@bogado.net> 0.6.00-14.20100505gitfadf11e
- updated to latest git version, that adds suport for the wii balance board and the wii motion plus
- Fixed DSO linking issues

* Wed Jan 27 2010 Victor Bogado <victor@bogado.net> 0.6.00-13
- atempt to fix bug #555449

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.00-10
- Rebuild for Python 2.6

* Thu Sep 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.6.00-9
- F-10: rebuild against new bluez
- Fix for bluez api change

* Thu May  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.6.00-7
- Rename -wmgui to -tools and repackage.

* Fri Apr 25 2008 Victor Bogado <victor@bogado.net> 0.6.00-6
- Fix mode for configuration files.

* Thu Apr 24 2008 Victor Bogado <victor@bogado.net> 0.6.00-5
- comment explaining why a subpackage has a different license.
- BuildRequires needed one more program.

* Mon Apr 21 2008 Victor Bogado <victor@bogado.net> 0.6.00-4
- Source URL has version on it.

* Sun Apr 20 2008 Victor Bogado <victor@bogado.net>
- Removing files that are included twice.

* Sat Apr 19 2008 Victor Bogado <victor@bogado.net> 0.6.00-3
- solved directory ownership problems
- Changed license of wminput to GPLv2
- AUTHORS and NEWS bundled as docs.
- Added desktop file
- Removed static library files
- Made the spec honor compiler flags.
- Added bluez-libs-devel to requires of the devel package
- Removed python from BuildRequires list
- Added bluez-libs-devel to requires of development package

* Wed Apr 09 2008 Victor Bogado <victor@bogado.net> 0.6.00-2
- added changelog.
- doc section of files.
- changed the line that specifies the python library to accomodate the file *.info that is generates with other versions of python.
- cutted long description lines
- fixed documentations tags

* Sat Apr 05 2008 Victor Bogado <victor@bogado.net>
- First verion

