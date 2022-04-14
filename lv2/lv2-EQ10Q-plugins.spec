Name:    lv2-EQ10Q-plugins
Version: 2.2
Release: 8%{?dist}
Summary: LV2 Plugin: Parametric audio equalizer with 12 different filter types

# The vuwidget class is under GPLv3+.  The rest is under GPLv2+.  The GPLv3+ is
# only only included in the parameq_gui.so library.  The other library,
# paramEQ.so, contains only GPLv2+ code.
License: GPLv2+ and GPLv3+
URL:     http://eq10q.sourceforge.net/

Source0: http://downloads.sourceforge.net/project/eq10q/eq10q-%{version}.tar.gz
# Patches from debian package
Patch0: eq10q_01-fix_prexix.patch
Patch1: eq10q_02-remove_sse_flags.patch
Patch2: eq10q_03-fix_flags.patch
Patch3: eq10q_04-spelling.patch
Patch4: eq10q_05-pow10.patch
Patch5: eq10q_0006-Fix-lv2-types.patch

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: gcc-c++
BuildRequires: fftw-devel
BuildRequires: gtkmm24-devel
BuildRequires: plotmm-devel
BuildRequires: lv2-c++-tools-static
BuildRequires: pstreams-devel
BuildRequires: lv2-devel

Requires: lv2

%description
EQ10Q is an audio plug-in using the LV2 standard implementing a powerful and
flexible parametric equalizer.
The goal is to create an equalizer plug-in that includes parametric equalization
with different filter types like peaking, HPF, LPF, Shelving and Notch with IIR
algorithms and a nice GUI displaying the equalization curve.
At the moment we have implemented second order biquadratic filters (Peaking,
Low Shelving, High Shelving and Notch), and configurable order (1, 2, 3, 4) HPF
and LPF filters. All with IIR algorithms.

%prep
%autosetup -p1 -n eq10q-%{version}

# Get rid of warnings about spurious exec permissions in debuginfo package
chmod -x gui/widgets/templatewidget.cpp gui/widgets/templatewidget.h *.c *.h */*.c */*.h

# Disable SSE on unsupported architectures
%ifnarch %ix86 x86_64
sed -i 's|-msse -mfpmath=sse||g' CMakeLists.txt
%endif

sed -i -e "/CMAKE_INSTALL_PREFIX/d" CMakeLists.txt

%build
%{cmake} -DCMAKE_INSTALL_PREFIX="%{_libdir}/lv2" ..
%cmake_build

%install
%cmake_install

%files
%doc README
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu Apr 14 2022 Yann Collette <ycollette.nospam@free.fr> - 2.2-8
- update to 2.2-8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Orcan Ogetbil <oget [dot] fedora [at] gmail [dot] com> - 2.2-1
- Update version
- Added BR: gcc-c++
- Some cleanup

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-17
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Brendan Jones <brendan.jones.it@gmail.com> - 1.0-11
- Rebuilt against new lv2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0-9
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 28 2010 David Cornette <rpm@davidcornette.com> 1.0-7
- Rebuilt for newly rebuilt lv2-c++-tools-devel

* Thu Jul 08 2010 David Cornette <rpm@davidcornette.com> 1.0-6
- Fixed some spelling errors and added comments about the patches

* Sun May 23 2010 David Cornette <rpm@davidcornette.com> 1.0-5
- Changed BuildRequires: to lv2-c++-tools-static instead of -devel
- Fixed executable permissions on two source files in debuginfo package

* Wed Apr 14 2010 David Cornette <rpm@davidcornette.com> 1.0-4
- Patch ttl file to define foaf
- Patch plugin gui to look for image files in /usr/share

* Mon Apr 12 2010 David Cornette <rpm@davidcornette.com> 1.0-3
- Using version macro in Source0:
- fixed license
- Patched Makefile to be able to override CXXFLAGS with optflags

* Sun Apr 11 2010 David Cornette <rpm@davidcornette.com> 1.0-2
- Adding BuildRequires:  lv2core-devel

* Fri Apr 9 2010 David Cornette <rpm@davidcornette.com> 1.0-1
- Initial build

