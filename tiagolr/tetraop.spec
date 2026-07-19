# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, LV2, VST3
# Category: Synthesizer

Name: tetraop
Version: 1.0.3
Release: 1%{?dist}
Summary: A 4OP FM Wavetable Synth
License: GPL-3.0-or-later
URL: https://github.com/tiagolr/tetraop
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ripplerx-source.sh <PROJECT> <TAG>
#        ./ripplerx-source.sh tetraop v1.0.3

Source0: tetraop.tar.gz
Source1: ripplerx-source.sh

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
tetraop is a wavetable synthesizer, it is based of Ableton Operator and combines four wavetable
oscillators with phase and ring modulation. Its built using Gin and Juce.
Overall it's a well executed synth with good performance and SIMD across voices, it doesn't have
however wavetable editor or a great filter section or a preset browser etc, due to FM not playing
well with wavetables I am not sure I'll be adding new features either.
Features:
- Wavetable based synthesis
- 4 operators with FM and RM routing
- 10 predefined FM layouts
- FM and RM routing matrix
- 16 Unison voices per operator
- 5 Unison modes
- 8 Phase distortion modes
- 2 Filters with 5 types and 4 modes each
- Drag-and-drop modulation system
- Envelopes, LFOs, Macros and other modulation sources

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

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n tetraop

%build

%set_build_flags
export CXXFLAGS="-include string $CXXFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/TetraOP_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/TetraOP_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/TetraOP_artefacts/Standalone/* %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Jul 18 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-1
- Initial spec file
