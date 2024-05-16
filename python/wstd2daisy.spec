# Tag: Library, Devel
# Type: Devel
# Category: Programming

%global __python %{__python3}

Name: python-wstd2daisy
Version: 0.5.2
Release: 1%{?dist}
Summary: Utility for converting JSON board definitions into valid, libDaisy compatible C++ board support files for the Daisy platform.
License: MIT
URL: https://github.com/Wasted-Audio/json2daisy
ExclusiveArch: x86_64 aarch64

Source0: %{pypi_source wstd2daisy}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description
Utility for converting JSON board definitions into valid,
libDaisy compatible C++ board support files for the Daisy platform.

%package -n python3-wstd2daisy
Summary: %{summary}

%description -n python3-wstd2daisy
Utility for converting JSON board definitions into valid,
libDaisy compatible C++ board support files for the Daisy platform.

%prep
%autosetup -n wstd2daisy-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files json2daisy

%files -n python3-wstd2daisy -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Feb 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- Initial release
