# Status: active
# Tag: Effects, Overdrive, Flanger, Analyzer
# Type: Plugin, VST3
# Category: Effect

Name: rokerpack
Version: 1.0.0
Release: 1%{?dist}
Summary: A set of VST3 guitar plugins and tuners
License: Unlicense
URL: https://github.com/psemiletov/rokerpack
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/psemiletov/rokerpack/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
ROKER PACK — a set of guitar VST3 plugins for both Linux and Windows.
Guitar pedal effects from Bedroom Studio ARE NOT emulation of famous Boss DS-1,
Boss Overdrive or Ibanez Tube Screamer. My effort is to create its own, specific sound,
although it can be designed after hardware analogs. As VST3 plugins,
you can use them in your preferred DAW: Ardour, Reaper, Muse, Cubase and others.
Bronza:
- The plain fuzz pedal with two parameters — Level and Fuzz. Sounds like in the sixties.
Grelka Overdrive:
- The classic overdrive. Has Drive, Level, Lows and Treble parameters to define the sound.
Metalluga:
- The hard and crisp distortion with five controls to customize the effect for your needs: Gate, Drive, Level.
Mistral:
- Old-fashioned flanger with warm sound.
Charm:
- Simple, one-parameter saturator to add some warmth. BTW, it is built into Metalluga at the end of the chain.
GuitarTuner:
- Tuner for six-string guitar with note display, frequency readout, and fretboard visualization.
For best results with the tuner:
- Tune from the thinnest string (E4) to the thickest (E2) - this completely eliminates the influence of residual vibrations from thicker strings.
- If tuning from E2 to E4, mute already tuned strings with your hand before tuning the next string.
BassTuner:
- Tuner for bass guitar with note display, frequency readout, and fretboard visualization.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: Unlicense

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: Unlicense
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/BassTuner_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Bronza_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Charm_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Grelka_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/GuitarTuner_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Metalluga_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Mistral_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Tembr_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files -n license-%{name}
%doc README.md docs/*
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Apr 23 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
