# version: dae177189b12f74ea01ac2389b76326c06d9be78
Name:           non-ntk
Version:        1.3.0
Release:        0.17.20191215gitdae17718%{?dist}
Summary:        A fork of FLTK for the non audio suite
# themse are GPLv2+, FLTK derived code is LGPLv2+
License:        LGPLv2+ with exceptions and GPLv2+
URL:            http://non.tuxfamily.org/

Vendor:       Audinux
Distribution: Audinux

# git clone git://git.tuxfamily.org/gitroot/non/fltk.git ntk
Source0:        non-ntk-20191215-gitdae177189b12f74ea01ac2389b76326c06d9be78.tar.bz2
# script to create source tarball from git
# sh non-snapshot.sh $(rev)
# no desktop file in tarball
Source1:        non-ntk-1.3.0-fluid.desktop
# sent upstream via email
Patch1:         non-ntk-1.3.0-fsf.patch
Patch2:         non-ntk-unused-shlib.patch
Patch3:         non-ntk-scandir.patch

BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python2
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xft)
BuildRequires:  gcc gcc-c++

%description
%{name} is a fork of the FLTK UI toolkit. It employs cairo support and
other additions not accepted upstream. It is currently used by the non-*
audio suite of programs.

%package devel
Summary:        Development files for the non-ntk GUI library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Non-ntk GUI library

%package fluid
Summary: Fast Light User Interface Designer
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep
%autosetup -p1 -n non-ntk-20191215

sed -i -e "s|append_value('C\(.*\)FLAGS', CFLAGS|append_value('C\1FLAGS','%{optflags}'.split(' ')|" wscript

sed -i -e "s/env python/env python2/g" test/wscript
sed -i -e "s/env python/env python2/g" wscript
sed -i -e "s/env python/env python2/g" fluid/wscript
sed -i -e "s/env python/env python2/g" waf

sed -i -e "s/function_name=//g" wscript

%build
#LDFLAGS="%{?__global_ldflags}"
./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-gl || true
./waf %{?_smp_mflags} 

%install 
./waf -v install --destdir=%{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/ntk-fluid.desktop
rm %{buildroot}%{_libdir}/libntk*.a*

%ldconfig_scriptlets
 
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-fluid.desktop

%files
%doc COPYING
%{_libdir}/libntk*.so.*

%files devel
%{_libdir}/libntk.so
%{_libdir}/libntk_images.so
%{_libdir}/libntk_gl.so
%{_includedir}/ntk
%{_libdir}/pkgconfig/*

%files fluid
%{_datadir}/applications/ntk-fluid.desktop
%{_bindir}/ntk-*

%changelog
* Sun Dec 15 2019 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-0.17.20191215gitdae17718
- Update to the last master version

* Tue Nov 5 2019 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-0.17.20130730gitd006352
- fixes for Fedora 31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.17.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.16.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.15.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.14.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.13.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.12.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.0-0.11.20130730gitd006352
- buildfix: missing fl_scandir
- Added BR: python2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.10.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.9.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.8.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.7.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.6.20130730gitd006352
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.5.20130730gitd006352
- Add exceptions to LGPLv2 license
- add desktop scriptlet post fluid

* Mon Sep 02 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.4.20130730gitd006352
- Adjust license 
- Remove icon scriptlets
- Correct BRs

* Thu Aug 29 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.3.20130730gitd006352
- Correct license
- Remove static libraries
- Correct optflags and BRs

* Sat Aug 17 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-0.1.20130730gitd006352
- Initial package
