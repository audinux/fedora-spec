# Status: active
# Tag: Effect
# Type: Plugin, Standalone, VST, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: rusty-amp
Version: 0.2.14
Release: 1%{?dist}
Summary: Guitar rig in your terminal with external plugins support
License: Apache-2.0
URL: https://github.com/danylokravchenko/rusty-amp
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/danylokravchenko/rusty-amp/archive/refs/tags/v0.2.14.tar.gz#/%{name}-%{version}.tar.gz

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
A complete guitar amp and pedalboard rig that runs right in your terminal.
Plug in your guitar, pick an amp, and play. rusty-amp recreates classic tube and solid-state amplifiers,
a full board of stompbox effects, and multi-mic'd 4×12 cabinets — all driven from a fast, keyboard-only
interface with live metering. It ships with artist-inspired presets, so you can dial in a great tone in
seconds and tweak from there.

%prep
%autosetup -n %{name}-%{version}

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
install -m 755 target/release/rusty-amp %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra examples %{buildroot}/%{_datadir}/%{name}/
cp -ra presets %{buildroot}/%{_datadir}/%{name}/

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/examples/*
%{_datadir}/%{name}/presets/*

%changelog
* Sun Aug 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.14-1
- Initial spec file
