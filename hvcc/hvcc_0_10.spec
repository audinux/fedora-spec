# Status: active
# Tag: Tool, Audio
# Type: Standalone
# Category: Tool, Audio

Name: hvcc_0_10
Version: 0.10.0
Release: 2%{?dist}
Summary: The heavy hvcc compiler for Pure Data patches.
URL: https://github.com/Wasted-Audio/hvcc
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Wasted-Audio/hvcc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: python3-poetry
BuildRequires: desktop-file-utils

Requires: python3-jinja2
Requires: python3-pydantic
Requires: python3-importlib-resources
Requires: python3-wstd2daisy
Requires: python3-setuptools
Requires: puredata

%description
hvcc is a python-based dataflow audio programming language compiler
that generates C/C++ code and a variety of specific framework wrappers.

%prep
%autosetup -n hvcc-%{version}

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files hvcc

# Cleanup
rm -rf %{buildroot}/%{python3_sitelib}/tests

%files -f %{pyproject_files}
%doc README.md docs/*
%license LICENSE
%{_bindir}/hvcc
%{_bindir}/hvutil

%changelog
* Wed Mar 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-2
- update to 0.10.0-2
