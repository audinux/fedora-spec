# Tag: Synthesizer
# Type: Plugin, DSSI
# Category: Audio, Synthesizer, Plugin

Summary: DSSI implementation of Fluidsynth
Name: fluidsynth-dssi
Version: 1.0.0
Release: 24%{?dist}
License: GPL-2.0-or-later
URL: http://dssi.sourceforge.net/download.html#FluidSynth-DSSI
ExclusiveArch: x86_64 aarch64

Source0:    http://download.sf.net/dssi/fluidsynth-dssi-%{version}.tar.gz
# Add Fedora's default soundfont path to the scanlist:
Patch0:     fluidsynth-dssi-sf2path.patch
# Fluidsynth 1 and 2 support
Patch1:     fluidsynth-dssi-fluidsynth1and2.patch

Requires: dssi

BuildRequires: gcc
BuildRequires: dssi-devel
BuildRequires: fluidsynth-devel
BuildRequires: gtk2-devel
BuildRequires: liblo-devel
BuildRequires: make

%description
This is an implementation of the FluidSynth soundfont-playing software
synthesizer as a DSSI plugin. It makes use of DSSI's run_multiple_synths()
interface to allow sharing of resources between multiple plugin instances --
soundfont data is shared between instances, and FluidSynth's usual voice
allocation methods are applied across multiple instances as if each were a
FluidSynth channel.

%prep
%setup -q
%patch0 -p1 -b .sf2path
%patch1 -p1 -b .fl1and2

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm $RPM_BUILD_ROOT%{_libdir}/dssi/fluidsynth-dssi.la

%files
%doc ChangeLog README TODO
%license COPYING
%{_libdir}/dssi/fluidsynth-dssi*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.0.0-22
- Rebuild against fluidsynth2
- Some SPEC cleanup

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.0.0-3
- Rebuild against new liblo-0.26

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.0.0-1
- Update to 1.0.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.1-9
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-8
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.1-7
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.9.1-6
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 0.9.1-5.1
- Rebuild.

* Sat Sep 16 2006 Anthony Green <green@redhat.com> 0.9.1-5
- Cleaned up BuildRequires.

* Sat Sep 16 2006 Anthony Green <green@redhat.com> 0.9.1-4
- Don't create fluidsynth-dssi symlink.
- Don't install .desktop file.
- Don't use %%makeinstall.
- Install COPYING.
- Fix License.
- Clean up Requires.
- Don't install libtool .la file.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 0.9.1-3
- Tweak fluidsynth-dssi symlink creation.
- Add parallel build flags to make.
- Fix BuildRequires.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.1-2
- Build for Fedora Extras.

* Fri May  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.1-1
- first build of fluidsynth-dssi as a separate package
