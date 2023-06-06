# Tag: Drum
# Type: LV2
# Category: Synthesizer

Name:    drumrox
Version: 2.0.0
Release: 1%{?dist}
Summary: A hydrogen compatible drum LV2 plugin
License: GPLv3+
URL:     https://github.com/psemiletov/drumrox

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/drumrox/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%cmake -DLV2_INSTALL_DIR:Path=%{_lib}/lv2
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Tue Jun 06 2023 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- Initial build
