# Tag: Sf2, Editor
# Type: Standalone
# Category: Audio, Tool

Name: swami
Version: 2.2.2
Release: 24%{?dist}
Summary: MIDI instrument and sound editor
License: GPL-2.0-only
URL: http://www.swamiproject.org/
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/swami/swami/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: fftw-devel
BuildRequires: fluidsynth-devel
BuildRequires: libglade2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libinstpatch-devel
BuildRequires: librsvg2-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
The Swami Project - Sampled Waveforms And Musical Instruments - is a collection
of free software for editing and sharing MIDI instruments and sounds. Swami
aims to provide an instrument editing and sharing software for instrument
formats such as SoundFont, DLS and GigaSampler.

%package libs
Summary: MIDI instrument and sound editor library

%description libs
Shared libraries for The Swami Project - Sampled Waveforms And Musical
Instruments.

%package devel
Summary: MIDI instrument and sound editor development files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for The Swami Project - Sampled Waveforms And
Musical Instruments.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DLIB_SUFFIX="" -DPLUGINS_DIR=%{_lib}/swami/
%cmake_build

%install

%cmake_install

desktop-file-install                                    \
    --add-category="AudioVideo"                         \
    --add-category="X-Jack"                             \
    --remove-category="Application"                     \
    --remove-key="Encoding"                             \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog NEWS README.md HACKERS
%license COPYING
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files libs
%{_libdir}/lib%{name}*.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}/

%changelog
* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 2.2.2-24
- update to 2.2.2-24

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-24.20110806svn386
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-23.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.0.0-22.20110806svn386
- Rebuild against fluidsynth2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.0.0-18.20110806svn386
- Patch for invalid pointer cast on 64bit systems
- Remove old scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-15.20110806svn386
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.0-9.20110806svn386
- update icon/mime scriptlets, use %%name macro in subpkg deps

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.0-2.20110806svn386
- Rebuild for new libpng

* Fri Aug 12 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.0.0-1.20110806svn386
- Update to swami2. Fixes RHBZ#728694

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-6
- Update .desktop file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-4
- Add Requires: hicolor-icon-theme

* Fri Mar 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-3
- Initial Fedora build

* Sun Jul 27 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.4-2
- updated for new fluidsynth libraries (1.0.8) on fc8

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- updated desktop categories
- add popt-devel build requirement for f8

* Fri Sep 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.4-1
- updated to 0.9.4

* Tue May  8 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.3-2
- build on fc7, use autogen.sh to use the newer versions of auto* tools
- add MKINSTALLDIRS explicitly in make invocation

* Mon Apr 16 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.3-2
- spec file tweaks, build on fc6

* Mon May 29 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.3-1
- added Planet CCRMA categories to desktop file, spec file cleanups
- updated to 0.9.3

* Fri Nov 18 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-3
- rebuild for new version of fluidsynth (1.0.6)
- build requires lash (name change from ladcca)
- change all references from ladcca to lash
- added autotools build requirement (for change to lash), needs
  automake17

* Fri Dec 31 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Fri Sep 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-2
- built for new fluidsynth libraries
- set libfluidsynth require to be for the exact version, swami is
  very picky and won't work with newer versions than the one it was
  compiled with

* Thu May 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added code to recognize libpng12.pc in configure

* Wed May 12 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added buildrequires

* Sun Feb 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-1
- updated to 0.9.2
- patched config.status to force recognition of libpng
- erased and obsoleted old libswami and libswami-devel packages

* Mon Nov 17 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.1a-3
- spec file tweaks, autogen ommited, does not work on FC1

* Fri Jul 25 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.1-3
- rebuilt for fluidsynth 1.0.3
- added release tags and an explicit dependency with the current
  version of libfluidsynth

* Fri Jul 25 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.1-2
- rebuilt for fluidsynth 1.0.2

* Thu May  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.1-1
- updated to 0.9.1a

* Thu Mar  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-1.cvs
- cvs: 20030306.185320

* Thu Feb 27 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-1.cvs
- adapted from mandrake spec file
- switched over to cvs swami

* Fri Jan 31 2003 Austin Acton <aacton@yorku.ca> 0.9.0-1mdk
- adapted spec file from Torbjorn Turpeinen <tobbe@nyvalls.se>
