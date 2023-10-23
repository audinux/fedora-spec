# Tag: Delau
# Type: Plugin, LV2
# Category: Audio, Effect

%global commit0 bf8e8f714d530789afbca4611e8e25c744ec5890
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    dm-graindelay
Version: 0.0.1
Release: 1%{?dist}
Summary: Granular delay, lv2 & vst audio plugin
License: MIT
URL:     https://github.com/moddevices/dm-GrainDelay

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/dm-GrainDelay/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake make
BuildRequires: rust cargo
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

rm .cargo/config.toml

%build

export RUSTFLAGS="-g -O"
export RUST_BACKTRACE=1

cd lv2
cargo build --release

cd ../vst
cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/

cp -rav lv2/dm-GrainDelay.lv2 %{buildroot}/%{_libdir}/lv2/
cp vst/target/release/libdm_graindelay.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Sun Apr 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
