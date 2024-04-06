# Tag: Drum
# Type: LV2
# Category: Synthesizer

Name: drumrox
Version: 3.3.0
Release: 1%{?dist}
Summary: A hydrogen compatible drum LV2 plugin
License: GPL-3.0-or-later
URL: https://github.com/psemiletov/drumrox

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/drumrox/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# TODO: https://github.com/psemiletov/drumrox-kits
# - check compatibility with hydrogen
# - add this to the repo

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: gtk2-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel

%description
Drumrox is LV2 drummachine (DrMr fork) to load Hydrogen drumkits.
The main goal of Drumrox is to keep it compatible with MODERN Hydrogen kit format.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%cmake -DLV2_INSTALL_DIR:Path=%{_lib}/lv2 \
       -DCMAKE_CXX_FLAGS="-Wno-implicit-function-declaration $CXXFLAGS" \
       -DCMAKE_C_FLAGS="-Wno-implicit-function-declaration $CFLAGS"
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Fri Apr 05 2024 Yann Collette <ycollette.nospam@free.fr> - 3.3.0-1
- update to 3.3.0-1

* Mon Jul 10 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-1
- update to 3.2.1-1

* Tue Jul 04 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.0-1
- update to 3.2.0-1

* Thu Jun 29 2023 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-1
- update to 2.3.1-1

* Tue Jun 20 2023 Yann Collette <ycollette.nospam@free.fr> - 2.2.1-1
- update to 2.2.1-1

* Mon Jun 19 2023 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-1
- update to 2.2.0-1

* Tue Jun 13 2023 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- update to 2.1.0-1

* Tue Jun 06 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- Initial build
