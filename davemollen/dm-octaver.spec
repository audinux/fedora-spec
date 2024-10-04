# Status: active
# Tag: Effect, Pitch
# Type: Plugin, LV2
# Category: Effect

%global debug_package %{nil}

%global commit0 5b1771c86c1c4ae8f3a60b5b13450b9de537b749

Name: dm-octaver
Version: 0.0.3
Release: 1%{?dist}
Summary: A harsh octave down effect written in Rust
URL: https://github.com/davemollen/dm-Octaver
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-Octaver/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
A harsh octave down effect written in Rust

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

%autosetup -n dm-Octaver-%{commit0}

rm -f .cargo/config.toml

%build

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init --no-modify-path -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
# rustup-init --no-modify-path -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env

%ifarch x86_64
rustup-init --no-modify-path -y --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init --no-modify-path -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cd lv2
cargo build --release
cp target/release/libdm_octaver.so dm-Octaver.lv2/
cd ..

%install

cd lv2/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-Octaver.lv2 %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Oct 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.3-1
- Initial spec file
