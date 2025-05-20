# Status: active
# Tag: Editor, Sequencer, Tool
# Type: Standalone
# Category: DAW

%global debug_package %{nil}

Name: tek
Version: 0.2.2
Release: 1%{?dist}
Summary: A music making program for 24-bit unicode terminals
License: GPL-3.0-or-later
URL: https://codeberg.org/unspeaker/tek
ExclusiveArch: x86_64

# aarch64 -> rust lilv crate build broken for now

Vendor:       Audinux
Distribution: Audinux

# Usage: ./tek-source.sh <TAG>
#        ./tek-source.sh 0.2.2

Source0: tek.tar.gz
Source1: tek-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: lilv-devel
BuildRequires: serd-devel
BuildRequires: sord-devel
BuildRequires: freetype-devel
BuildRequires: clang-devel

%description
A music making program for 24-bit unicode terminals.
Written in rust with ratatui on crossterm for jack and pipewire.

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
install -m 755 target/release/tek %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Tue May 20 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- Initial spec file
