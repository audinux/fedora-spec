Name: pyliblo
Version: 0.12.0
Release: 1%{?dist}
Summary: Python bindings for the liblo OSC library

License: GPLv2+
URL: https://github.com/gesellkammer/pyliblo3
Source0: https://github.com/gesellkammer/pyliblo3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-Cython
BuildRequires: liblo-devel

Provides: %{name} = %{version}-%{release}

%description
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

Also included are the command line utilities send_osc and dump_osc.

%package -n python3-%{name}
Summary: Python bindings for the liblo OSC library
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

Also included are the command line utilities send_osc and dump_osc.

%prep
%autosetup -n pyliblo3-%{version}

# Remove shebang and executable bit from example scripts
find examples/ -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?==' {} +
chmod -x examples/*

%build
%py3_build

%install
%py3_install

%files -n python3-%{name}
%doc NEWS README.md examples/
%license COPYING
%{_bindir}/*_osc.py
%{python3_sitearch}/liblo*.so
%{python3_sitearch}/pyliblo*.egg-info

%changelog
* Tue Sep 27 2022 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- update to 0.12.0-1
