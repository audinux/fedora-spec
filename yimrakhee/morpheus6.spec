# Status: active
# Tag: Effect
# Type: Standalone, Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: morpheus6
Version: 0.4.7
Release: 1%{?dist}
Summary: 6-slot stereo modulation rack audio plugin
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/morpheus6
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/morpheus6/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
6-slot stereo modulation rack audio plugin (VST3 / CLAP)
Focuses on authentic vintage analog modeling combined with zero-allocation, SIMD-optimized DSP.
Key features:
- Flexible 6-Slot Routing: Seamlessly drag and drop modules to reorder the signal chain in real-time.
- BPM Sync: All rate and time parameters can be synchronized to your host DAW's tempo.
- Hardware-Accelerated UI: Custom interface running at 60FPS with dynamic waveform animations,
  completely bypassing heavy webview wrappers.
- SIMD Optimized: Core DSP is auto-vectorized stereo processing, ensuring ultra-low CPU usage.
- Allocation-Free DSP: The audio thread is lock-free and allocation-free, preventing xruns and
  dropouts in real-time environments.
The Modules:
- Chorus: Modeled after classic BBD (Bucket Brigade Device) analog chips. Features a true
  1-pole analog low-pass filter for the Warmth parameter and subtle soft-saturation drive when pushed.
- Flanger: A lush, sweeping comb filter with extreme resonance capabilities and anti-denormal protection.
- Phaser: Selectable 4-stage or 8-stage all-pass filter network with deep feedback control for classic
  vocal-like sweeps.
- Tremolo: Features a morphable LFO shape (Sine to Square) and a dedicated Harmonic Tremolo mode that
  splits and modulates high and low frequencies out of phase.
- Delay: A massive stereo delay system supporting extreme BPM sync lengths. Includes authentic Tape
  Wow (pitch drift) and true cross-feedback PingPong routing.
- UniVibe: Authentic optical bulb emulation. The Asymmetry control warps time to recreate the iconic
  "throb" and staggering capacitor frequencies of vintage 60s hardware.

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
%autosetup -n %{name}

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

cargo build --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/morpheus6.vst3/Contents/%{_target}/
cp -ra target/release/libmorpheus6.so %{buildroot}/%{_libdir}/vst3/morpheus6.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libmorpheus6.so %{buildroot}/%{_libdir}/clap/morpheus6.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/morpheus6 %{buildroot}/%{_bindir}/

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
* Mon Jul 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.7-1
- Initial spec file
