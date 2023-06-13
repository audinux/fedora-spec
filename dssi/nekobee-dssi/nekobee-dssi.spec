Summary:       Acid sounds synthesizer
Name:          nekobee-dssi
Version:       0.1.7
Release:       24%{?dist}
License:       GPL-2.0-or-later
URL:           http://www.nekosynth.co.uk/wiki/nekobee
Source0:       http://www.nekosynth.co.uk/releases/nekobee-%{version}.tar.gz
Source1:       nekobee.desktop
# Derived from extra/knob.png
Source2:       nekobee.png
Patch0:        nekobee-gcc10.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
BuildRequires: gcc
BuildRequires: gtk2-devel
BuildRequires: liblo-devel

Requires:      dssi

%description
Since it was first released in 2004, the Disposable Soft Synth Interface has
allowed Linux audio users to have simple plugin software synthesizers. Over
time, the number of these has grown as users and coders have developed new
plugins for particular sounds. Now, nekosynth brings some new plugins to enrich
your sonic palette.

This package provides the nekobee DSSI plugin, which is suitable for recreating
those squelchy acid sounds.

%prep
%setup -q -n nekobee-%{version}
%patch0 -p1 -b .gcc10

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="install -p"

# Make a symlink for easy access
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -s jack-dssi-host $RPM_BUILD_ROOT%{_bindir}/nekobee

# Kill .la file
rm $RPM_BUILD_ROOT%{_libdir}/dssi/nekobee.la

# Kill zero-length file
rm $RPM_BUILD_ROOT%{_libdir}/dssi/nekobee/switch.png

# Desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                              \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  %{SOURCE1}

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/nekobee.png

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/nekobee
%{_libdir}/dssi/nekobee/
%{_libdir}/dssi/nekobee.so
%{_datadir}/applications/nekobee.desktop
%{_datadir}/icons/hicolor/48x48/apps/nekobee.png

%changelog
* Sat Feb 08 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1.7-24
- gcc 10 fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.7-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1.7-4
- Rebuild against new liblo-0.26

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1.7-2
- Add icon cache scriptlet

* Sat May 30 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1.7-1
- Initial build
