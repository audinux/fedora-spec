# Tag: Audio, Effect
# Type: Plugin, LV2
# Category: Audio, Effect

# Global variables for github repository
%global commit0 46af4c950c6fb935145e16be09808f393da69ca3
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: lv2-avw-plugins
Version: 0.0.8
Release: 19%{?dist}
Summary: A port of the AMS internal modules to LV2 plugins
License: GPL-2.0-only
URL: https://github.com/harryhaaren/avw.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/harryhaaren/avw.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lvtk
BuildRequires: python2
BuildRequires: lv2-devel
BuildRequires: lv2-c++-tools-devel >= 1.0.4
BuildRequires: gtk2-devel
BuildRequires: pkgconfig(jack)

Requires: lv2

%description
A port of the Alsa Modular Synth internal modules to LV2

%prep
%autosetup -n avw.lv2-%{commit0}

# Use lvtk-2
for Files in src/*; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

# For use of python2
sed -i -e "s/env python/env python2/g" waf
sed -i -e "s/env python/env python2/g" wscript

# disable lvtk detection
sed -i -e "/lvtk-/d" wscript

# ensure the correct flags are used and enforce use of our lv2core headers
sed -i -e 's|-std=c99|-std=c99 %{optflags}|' \
       -e 's|lv2/lv2plug.in/ns/lv2core/lv2.h|lv2.h|' \
       -e 's|lv2-c++-tools/lv2.h|lv2.h|' \
    wscript
#rm waf

%build
%set_build_flags
CXXFLAGS=-I/usr/include/lvtk-2 ./waf -v configure --prefix=%{_prefix} --libdir=%{_libdir} --debug
./waf build

%install
./waf install --destdir=%{buildroot}

%files
%doc THANKS
%license COPYING
%{_libdir}/lv2/avw.lv2

%changelog
* Wed Dec 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.8.19
- update to last master

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Orcan Ogetbil <oget [dot] fedora [at] gmail [dot] com> - 0.0.8-16
- Added BR: gcc-c++
- Moved COPYING to %%license
- Build against new lv2-c++-tools

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.8-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.8-3
- New jack BuildRequires

* Sun Jul 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.8-2
- Build using lv2-devel

* Sun Jul 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.8-1
- Update to upstream 0.0.8

* Sun Mar 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.7-1
- Update to upstream 0.0.8

* Mon Jan 16 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.6-3
- Remove build flags, correct release

* Sun Nov 27 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.6-2
- License is GPLv2 not GPLv2+
- Patch FSF address

* Sun Nov 27 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.6-1
- Update to upstream 0.0.6

* Sun Nov 27 2011 Brendan Jones <brendan.jones.it@gmail.com> 0.0.5-1
- Initial build

