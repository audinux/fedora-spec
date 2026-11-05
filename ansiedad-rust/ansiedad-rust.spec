# Status: active
# Tag: Tool, Video
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

%global commit0 b2c06f942492bbe899b05a917859b999c3645cb5

Name: ansiedad-rust
Version: 0.0.1
Release: 3%{?dist}
Summary: A Rust version of the Ansledad live visual generator program.
License: GPL-3.0-or-later
URL: https://github.com/ycollet/ansiedad-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ansiedad-rust/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

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

Requires: (ffmpeg or ffmpeg-free)

%description
A native Rust terminal port of gabochi/ANSIedad, a live-coding visual instrument inspired by bytebeat
and IBNIZ. No GUI or audio device is needed: the output is a grid of CP437-style Unicode characters
with 256-color ANSI foregrounds and backgrounds.

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
# cargo build --release

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --features gui --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/ansiedad %{buildroot}/%{_bindir}/
install -m 755 target/release/ansiedad-gui %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
install -m 644 examples/* %{buildroot}/%{_datadir}/%{name}/examples/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/ansiedad.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp assets/ansiedad.ico %{buildroot}/%{_datadir}/pixmaps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 packaging/ansiedad-gui.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ansiedad-gui.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/ansiedad-gui.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/examples/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Thu Nov 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 0.0.1-3 - update to last master

* Wed Nov 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 0.0.1-2 - update to last master

* Tue Nov 03 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
