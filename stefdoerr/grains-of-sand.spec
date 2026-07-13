# Status: active
# Tag: Plugin
# Type: Plugin, LV2, MODGUI
# Category: Audio, Effect

Name: grains-of-sand
Version: 0.0.1
Release: 1%{?dist}
Summary: A granular delay 
License: GPL-2.0-or-later
URL: https://github.com/stefdoerr/grains-of-sand
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./stefdoerr-source.sh <PROJECT> <TAG>
#        ./stefdoerr-source.sh grains-of-sand main

Source0: grains-of-sand.tar.gz
Source1: stefdoerr-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
A starting point for building LV2 audio plugins targeting MOD Desktop using DPF.
Includes a working passthrough+gain example and a MOD pedalboard GUI (modgui).

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

%build

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
mv bin/myplugin.lv2 bin/grains-of-sand.lv2
cp -ra bin/grains-of-sand.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Jun 09 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
