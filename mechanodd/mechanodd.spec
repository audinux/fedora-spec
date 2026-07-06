# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3
# Category: Synthesizer

Name: mechanodd
Version: 0.3.0
Release: 1%{?dist}
Summary: MechanOdd is a polyphonic physical-modelling synthesizer plugin
License: GPL-2.0-or-later
URL: https://github.com/odoare/Mechanodd
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./mechanodd-source.sh <TAG>
#        ./mechanodd-source.sh v0.3.0

Source0: Mechanodd.tar.gz
Source1: mechanodd-source.sh

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
MechanOdd is a polyphonic physical-modelling synthesizer plugin.
It synthesizes sound by exciting simulated mechanical resonators
(strings, plates, membranes, and beams) and routing the results
through a feedback matrix, effects chains, and a modulation engine.

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
%autosetup -n Mechanodd

sed -i -e "s|add_subdirectory(../JUCE JUCE)|add_subdirectory(JUCE)|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/MechanOdd_artefacts/Release/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/MechanOdd_artefacts/Release/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md doc/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Mon Jul 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update to 0.3.0-1

* Fri Jul 03 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
