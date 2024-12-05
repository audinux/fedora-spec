# Status: active
%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:    wavefile
Version: 1.6.3
Release: 1%{?dist}
Summary: Pythonic access to audio files
License: GPL3
URL:     https://github.com/vokimon/python-wavefile
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/vokimon/python-wavefile/archive/refs/tags/python-wavefile-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-wheel

%{?python_enable_dependency_generator}

%description
Pythonic libsndfile wrapper to read and write audio files.

%package -n python%{python3_pkgversion}-%{name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python%{python3_pkgversion}-%{name}
Pythonic libsndfile wrapper to read and write audio files.

%prep
%autosetup -p1 -n python-wavefile-python-%{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wavefile

%files -f %{pyproject_files}
%doc README.md
%{python3_sitelib}/examples/__pycache__/*
%{python3_sitelib}/examples/play.py
%{python3_sitelib}/examples/process.py
%{python3_sitelib}/examples/record.py
%{python3_sitelib}/examples/synth.py
%{python3_sitelib}/examples/wholefile.py

%changelog
* Wed Dec 04 2024 Yann Collette <ycollette.nospam@free.fr> 1.6.3-1
- update to 1.6.3-1

* Tue Oct 10 2023 Yann Collette <ycollette.nospam@free.fr> 1.6.2-1
- update to 1.6.2-1

* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> 1.5-1
- initial spec file.
