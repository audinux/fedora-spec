%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: slv2
Summary: LV2 host library
Version: 0.6.6
Release: 35%{?dist}
License: GPLv2+
URL: http://drobilla.net/software/slv2/

Source0: http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Remove dates from html doc files RHBZ#566345
Patch0: %{name}-no-date-on-docs.patch

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: lv2-devel
BuildRequires: python2
BuildRequires: redland-devel
BuildRequires: jack-audio-connection-kit-devel

# To provide a clean upgrade path from PlanetCCRMA:
Obsoletes: %{name}-examples < 0.6
Provides: %{name}-examples = %{version}-%{release}

%description
SLV2 is a library to make the use of LV2 plugins as simple as possible for 
applications. It is written in standard C using the Redland RDF toolkit. The 
Data (RDF) and code (shared library) functionality in SLV2 is strictly
separated so it is simple to control where each is used (e.g. it is possible
to discover/investigate plugins and related data without loading any shared 
libraries, avoiding the associated risks).

%package devel
Summary: Development libraries and headers for %{name}
Requires: lv2-devel 
Requires: redland-devel
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
SLV2 is a library to make the use of LV2 plugins as simple as possible for
applications. It is written in standard C using the Redland RDF toolkit. The
Data (RDF) and code (shared library) functionality in SLV2 is strictly
separated so it is simple to control where each is used (e.g. it is possible
to discover/investigate plugins and related data without loading any shared
libraries, avoiding the associated risks).

This package contains the headers and development libraries for SLV2.

%prep
%autosetup -p1 

# Fix possible multilib issues
sed -i 's|/lib/|/%{_lib}/|g' src/world.c
sed -i "s|/lib'|/%{_lib}'|" autowaf.py

# Remove unnecessary flags
sed -i 's|@REDLAND.*@||' slv2.pc.in
# Fix CFLAGS issue in slv2->redland->rasqal dependency chain
echo "Requires.private: redland" >> slv2.pc.in

# Fix Python shebangs
sed -i 's|/usr/bin/.*python$|/usr/bin/python2|' autowaf.py swig/python/*.py wscript */wscript waf

# Quick hack. lv2core seemingly permanently renamed to lv2 at version 1.16
sed -i 's|lv2core|lv2|g' wscript

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LINKFLAGS="$RPM_LD_FLAGS"
./waf configure --prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--htmldir=%{_pkgdocdir} \
	--build-docs
./waf build -v %{?_smp_mflags}

# Workaround the doxygen bug
rm -f build/default/doc/man/man3/_*

%install
DESTDIR=%{buildroot} ./waf install
chmod +x %{buildroot}%{_libdir}/lib%{name}.so*
install -pm 644 AUTHORS ChangeLog COPYING README %{buildroot}%{_pkgdocdir}


%files
%license %{_pkgdocdir}/COPYING
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/README
%{_bindir}/lv2*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/*

%files devel
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/AUTHORS
%exclude %{_pkgdocdir}/ChangeLog
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/README
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_mandir}/man3/%{name}*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.6-29
- lv2core -> lv2 in wscript

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.6-26
- Fixed Python shebangs
- Added BR: gcc
- Use Fedora link flags

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.6-24
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Karsten Hopp <karsten@redhat.com> 0.6.6-17
- bump and rebuild to fix dependency issues on ppc64le

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.6-14
- Install docs to %%{_pkgdocdir} where available (#994098).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.6-11
- Workaround the doxygen bug by removing the spurious manpage file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.6.6-9
- Rebuilt against new LV2 package

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 01 2010 Dan Horák <dan[at]danny.cz> - 0.6.6-6
- Fix CFLAGS issue in slv2->redland->rasqal dependency chain

* Fri Feb 19 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.6-5
- Remove dates from html doc files RHBZ#566345

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.6-4
- rebuild (redland)

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.6.6-3
- rebuild (rasqal/redland)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.6-1
- Version update: 0.6.6
- Add Obsoletes/Provides to slv2-examples

* Tue May 05 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.4-1
- Version update: 0.6.4
- Drop plugininstance patch (upstreamed)

* Wed Apr 08 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-3
- Change CCFLAGS to CFLAGS

* Sat Mar 28 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-2
- Remove redland flags from the .pc file
- Change CPPFLAGS to CXXFLAGS
- Move API documentation to the -devel package

* Thu Mar 26 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-1
- Initial build
