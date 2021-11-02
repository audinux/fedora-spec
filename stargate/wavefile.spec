%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:    wavefile
Version: 1.5
Release: 1%{?dist}
Summary: Pythonic access to audio files	
License: GPL3	
URL:     https://github.com/vokimon/python-wavefile

Source0: https://github.com/vokimon/python-wavefile/archive/refs/tags/python-wavefile-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pip

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
%py3_build

%install
%py3_install

%files -n  python%{python3_pkgversion}-%{name}
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> 1.5-1
- initial spec file.
