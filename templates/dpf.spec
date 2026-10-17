# Status: active
# Tag: Synthesizer
# Type: Plugin, LV2
# Category: Synthesizer

Name: lv2-triceratops
Version: 0.8.5
Release: 13%{?dist}
Summary: An LV2 polyphonic synthesizer
# license specified in headers and in plugin manifest (triceratops.ttl) is ISC
# http://opensource.org/licenses/isc
License: ISC
URL: https://sourceforge.net/projects/triceratops/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/triceratops/files/triceratops-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: libglvnd-devel

%description
Triceratops a polyphonic subtractive synthesizer plugin for use with the LV2
architecture, there is no standalone version and LV2 is required along
with a suitable host (e.g. Jalv, Zynjacku, Ardour, Qtractor).

%package -n license-%{name}
Summary: License and documentation for %{name}
License: ISC

%description -n license-%{name}
License and documentation for %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: ISC
Requires: license-%{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: ISC
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n dssi-%{name}
Summary: DSSI version of %{name}
License: ISC
Requires: license-%{name}

%description -n dssi-%{name}
DSSI version of %{name}

%prep
%autosetup -c -n triceratops-lv2-%{version}

%build

cd triceratops

%make_build SKIP_STRIPPING=true

%install

cd triceratops

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/triceratops.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra plugins/triceratops/triceratops_presets.lv2 %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/triceratops %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/dssi/
cp -ra bin/triceratops-dssi %{buildroot}/%{_libdir}/dssi/
cp -ra bin/triceratops-dssi.so %{buildroot}/%{_libdir}/dssi/

install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 bin/triceratops-vst.so %{buildroot}/%{_libdir}/vst/

%files
%{_bindir}/*

%files -n license-%{name}
# do not include COPYING - it is GPLV3 where the project is clearly ISC
# https://sourceforge.net/p/triceratops/featurerequests/4/
%doc triceratops/README.md triceratops/AUTHORS
%license triceratops/COPYING

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%changelog
* Sat Oct 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.5-19
- update to 0.8.5-19

* Mon Oct 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.5.0.19
- update to 0.5.0-19

* Wed Jul 28 2021 Yann Collette <ycollette.nospam@free.fr> - 0.4.0.19
- update to 0.4.0-19

* Thu Dec 31 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.2.19
- update to 0.3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.7-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.7-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.7-1
- New upstream 0.1.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.6-1
- New upstream release

* Sun Mar 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.2-3
- adjust CXXFLAGS to fix FTBFS on ARM

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.2-1
- New upstream release
- Remove patches
- Fix wscript bug

* Tue Dec 18 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.1-2.d
- Correct install directory patch

* Mon Dec 17 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.1-1.d
- Initial development
