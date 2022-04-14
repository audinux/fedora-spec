# Tag: Reverb
# Type: Plugin, LV2
# Category: Audio, Effect

Name: aether
Version: 1.2.1
Release: 1%{?dist}
Summary:  An algorithmic reverb LV2 based on Cloudseed 
License: MIT
URL: https://dougal-s.github.io/Aether/

# Usage:
# ./aether-source.sh <TAG>
# ./aether-source.sh v1.2.1

Source0: Aether.tar.gz	
Source1: aether-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: libX11-devel
BuildRequires: freeglut-devel
BuildRequires: mesa-libGL-devel

%description
Aether is an algorithmic reverb LV2 plugin based on Cloudseed.

%prep
%autosetup -n Aether

%build

%set_build_flags
export CXXFLAGS="$CXXFLAGS -Wno-error=stringop-overflow"

%cmake
%cmake_build

%install

install -d 755 %buildroot/%{_libdir}/lv2/aether.lv2/
cp -r %{__cmake_builddir}/aether.lv2/* %buildroot/%{_libdir}/lv2/aether.lv2/

%files
%license LICENSE.md
%doc README.md
%{_libdir}/lv2/*

%changelog
* Sun Feb 20 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- initial version of the spec file
