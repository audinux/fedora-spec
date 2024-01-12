# Tag: Audio, AI
# Type: Plugin, LV2
# Category: Audio, Tool

Name: lv2-aidadsp
Version: 0.95
Release: 1%{?dist}
Summary: Aida DSP's audio plugins in lv2 format
License: GPL-3.0-or-later
URL: https://github.com/moddevices/aidadsp-lv2

# Usage: ./aidadsp-lv2-source.sh <TAG>
#        ./aidadsp-lv2-source.sh v0.95

Source0: aidadsp-lv2.tar.gz
Source1: aidadsp-lv2-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: eigen3-devel
BuildRequires: lv2-devel

%description
Aida DSP's audio plugins in lv2 format

%prep
%autosetup -n aidadsp-lv2

%build

#    RTNEURAL_ENABLE_AARCH64 specific option for aarch64 builds
#    RTNEURAL_XSIMD=ON or RTNEURAL_EIGEN=ON to select an available backend for RTNeural library

%set_build_flags
export CXXFLAGS="-fPIC $CXXFLAGS"

%ifarch aarch64
%cmake -DRTNEURAL_EIGEN=ON -DRTNEURAL_ENABLE_AARCH64=ON
%else
%cmake -DRTNEURAL_EIGEN=ON
%endif
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
mv %{buildroot}/rt-neural-generic.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Thu Mar 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.95-1
- Initial creation
