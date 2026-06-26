# Status: active
# Tag: Distortion
# Type: Standalone, Plugin, LV2
# Category: Effect

%global debug_package %{nil}
%global commit0 250c446e07835f0743fc24e90eb54c18c35fdeee

Name: satordist
Version: 0.0.1
Release: 1%{?dist}
Summary: SatorDist is a high-performance saturation and distortion LV2 plugin
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/satordist.lv2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/satordist.lv2/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: xsimd-devel

Requires: license-%{name}

%description
SatorDist is a high-performance saturation and distortion LV2 plugin designed for professional
audio mixing and sound design.
Built entirely in C++, it leverages xsimd for ultra-fast SIMD vectorization (AVX2/AVX-512) and
integrates HIIR (Polyphase IIR Half-band filters) to provide pristine, aliasing-free oversampling.
Whether you need the gentle warmth of analog hardware or the aggressive destruction of digital
wavefolding, SatorDist delivers it with minimal CPU footprint.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}.lv2

sed -i -e "/set(LV2_INSTALL_DIR/d" CMakeLists.txt

%build

%cmake -DLV2_INSTALL_DIR=%{_libdir}/lv2/
%cmake_build

%install

%cmake_install

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Jun 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
