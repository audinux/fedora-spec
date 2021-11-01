# Global variables for github repository
%global commit0 d909db65ed706188a2549838b3fc8a3a37fa685b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    toccata
Version: 0.0.1
Release: 1%{?dist}
License: BSD-2-Clause
Summary: A reasonable LV2 church organ
Url:     https://github.com/sfztools/toccata.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sfztools/%{name}.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: sfizz-devel

%description
toccata.lv2 is a simple wavetable-based church organ as an LV2 plugin.
It uses the sfizz library to load an SFZ file containing the wavetables,
and create LV2 parameters for the volume of each rank.

%package -n lv2-%{name}
Summary: A reasonable LV2 church organ

%description -n lv2-%{name}
toccata.lv2 is a simple wavetable-based church organ as an LV2 plugin.
It uses the sfizz library to load an SFZ file containing the wavetables,
and create LV2 parameters for the volume of each rank.

%prep
%autosetup -n %{name}.lv2-%{commit0}

%build

%set_build_flags

%cmake -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2

%cmake_build

%install

%cmake_install

%files -n lv2-%{name}
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sun Oct 31 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial release of the spec file
