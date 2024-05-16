# Tag: Controller
# Type: Standalone
# Category: Audio, Tool

%global debug_package %{nil}

Name: equis
Version: 0.6.3
Release: 1%{?dist}
Summary: The hackable DJ Mixer inspired by the playdifferently model 1
License: GPL-3.0-or-later
URL: https://codeberg.org/obsoleszenz/equis
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/obsoleszenz/EQUIS/archive/main.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: rustup
BuildRequires: pkgconfig(jack)

%description
This is a 8 Channel DJ Mixer built on top of JACK. It's EQ is inspired
by the Playdifferently Model1 and offers per channel a highpass, lowpass
and sculpt eq. Two channels can be used as send/return channels for effects.
Also you can assign every channel to one of two SubFilters that are
modeled after the Xone:96 DUAL VCF Filters. EQUIS offers 2 seperate CUE
systems for pre-listening the different channels or main signal on headphones.

This project is meant to be extended and played around with.
It should be easy to tweak the filters/eqs, change the midi mapping or
embed this in your own application.

%prep
%autosetup -n equis

%build

export RUSTFLAGS="-g -O"
export RUST_BACKTRACE=1

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
# rustup-init -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/

cp -ra target/release/equis %{buildroot}/%{_bindir}/

%files
%doc README.md NOTES.md
%license LICENSE.md
%{_bindir}/*

%changelog
* Thu Feb 15 2024 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Tue Oct 17 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2-1

* Mon Oct 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-1
- update to 0.6.1-1

* Fri Oct 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Thu Oct 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Tue Sep 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
