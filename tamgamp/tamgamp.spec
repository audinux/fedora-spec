# Tag: Amp Simul, Cabinet
# Type: Plugin, LV2
# Category: Audio, Effect

# Global variables for github repository
%global commit0 426da74142fcb6b7687a35b2b1dda3392e171b92
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    tamgamp
Version: 0.0.1
Release: 1%{?dist}
Summary: Tamgamp is a LV2 guitar amp simulator
License: LGPL3
URL:     https://github.com/sadko4u/tamgamp.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sadko4u/tamgamp.lv2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: zita-resampler-devel

%description
Tamgamp (Rhymes with: "Damage Amp") is a LV2 guitar amp simulator.

%package -n lv2-%{name}
Summary:  Tamgamp is a LV2 guitar amp simulator
License:  LGPL3

%description -n lv2-%{name}
Tamgamp (Rhymes with: "Damage Amp") is a LV2 guitar amp simulator.

%prep
%autosetup -n %{name}.lv2-%{commit0}

%build
%set_build_flags
%make_build

%install
%make_install LV2DIR=%{_libdir}/lv2

%files -n lv2-%{name}
%license COPYING COPYING.LESSER
%doc README.md
%{_libdir}/lv2/*

%changelog
* Wed Nov 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial version of the spec
