# Status: active
# Tag: Editor, Audio, MIDI, Sequencer
# Type: Standalone
# Category: DAW, MIDI

%global debug_package %{nil}

Name: soundcraft
Version: 0.11.0
Release: 1%{?dist}
Summary: An open-source, clean-room reimplementation of Avid Pro Tools in pure Rust
License: MIT
URL: https://github.com/storytold/soundcraft
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/storytold/soundcraft/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A complete digital audio workstation that runs natively Linux and in the browser.
Multitrack editing, a full mixer with plugins, sends and automation, MIDI,
recording and bouncing, and every action scriptable from the command line or by
an AI agent.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s|@VERSION@|%{version}|g" packaging/linux/ai.storyteller.soundcraft.metainfo.xml.in
sed -i -e "s|@DATE@|10192026|g" packaging/linux/ai.storyteller.soundcraft.metainfo.xml.in

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
install -m 755 target/release/soundcraft-cli %{buildroot}/%{_bindir}/
install -m 755 target/release/soundcraft-web %{buildroot}/%{_bindir}/
install -m 755 target/release/soundcraft %{buildroot}/%{_bindir}/

FORMATS="16x16 24x24 32x32 48x48 64x64 128x128 256x256 512x512"
for Format in ${FORMATS}
do
    install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/$Format/apps/
    install -m 644 assets/app-icon/hicolor/$Format/apps/ai.storyteller.soundcraft.png %{buildroot}/%{_datadir}/icons/hicolor/apps/$Format/apps/
done

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/scalable/apps/
install -m 644 assets/app-icon/hicolor/scalable/apps/ai.storyteller.soundcraft.svg %{buildroot}/%{_datadir}/icons/hicolor/apps/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 packaging/linux/ai.storyteller.soundcraft.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 packaging/linux/ai.storyteller.soundcraft.mime.xml %{buildroot}/%{_datadir}/mime/packages/

install -m 755 -d %{buildroot}/%{_datadir}/metainfo/
install -m 644 packaging/linux/ai.storyteller.soundcraft.metainfo.xml.in %{buildroot}%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ai.storyteller.soundcraft.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.soundcraft.desktop
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.soundcraft.metainfo.xml
# ../BUILD/soundcraft-0.8.0-build/BUILDROOT/usr/share/metainfo/ai.storyteller.soundcraft.metainfo.xml: FAILED:
# • tag-invalid           : stock icon is not valid [ai.storyteller.soundcraft]

%files
%doc README.md ROADMAP.md docs/*
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/*
%{_datadir}/mime/packages/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/apps/16x16/apps/*
%{_datadir}/icons/hicolor/apps/24x24/apps/*
%{_datadir}/icons/hicolor/apps/32x32/apps/*
%{_datadir}/icons/hicolor/apps/48x48/apps/*
%{_datadir}/icons/hicolor/apps/64x64/apps/*
%{_datadir}/icons/hicolor/apps/128x128/apps/*
%{_datadir}/icons/hicolor/apps/256x256/apps/*
%{_datadir}/icons/hicolor/apps/512x512/apps/*
%{_datadir}/icons/hicolor/apps/scalable/apps/*
%{_datadir}/metainfo/*

%changelog
* Wed Oct 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-1
- update to 0.11.0-1

* Tue Oct 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- update to 0.10.0-1

* Mon Oct 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- Initial spec file
