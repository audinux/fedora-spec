# Tag: Equalizer
# Type: Plugin, LV2
# Category: Audio, Effect

%global pkgname lv2fil

Summary: Four-band parametric equalizers
Name: lv2-fil-plugins
Version: 2.0
Release: 13%{?dist}
# lv2_ui.h is LGPLv2+
# log.*, lv2filter.*, lv2plugin.c are GPLv2
# The rest is GPLv2+
# The author claims GPLv2 for the software
License: LGPLv2+ and GPLv2 and GPLv2+
URL: http://nedko.arnaudov.name/soft/lv2fil/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source: https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/lv2fil/2.0+20100312.git18130f5a+dfsg0-2/lv2fil_2.0+20100312.git18130f5a+dfsg0.orig.tar.gz#/lv2fil-2.0.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python2
BuildRequires: liblo-devel
BuildRequires: lv2-devel

Requires: lv2
Requires: pycairo
Requires: pygtk2
Requires: python3-pyliblo

%description
Stereo and mono LV2 plugins, four-band parametric equalizers.
Each section has an active/bypass switch, frequency, bandwidth and
gain controls. There is also a global bypass switch and gain control.

The 2nd order resonant filters are implemented using a Mitra-Regalia
style lattice filter, which has the nice property of being stable
even while parameters are being changed.

All switches and controls are internally smoothed, so they can be
used 'live' without any clicks or zipper noises. This should make
this plugin a good candidate for use in systems that allow automation
of plugin control ports, such as Ardour, or for stage use.

The GUI provides knobs and toggle buttons for tweaking filter
parameters. It also provides frequency response widget with
differently colored curve for each section and separate curve for
total equalization effect.

%prep
%autosetup -n lv2fil-2.0+20100312.git18130f5a+dfsg0

sed -i -e "s/lv2core/lv2/g" wscript

# Force python2 usage
sed -i -e "s/env python/env python2/g" waf
sed -i -e "s/env python/env python2/g" wscript
sed -i -e "s/env python/env python2/g" lv2plugin.py
sed -i -e "s/env python/env python2/g" ui
sed -i -e "s/\"python\"/\"python2\"/g" lv2_ui.c

%build
%set_build_flags
export LINKFLAGS="-lm"
./waf configure --lv2-dir=%{_libdir}/lv2
./waf %{?_smp_mflags} -v

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot} -v
# Fix weird permissions on installed files
chmod 755 %{buildroot}%{_libdir}/lv2/filter.lv2/filter.so
chmod 755 %{buildroot}%{_libdir}/lv2/filter.lv2/ui

%files
%doc AUTHORS README NEWS
%license COPYING
%{_libdir}/lv2/filter.lv2/

%changelog
* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 2.0-13
- fix for Fedora 31

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0-13
- update for Fedora 29

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Brendna Jones <brendan.s.jones@gmail.com> - 2.0-6
- Rebuilt against new lv2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0-3
- More language fixes

* Fri Dec 11 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0-2
- Obey American English rules (equaliser -> equalizer)
- Fix license. Add comments.

* Fri Nov 13 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0-1
- initial build
