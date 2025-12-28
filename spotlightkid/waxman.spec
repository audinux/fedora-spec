# Status: active
# Tag: Effect, Delay, Reverb
# Type: Plugin, Standalone, LV2, VST3, CLAP
# Category: Audio, Effect

Name: waxman
Version: 0.1.0
Release: 1%{?dist}
Summary: Multi-effects for guitar and bass
License: MIT
URL: https://github.com/SpotlightKid/waxman
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh waxman v0.1.0

Source0: waxman.tar.gz
Source1: spotlightkid-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: desktop-file-utils

%description
Waxman is a virtual guitar pre-amp and tone-stack comprising of a
compressor, distortion and equalizer stage. It is a multi-format,
cross-platform audio effect plugin, which can be loaded in to any DAW, which
supports one of the plugin formats listed below.

The plugin was created to emulate the kind of sounds you can get from a "Tom
Scholz Rockman", which were a series of well-known headphone practice amps
from the 80s. These were also one of the first guitar amp simulators and were
used on countless hit records in that decade and in the nineties. The plugin
does not simulate the exact circuit of a Rockman but mimics the general chain
of tone-shaping components the original had.

It does not include the chorus and echo the original had, since these effects
can be easily added with other plugins (see the audio examples below) but it
adds a noise gate with adjustable threshold after the input, since that is often
useful for distortion sounds.

The plugin can be used to create sparkly clean sounds, crunchy overdrive tones
and mild to medium-heavy distortion. Think 80s pop/hairmetal rather modern
hi-gain mayhem. The eight-band EQ allows to shape the sound drastically, so it
can better fit in a mix. In fact, the Rockman is famous for its compressed,
mid-boosted tones, that may sound strange on their own but can punch through
a busy mix or lend themselves to layering.

Note: This software is still in Beta Status and some fine-tuning of it
tone-shaping blocks may still occur. Until the first stable release comes out,
no guarantee is made that plugin presets stay compatible with the next version.
So, for now, I suggest you take screenshots of your favourite settings!

%package -n license-%{name}
Summary: License and documentation for the adt plugin.

%description -n license-%{name}
License and documentation for the adt plugin.

%package -n lv2-%{name}
Summary: LV2 version of the adt plugin.
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of the adt plugin.

%package -n vst3-%{name}
Summary: VST3 version of the adt plugin.
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of the adt plugin.

%package -n clap-%{name}
Summary: CLAP version of the adt plugin.
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of the adt plugin.

%prep
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Nov 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial version of the spec file
