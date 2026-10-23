# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Programming

%global debug_package %{nil}

Name: bytebeat
Version: 1.0.0
Release: 1%{?dist}
Summary: Bytebeat player in Rust with a collection of many formulas from around the internet.
License: MIT
URL: https://github.com/ycollet/ByteBeat
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/ByteBeat/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A standalone desktop bytebeat studio inspired by the layout and workflow of Dollchan Bytebeat Composer.
This is an independent implementation, not a web wrapper: one executable, no browser or server required.
Built-in demos work offline; the optional upstream library is downloaded automatically when no local,
installed, or cached catalog is available.

%prep
%autosetup -n ByteBeat-%{version}

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
install -m 755 target/release/bytebeat %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/data/
cp -ra data/* %{buildroot}/%{_datadir}/%{name}/data/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/bytebeat.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/bytebeat.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name} --catalog %{_datadir}/%{name}/data/catalog.json
Icon=%{name}
Comment=Bytebeat player in Rust with a collection of many formulas from around the internet
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
%doc README.md DOCUMENTATION.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/bytebeat/data/*

%changelog
* Thu Oct 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
