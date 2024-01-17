# Tag: Synthesizer
# Type: Plugin, LV2
# Category: Synthesizer

Name: lv2-triceratops
Version: 0.5.0
Release: 13%{?dist}
Summary: An LV2 polyphonic synthesizer
# license specified in headers and in plugin manifest (triceratops.ttl) is ISC
# http://opensource.org/licenses/isc
License: ISC
URL: https://sourceforge.net/projects/triceratops/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/triceratops/files/triceratops_v0.5.0_Oct_2022.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python2
BuildRequires: pkgconfig(jack)
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: gtkmm24-devel

%description
Triceratops a polyphonic subtractive synthesizer plugin for use with the LV2
architecture, there is no standalone version and LV2 is required along
with a suitable host (e.g. Jalv, Zynjacku, Ardour, Qtractor).

%prep
%autosetup -c -n triceratops-lv2-v0.0.4
# this is a bug in the installer script - however -finline-functions is necessary here
# https://sourceforge.net/p/triceratops/featurerequests/3/
sed -i -e "s|-lX11'],'-finline-functions'|-lX11','-finline-functions']|" triceratops/wscript
sed -i -e "s|\['-O3','-std=c++0x'\]|'-std=c++0x %{optflags}'.split(' ')|" triceratops/wscript
# Force use of python2
sed -i -e "s|env python|env python2|g" triceratops/waf
sed -i -e "s|env python|env python2|g" triceratops/wscript
# set LV2PATH
sed -i -e "/conf.env.LV2DIR/d" triceratops/wscript

%build

cd triceratops

export CXXFLAGS="%{optflags} -fPIC"
export LV2_PATH=:%{_libdir}/lv2

./waf configure -vv --prefix=%{_prefix} --libdir=%{_libdir}
./waf -vv %{?_smp_mflags}

%install

cd triceratops

./waf install --destdir=%{buildroot}

mkdir -p %{buildroot}%{_libdir}/lv2/
mv %{buildroot}/triceratops.lv2 %{buildroot}%{_libdir}/lv2/
mv %{buildroot}/triceratops-presets.lv2 %{buildroot}%{_libdir}/lv2/
rm  -rf %{buildroot}%{_libdir}/lv2/triceratops-presets.lv2/.directory

%files
# do not include COPYING - it is GPLV3 where the project is clearly ISC
# https://sourceforge.net/p/triceratops/featurerequests/4/
%doc triceratops/README triceratops/AUTHORS
%license triceratops/COPYING
%{_libdir}/lv2/triceratops.lv2
%{_libdir}/lv2/triceratops-presets.lv2

%changelog
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
