%global commit0 38f3c046dadc81da94783c76c6fc697b0ae32c8a

Name: pyliblo
Version: 0.12.0
Release: 1%{?dist}
Summary: Python bindings for the liblo OSC library
License: GPL-2.0-or-later
URL: https://github.com/mididings/pyliblo
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/mididings/pyliblo/archive/%{commit0}.zip#/%{name}-%{version}.zip
Patch0: pyliblo_fix_cython.patch
Patch1: pyliblo_fix_install.patch

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
%setup -n pyliblo-%{commit0}

%if 0%{?fedora} >= 40
%patch 0 -p1
%endif
%patch 1 -p1

%build

%set_build_flags
export CFLAGS="-Wno-incompatible-pointer-types $CFLAGS"

%py3_build

%install
%py3_install

%files -n python3-%{name}
%doc NEWS README.md examples/
%license COPYING
%{_bindir}/dump_osc
%{_bindir}/send_osc
%{python3_sitearch}/liblo*.so
%{python3_sitearch}/pyliblo*.egg-info
%{python3_sitearch}/liblo/__init__.pyi
%{python3_sitearch}/liblo/py.typed

%changelog
* Tue Sep 27 2022 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- update to 0.12.0-1
