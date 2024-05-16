Name: plotmm
Version: 0.1.2
Release: 35%{?dist}
Summary: GTKmm plot widget for scientific applications
License: LGPLv2
URL: http://plotmm.sourceforge.net/
ExclusiveArch: x86_64 aarch64

Source0: http://download.sourceforge.net/plotmm/plotmm-%{version}.tar.gz
# Fix code to build against libsigc++20
# Upstream:
# https://sourceforge.net/tracker/?func=detail&atid=632478&aid=2082337&group_id=102665
Patch0: plotmm-0.1.2-libsigc++20.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtkmm24-devel >= 2.4.0
BuildRequires: chrpath

%description
This package provides an extension to the gtkmm library.
It contains widgets which are primarily useful
for technical and scientifical purposes.
Initially, this is a 2-D plotting widget.

%package devel
Summary: Headers for developing programs that will use plotmm
Requires: %{name} = %{version}-%{release}
Requires: gtkmm24-devel

%description devel
This package contains the headers that programmers will
need to develop applications which will use plotmm.

%package -n plotmm-examples
Summary: Plotmm sample applications
Requires: %{name} = %{version}-%{release}

%description -n plotmm-examples
Plotmm sample applications: plotmm-curves, plotmm-simple

%prep
%autosetup -p1 -n plotmm-%{version}

%build
%configure --disable-static --enable-docs
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_libdir}/plotmm/examples
mv $RPM_BUILD_ROOT%{_bindir}/curves $RPM_BUILD_ROOT%{_bindir}/plotmm-curves
mv $RPM_BUILD_ROOT%{_bindir}/simple $RPM_BUILD_ROOT%{_bindir}/plotmm-simple

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/plotmm-curves
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/plotmm-simple

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_includedir}/plotmm/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n plotmm-examples
%{_bindir}/plotmm-curves
%{_bindir}/plotmm-simple

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.2-21
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.2-14
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 31 2010 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-12
- Rebuilt for F-13

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.2-9
- fix code to compile against libsigc++20

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.2-8
- fix broken BR

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.2-7
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.2-6
- Autorebuild for GCC 4.3

* Tue Sep 12 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-5
- rebuild for FC6

* Tue Jun 13 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-4
- some fixes to the spec

* Tue Jun 13 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-3
- some syntax fixes to post and postun section

* Fri May 26 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-2
- added doc to devel package and put sample applications into plotmm-examples package

* Sat May 20 2006 Haïkel Guémar <karlthered@gmail.com> - 0.1.2-1
- First Packaging
