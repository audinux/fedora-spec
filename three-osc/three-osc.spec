# Status: active
# Tag: Synthesizer
# Type: Plugin, LV2
# Category: Audio, Synthesizer

%global debug_package %{nil}

Name: three-osc
Version: 0.2.0
Release: 1%{?dist}
Summary: LV2 clone of Triple Oscillator with extended feature set
License: GPL-3.0-or-later
URL: https://github.com/Madadog/three_osc
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Madadog/three_osc/archive/refs/tags/v0.2.0.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel

%description
An LV2 synthesizer based on Triple Oscillator, a polyphonic
subtractive synthesizer with three oscillators that can modulate
each other in various ways.

Extends the original with several useful QOL features, including
bandlimited synthesis by default, unison with many detuned voices,
and legato.

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n three_osc-%{version}

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

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp target/release/libthree_osc.so three_osc.lv2
cp -ra three_osc.lv2 %{buildroot}/%{_libdir}/lv2/

%files -n lv2-%{name}
%doc README.md
%license LICENSE.txt
%{_libdir}/lv2/*

%changelog
* Thu Sep 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
