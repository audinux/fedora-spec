# Status: active
# Tag: Tool, Video, Audio
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

%global commit0 beafc79a070aa84cec785423ed41dda247dbd1e6

Name: hydra-rust
Version: 0.0.1
Release: 8%{?dist}
Summary: Prototype of hydra remade in Rust
License: AGPL-3.0-or-later
URL: https://github.com/sova-org/hydra-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/hydra-rust/archive/%{commit0}.tar.gz#/hydra-rust.tar.gz
Source1: hydra-examples.tar.gz
Source2: http://ycollette.free.fr/Guitare/hydra-sketches.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: clang-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: libv4l-devel
BuildRequires: python3

Requires: (ffmpeg or ffmpeg-free)

%description
A Rust port of Hydra — the live-codable video synthesizer created by Olivia Jack. Takes Rhai scripts,
compiles them to GLSL shaders, and renders them via OpenGL. The core is a library with zero GUI
dependencies, suitable for embedding. A standalone binary is included for testing and standalone use.
Originally extracted from Sova, the polyglot live coding sequencer.
Some shortcuts:
- Ctrl/Cmd + Enter         Evaluate the current sketch
- Ctrl/Cmd + S             Save the current sketch to a .hydra file
- Ctrl/Cmd + O             Open a .hydra file
- Ctrl/Cmd + Shift + H     Toggle editor visibility (hide the code overlay, keep the visuals running)
- Tab                      Toggle the options sidebar — tempo/font/text-opacity, camera status, and the scene-bank grid (see below)
- Alt + 0-9 / A-F          Recall slot 0-F (hex) in the active bank — loads and immediately evaluates its saved code
- Alt + Shift + 0-9 / A-F  Save the editor's current code into that slot
- Alt + -> / <-            Cycle to the previous/next scene bank
- Alt + X                  Export the active bank (16 slots) as a .bhr file
- Alt + I                  Import a .bhr file into the active bank, replacing its 16 slots

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

cargo build --release --features webcam,audio,image_url,midi,video

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/hydra %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cd %{buildroot}/%{_datadir}/%{name}/
tar xvfz %{SOURCE1}
tar xvfz %{SOURCE2}

%files
%doc README.md CHANGELOG.md SPEC.md DOCUMENTATION.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/hydra-examples/*
%{_datadir}/%{name}/hydra-sketches/*

%changelog
* Wed Sep 16 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-8
- update to 0.0.1-8 - update to last master - add documentation

* Tue Sep 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-7
- update to 0.0.1-7 - update to last master - add video + fixes

* Mon Sep 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6
- update to 0.0.1-6 - update to last master - add midi + image_url

* Sun Sep 13 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 0.0.1-5 - update to last master

* Thu Sep 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 0.0.1-4 - activate audio - use fork

* Mon Sep 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3 - activate webcam

* Sun Sep 06 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - add examples

* Mon Jul 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
