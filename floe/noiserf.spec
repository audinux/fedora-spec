# Status: active
# Tag: Effect
# Type: Plugin, CLAP
# Category: Audio, Effect

%global debug_package %{nil}
%global zig_version 0.13.0

Name: noiserf
Version: 0.7.0
Release: 1%{?dist}
Summary:  High quality noise reduction plugin
License: GPL-3.0-or-later
URL: https://github.com/floe-audio/NoiseRF
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/floe-audio/NoiseRF/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://ziglang.org/download/%{zig_version}/zig-linux-x86_64-%{zig_version}.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: wget
BuildRequires: git
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel

%description
This is a fork of Luciano Dato's noise reduction library
libspecbleach and LV2 plugin, noise-repellent.
It's licensed under LGPLv3.
As of writing this (April 2024), the original version is
not maintained, and has tricky dependencies for compiling
on all 3 OS. This version differs from the original library
and plugin in the following ways:
- It is a CLAP plugin instead of LV2 (still supports Linux, macOS, and Windows)
- Exposes a few more parameters in the plugin
- It uses pffft instead of fftw3
- It uses Zig for the build system allowing for simple compilation across
  all platforms
- There is no adaptive mode
- Adds support for loading noise profiles that have a different sample rate
  than the audio being processed (often happens when rendering out of a DAW).
- It fixes state saving (issue)
- It fixes input latency (issue1, issue2)
- The library code (libspecbleach) and plugin code (noise-repellent) are in a
  single repository - this was just done for convenience

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n NoiseRF-%{version}

tar xvfJ %{SOURCE1}
mv zig-linux-%{_arch}-%{zig_version} zig-bin

git config --global user.email "yc@example.com"
git config --global user.name "Yann Collette"

git init .
git add .
git commit -m "init"
git tag %{version}

%build

%set_build_flags

zig-bin/zig build install

%install

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr zig-out/x86_64-linux/* %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md 
%license LICENSE

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Jan 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
