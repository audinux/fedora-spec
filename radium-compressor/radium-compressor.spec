# Tag: Audio, Effect, Compressor, Jack
# Type: Standalone
# Category: Audio, Effect

%ifarch %ix86 x86_64
%define msse_flags -msse -mfpmath=sse
%endif

Name: radium-compressor
Version: 0.5.1
Release: 20%{?dist}
Summary: An audio compressor for JACK
License: GPL-3.0-or-later
URL: http://users.notam02.no/~kjetism/radium/
ExclusiveArch: x86_64 aarch64

Source0: http://archive.notam02.no/arkiv/src/radium_compressor-0.5.1.tar.gz
Source1: radium-compressor.desktop
Patch0: radium_compressor-0.5.1-cstdlib.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: qt4-devel
BuildRequires: desktop-file-utils

%description
Radium Compressor is the system compressor in Radium,
but distributed as a standalone jack application.

Radium Compressor uses the stereo compressor found in
effect.lib in the Faust distribution.

%prep
%autosetup -p1 -n radium_compressor-%{version}

find -name "*.h" -exec chmod 0644 {} \;
# see https://bugzilla.redhat.com/show_bug.cgi?id=904658 for
# justification of non-standard optflags
sed -i -e 's|-O3 -Wall -msse -mfpmath=sse|%{optflags} %{?msse_flags} -O3|' Makefile

%build
%make_build

%install
install -p -D -m0755 radium_compressor %{buildroot}%{_bindir}/radium_compressor
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %SOURCE1

%files
%doc README Changelog
%license COPYING
%{_bindir}/radium_compressor
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Dan Horák <dan[at]danny.cz> 0.5.1-4
- fix build on arches where the msse_flags variable is not defined

* Wed Feb 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-3
- Link to review BZ for optflag justification
- Set optflags only once

* Sat Feb 09 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-2
- Adjust build flags, file permissions and license

* Sat Jan 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-1
- New upstream release

* Fri Jan 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-1
- Initial development
