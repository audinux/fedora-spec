# Status: active
# Tag: Editor, Live
# Type: Standalone, Language
# Category: Audio, Programming

%global debug_package %{nil}
%global commit0 ffa48cfb8883339d9d71a4f02a0b6965d12a776d

Name: sova
Version: 0.1.1
Release: 1%{?dist}
Summary: A polyglot sequencer and virtual machine for music live coding
License: AGPL-3.0-or-later OR MIT
URL: https://github.com/sova-org/sova
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/sova-org/Sova/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: sova-0001-Fix-solo-tui-fails-to-build-after-Snapshot-struct-ga.patch

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: clang
BuildRequires: git
BuildRequires: pipewire-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: dbus-devel
BuildRequires: fontconfig-devel
BuildRequires: python3
BuildRequires: desktop-file-utils

%description
Sova is a sequencer and musical programming environment written in Rust.
It is built on a virtual machine designed for real-time musical improvisation through code,
supporting multiple programming languages concurrently — each offering a different way to
think about musical expression. Sova is free and open-source software, built for artists,
students, researchers and developers.
Features:
- Precision: Two-thread execution model — a scheduler running ~30ms ahead of real time and
  a world thread at real-time priority with microsecond-accurate dispatch. Tightly coupled
  with Ableton Link for tempo synchronization.
- Languages: Ships with four languages — Bob (imperative), BaLi (Lisp-like),
  Boinx (pattern streams) and Cagire (stack-based). Compiled or interpreted, all sharing
  the same VM and I/O. Extensible via a single trait.
- Sequencer: A timeline of Lines (parallel tracks) and Frames (sequential steps).
  Per-line speed, loop boundaries, multiple execution modes.
  Compose structured pieces or improvise freely.
- Multiplayer: TCP client-server architecture with shared scene editing, real-time peer
  awareness and integrated chat. Start a session, anyone on the network can join.
- Protocols: MIDI I/O (16 device slots, notes/CC/bend/sysex/transport), OSC with
  timetag-accurate scheduling, SuperDirt integration.
  Per-device latency compensation.
- Audio: Built-in Doux engine — oscillators, filters, effects, sample playback with
  slicing and stretching. Also compatible with SuperDirt and Dough.
- Visuals: Built-in GLSL shader editor with real-time compilation.
- Modular: VM, server and clients are separate components. Use the whole system or just
  the parts you need.

%prep
%autosetup -p1 -n Sova-%{commit0}

git clone -b v0.0.32 https://github.com/sova-org/doux ../doux

sed -i -e "s|Categories=Audio;Music;Development;|Categories=Audio;AudioVideo;|g" ./desktop/assets/sova.desktop

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
rustup-init -y --no-modify-path --default-toolchain 1.98.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.98.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build -p sova-desktop --release # desktop client (release)
cargo build -p sova-server --release  # server (release)
cargo build -p solo-tui --release     # TUI client (release)

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/sova-frontend %{buildroot}/%{_bindir}/
install -m 755 target/release/sova_server %{buildroot}/%{_bindir}/
install -m 755 target/release/solo-tui %{buildroot}/%{_bindir}/

# install server elements
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/server/
cp -ra server/assets/* %{buildroot}/%{_datadir}/%{name}/server/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 desktop/assets/Sova.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 desktop/assets/sova.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md desktop/docs/en/*
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/server/*
%{_datadir}/applications/sova.desktop
%{_datadir}/pixmaps/sova.ico

%changelog
* Mon Jul 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.9-1
- Initial spec file
