# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

%global commit0 fd160b9af0f1c764e528aa279556c2720ec2296e

Name: thekissofshame
Version: 1.0.0
Release: 1%{?dist}
Summary: DSP Magnetic Tape Emulation
License: GPL-3.0-or-later
URL: https://github.com/hollance/TheKissOfShame

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hollance/TheKissOfShame/archive/%{commit0}.zip#/%{name}-%{version}.zip

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
The Kiss of Shame, debuted at the Audio Engineering Society Convention 2014
in Los Angeles, was a pioneering DAW plugin that leveraged commercial UX/UI
design principles to shape its magnetic tape + circuitry emulation algorithms.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n TheKissOfShame-%{commit0}

sed -i -e "s/The Kiss Of Shame/The_Kiss_Of_Shame/g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/TheKissOfShame_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp %{__cmake_builddir}/TheKissOfShame_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Apr 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
