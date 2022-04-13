%global        commit0 4b482db17f8d8567ba0abf33459ceb5f756f088c
%global        shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global        commitdate 20190803
%global        gitname realtimeconfigquickscan
%global        debug_package %{nil}

Summary:       Inspect realtime system settings
Name:          realTimeConfigQuickScan
Version:       0
Release:       5.%{commitdate}git%{shortcommit0}%{?dist}
License:       GPLv2+
URL:           https://github.com/raboof/%{gitname}
Source0:       %{URL}/archive/%{commit0}/%{gitname}-%{commit0}.tar.gz
Source1:       realTimeConfigQuickScan
Source2:       QuickScan
Source3:       QuickScan.desktop
BuildArch:     noarch
Requires:      perl(Tk)
BuildRequires: desktop-file-utils
BuildRequires: perl-generators
Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Prevent bogus perl-provides/requires from polluting rpm
%{?perl_default_filter}

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(.*Check\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(.*Check\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(QuickScanEngine\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(QuickScanEngine\\)

%description
Inspects system settings, and makes suggestions for improving realtime/audio 
performance. 

%prep
%setup -q -n %{gitname}-%{commit0}
# correct permissions
chmod +x *.pl

%build

%install
install -D %{SOURCE1} -m 0755 %{buildroot}%{_bindir}/%{name}
install -D %{SOURCE2} -m 0755 %{buildroot}%{_bindir}/QuickScan
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rp * %{buildroot}%{_datadir}/%{name}

desktop-file-install            \
  --dir %{buildroot}%{_datadir}/applications \
 %{SOURCE3}

%files
%doc COPYING
%{_datadir}/%{name}
%{_datadir}/applications/QuickScan.desktop
%{_bindir}/QuickScan
%{_bindir}/%{name}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20190803git4b482db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20190803git4b482db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0-3.20190803git4b482db
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0-2.20190803git4b482db
- Perl 5.32 rebuild

* Sun Mar 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0-1.20190803git4b482db
- New sources from github, first source update since 2012

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.26.20120506hg
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.23.20120506hg
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.20.20120506hg
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.18.20120506hg
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.15.20120506hg
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.14.20120506hg
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0-0.11.20120506hg
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20120506hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.9.20120506hg
- Update desktop file - wrong exec

* Tue Nov 06 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.8.20120506hg
- Simplify requires

* Wed Oct 31 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.7.20120506hg
- Handle bogus requires

* Tue Oct 30 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.6.20120506hg
- User perl(Tk) as BR, edit desktop source

* Mon Oct 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.5.20120506hg
- License missing from %%doc 

* Mon Oct 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.4.20120506hg
- Update source and BuildRequires
- Add source instructions

* Fri Oct 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.2.20121011hg
- Add desktop file

* Thu Oct 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.1.20121011hg
- Initial package 
