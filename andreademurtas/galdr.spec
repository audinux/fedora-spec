# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

Name: galdr
Version: 1.1.0
Release: 1%{?dist}
Summary: Galdr is a free and open-source synthesizer plugin
License: GPL-3.0-or-later
URL: https://github.com/andreademurtas/galdr
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./andreademurtas-source.sh <PROJECT> <TAG>
#        ./andreademurtas-source.sh galdr v1.1.0

Source0: galdr.tar.gz
Source1: andreademurtas-source.sh

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
Galdr (Old Norse for a spell sung rather than spoken) is a free and open-source synthesizer
plugin (VST3, CLAP + standalone) with a black-metal soul, built with JUCE.

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n galdr

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Galdr_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Galdr_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Galdr_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md NOTICE.txt
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Aug 17 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
