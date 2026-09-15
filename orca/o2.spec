# Status: active
# Tag: Live, MIDI, OSC
# Type: Language
# Category: Sequencer, Programming

%global debug_package %{nil}

Name: o2
Version: 0.3.6
Release: 1%{?dist}
Summary: Rust port of the ORCΛ esoteric programming language and terminal livecoding environment
License: GPL-3.0-or-later
URL: https://github.com/coignard/o2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/coignard/o2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%description
Rust port of the ORCΛ esoteric programming language and terminal livecoding environment.

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
install -m 755 target/release/o2 %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -rav examples %{buildroot}/%{_datadir}/%{name}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp assets/orca.png %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=orca
Comment=Rust port of the ORCΛ esoteric programming language and terminal livecoding environment
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md CREDITS SECURITY.md
%license LICENSE
%{_bindir}/o2
%{_datadir}/%{name}/examples/*
%{_datadir}/applications/o2.desktop
%{_datadir}/pixmaps/orca.png

%changelog
* Tue Sep 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- Initial spec file
