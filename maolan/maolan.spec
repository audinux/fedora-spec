# Status: active
# Tag: DWA
# Type: Standalone
# Category: DAW

%global debug_package %{nil}

Name: maolan
Version: 0.0.4
Release: 1%{?dist}
Summary: Maolan is a Rust DAW focused on recording, editing, routing, automation, export, and plugin hosting
License: BSD-2-Clause
URL: https://github.com/maolan/maolan
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/maolan/maolan/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: rubberband-devel
BuildRequires: gtk2-devel
BuildRequires: python3

%description
Maolan is a Rust DAW focused on recording, editing, routing, automation, export, and plugin hosting.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
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

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/maolan %{buildroot}/%{_bindir}/

%files
%doc README.md docs/*.md
%license LICENSE
%{_bindir}/*

%changelog
* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
