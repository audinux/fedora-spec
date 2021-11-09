Name:    lv2-kn0ck0ut
Version: 1.12
Release: 1%{?dist}
Summary: An LV2 spectral subtraction plugin
License: GPLv3+
URL:     https://github.com/jeremysalwen/kn0ck0ut-LV2

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: lv2-c++-tools-devel

Requires:      lv2

%description
Kn0ck0ut-LV2 is an LV2 plugin to perform spectral subtraction. It can be used
to achieve a wide variety of effects, most notably removing or extracting the
center of a two channel audio file. As Kn0ck0ut is only a plugin, you will
need a host for LV2 plugins in order to use it, such as Ardour, Qtractor, Ingen,
lv2_jack_host, or lv2file.

%prep
%autosetup -n kn0ck0ut-LV2-%{version}  
sed -i -e 's|^CXXFLAGS+=-O3 -ffast-math |CXXFLAGS += %{optflags} -I/usr/include/lv2-c++-tools/ |' Makefile
sed -i -e 's|^LDFLAGS +=|LDFLAGS += %{optflags} |' Makefile
sed -i -e 's|^INSTALL_DIR = $(DESTDIR)/usr/lib/lv2|INSTALL_DIR = $(DESTDIR)%{_libdir}/lv2|' Makefile

%build
%set_build_flags
%make_build

%install
%make_install

%files
%doc readme.txt
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu Dec 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.12-16
- update to 1.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.1-9.0.giteaeb2d90
- Remove %%lib sed-ing (F23FTBFS, RHBZ#1239661, F24FTBFS, RHBZ#1307758).
- Rework %%optflags handling.
- Add %%license.
- BR pkgconfig(*) instead of *-devel.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2.0.giteaeb2d90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.0.giteaeb2d9
- Update git, and build against lv2

* Fri Jan 20 2012 Dan Horák <dan[at]danny.cz> 1.1-0.4.git60421a3
- fix build on non-x86 64-bit arches

* Tue Jan 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1-0.3.git60421a3
- git commit containing license clarification 

* Fri Jan 06 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1-0.2.gitd03e8db0
- removed lv2config 

* Mon Oct 31 2011 Brendan Jones <brendan.jones.it@gmail.com> 1.1-0.1.gitd03e8db0
- Initial build

