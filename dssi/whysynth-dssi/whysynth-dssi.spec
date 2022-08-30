Summary:      DSSI software synthesizer plugin
Name:         whysynth-dssi
Version:      20120903
Release:      12%{?dist}
URL:          http://www.smbolton.com/whysynth.html
Source0:      http://www.smbolton.com/whysynth/whysynth-%{version}.tar.bz2
Source2:      whysynth.desktop
Patch0:       whysynth-noinline.patch
License:      GPLv2+

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
BuildRequires: gtk2-devel
BuildRequires: fftw-devel
BuildRequires: gcc
BuildRequires: liblo-devel

Requires:     dssi
Requires:     hicolor-icon-theme



%description
WhySynth is a versatile softsynth which operates as a plugin for the Disposable
Soft Synth Interface (DSSI).

%prep
%setup -q -n whysynth-%{version}
%patch0 -p1 -b .noinline

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_bindir}
pushd $RPM_BUILD_ROOT%{_bindir}
ln -s jack-dssi-host whysynth
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install           \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -pm 644 extra/whysynth-icon-32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/whysynth.png

%files
%doc AUTHORS ChangeLog COPYING doc README TODO extra/COPYING-patches
%{_datadir}/whysynth
%{_bindir}/whysynth
%{_libdir}/dssi/*
%{_datadir}/applications/whysynth.desktop
%{_datadir}/icons/hicolor/32x32/apps/whysynth.png

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20120903-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20120903-1
- Update to 20120903
- Fix undefined symbols RHBZ#1305660

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120729-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120729-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120729-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120729-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120729-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 20120729-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Sat Aug 25 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20120729-1
- Update to 20120729

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100922-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100922-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 20100922-4
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100922-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 20100922-2
- Rebuilt for gcc bug 634757

* Sun Sep 26 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20100922-1
- Update to 20100922

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20090608-2
- Rebuild against new liblo-0.26

* Sun Nov 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20090608-1
- Update to 20090608

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090403-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 20090403-1
- Update to 20090403

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080412-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 20080412-2
- fix license tag

* Mon Jul 07 2008 Anthony Green <green@redhat.com> 20080412-1
- Upgrade sources.  Add COPYING-patches.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20070418-2
- Autorebuild for GCC 4.3

* Thu Apr 19 2007 Anthony Green <green@redhat.com> 20070418-1
- Upgrade sources.

* Tue Mar 27 2007 Anthony Green <green@redhat.com> 20060122-9
- Move icon.

* Mon Mar 26 2007 Anthony Green <green@redhat.com> 20060122-8
- Tweak .desktop categories.
- Remove extra icons.

* Sat Oct 21 2006 Anthony Green <green@redhat.com> 20060122-7
- Remove useless desktop-file-install --add-category options.
- Remove Requires for post and postun.

* Sat Sep 16 2006 Anthony Green <green@redhat.com> 20060122-6
- Don't create and install resized icons.
- Don't BuildRequire ImageMagik.
- Require hicolor-icon-theme since we're installing in its directory.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 20060122-5
- Add .desktop file and icons.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 20060122-4
- Clean up changlog.
- Fix %%defattr in %%files section.
- Don't use %%makeinstall.
- Fix symlink to be relative.

* Thu Jun  1 2006 Anthony Green <green@redhat.com> 20060122-3
- Removed extra changelog line.

* Thu May 18 2006 Anthony Green <green@redhat.com> 20060122-2
- Clean up Requires & BuildRequires.
- Don't use %%{__rm} & %%{__make}.
- Use %%makeinstall.
- Add whysynth symlink.

* Tue Apr 25 2006 Anthony Green <green@redhat.com> 20060122-1
- Created.
