# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: openwurli
Version: 0.4.0
Release: 1%{?dist}
Summary: An audio plugin attempting to recreate the Wurlitzer 200A sound with circuit & physics modeling
License: GPL-3.0-or-later
URL: https://github.com/hal0zer0/openwurli
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hal0zer0/openwurli/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: python3

Requires: license-%{name}

%description
OpenWurli models the complete analog signal chain of a Wurlitzer 200A electric piano
from first principles — no samples, no impulse responses, no curve-fitted approximations.
Every stage is derived from the actual circuit schematic and validated against SPICE
simulations. Which, by the way, was REALLY REALLY HARD.
That's probably why there are so few decent Wurlitzer style plugins out there.
We learned (the hard way, after several false starts) that you cannot come close to
approximating the sound of a Wurli without modeling EVERYTHING that makes it sound
the way it does.
We drew from the real 200A schematic diagram to model every resistor, every diode,
even the little 4x8 ceramic cone speakers.
As far as we can tell, this is both the most accurate and best sounding open source
Wurli EP plugin in existence. Though there's still room for improvement.

The signal chain:
* Modal reed oscillator — 7-mode synthesis with per-note frequency ratios, decay rates, and inharmonicity from Euler-Bernoulli beam theory
* Electrostatic pickup — capacitive 1/(1-y) nonlinearity (the primary source of Wurlitzer "bark") with RC high-pass filter
* Hammer model — Gaussian dwell filter, register-dependent onset ramp, impact noise burst
* DK method preamp — coupled 8-node Modified Nodal Analysis with Newton-Raphson solving, modeling the 200A's two-stage direct-coupled NPN amplifier
* Tremolo — LDR feedback modulation inside the preamp loop (timbral, not just volume)
* Power amplifier — closed-loop negative feedback NR solver with Gaussian crossover distortion and tanh soft-clip rail saturation
* Speaker cabinet — HPF/LPF with Hammerstein polynomial nonlinearity, tanh excursion limiting, and thermal voice coil compression

Features:
* Physically accurate sound derived from component-level circuit analysis
* Full 64-voice polyphony (matches real 200A's 64 keys) with voice stealing and crossfade
* 2x oversampled preamp processing (bypassed at >= 88.2 kHz host rates)
* Tremolo that modulates timbre (not just amplitude), matching the real 200A topology
* Per-note MLP corrections trained on real Wurlitzer recordings (experimental)
* Per-note variation in tuning and amplitude (no two notes sound identical)
* Per-mode frequency jitter to break digital coherence
* CLAP and VST3 plugin formats

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

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
# rustup-init -y --no-modify-path --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle openwurli --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra target/bundled/openwurli.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/bundled/openwurli.clap %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/

%files -n clap-%{name}
%{_libdir}/clap/

%changelog
* Tue Mar 31 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update to 0.4.0-1

* Sun Mar 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to 0.3.1-1

* Sat Mar 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update to 0.3.0-1

* Wed Mar 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- Initial spec file
