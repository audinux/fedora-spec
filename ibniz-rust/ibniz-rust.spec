# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Programming

%global debug_package %{nil}

Name: ibniz-rust
Version: 1.0.0
Release: 1%{?dist}
Summary: A virtual machine designed for extremely compact low-level audiovisual programs.
License: MIT
URL: https://github.com/ycollet/IBNIZ-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/IBNIZ-rust/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: desktop-file-utils

%description
This is a Rust version of IBNIZ.
IBNIZ is a virtual machine designed for extremely compact low-level audiovisual programs.
The leading design goal is usefulness as a platform for demoscene productions, glitch art
and similar projects. Mainsteam software engineering aspects are considered totally irrelevant.
IBNIZ stands for Ideally Bare Numeric Impression giZmo. The name also refers to Gottfried
Leibniz, the 17th-century polymath who, among all, invented binary arithmetic, built the
first four-operation calculating machine, and believed that the world was designed with the
principle that a minimal set of rules should yield a maximal diversity.

%prep
%autosetup -n IBNIZ-rust-%{version}

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
install -m 755 target/release/ibniz %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/ibniz/examples/
cp -ra examples/* %{buildroot}/%{_datadir}/ibniz/examples/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/ibniz.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/ibniz.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp assets/ibniz.desktop %{buildroot}/%{_datadir}/applications/ibniz.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ibniz.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ibniz.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/ibniz/examples/*

%changelog
* Sat Oct 24 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
