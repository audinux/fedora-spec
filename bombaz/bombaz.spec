# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name: bombaz
Version: 1.0.0
Release: 1%{?dist}
Summary: Simple bass synth VSTi based on window function synthesis
License: GPL-3.0-or-later
URL: https://github.com/hollance/bombaz
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hollance/bombaz/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: bombaz-0001-fix-flags.patch

# Build with JUCE-8

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: JUCE
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

Requires: license-%{name}

%description
Monophonic bass synth VST plug-in based on Window Function synthesis.
It's particularly useful for adding sub-bass layers.

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Bombaz_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Bombaz_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Feb 27 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
