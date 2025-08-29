# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

%global debug_package %{nil}

Name: audibleplanets
Version: 1.2.3
Release: 2%{?dist}
Summary: An expressive, quasi-Ptolemaic semi-modular synthesizer
License: GPL-3.0-or-later
URL: https://github.com/gregrecco67/AudiblePlanets
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./audibleplanets-source.sh <TAG>
#        ./audibleplanets-source.sh v1.2.3

Source0: AudiblePlanets.tar.gz
Source1: audibleplanets-source.sh

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

%description
Four bodies revolve with uniform circular motion, each around one of
the others or, in the case of the first body, a fixed central point.
Each body around which no other body revolves serves as an oscillator,
producing sound. The interpretation of these terminal bodies as
oscillators depends on their positions as viewed from a point that is
either at the fixed center of revolution or nearby, at a point called
the "equant," more in honor of Ptolemy than in strict adherence to his
system (hence "quasi-Ptolemaic"). In the engine's fully modulated state
(i.e., with the "Demodulate" knob turned all the way down), only the
angle formed by a reference line and the line connecting the equant to
the terminal body matters to the sound, just as, in Ptolemy's system,
the distances of the heavenly bodies are unknown. This system of sound
generation closely resembles frequency modulation (FM) synthesis.
The relative speeds of revolution of the various bodies have their
analogues in the frequencies of so-called "carrier" and "modulator"
(or "operator") waves in traditional FM synthesis. Accordingly, the
interface allows both ("coarse") whole-number and ("fine") fractional
variation of these relative frequencies, producing a wide array of
timbres, from the pure and simple to the densely inharmonic.
Many mutually modulatable parameters are configurable by the user,
and a robust system of randomization facilitates sonic exploration
and discovery.

%package -n license-%{name}
Summary:  License and documentation fpr %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n AudiblePlanets

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/AudiblePlanets_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/AudiblePlanets_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Aug 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-2
- update to 1.2.3-2 - remove unused dep

* Sun Jun 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-1
- update to 1.2.3-1

* Thu May 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- update to 1.2.2-1

* Wed May 28 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update to 1.2.1-1

* Tue May 27 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Fri Aug 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.5-1
- update to 1.1.5-1

* Tue Jul 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-1
- update to 1.1.4-1

* Sat Jul 13 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-1
- update to 1.1.3-1

* Thu Jul 11 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.2-1
- update to 1.1.2-1

* Sun Jul 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Sun Jul 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Tue May 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.22-1
- update to 1.0.22-1

* Sat May 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.21-1
- update to 1.0.21-1

* Tue Apr 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.20-1
- update to 1.0.20-1

* Fri Apr 26 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.19-1
- update to 1.0.19-1

* Tue Apr 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.18b-1
- update to 1.0.18b-1

* Mon Apr 22 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.18a-1
- update to 1.0.18a-1

* Sun Apr 21 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.18-1
- update to 1.0.18-1

* Thu Apr 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.17-1
- update to 1.0.17-1

* Tue Apr 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.16-1
- update to 1.0.16-1

* Sun Apr 14 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.15-1
- update to 1.0.15-1

* Thu Apr 11 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-1
- update to 1.0.14-1

* Sun Apr 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.13-1
- update to 1.0.13-1

* Mon Mar 25 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.4-1
- Initial spec file
