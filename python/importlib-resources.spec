# Tag: Library, Devel
# Type: Devel
# Category: Programming

# 5.9 	3.12
# 5.7 	3.11
# 5.0 	3.10

%global __python %{__python3}

Name: python-importlib-resources
Version: 5.10.2
Release: 1%{?dist}
Summary: a backport of Python standard library importlib.resources module for older Pythons.

License: ASL 2.1
URL: https://github.com/python/importlib_resources
Source0: %{pypi_source importlib_resources}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description
importlib_resources is a backport of Python standard library
importlib.resources module for older Pythons.

The key goal of this module is to replace parts of pkg_resources
with a solution in Python's stdlib that relies on well-defined APIs.
This makes reading resources included in packages easier, with more
stable and consistent semantics.

%package -n python3-importlib-resources
Summary: %{summary}

%description -n python3-importlib-resources
importlib_resources is a backport of Python standard library
importlib.resources module for older Pythons.

The key goal of this module is to replace parts of pkg_resources
with a solution in Python's stdlib that relies on well-defined APIs.
This makes reading resources included in packages easier, with more
stable and consistent semantics.

%prep
%autosetup -n importlib_resources-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files importlib_resources

%files -n python3-importlib-resources -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial release
