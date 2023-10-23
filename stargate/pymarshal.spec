%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:    pymarshal
Version: 2.2.0
Release: 1%{?dist}
Summary: Python data serialization library
License: BSD-2
URL:     https://github.com/stargateaudio/pymarshal

Vendor:       Audinux
Distribution: Audinux

Source0: https://files.pythonhosted.org/packages/62/ef/e04a84361e82c8f0b750a63691404ed47dcfa3c7463eab16ec7607be0efc/pymarshal-2.2.0.tar.gz

BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-wheel
BuildRequires: python%{python3_pkgversion}-pip

%{?python_enable_dependency_generator}

%description
pymarshal replicates the feature of (un)marshalling structs in Golang.
Rather than replicating the exact feature as it exists in Go, pymarshal
aims for elegant, Pythonic simplicity, and to fix the flaws in Go's
implementation such as:

- extra keys being silently ignored
- lack of mandatory fields
- lack of default values See control variables for the many options that can be configured per-class.

%package -n python%{python3_pkgversion}-%{name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python%{python3_pkgversion}-%{name}
pymarshal replicates the feature of (un)marshalling structs in Golang.
Rather than replicating the exact feature as it exists in Go, pymarshal
aims for elegant, Pythonic simplicity, and to fix the flaws in Go's
implementation such as:

- extra keys being silently ignored
- lack of mandatory fields
- lack of default values See control variables for the many options that can be configured per-class.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
%py3_build

%install
%py3_install

%files -n  python%{python3_pkgversion}-%{name}
%doc README.md
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-1
- initial spec file
