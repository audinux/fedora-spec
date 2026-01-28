# Status: active
# Tag: Sequancer
# Type: Standalone
# Category: Audio, Synthesizer

%global debug_package %{nil}
%global commit0 34a997d884aaa02706e998dd43e0b277247d9886

Name: cacophony
Version: 0.2.7
Release: 1%{?dist}
Summary: Minimalist MIDI Sequencer
License: MIT
URL: https://github.com/subalterngames/cacophony
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/subalterngames/cacophony/archive/%{commit0}.zip#/cacophony.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: speech-dispatcher-devel
BuildRequires: openssl-devel
BuildRequires: clang-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel

%description
Cacophony is a minimalist and ergonomic MIDI sequencer.
It's minimalist in that it doesn't have a lot of functionality MIDI sequencers have.
It's ergonomic in that there is no mouse input and a very clean interface, allowing
you to juggle less inputs and avoid awkward mouse motions.

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
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

export CACOPHONY_BUILD_DATA_DIR=/usr/share/%{name}/
cargo build
cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/cacophony %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
cp -ra html/* %{buildroot}/%{_datadir}/%{name}/doc/

%files
%doc README.md changelog.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/doc/*

%changelog
* Mon Jan 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.7-1
- Initial spec file
