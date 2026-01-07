# Status: active
# Tag: Jack, MIDI, OSC
# Type: Standalone
# Category: Audio, Tool

Name: element
Version: 1.0.0b2
Release: 1%{?dist}
Summary: This is the community version of Element, a modular LV2/VST/VST3/LADSPA audio plugin host.
URL: https://github.com/kushview/Element
ExclusiveArch: x86_64 aarch64
License: GPL3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./element-source.sh <PROJECT> <TAG>
#        ./element-source.sh Element 1.0.0b2
Source0: Element.tar.gz
Source1: element-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lua-ldoc
BuildRequires: ImageMagick
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: lua-devel
BuildRequires: boost-devel
BuildRequires: ladspa-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: libcurl-devel
BuildRequires: gtk2-devel
BuildRequires: readline-devel
BuildRequires: desktop-file-utils

%description
This is the community version of Element, a modular LV2/VST/VST3/LADSPA audio plugin host.
Create powerful effects, racks and instruments by connecting nodes to one another.
Integrates with your existing hardware via standard protocols such as MIDI.

%prep

%autosetup -n Element

%build

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/element.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/element.desktop

%files
%doc README.md AUTHORS.md CODE_OF_CONDUCT.md  CONTRIBUTING.md
%license LICENSES/GPL3.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Tue Jan 06 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0b2-1
- update to 1.0.0b2-1

* Tue May 31 2022 Yann Collette <ycollette.nospam@free.fr> - 0.46.6-1
- update to 0.46.6-1

* Tue Mar 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.46.4-1
- update to 0.46.4-1

* Wed Jul 28 2021 Yann Collette <ycollette.nospam@free.fr> - 0.46.3-1
- update to 0.46.3-1

* Tue Jul 20 2021 Yann Collette <ycollette.nospam@free.fr> - 0.46.2-1
- update to 0.46.2-1

* Fri Apr 02 2021 Yann Collette <ycollette.nospam@free.fr> - 0.46.0-1
- update to 0.46.0

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 0.45.1-1
- update to 0.45.1

* Wed Oct 14 2020 Yann Collette <ycollette.nospam@free.fr> - 0.44.0-1
- Initial spec file
