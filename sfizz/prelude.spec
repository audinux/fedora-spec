# Tag: Organ, Synthesizer
# Type: Plugin, LV2
# Category: Synthesizer

# Global variables for github repository
%global commit0 176abd3f6ccabe10699275b8c7b9fd6c3b4ca40c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name: prelude
Version: 0.0.1
Release: 1%{?dist}
License: BSD-2-Clause
Summary: A wavetable-based church organ
URL: https://github.com/sfztools/prelude.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sfztools/%{name}.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: sfizz-devel

%description
A simple wavetable-based church organ as an LV2 plugin
with a very reduced set of parameters.

%package -n lv2-%{name}
Summary: A wavetable-based church organ

%description -n lv2-%{name}
A simple wavetable-based church organ as an LV2 plugin
with a very reduced set of parameters.

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
%license LICENSE.md
%{_libdir}/lv2/*

%changelog
* Sun Oct 31 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial release of the spec file
