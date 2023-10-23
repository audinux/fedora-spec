Name:    lv2-fomp-plugins
Version: 1.2.0
Release: 14%{?dist}
Summary: A collection of LV2 plugins
License: GPL-2.0-or-later
URL:     http://drobilla.net/

Vendor:       Audinux
Distribution: Audinux

Source0: http://deb.debian.org/debian/pool/main/f/fomp/fomp_1.2.0.orig.tar.bz2

BuildRequires: gcc-c++ make
BuildRequires: lv2-devel
BuildRequires: python2

Requires:      lv2

%description
Fomp is an LV2 port of the MCP, VCO, FIL, and WAH plugins by Fons Adriaensen.

There are 13 plugins in total: 1 auto-wah, 1 EQ, 3 chorus, 5 filters, and 3
oscillators.

The plugin implementations are identical to their LADSPA forebears, except
the primary frequency port of oscillators and filters has been converted to
Hz to facilitate use in any host without assuming the hidden tuning frequency
of AlsaModularSynth. All other frequency ports remain as they were, using
octaves for faithful Moog-like modulation.

%prep
%autosetup -n fomp-%{version}

# Force use of python2
sed -i -e "s|env python|env python2|g" waf
sed -i -e "s|env python|env python2|g" wscript

%build
%set_build_flags
./waf configure -v --prefix=%{_prefix} --libdir=%{_libdir}
./waf -v build %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}

%files
%doc README.md NEWS AUTHORS
%license COPYING
%{_libdir}/lv2/fomp.lv2

%changelog
* Thu Dec 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.0.14
- update to 1.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Dec 17 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-1
- Initial build

