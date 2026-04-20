# Status: active
# Tag: Tool
# Type: Standalone
# Category: TOOL, Plugin

%global debug_package %{nil}

Name: yabridge-tui
Version: 0.2.1
Release: 2%{?dist}
Summary: TUI wrapper for yabridgectl
License: GPL-3.0-or-later
URL: https://codeberg.org/olivierlm/yabridge-tui
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/olivierlm/yabridge-tui/archive/v0.2.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup

Requires: yabridge

%description
TUI wrapper for yabridgectl. Manage Windows VST2/VST3/CLAP plugins on Linux without typing commands.
Browse your bridged plugins, add/remove directories with a file picker, sync, and edit per-plugin
yabridge.toml options — all from one terminal screen.

%prep
%autosetup -n %{name}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.88.0-x86_64-unknown-linux-gnu
# rustup-init -y --no-modify-path --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain 1.88.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.88.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/yabridge-tui %{buildroot}/%{_bindir}/

%files
%doc README.md
%{_bindir}/*

%changelog
* Sat Apr 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-2
- update to 0.2.1-2: add yabridge as requirements

* Sat Apr 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- Initial spec file
