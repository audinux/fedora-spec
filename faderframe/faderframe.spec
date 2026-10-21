# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

%global debug_package %{nil}

Name: faderframe
Version: 0.26.0
Release: 1%{?dist}
Summary: A DAW. For Linux
License: MIT
URL: https://github.com/BurningTreeC/faderframe
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/BurningTreeC/faderframe/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: glib2-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: pango-devel
BuildRequires: cairo-gobject-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: pipewire-devel
BuildRequires: clang-devel
BuildRequires: gtk4-devel
BuildRequires: python3
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%description
A multitrack recording, editing, mixing and mastering environment written in Rust,
Wayland native, GTK 4 native.
FaderFrame aims to be a professional DAW: graph-based routing with buses, aux sends
and sidechains, hard-realtime multicore audio processing with automatic plugin delay
compensation, MIDI and virtual instruments with a key, a chord track and MIDI effects,
modulators and parallel effect containers, automation, CLAP/VST3/LV2 hosting, an
analogue-console-style mixer, a full set of stock devices, mastering meters, surround,
object-based (ADM BWF) and IAMF masters with binaural monitoring, album delivery down
to CD and vinyl masters, video for working to picture, project templates,
and dockable, detachable editors.

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
install -m 755 target/release/faderframe %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 packaging/icons/io.github.BurningTreeC.FaderFrame.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Install desktop file
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 packaging/linux/io.github.BurningTreeC.FaderFrame.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/io.github.BurningTreeC.FaderFrame.desktop

# Install metainfo file
install -m 755 -d %{buildroot}/%{_datadir}/metainfo/
install -m 644 packaging/linux/io.github.BurningTreeC.FaderFrame.metainfo.xml %{buildroot}/%{_datadir}/metainfo/

# Install mime file
install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 packaging/linux/io.github.BurningTreeC.FaderFrame.xml %{buildroot}/%{_datadir}/mime/packages/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.BurningTreeC.FaderFrame.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.BurningTreeC.FaderFrame.metainfo.xml

%files
%doc README.md
%license LICENSE THIRD_PARTY_LICENSES.md
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/*

%changelog
* Wed Oct 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.26.0-1
- update to 0.26.0-1

* Wed Oct 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.24.0-1
- update to 0.24.0-1

* Fri Oct 16 2026 Yann Collette <ycollette.nospam@free.fr> - 0.22.0-1
- Initial spec file
