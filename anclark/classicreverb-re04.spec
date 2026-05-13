# Status: active
# Tag: Reverb
# Type: Plugin, VST3, VST, CLAP
# Category: Effect

%global commit0 2204099a3a9bcd559027e6587f913d1eb7f0ac3c

Name: classicreverb-re04
Version: 0.0.1
Release: 1%{?dist}
Summary: Reversed engineering of Kjaerhus Audio Classic Reverb, with enhancements
URL: https://github.com/AnClark/ClassicReverb-RE04
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./cetone-source.sh ClassicReverb-RE04 develop

Source0: ClassicReverb-RE04.tar.gz
Source1: cetone-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libglvnd-devel

Requires: license-%{name}

%description
Classic Reverb RE-04 is a reversed engineering of Kjaerhus Classic Reverb, a studio-quality free reverb plugin.
It sounds professional, with a flavor of vintage reverb, suitable for many applications from vocals to instruments.
It has enhanced features and a modern interface, while still retaining the charm of the original plugin.
This project is open-source and available for free, allowing users to enjoy the classic reverb sound on their
modern DAWs and operating systems.

Background

Classic Reverb was part of Classic Series by Kjaerhus Audio, a Danish company that developed audio plugins.
The original plugin was released in the early 2000s and became popular for its high-quality sound and
user-friendly interface.
However, it was discontinued in early 2010s, leaving many users without access to this beloved reverb.
Several DAWs like Acoustica Mixcraft included Classic Reverb as a built-in plugin, but it was only available
on Windows, and it only had a 32-bit VST2 version. Modern 64-bit-only DAWs and non-Windows users were left
out of the fun.
Years later, in 2026, I (AnClark Liu) decided to reverse engineer the Classic Reverb to bring it back to life.
The result is this open-source implementation that closely mimics the sound and behavior of the original plugin.
Now it's available in a modern format, compatible with today's DAWs and operating systems.

Features

- High-quality reverb algorithm that captures the essence of the original Classic Reverb.
- Bring back the original panel design and controls with modern technology.
- Multi-platform support, including Windows, macOS, and Linux.
- Multiple plugin formats, including VST 2.4, VST3, CLAP, LV2 and JACK standalone (optional).
- Advanced preset management system, allowing users to save and load their favorite reverb settings.
- Shipped with a collection of factory presets that cover common reverb styles.

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

%autosetup -n ClassicReverb-RE04

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/clap/

cp %{__cmake_builddir}/bin/ClassicReverb.clap %{buildroot}%{_libdir}/clap/
cp %{__cmake_builddir}/bin/ClassicReverb-vst2.so %{buildroot}%{_libdir}/vst/
cp -ra %{__cmake_builddir}/bin/ClassicReverb.vst3 %{buildroot}%{_libdir}/vst3/

%files -n license-%{name}
%license LICENSE
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed May 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
