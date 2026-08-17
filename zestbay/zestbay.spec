# Status: active
# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

%global debug_package %{nil}

Name: zestbay
Version: 0.8.6
Release: 1%{?dist}
Summary: A PipeWire patchbay for Linux that visualizes your audio graph, hosts LV2 effects plugins inline, and auto-connects ports with persistent routing rules.
License: MIT
URL: https://github.com/lemonxah/zestbay
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/lemonxah/zestbay/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: cmake
BuildRequires: clang
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: lilv-devel
BuildRequires: lv2-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: pipewire-devel
BuildRequires: dbus-devel
BuildRequires: suil-devel
BuildRequires: gtk3-devel
BuildRequires: python3
BuildRequires: desktop-file-utils

Requires: dbus
Requires: suil

%description
ZestBay is a visual audio routing tool for PipeWire on Linux.
It lets you see every audio node in your system (applications, hardware devices, virtual sinks),
connect and disconnect ports with drag-and-drop, host LV2, VST3, and CLAP effects plugins inline,
and define patchbay rules that automatically restore your routing whenever devices or apps appear.

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

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --workspace --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

install -m 755 target/release/zestbay %{buildroot}/%{_bindir}/

install -m 644 zestbay.desktop %{buildroot}/%{_datadir}/applications/zestbay.desktop
install -m 644 images/zesticon.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/zestbay.png
install -m 644 images/zesttray.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/zestbay-tray.png

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/zestbay.desktop
%{_datadir}/icons/hicolor/256x256/apps/zestbay.png
%{_datadir}/icons/hicolor/256x256/apps/zestbay-tray.png

%changelog
* Mon Aug 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- Initial spec file
