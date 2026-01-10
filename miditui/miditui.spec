# Status: active
# Tag: Editor, MIDI
# Type: Standalone
# Category: DAW, MIDI

%global debug_package %{nil}

Name: miditui
Version: 0.1.8
Release: 1%{?dist}
Summary: An interactive terminal app/UI for MIDI composing, mixing, and playback
License: MIT
URL: https://github.com/minimaxir/miditui
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/minimaxir/miditui/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
An interactive terminal app/UI for MIDI composing, mixing, and playback—written in Rust.
miditui allows for a DAW-like experience in the terminal and has many features that you
wouldn't expect a terminal app to have:

- Full terminal mouse support: click, drag, scroll, double-click, right-click all work,
  which allows you to pan views, select notes, click piano keys to play them
- A piano roll view for showing the notes as they are played in the song
- An Insert mode to press keys on your keyboard (or simply click the piano roll) and create
  music in real time: Two-octave QWERTY layout (Z-M and Q-I rows) with live audio playback as you type
- A project timeline view to see all the MIDI tracks with active notes at the timestep
- Low-latency 44.1kHz audio via rustysynth
- Timeline seeking by clicking the time rulers to skip to any point of the track
- Unlimited MIDI tracks with per-track mute/solo, volume/pan (L/R) controls, and automatic MIDI channel assignment
- Autosave that periodically saves your project and automatically reloads it when restarting the app
- Undo/Redo support to avoid losing work
- Import/Export MIDI and JSON files, plus export the music as a WAV file.

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
rustup-init -y --no-modify-path --default-toolchain 1.92.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.92.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/miditui %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
cp -ra examples/* %{buildroot}/%{_datadir}/%{name}/examples/

%files
%doc README.md
%license LICENSE
%{_bindir}/miditui
%{_datadir}/%{name}/examples/*

%changelog
* Sat Jan 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- Initial spec file
