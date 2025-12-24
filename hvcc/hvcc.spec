# Status: active
# Tag: Tool, Audio
# Type: Standalone
# Category: Tool, Audio

Name: hvcc
Version: 0.15.0
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
%autosetup -n %{name}-%{version}

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files hvcc

install -m 755 -d %{buildroot}%{_datadir}/%{name}/docs/
cp -rav docs/* %{buildroot}%{_datadir}/%{name}/docs/

# Cleanup
rm -rf %{buildroot}/%{python3_sitelib}/tests

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/hvcc
%{_bindir}/hvutil
%{_datadir}/hvcc/docs/*

%changelog
* Wed Dec 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.15.0-2
- update to 0.15.0-2

* Fri Sep 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.14.0-2
- update to 0.14.0-2

* Mon May 12 2025 Yann Collette <ycollette.nospam@free.fr> - 0.10-2
- build 0.11-2 because of wrong set of python modules for 0.11 and 0.13

* Wed Jan 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.13.2-2
- update to 0.13.2-2

* Fri Dec 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.13.0-2
- update to 0.13.0-2

* Sat Sep 21 2024 Yann Collette <ycollette.nospam@free.fr> - 0.12.1-2
- update to 0.12.1-2

* Fri Jun 21 2024 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to 0.12.0-2

* Fri Feb 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.11-2
- update to 0.11-2

* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-2
- update to 0.10.0-2 - fix python deps

* Wed Dec 06 2023 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- update to 0.10.0-1

* Tue Sep 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- update to 0.9.0-1

* Mon Aug 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Thu Apr 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0-1

* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial release
