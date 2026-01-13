# Status: active
# Tag: Tool, Video, Audio
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

Name: radiance
Version: 0.7.1
Release: 1%{?dist}
Summary: Radiance is video art software for VJs
License: MIT
URL: https://github.com/zbanks/radiance
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zbanks/radiance/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: mpv-devel
BuildRequires: desktop-file-utils

%description
Radiance is video art software designed for live performance.
More information is available at radiance.video.

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
install -m 755 target/release/radiance %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/radiance/data/
cp -ra library/* %{buildroot}/%{_datadir}/radiance/data/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp exe_icon.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=Radiance is video art software for VJs
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
%doc README.md TODO.md
%license LICENSE
%{_bindir}/radiance
%{_datadir}/radiance/data/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Mon Jan 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- update to 0.7.1-1

* Fri Dec 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
