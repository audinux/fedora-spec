# Status: active
# Tag: Jack, Synthesizer, Modular
# Type: Plugin, Standalone, VST, VST3, CLAP
# Category: Audio, Synthesizer

%global debug_package %{nil}

Name: songrec
Version: 0.7.4
Release: 1%{?dist}
Summary: An open-source Shazam client for Linux.
License: GPL-3.0-or-later
URL: https://github.com/marin-m/SongRec
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/marin-m/SongRec/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: libadwaita-devel
BuildRequires: pipewire-devel
BuildRequires: (ffmpeg-devel or ffmpeg-free-devel)
BuildRequires: clang-devel
BuildRequires: libsoup3-devel
BuildRequires: desktop-file-utils

%description
SongRec is an open-source Shazam client for Linux.

%prep
%autosetup -n SongRec-%{version}

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
rustup-init -y --no-modify-path --default-toolchain 1.88-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.88-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release --no-default-features -F gui,ffmpeg,pulse,pipewire,mpris

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/songrec %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/
cp -ra packaging/rootfs/* %{buildroot}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/*
%{_mandir}/man1/*

%changelog
* Sun Jun 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.4-1
- update to 0.7.4-1

* Thu Jun 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.3-1
- Initial spec file
