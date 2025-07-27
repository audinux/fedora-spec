# Status: active
# Tag: Effect, Reverb
# Type: Plugin, LV2, CLAP, VST3
# Category: Effect

%global debug_package %{nil}

%global commit0 d117341478a9c9706c2edba1d490f4621f3f19db

Name: dm-seq
Version: 0.0.1
Release: 1%{?dist}
Summary: A monophonic step sequencer effect
URL: https://github.com/davemollen/dm-Seq
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-Seq/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
A monophonic step sequencer effect written in Rust.

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

%autosetup -n dm-Seq-%{commit0}

%build

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
cp target/release/libdm_seq.so dm-Seq.lv2/

%install

cd lv2/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-Seq.lv2 %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
