# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

%global commit0 fa52c4410aad470346fecc35b9b03100207199e5

Name: xenos
Version: 1.0.1
Release: 1%{?dist}
Summary: Xenos: Xenharmonic Stochastic Synthesizer
License: GPL-3.0-or-later
URL: https://github.com/raphaelradna/xenos
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./xenos-source.sh <TAG>
#        ./xenos-source.sh main

Source0: xenos.tar.gz
Source1: xenos-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
Xenos is a virtual instrument plug-in that implements and extends the
Dynamic Stochastic Synthesis (DSS) algorithm invented by Iannis Xenakis.
Programmed in C++ with the JUCE framework, Xenos is open-source,
cross-platform, and can be built in a number of plug-in formats.

%package -n license-%{name}
Summary: License files for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License files for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n xenos

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Xenos_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Xenos_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Jan 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Initial spec file
