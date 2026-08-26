# Status: active
# Tag: Effect, Synthesizer
# Type: Plugins, CLAP
# Category: Effect, Synthesizer

#global _dwz_low_mem_die_limit 0
#global _dwz_max_die_limit 0
%global _find_debuginfo_dwz_opts %{nil}
%global __brp_mangle_shebangs %{nil}

Name: maolan-plugins
Version: 0.0.3
Release: 1%{?dist}
Summary: Maolan plugins
License: BSD-2-Clause
URL: https://github.com/maolan/plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/maolan/plugins/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A collection of audio plugins written in Rust for the Maolan ecosystem.
All plugins implement the CLAP plugin API and include an Iced-based GUI
using the TokyoNight theme.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD-2-Clause

%description -n license-%{name}
License and documentation for %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: BSD-2-Clause
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n plugins-%{version}

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
# cargo build --release

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

install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 target/release/libmaolan_plugins.so %{buildroot}%{_libdir}/clap/Maolan.so

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Aug 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.3-1
- Initial spec file
