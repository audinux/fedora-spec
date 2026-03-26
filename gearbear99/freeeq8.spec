# Status: active
# Tag: Equalizer
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: freeeq8
Version: 2.1.0
Release: 1%{?dist}
Summary: FreeEQ8 is a professional-grade, free and open-source 8-band parametric EQ
License: GPL-3.0-or-later
URL: https://github.com/GareBear99/FreeEQ8
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gearbear99-source.sh <PROJECT> <TAG>
#        ./gearbear99-source.sh FreeEQ8 v2.1.0

Source0: FreeEQ8.tar.gz
Source1: gearbear99-source.sh

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

%description
FreeEQ8 is a professional-grade, free and open-source 8-band parametric EQ.
Linear phase, dynamic EQ, match EQ, per-band drive, band linking, M/S processing,
oversampling, and a real-time spectrum analyzer — all in a single, zero-cost plugin.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n FreeEQ8

%build

%set_build_flags

%cmake -DCMAKE_CXX_FLAGS="-DJUCE_USE_CURL=0 $CXXFLAGS"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/FreeEQ8_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/FreeEQ8_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files -n license-%{name}
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE

%files
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Mar 25 2026 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- Initial spec file
