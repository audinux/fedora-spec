# Status: active
# Tag: Tool
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

Name: clap-validator
Version: 0.3.4
Release: 1%{?dist}
Summary: An automatic CLAP validation and testing tool
License: MIT
URL: https://github.com/LX-Audiolabs/clap-validator
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/LX-Audiolabs/clap-validator/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A validator and automatic test suite for CLAP plugins.
Clap-validator can automatically test one or more plugins for common bugs
and incorrect behavior.

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
cp -vfr target/release/clap-validator %{buildroot}/%{_bindir}/

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/*

%changelog
* Thu Jul 16 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- Initial spec file
