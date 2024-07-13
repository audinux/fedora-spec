# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Distortion

Name: dexed
Version: 0.9.7
Release: 1%{?dist}
Summary: DX7 FM multi plaform/multi format plugin
License: GPL-3.0-or-later
URL: https://github.com/asb2m10/dexed
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./dexed-source.sh <TAG>
#        ./dexed-source.sh v0.9.7

Source0: dexed.tar.gz
Source1: dexed-source.sh

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
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Under the hood it uses music-synthesizer-for-android for the synth engine and JUCE as an
application/plugin wrapper.

The goal of this project is to be a tool/companion for the original DX7. Sound engine with
'float' value parameters, different waveform à la TX81z would be great but anything that
goes beyond the DX7 should and will be a fork of this project. This is to keep the
compatibility with the original machine.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n dexed

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Source/Dexed_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Source/Dexed_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra %{__cmake_builddir}/Source/Dexed_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Jul 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.7-1
- update to 0.9.7-1

* Sat Jun 22 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.6-1
- Initial spec file
