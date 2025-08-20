# Status: active
# Tag: Tracker, Alsa
# Type: Standalone
# Category: Audio, Sequencer

%global debug_package %{nil}

Name: chiptrack
Version: 0.5
Release: 1%{?dist}
Summary: A programmable cross-platform sequencer for the Game Boy Advance sound chip
URL: https://github.com/jturcotte/chiptrack
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jturcotte/chiptrack/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: python3
BuildRequires: clang-devel
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: desktop-file-utils

%description
A programmable cross-platform sequencer for the Game Boy Advance sound chip.

%prep

%autosetup -n %{name}-%{version}

%build

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init --no-modify-path -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
# rustup-init --no-modify-path -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env

%ifarch x86_64
rustup-init --no-modify-path -y --default-toolchain 1.77.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init --no-modify-path -y --default-toolchain 1.77.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp -vfr target/release/chiptrack %{buildroot}/%{_bindir}/

# Install instruments

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/instruments/
cp -r instruments/* %{buildroot}/%{_datadir}/%{name}/instruments/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp pkg/chiptrack.ico %{buildroot}/%{_datadir}/pixmaps/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -m 644 pkg/128x128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 pkg/256x256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A programmable cross-platform sequencer for the Game Boy Advance sound chip
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

%files
%doc README.md
%license LICENSE-MIT LICENSE-GPL
%{_bindir}/*
%{_datadir}/%{name}/instruments/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*

%changelog
* Wed Aug 20 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
