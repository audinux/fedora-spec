# Status: active
# Tag: Distortion
# Type: Standalone, Plugin, LV2
# Category: Effect

%global debug_package %{nil}

Name: satordist2
Version: 0.6.5
Release: 1%{?dist}
Summary: SatorDist is a high-performance saturation and distortion LV2 plugin
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/satordist2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/satordist2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

Requires: license-%{name}

%description
SATORDIST2 is a optimized, 4-band multi-band saturator audio plugin (CLAP / VST3) built exclusively for Linux.
Designed for both creative sound mangling and surgical mastering tasks, provides zero-latency IIR processing
for mixing and precise Linear-phase FIR processing for mastering, alongside independent Mid/Side routing
per band.
PLATFORM SUPPORT NOTICE:
The source code will not compile on Windows or macOS. SATORDIST2 utilizes Linux-specific kernel features to prevent
page faulting in the audio thread and aggressive Linux-native compiler flags to achieve ultra-low latency and maximum
CPU efficiency.
Key features:
- 4-Band Precision Crossover: Fixed-band architecture (Low, Low-Mid, High-Mid, High) utilizing Linkwitz-Riley 4th order (LR4) filters with perfect phase alignment.
- Saturation Algorithms: Ranging from subtle Symmetric Tubes to aggressive Sine Wavefolders and Chebyshev harmonic generators.
- Per-Band Mid/Side Routing: Process Stereo, Mid-only, or Side-only signals independently for each band without breaking the SIMD pipeline.
- Dual Processing Modes:
  - CHARACTER Mode: Zero-latency Minimum-phase IIR oversampling. Retains analog punch and transients.
  - MASTERING Mode: Linear-phase FIR polyphase oversampling with Kaiser-windowed coefficients for pristine top-end and -100dB aliasing rejection. Master-bus safe soft-knee limiting.

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
# rustup-init -y --no-modify-path --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
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

# Build jack standalone
cargo build --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/satordist2.vst3/Contents/%{_target}/
cp -ra target/release/libsatordist2.so %{buildroot}/%{_libdir}/vst3/satordist2.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libsatordist2.so %{buildroot}/%{_libdir}/clap/satordist2.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/satordist2 %{buildroot}/%{_bindir}/

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
* Mon Jul 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- Initial spec file
