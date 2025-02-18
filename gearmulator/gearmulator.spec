# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3, CLAP
# Category: Audio, Synthesizer

Name: gearmulator
Version: 1.4.2
Release: 1%{?dist}
Summary: Emulation of classic VA synths of the late 90s/2000s that are based on Motorola 56300 family DSPs 
License: GPL-3.0-or-later
URL: https://github.com/dsp56300/gearmulator
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gearmulator-source.sh <TAG>
#        ./gearmulator-source.sh 1.4.2

Source0: gearmulator.tar.gz
Source1: gearmulator-source.sh
Patch0: gearmulator-0002-remove-static-flags.patch

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

This project emulates various musical devices that used the Motorola 56300 family DSPs.
The supported plugin formats are VST3 and CLAP.
At the moment, the following synthesizers are supported:
- Osirus: Access Virus A,B,C
- OsTIrus: Access Virus TI/TI2/Snow
- Vavra: Waldorf microQ
- Xenia: Waldorf Microwave II/XT
- Nodal Red 2x: Clavia Nord Lead/Rack 2x

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for version of %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -p1 -n gearmulator

%build

%cmake \
    -Dgearmulator_BUILD_FX_PLUGIN=ON
    
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/clap/

cp -ra bin/plugins/Release/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra bin/plugins/Release/VST/*  %{buildroot}/%{_libdir}/vst/
cp -ra bin/plugins/Release/CLAP/* %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Feb 18 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-1
- update to 1.4.2-1

* Sat Dec 14 2024 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-1
- update to 1.4.1-1

* Tue Nov 19 2024 Yann Collette <ycollette.nospam@free.fr> - 1.4.0-1
- update to 1.4.0-1

* Fri Nov 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.21-1
- update to 1.3.21-1

* Sun Sep 08 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.20-1
- update to 1.3.20-1

* Sat Aug 31 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
