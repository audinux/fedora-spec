Summary:       VST plug-ins host
Name:          dssi-vst
Version:       0.9.2
Release:       26%{?dist}
License:       GPLv2
URL:           http://breakfastquay.com/dssi-vst/
Source0:       http://code.breakfastquay.com/attachments/download/10/%{name}-%{version}.tar.bz2
# wine-g++ on wine-devel-1.1.18 (Fedora 11) creates executables with .exe suffix:
Patch1:        %{name}-wine1118.patch
ExclusiveArch: %{ix86} x86_64

BuildRequires: dssi-devel
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
# The -wine subpackage will only be built on ix86
%ifarch %{ix86}
BuildRequires: wine-devel
%endif
BuildRequires: make

Requires:      dssi
Requires:      ladspa

# Both packages depend on each other
Requires:      %{name}-wine = %{version}-%{release}

%description
dssi-vst is an adapter that allows users of Linux audio software to take VST
and VSTi audio effects and instrument plug-ins compiled for Windows, and load
them into native LADSPA or DSSI plug-in hosts. Plug-ins run at full speed for
most audio processing, although their user interfaces are slower because of the
Windows emulation.

This package contains the DSSI host for the plug-ins.

%ifarch %{ix86}
%package wine
Summary:       VST plug-ins wrapper
Requires:      %{name} = %{version}-%{release}

%description wine
dssi-vst is an adapter that allows users of Linux audio software to take VST
and VSTi audio effects and instrument plug-ins compiled for Windows, and load
them into native LADSPA or DSSI plug-in hosts. Plug-ins run at full speed for
most audio processing, although their user interfaces are slower because of the
Windows emulation.

This package contains the plug-in wrapper that works through wine.
%endif

%prep
%setup -q
%if 0%{fedora} >= 11
%patch1 -p1 -b .wine1118
%endif


%build
# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%define _lto_cflags %{nil}

# Parallel build fails sometimes:
%ifarch %{ix86}
make CXXFLAGS="%{optflags} -fno-omit-frame-pointer -Ivestige -fPIC -I/usr/include/wine/wine/windows"
%else
# Build non-wine parts only on x86_64:
make dssi-vst.so vsthost dssi-vst_gui CXXFLAGS="%{optflags} -Ivestige -fPIC"
%endif


%install
%ifarch %{ix86}
make  DSSIDIR=%{buildroot}%{_libdir}/dssi   \
    LADSPADIR=%{buildroot}%{_libdir}/ladspa \
       BINDIR=%{buildroot}%{_bindir}        \
    install
# No need for duplicate files. We'll create a symlink instead.
rm -f %{buildroot}%{_libdir}/ladspa/*
%else
mkdir -p %{buildroot}%{_libdir}/dssi/%{name} \
         %{buildroot}%{_bindir}              \
         %{buildroot}%{_libdir}/ladspa
install -pm 755 vsthost %{buildroot}%{_bindir}
install -pm 755 %{name}.so %{buildroot}%{_libdir}/dssi/
install -pm 755 %{name}_gui %{buildroot}%{_libdir}/dssi/%{name}/
%endif
ln -s ../dssi/%{name}.so %{buildroot}%{_libdir}/ladspa

%files
%doc README
%license COPYING
%{_bindir}/vsthost
%{_libdir}/dssi/%{name}.so
%dir %{_libdir}/dssi/%{name}/
%{_libdir}/dssi/%{name}/%{name}_gui
%{_libdir}/ladspa/*

%ifarch %{ix86}
%files wine
%dir %{_libdir}/dssi/
%dir %{_libdir}/dssi/%{name}/
%{_libdir}/dssi/%{name}/%{name}-scanner*
%{_libdir}/dssi/%{name}/%{name}-server*
%endif

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 0.9.2-24
Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.2-20
- Provide the wine include path explicitly. With recent wine, this seems to be
  required.
- Some spec cleanup

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.2-12
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 18 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.2-4
- Rebuild with -fno-omit-frame-pointer RHBZ#704674

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.2-2
- Rebuild against new liblo

* Sun May 09 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.2-1
- Update to 0.9.2
- Drop upstreamed patches

* Sat Feb 13 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8-6
- Disable parallel build
- Correct the glibc212 patch

* Sat Feb 13 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8-5
- Fix build failure against glibc-2.12 RHBZ#564821
- Fix DSO linking failure

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8-3
- Fix wine1118 patch

* Thu Apr 30 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8-2
- Make a ix86 only -wine subpackage

* Wed Mar 25 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8-1
- Update to 0.8. SPEC file is courtesy of PlanetCCRMA.

* Tue Jul  8 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added gcc43 patch for building on fc9

* Fri May 23 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.7-1
- updated to 0.7, added LADSPADIR to make install

* Fri Dec 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.5-1
- initial build.
