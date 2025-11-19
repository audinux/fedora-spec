# Status: active
# Tag: Audio, Player
# Type: Standalone
# Category: Audio, Tool

%global commit0 67e8a15dda8cb7b5f052ade0731db3de62d82063
%global __python /usr/bin/python3

Name: karmaviz
Version: 0.0.1
Release: 1%{?dist}
Summary: Music Visualization Software for Linux
URL: https://github.com/karmatripping/KarmaViz
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/karmatripping/KarmaViz/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: python3-virtualenv
BuildRequires: python3-cython
BuildRequires: python3-setuptools
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: pyproject-rpm-macros

Requires: python3-qt5
Requires: python3-pygame
Requires: python3-moderngl
Requires: python3-sounddevice
Requires: python3-numpy
Requires: python3-cython

%description
A cutting-edge, GPU-accelerated audio visualizer for Linux with real-time GLSL
shader compilation, advanced waveform rendering, and immersive visual effects.

%prep
%autosetup -p1 -n KarmaViz-%{commit0}

%build

%pyproject_wheel

%install

%pyproject_install

%files
%doc README.md
%license LICENSE.md
%{_bindir}/*
%{_libdir}/python%{python3_version}/site-packages/__pycache__/*
%{_libdir}/python%{python3_version}/site-packages/config/*
%{_libdir}/python%{python3_version}/site-packages/modules/*
%{_libdir}/python%{python3_version}/site-packages/shaders/*
%{_libdir}/python%{python3_version}/site-packages/main.py
%{_libdir}/python%{python3_version}/site-packages/*.dist-info/*

%changelog
* Tue Nov 18 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial release
