# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name:    drumlabooh
Version: 0.0.4
Release: 1%{?dist}
Summary: LV2/VSTi drum machine that can use Hydrogen, SFZ, and other drumkit formats
License: GPL-3.0-only
URL:     https://github.com/psemiletov/drumlabooh

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/drumlabooh/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

%description
LV2/VSTi drum machine that can use Hydrogen,
SFZ, and other drumkit formats

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install 

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra %{__cmake_builddir}/drumlabooh_artefacts/VST3/*    %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/drumlabooh_artefacts/LV2/*     %{buildroot}/%{_libdir}/lv2/
cp %{__cmake_builddir}/drumlabooh_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Sep 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- update to 0.0.4-1

* Sat Sep 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-1
- Initial spec file
