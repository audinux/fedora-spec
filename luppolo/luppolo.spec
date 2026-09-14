# Status: active
# Tag: Jack, Loop
# Type: Standalone
# Category: Audio, Sequencer

%global debug_package %{nil}

Name: luppolo
Version: 0.1.3
Release: 1%{?dist}
Summary: A looper for Linux
License: MIT
URL: https://codeberg.org/n_malo/Luppolo
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/n_malo/Luppolo/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: libappstream-glib

%description
A real-time, multi-track audio looper for guitar (or any instrument), built for Linux on top of PipeWire/JACK.
Record a phrase, loop it, and keep layering more tracks on top — in the style of Loopy HD, but as a desktop
app instead of an iPad app.

%prep
%autosetup -n %{name}

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
install -m 755 target/release/luppolo %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 assets/icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 flatpak/page.codeberg.n_malo.Luppolo.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/page.codeberg.n_malo.Luppolo.desktop

# Install the metainfo file
install -m 755 -d  %{buildroot}%{_datadir}/metainfo/
install -m 644 flatpak/page.codeberg.n_malo.Luppolo.metainfo.xml %{buildroot}/%{_datadir}/metainfo/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/page.codeberg.n_malo.Luppolo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/page.codeberg.n_malo.Luppolo.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*

%changelog
* Mon Sep 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- Initial spec file
