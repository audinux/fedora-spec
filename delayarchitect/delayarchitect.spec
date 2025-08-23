# Status: active
# Tag: Effect, Delay
# Type: VST3
# Category: Effect

%global commit0 84e7e3d19ecb06884d5a7d9775737c31e6383fac

Name: delay-architect
Version: 0.1
Release: 2%{?dist}
Summary: A visual, musical editor for delay effects
URL: https://github.com/jpcima/DelayArchitect
ExclusiveArch: x86_64 aarch64
License: BSL-2.0

Vendor:       Audinux
Distribution: Audinux

# ./delayarchitect-source.sh <tag>
# ./delayarchitect-source.sh master

Source0: DelayArchitect.tar.gz
Source1: delayarchitect-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel

%description
A visual, musical editor for delay effects.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n DelayArchitect

sed -i -e "s|PRODUCT_NAME \"Delay Architect\"|PRODUCT_NAME \"Delay_Architect\"|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/DelayArchitect_artefacts/RelWithDebInfo/VST3//* %{buildroot}/%{_libdir}/vst3/

%files -n vst3-%{name}
%doc README.md
%license LICENSE.BSD-2-Clause LICENSE.GPL-3.0-or-later LICENSE.OFL-1.1
%{_libdir}/vst3/*

%changelog
* Sat Aug 23 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to 0.1-2 - remove unused dep

* Thu Feb 17 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
