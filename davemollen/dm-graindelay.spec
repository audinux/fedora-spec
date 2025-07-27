# Status: active
# Tag: Delay
# Type: Plugin, LV2
# Category: Audio, Effect

%global debug_package %{nil}

%global commit0 69a655147823b9ef3083dced5bb1d7a8c49d64be

Name: dm-graindelay
Version: 0.0.5
Release: 2%{?dist}
Summary: Granular delay, lv2 & vst audio plugin
License: MIT
URL: https://github.com/davemollen/dm-GrainDelay
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-GrainDelay/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rustup
BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: libcurl-devel

%description
A granular delay effect written in Rust.
The effect can be compiled to a lv2 or vst plugin.
This plugin has been written primarily to run on Mod devices.
And because I mainly use this for guitar it's just mono for now.

%prep
%autosetup -n dm-GrainDelay-%{commit0}

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

cd ../vst
cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst/

cp -rav lv2/dm-GrainDelay.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-2
- update to 0.0.5-2

* Thu Aug 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to last master - update git url

* Sun Apr 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
