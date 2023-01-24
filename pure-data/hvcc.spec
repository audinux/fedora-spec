Name:    hvcc
Version: 0.6.3
Release: 1%{?dist}
Summary: The heavy hvcc compiler for Pure Data patches.
URL:     https://github.com/Wasted-Audio/hvcc
License: GPLv3+

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Wasted-Audio/hvcc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: desktop-file-utils

Requires: python3-jinja2
Requires: python3-importlib-resources
Requires: python3-json2daisy
Requires: python3-setuptools
Requires: puredata

%description
hvcc is a python-based dataflow audio programming language compiler
that generates C/C++ code and a variety of specific framework wrappers.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

install -m 755 -d %{buildroot}%{_datadir}/%{name}/docs/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/examples/
cp -rav docs/* %{buildroot}%{_datadir}/%{name}/docs/
cp -rav examples/* %{buildroot}%{_datadir}/%{name}/examples/

# Cleanup
rm -rf %{buildroot}/%{python3_sitelib}/tests

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/%{name}/*
%{python3_sitelib}/%{name}-*.egg-info
%{_datadir}/%{name}/docs/*
%{_datadir}/%{name}/examples/*

%changelog
* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial release
