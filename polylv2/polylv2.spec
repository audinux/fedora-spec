# Global variables for github repository
%global commit0 3fd1dd43375d8d2ff806da8a8ce929e338d12478
%global gittag0 main
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    lv2-polylv2
Version: 0.0.1
Release: 1%{?dist}
Summary: a collection of LV2 plugins designed for modular / eurorack style use.
License: GPLv3+
URL:     https://github.com/polyeffects/PolyLV2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/polyeffects/PolyLV2/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: boost-devel

%description
Valve amplifier simulation

%prep
%autosetup -n PolyLV2-%{commit0}

%build

%set_build_flags

cd basic_modular.lv2  && %make_build STRIP=true && cd ..
cd basic_quantizer    && %make_build STRIP=true && cd ..
cd poly_chorus        && %make_build STRIP=true && cd ..
cd poly_chorus_ext    && %make_build STRIP=true && cd ..
cd poly_flange        && %make_build STRIP=true && cd ..
cd poly_flange_ext    && %make_build STRIP=true && cd ..
cd poly_harm_trem     && %make_build STRIP=true && cd ..
cd poly_harm_trem_ext && %make_build STRIP=true && cd ..
cd poly_step          && %make_build STRIP=true && cd ..
cd poly_step_bpm      && %make_build STRIP=true && cd ..
cd poly_vibrato       && %make_build STRIP=true && cd ..
cd poly_vibrato_ext   && %make_build STRIP=true && cd ..

%install 

cd basic_modular.lv2  && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd basic_quantizer    && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_chorus        && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_chorus_ext    && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_flange        && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_flange_ext    && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_harm_trem     && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_harm_trem_ext && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_step          && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_step_bpm      && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_vibrato       && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..
cd poly_vibrato_ext   && %make_install LV2DIR=/usr/%{_lib}/lv2 STRIP=true && cd ..

%files
%doc basic_modular.lv2/AUTHORS
%license basic_modular.lv2/COPYING
%{_libdir}/lv2/*

%changelog
* Fri Dec 25 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file - main / 3fd1dd43375d8d2ff806da8a8ce929e338d12478
