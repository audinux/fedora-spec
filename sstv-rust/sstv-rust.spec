# Status: active
# Tag: Jack, Alsa
# Type: Synthesizer
# Category: Audio

%global debug_package %{nil}

Name: sstv-rust
Version: 1.2.0
Release: 1%{?dist}
Summary: Some Jack audio modules to manage SSTV transmissions.
License: MIT
URL: https://github.com/ycollet/sstv-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/sstv-rust/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Two independent Rust applications for still-image experiments.
The encoder transmits a PNG or JPEG using Robot 36 (320x240).
The receiver detects the SSTV mode from its header and displays decoded rows progressively.
It keeps listening after each image. No radio hardware is required.
This is actual SSTV timing, not video-rate playback: Robot 36 takes about 38 seconds per image
including its header, followed by two seconds of silence. Images are resized to the mode's
resolution, which can change their aspect ratio.

%prep
%autosetup -n sstv-rust-%{version}

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

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/sstv-decoder %{buildroot}/%{_bindir}/
install -m 755 target/release/sstv-encoder %{buildroot}/%{_bindir}/
install -m 755 target/release/nbtv-decoder %{buildroot}/%{_bindir}/
install -m 755 target/release/nbtv-encoder %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
install -m 644 examples/* %{buildroot}/%{_datadir}/%{name}/examples/

%files
%doc README.md PROTOCOLS.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/examples/*

%changelog
* Thu Nov 12 2026 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Thu Nov 12 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Wed Nov 11 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Tue Nov 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
