# Status: active
# Tag: DWA
# Type: Standalone
# Category: DAW

#global _dwz_low_mem_die_limit 0
#global _dwz_max_die_limit 0
%global _find_debuginfo_dwz_opts %{nil}
%global __brp_mangle_shebangs %{nil}

Name: maolan
Version: 0.1.0
Release: 1%{?dist}
Summary: Maolan is a Rust DAW focused on recording, editing, routing, automation, export, and plugin hosting
License: BSD-2-Clause
URL: https://github.com/maolan/maolan
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/maolan/maolan/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: cmake
BuildRequires: python3
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: rubberband-devel
BuildRequires: gtk2-devel
BuildRequires: (ffmpeg-devel or ffmpeg-free-devel)
BuildRequires: clang-devel
BuildRequires: cargo-rpm-macros
BuildRequires: desktop-file-utils

%description
Maolan is a Rust DAW focused on recording, editing, routing, automation, export, and plugin hosting.

%prep
%autosetup -n %{name}-%{version}

# Manage debug flags via a build section
mkdir -p .cargo
cat >> .cargo/config.toml << 'EOF'
[build]
rustflags = ["-C", "debuginfo=2", "-C", "dwarf-version=4"]
EOF

%build

%set_build_flags

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
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

export LIBCLANG_PATH=/usr/lib64/
cargo build --release

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 target/release/maolan %{buildroot}/%{_bindir}/
install -m 755 target/release/maolan-cli %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp images/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp desktop/%{name}-linux.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md docs/*.md
%license LICENSE
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*

%changelog
* Sun May 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Thu Apr 30 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Tue Apr 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.6-1
- update to 0.0.6-1

* Mon Mar 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
