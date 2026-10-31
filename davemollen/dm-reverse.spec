# Status: active
# Tag: Effect, Phaser
# Type: Plugin, LV2, VST, MODGUI
# Category: Effect

%global debug_package %{nil}

Name: dm-Reverse
Version: 0.0.8
Release: 1%{?dist}
Summary: Reverse delay audio plugin
URL: https://github.com/davemollen/dm-Reverse
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-Reverse/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: dm-reverse-0001-fix-cargo-conf.patch

BuildRequires: gcc gcc-c++
BuildRequires: rustup

%description
A mono reverse delay effect written in Rust.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-only

%description -n license-%{name}
License and documentations for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -p1 -n dm-Reverse-%{version}

%build

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
rustup-init --no-modify-path -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cd lv2
cargo build --release
cd ..

%install

cd lv2
cp target/release/libdm_reverse.so dm-Reverse.lv2/

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-Reverse.lv2 %{buildroot}/%{_libdir}/lv2/
cd ..

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sat Oct 31 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- update to 0.0.8-1

* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.6-1
- update to 0.0.6-1

* Tue May 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Tue Oct 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
