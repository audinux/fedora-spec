# Status: active
# Tag: Synthesizer, Drum
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: niner
Version: 0.7.8
Release: 1%{?dist}
Summary: Monophonic analogue kick drum synthesizer
License: GPL-3.0-or-later
URL: https://github.com/hyperfocusdsp/niner
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hyperfocusdsp/niner/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A three-layer synthesized kick drum plugin with a parallel 909-style clap voice.
SUB sine, MID sine+noise, and a band-passed click TOP mix into a five-voice distortion palette,
a tilt/low/notch master EQ, and a full master bus
(RMS compressor → transformer drive → brickwall limiter → auto tube warmth). Ships with a
16-step pattern sequencer, a factory

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
rustup-init -y --no-modify-path --default-toolchain 1.88.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.88.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle niner --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp -vfr target/release/niner-standalone %{buildroot}/%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/*.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/*.clap %{buildroot}/%{_libdir}/clap/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md docs/*
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu May 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.8-1
- Initial spec file
