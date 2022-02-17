Name:    delay-architect
Version: 0.1
Release: 1%{?dist}
Summary: A visual, musical editor for delay effects
URL:     https://github.com/jpcima/DelayArchitect
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
BuildRequires: libcurl-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: freetype-devel

%description
A visual, musical editor for delay effects.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
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
* Thu Feb 17 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
