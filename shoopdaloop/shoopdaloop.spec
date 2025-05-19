# Status: active
# Tag: Live, Sequencer, Editor
# Type: Standalone
# Category: Tool, Audio, DAW

%define commit0 ef5c1664e1b3324a6538dec5124e24304b23154b

Name: shoopdaloop
Version: 0.1
Release: 2%{?dist}
Summary: A (live) looping application with DAW elements.
License: GPL
URL: https://github.com/SanderVocke/shoopdaloop
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./shoopdaloop-source.sh <TAG>
#        ./shoopdaloop-source.sh ef5c1664e1b3324a6538dec5124e24304b23154b

Source0: shoopdaloop.tar.gz
Source1: shoopdaloop-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git

%description
ShoopDaLoop is a live looping application for Linux with a few DAW-like features.

%prep
%autosetup -n %{name}

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
rustup-init -y --no-modify-path --default-toolchain 1.82.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.82.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install


%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon May 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- update to 0.1-2

* Fri Oct 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version
