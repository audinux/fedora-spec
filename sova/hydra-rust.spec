# Status: active
# Tag: Tool, Video, Audio
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

%global commit0 01e415c55a2c7aed575d8f70c083093f528da924

Name: hydra-rust
Version: 0.0.1
Release: 1%{?dist}
Summary: Prototype of hydra remade in Rust
License: AGPL-3.0-or-later
URL: https://github.com/sova-org/hydra-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sova-org/hydra-rust/archive/%{commit0}.tar.gz#/hydra-rust.tar.gz

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

%description
A Rust port of Hydra — the live-codable video synthesizer created by Olivia Jack. Takes Rhai scripts,
compiles them to GLSL shaders, and renders them via OpenGL. The core is a library with zero GUI
dependencies, suitable for embedding. A standalone binary is included for testing and standalone use.
Originally extracted from Sova, the polyglot live coding sequencer.

%prep
%autosetup -n %{name}-%{commit0}

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

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/hydra %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Mon Jul 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
