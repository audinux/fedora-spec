# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3, CLAP
# Category: Audio, Synthesizer

Name: terrain
Version: 1.2.2
Release: 2%{?dist}
Summary: Open Source Wave Terrain Synth 
License: GPL-3.0-or-later
URL: https://github.com/aaronaanderson/Terrain
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./terrain-source.sh <TAG>
#        ./terrain-source.sh 1.2.2

Source0: Terrain.tar.gz
Source1: terrain-source.sh

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

Requires: license-%{name}

%description
Terrain is a Wave Terrain Synthesis instrument plugin.

In wave terrain synthesis, a sound is produced via a 2D trajectory scanning over a 3D surface,
or terrain. The timbre produced is dependent on the shape and parameters of the trajectory,
as well as the shape of the scanned terrain.

In Terrain, both the trajectory and terrain parameters may me modified at audio rate.
To achieve this level of modification, both the trajectory and terrain are calculated per sample.
This comes at the cost of computation time; Terrain is a computationally expensive synthesizer.

In a simple case, an elliptical orbit scans a sinusoidal terrain. Introducing higher frequency
sinusoids into the terrain introduces more harmonics into the resulting signal.
The same goal may be accomplished by increasing the size of the trajectory.

If I adjust the modifier parameter on the trajectory, the ellipse will become narrow.
In this narrow state, changes in phase and the balance of harmonics may be heard as the
trajectory is rotated. This becomes more obvious on more complex terrains.

Translation of the trajectory also has a substantial impact on the resulting signal.
The peaks and troughs traversed by the trajectory determine the output; translation adjust which
peaks and troughs are traversed, and when this traversal happens relative to the trajectory's phase.

A trajectory that remains in the same location, and is otherwise unmodified, will create a static
timbre. However, moving this otherwise static trajectory will create time-varying timbre.
To this affect, I've added a modifier I've named Meanderance. This allows trajectories to displace
about the terrain on their own accord. Both the speed and the scale of this meanderance can be
controlled and automated.

A novel feature of terrain is the recursive trajectory feedback loop. In a similar manner to
an audio feedback loop, the trajectory position feeds back onto itself over a determined amount of time.
This effect will drastically modify the shape of a given trajectory. The problem of feedback explosion
is even more pronounced with a two-dimensional signal. To remedy this, I developed a spatial compressor
that keeps the signal within the bounds of a determined radius.

All trajectories delivered with Terrain are periodic. In other words, the shape of the trajectory
repeats itself at a given frequency. This is musically useful as the fundamental frequency may be
determined and mapped to a keyboard or piano roll. While there are many trajectories to choose,
I'll leave exploring them as an exercise to the user.

A terrain may be chosen from the given list; each with their own parameters. I will once again
leave exploring this list as an exercise to the user. In addition to the specialized terrain
parameters, each terrain may be freely saturated. The effect of this is very similar to
traditional wave shaping.

The envelope generator mimics an analog style. The ES toggle determines whether or not the envelope
will effect the size of the trajectory. This allows the brightness of the output signal to follow
the loudness; a characteristic found in many acoustic instruments.

Given the flexibility of trajectory behavior and terrain shape, alias frequencies are nearly
impossible to predict and therefore cannot be prevented at the source. Anti-aliasing in Terrain is
thus handled by oversampling. Be wary of using high oversampling factors for live performance as
this method of alias reduction comes at a great computational cost.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n Terrain

sed -i -e "/Wall/d" clap-juce-extensions/clap-libs/clap/CMakeLists.txt
sed -i -e "/Wall/d" glm_module/glm/test/CMakeLists.txt
sed -i -e "/-Werror/d" glm_module/glm/test/CMakeLists.txt

%build

%set_build_flags

export CXXFLAGS="-Wno-error=sign-conversion $CXXFLAGS"
export CXXFLAGS="-Wno-error=float-equal $CXXFLAGS"
export CXXFLAGS="-Wno-error=write-strings $CXXFLAGS"
export CXXFLAGS="-Wno-error=sequence-point $CXXFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/WaveTerrainSynth_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/WaveTerrainSynth_artefacts/CLAP/*  %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/WaveTerrainSynth_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Sep 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-2
- update to 1.2.2-2 - remove unused dep

* Mon Nov 04 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- Initial spec file
