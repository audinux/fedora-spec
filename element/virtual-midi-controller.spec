# Status: active
# Tag: Keyboard
# Type: Standalone
# Category: Audio, MIDI

Name: virtual-midi-controller
Version: 0.0.1
Release: 1%{?dist}
Summary: A software MIDI controller which can send MIDI to any input device
URL: https://github.com/kushview/virtual-midi-controller
ExclusiveArch: x86_64 aarch64
License: GPL3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./element-source.sh <PROJECT> <TAG>
#        ./element-source.sh virtual-midi-controller main
Source0: virtual-midi-controller.tar.gz
Source1: element-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils

%description
A software MIDI controller which can send MIDI to any input device.

%prep

%autosetup -n virtual-midi-controller

%build

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/virtual-midi-controller.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/virtual-midi-controller.desktop

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/applications/virtual-midi-controller.desktop
%{_datadir}/icons/hicolor/512x512/apps/virtual-midi-controller.png

%changelog
* Wed Jan 07 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- First version of the spec
