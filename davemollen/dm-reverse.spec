# Status: active
# Tag: Effect, Phaser
# Type: Plugin, LADSPA, LV2, VST
# Category: Effect

%global debug_package %{nil}

%global commit0 d1ac5e72ec0fd7aeea8faf3a91b571b7398eb48e

Name: dm-Reverse
Version: 0.0.5
Release: 1%{?dist}
Summary: Reverse delay audio plugin
URL: https://github.com/davemollen/dm-Reverse
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-Reverse/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup

%description
A mono reverse delay effect written in Rust.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-only

%description -n license-%{name}
License and documentations for %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -n dm-Reverse-%{commit0}

rm -f .cargo/config.toml

%build

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
rustup-init --no-modify-path -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cd lv2
cargo build --release
cd ..

cd vst
cargo build --release

%install

cd lv2
cp target/release/libdm_reverse.so dm-Reverse.lv2/

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-Reverse.lv2 %{buildroot}/%{_libdir}/lv2/
cd ..

cd vst
install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp -vfr target/release/libdm_reverse.so %{buildroot}/%{_libdir}/vst/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Tue May 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- update to 0.0.5-1

* Tue Oct 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
