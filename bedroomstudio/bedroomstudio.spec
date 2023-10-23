Name: bedroomstudio
Version: 1.0.0
Release: 1%{?dist}
Summary: A set of LV2 plugins
License: MIT
URL: https://github.com/psemiletov/bedroomstudio

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/bedroomstudio/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel

%description
A set of LV2 plugins for bedroom music studio :) The idea is to
provide simple, nice sounding effects those become a legend.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/lib\/lv2/%{_lib}\/lv2/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial packaging.
