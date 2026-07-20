# Status: active
# Tag: Editor, Live
# Type: Standalone, Language
# Category: Audio, Programming

%global debug_package %{nil}

Name: cagire
Version: 0.1.9
Release: 1%{?dist}
Summary: Forth music sequencer for live coding
License: GPL-3.0-or-later
URL: https://git.raphaelforment.fr/BuboBubo/Cagire
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.raphaelforment.fr/BuboBubo/Cagire/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: clang
BuildRequires: pipewire-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
Cagire is a terminal step sequencer for live coding, where every step in a pattern is a small Forth program that
is compiled and played in real time. It bundles a complete synthesis and sampling engine, so nothing else is
needed to make sound: oscillators, FM, Karplus-Strong, drum models, samplers, filters, effects, and bus sends
are all built in and controlled from the same stack-based, generative language. It runs in the terminal or as
a desktop window on macOS, Linux, and Windows, and synchronises with other software and hardware over MIDI
and Ableton Link.

%prep
%autosetup -n cagire

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

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/cagire %{buildroot}/%{_bindir}/

%files
%doc README.md docs/* demos/*
%license LICENSE
%{_bindir}/*

%changelog
* Mon Jul 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.9-1
- Initial spec file
