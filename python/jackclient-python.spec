# Status: active
# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global srcname0 JACK-Client
%global srcname1 jackclient-python
%global srcname2 JACK_Client

Name: python-jack-client
Version: 0.5.5
Release: 16%{?dist}
Summary: JACK Audio Connection Kit (JACK) Client for Python
URL: http://jackclient-python.rtfd.org
License: MIT
BuildArch: noarch

Source0: https://github.com/spatialaudio/jackclient-python/archive/%{version}/%{srcname0}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-cffi

%{?python_provide:%python_provide %{name}}
Requires: python3-cffi
Requires: pkgconfig(jack)
Suggests: python3-numpy

%description
Python module that provides bindings for the JACK library.
The module is able to create audio input and output ports,
also provides the functionality to manage MIDI ports.

This package installs the library for Python.

%prep
%autosetup -n %{srcname1}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%doc NEWS.rst
%doc CONTRIBUTING.rst
%{python3_sitelib}/%{srcname2}-*.egg-info/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/_jack.py
%{python3_sitelib}/jack.py

%changelog
* Mon Jun 02 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-16
- update to 0.5.5-16

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.2-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.2-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro HronÄ¨ok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.9

* Mon Feb 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.5.2-1
- Initial release for Fedora
