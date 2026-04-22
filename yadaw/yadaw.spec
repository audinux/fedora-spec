# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

%global debug_package %{nil}

Name: yadaw
Version: 0.7.11
Release: 1%{?dist}
Summary: An sfx creation tool and midi player that doesn't crash often
License: AGPL-3.0-or-later
URL: https://github.com/mlm-games/yadaw
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mlm-games/yadaw/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: lilv-devel
BuildRequires: python3
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
A basic daw for sound effects (works on Android too, but not as functional). Is also pretty lightweight (<20mb)

Current intention is to not fill the app with patches for outdated/non-standardised parts, and to keep it minimal;
helps refactoring later on, might implement a plugin system like blender if needed (for example, midi controller
lanes feature could be implemented as a plugin, etc..)

%prep
%autosetup -n %{name}-%{version}

%build

# Remove file because it defines an incompatible compiler
rm .cargo/config.toml

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.92.0-x86_64-unknown-linux-gnu
# rustup-init -y --no-modify-path --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain 1.92.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.92.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/yadaw %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp others/packaging/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.github.mlm_games.yadaw.svg

# Write desktop file
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp others/flathub/io.github.mlm_games.yadaw.desktop %{buildroot}/%{_datadir}/applications/

# Install metainfo file
install -m 755 -d %{buildroot}/%{_datadir}/metainfo/
cp others/flathub/io.github.mlm_games.yadaw.metainfo.xml %{buildroot}/%{_datadir}/metainfo/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/io.github.mlm_games.yadaw.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mlm_games.yadaw.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.mlm_games.yadaw.metainfo.xml

%files
%doc README.md quick_start.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/metainfo/*

%changelog
* Tue Apr 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.11-1
- update to 0.7.11-1

* Mon Apr 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.10-1
- update to 0.7.10-1

* Sun Apr 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.8-1
- update to 0.7.8-1

* Tue Apr 14 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.6-1
- Initial spec file
