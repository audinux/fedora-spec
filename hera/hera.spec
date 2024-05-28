# Tag: Synthesizer
# Type: Plugin, VST3
# Category: Synthesizer

Name: hera
Version: 0.0.1
Release: 1%{?dist}
Summary: Juno 60 emulation synthesizer
URL: https://github.com/jpcima/Hera
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./hera-source.sh <tag>
# ./hera-source.sh f6fe5b900f4cf84809686466e0a37de5edf008fd

Source0: Hera.tar.gz
Source1: hera-source.sh

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
Juno 60 emulation synthesizer, with support of MPE.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep

%autosetup -n Hera

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Hera_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue May 28 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
