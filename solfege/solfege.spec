# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global  py_byte_compile 1
%global debug_package %{nil}

Name:    solfege
Version: 3.23.4
Release: 11%{?dist}
Summary: Music education software

License: GPLv3
URL:     https://www.gnu.org/software/solfege/
Source0: https://alpha.gnu.org/gnu/solfege/solfege-%{version}.tar.gz
# Fix startup issue on F17+ (BZ 832764):
# Correctly determine the PREFIX even if solfege is executed as /bin/solfege
Patch0: solfege-3.20.6-prefix.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: texinfo
BuildRequires: swig
BuildRequires: gettext
BuildRequires: docbook-style-xsl
BuildRequires: pygtk2-devel >= 2.12
BuildRequires: python3-gobject-base
BuildRequires: libxslt
BuildRequires: txt2man
BuildRequires: desktop-file-utils

Requires: timidity++
Requires: pygtk2 >= 2.12
Requires: python3
Requires: bash

%description
Solfege is free music education software. Use it to train your rhythm,
interval, scale and chord skills. Solfege - Smarten your ears!

%prep
%setup -q
%patch0 -F 2 -p1 -b .prefix

%build

export INSTALL="%{__install} -c -p"
#override hardocded path
%configure --enable-docbook-stylesheet=`ls %{_datadir}/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl` --disable-oss-sound
%make_build

%install

%make_install

#permissions
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/solfege/solfege/_version.py

#Change encoding to UTF-8
for f in AUTHORS README ; do
	iconv -f ISO-8859-15 -t UTF-8 $f > ${f}.tmp && \
		mv -f ${f}.tmp ${f} || \
		rm -f ${f}.tmp
done

sed -i -e "s/usr\/bin\/python/usr\/bin\/python3/g" %buildroot/%{_bindir}/solfege

%find_lang %{name}

desktop-file-install --delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-category Application \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README AUTHORS COPYING
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/solfege/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man?/*

%changelog
* Wed Nov 02 2022 Yann Collette <ycollette.nospam@free.fr> - 3.23.4-11
- update to 3.23.4-11

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 09 2013 Christian Krause <chkr@fedoraproject.org> - 3.22.2-1
- Update to new upstream release (BZ 1016286)

* Mon Sep 16 2013 Christian Krause <chkr@fedoraproject.org> - 3.22.1-1
- Update to new upstream release (BZ 1008434)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Christian Krause <chkr@fedoraproject.org> - 3.22.0-1
- Update to new major upstream release (BZ 895045)
- Remove upstreamed patch
- Remove conditional --vendor since new release will be built for F19+ only

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.20.7-3
- Remove --vendor from desktop-file-install. https://fedorahosted.org/fesco/ticket/1077
- Patch to fix up the FAQ texi file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Christian Krause <chkr@fedoraproject.org> - 3.20.7-1
- Update to new upstream release (BZ 880539)

* Sun Sep 02 2012 Christian Krause <chkr@fedoraproject.org> - 3.20.6-2
- Add patch to fix startup issue on F17+ (BZ 832764)

* Sat Jul 21 2012 Christian Krause <chkr@fedoraproject.org> - 3.20.6-1
- Update to new upstream release (BZ 834200)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.3-1
- Update to new upstream release (BZ 748133)

* Tue Oct 11 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.3-1
- Update to new upstream release (BZ 741233)

* Mon Sep 12 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.2-1
- Update to new upstream release (BZ 737498)

* Sat Sep 10 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.1-2
- Remove superfluous Requires: gnome-python2-gtkhtml2

* Sun Jul 24 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.1-1
- Update to new upstream release (BZ 720301)

* Sat Jun 18 2011 Christian Krause <chkr@fedoraproject.org> - 3.20.0-1
- Update to new upstream release (BZ 713414)
- Remove upstreamed patches
- Minor spec file cleanup

* Mon May 30 2011 Christian Krause <chkr@fedoraproject.org> - 3.18.8-1
- Update to new upstream release (BZ 707534)
- Minor spec file cleanup

* Sun Mar 06 2011 Christian Krause <chkr@fedoraproject.org> - 3.18.7-3
- Remove superfluous dependency to esound (BZ 678361)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Christian Krause <chkr@plauener.de> - 3.18.7-1
- Update to new upstream release (BZ 648180)

* Wed Oct 27 2010 Christian Krause <chkr@fedoraproject.org> - 3.18.6-1
- Update to new upstream release (BZ 643606)
- Remove upstreamed patch

* Sun Oct 10 2010 Christian Krause <chkr@fedoraproject.org> - 3.18.3-1
- Update to new upstream release (BZ 636475)
- Update patch to fix the build problem with swig 2.0

* Sat Jul 24 2010 Christian Krause <chkr@fedoraproject.org> - 3.16.4-1
- Update to new upstream release (BZ 617836)
- Add patch to fix a build problem

* Wed May 19 2010 Christian Krause <chkr@fedoraproject.org> - 3.16.3-1
- Update to new upstream release

* Sun Apr 18 2010 Christian Krause <chkr@fedoraproject.org> - 3.16.1-1
- Update to new upstream release

* Fri Apr 02 2010 Christian Krause <chkr@fedoraproject.org> - 3.16.0-1
- Update to new upstream release
- Remove patch to fix python's search path, solfege uses absolute
  imports now

* Sun Mar 07 2010 Christian Krause <chkr@fedoraproject.org> - 3.14.11-1
- Update to new upstream release
- Remove upstreamed patch
- Use timitidy as default
- Add patch to remove /usr/bin from python's search path to avoid crash
  on startup if package mpich2 is installed

* Sun Feb 07 2010 Christian Krause <chkr@fedoraproject.org> - 3.14.10-1
- Update to new upstream release
- Some spec file cleanup
- Add minor patch to fix a problem with the default config (programs and
  their parameters are now stored in separate config entries)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.14.2-1
- New upstream release
- No-X patch merged upstream, remove it.

* Sat Apr 11 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.14.1-2
- Don't depend on lilypond

* Wed Apr 7 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.14.1-2
- Update launcher script to use esdcompat and not esd

* Wed Apr 7 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.14.1-1
- New upstream release
- Add patch to not require X to build
- Add patch to fix desktop file, don't use extensions without path in Icon=
- Add lilypond dependency
- Make sure permissions in debuginfo are sane

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.10.4-2
- Rebuild for Python 2.6

* Tue Mar 18 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.10.4-1
- New bugfix release

* Tue Mar 18 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.10.3-1
- New release

* Sun Mar 16 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.10.2-5
- Clean up docbook path override

* Sun Mar 16 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 3.10.2-1
- New major release
- Update license to GPLv3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.8.0-2
- Autorebuild for GCC 4.3

* Mon Jun 04 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.8.0-1
- New major release
* Sun Mar 11 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.5-1
- Update to 3.6.5
* Sun Dec 31 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-8
- Rebuild for new pygtk2-devel

* Wed Dec 20 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-6
- Fix charset conversion
- Remove Application category from desktop file
- Fix changelog

* Tue Dec 19 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-5
- Move original binary to %%{_libexecdir}
- Remove X-Fedora Category from meny entry
- Add pygtk2 Requires
- Replace libxlst-devel BuildRequires with libxlst
- Keep timestamps for image files 
- Convert AUTHORS and README from iso8859 to UTF-8 

* Fri Dec 15 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-4
- Fix permissions issue in wrapper script
- Fix debuginfo package
- Fix indentation

* Fri Dec 15 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-3
- Change permissions

* Thu Dec 14 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-2
- Use install to install wrapper script
- Improvements to wrapper script

* Thu Dec 14 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.6.4-1
- Initial build
