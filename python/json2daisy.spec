# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global __python %{__python3}

Name: python-json2daisy
Version: 0.4.2
Release: 1%{?dist}
Summary: Utility for converting JSON board definitions into valid, libDaisy compatible C++ board support files for the Daisy platform.

License: MIT
URL: https://github.com/electro-smith/json2daisy
Source0: %{pypi_source json2daisy}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description
Utility for converting JSON board definitions into valid,
libDaisy compatible C++ board support files for the Daisy platform.

%package -n python3-json2daisy
Summary: %{summary}

%description -n python3-json2daisy
Utility for converting JSON board definitions into valid,
libDaisy compatible C++ board support files for the Daisy platform.

%prep
%autosetup -n json2daisy-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files json2daisy

%files -n python3-json2daisy -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial release
