# Tag: Tool
# Type: Standalone, Pipewire
# Category: Tool

%global debug_package %{nil}

Name: coppwr
Version: 1.5.1
Release: 1%{?dist}
Summary: Low level control GUI for the PipeWire multimedia server
License: GPL-3.0-or-later
URL: https://github.com/dimtpap/coppwr

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/dimtpap/coppwr/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: pipewire-devel
BuildRequires: clang-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%description
coppwr is a tool that provides low level control over the PipeWire multimedia server.
It aims to expose and provide as many ways to inspect and control the many aspects
of the PipeWire multimedia server as possible. It can be used as a diagnostic tool
for PipeWire and to help develop software that interacts with it.
End-users of PipeWire that want to configure it should look into simpler tools
recommended by the PipeWire devs. If you want to learn the inner workings of PipeWire
check out the docs page on its internals and its wiki.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
# rustup-init -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --default-toolchain=1.76.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/coppwr %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/scalable/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/metainfo/

cp assets/icon/scalable.svg %{buildroot}/%{_datadir}/icons/scalable/io.github.dimtpap.coppwr.svg 
cp assets/icon/32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/io.github.dimtpap.coppwr.png
cp assets/icon/48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/io.github.dimtpap.coppwr.png
cp assets/icon/64.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/io.github.dimtpap.coppwr.png
cp assets/icon/128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/io.github.dimtpap.coppwr.png
cp assets/icon/256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/io.github.dimtpap.coppwr.png
cp assets/icon/512.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/io.github.dimtpap.coppwr.png

cp assets/io.github.dimtpap.coppwr.metainfo.xml %{buildroot}/%{_datadir}/metainfo/

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications assets/io.github.dimtpap.coppwr.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/*

%changelog
* Thu Mar 07 2024 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- Initial spec file
