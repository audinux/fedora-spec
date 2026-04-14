# Status: active
# Tag: Drum
# Type: Plugin, Standalone, VST3
# Category: Audio, Sequencer

Name: drummock
Version: 0.0.1
Release: 1%{?dist}
Summary: Simple drum sampler
License: GPL-2.0-or-later
URL: https://github.com/ameyakakade/drummock
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./drummock-source.sh <TAG>
#        ./drummock-source.sh 0.0.1

Source0: drummock.tar.gz
Source1: drummock-source.sh

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

Requires: license-%{name}

%description
A fast and simple drum sampler meant for trap/hip-hip production.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n drummock

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/AudioPluginExample_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/AudioPluginExample_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Apr 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
