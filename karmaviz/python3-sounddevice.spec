# Status: active
# Tag: Library, Devel
# Type: Devel
# Category: Programming

Name: python3-sounddevice
Version: 0.5.5
Release: 1%{?dist}
Summary: Python PortAudio bindings
License: MIT
URL: https://github.com/spatialaudio/python-sounddevice

BuildArch: noarch

Source: https://github.com/spatialaudio/python-sounddevice/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: pyproject_deps.json

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-pip
BuildRequires: python3-cffi
BuildRequires: pyproject-rpm-macros

%description
This Python module provides bindings for the PortAudio library and a few
convenience functions to play and record NumPy_ arrays containing audio signals

%prep
%autosetup -n python-sounddevice-%{version}

%build

%pyproject_wheel

%install

%pyproject_install

%files
%doc README.rst NEWS.rst CONTRIBUTING.rst
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sounddevice.py
%{python3_sitelib}/sounddevice-*.dist-info/*
%{_usr}/lib/python%{python3_version}/site-packages/_sounddevice.py

%changelog
* Fri Jan 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.5-1
- update to 0.5.5-1 

* Thu Jan 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.4-1
- update to 0.5.4-1 

* Tue Nov 18 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- Initial spec file 
