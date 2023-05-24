# Global variables for github repository
%global commit0 bf8e8f714d530789afbca4611e8e25c744ec5890
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    mod-dm-graindelay
Version: 0.1.%{shortcommit0}
Release: 1%{?dist}
License: MIT
Summary: Granular delay, lv2 & vst audio plugin
Url:     https://github.com/moddevices/dm-GrainDelay

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/moddevices/dm-GrainDelay/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: clang
BuildRequires: rust cargo
BuildRequires: lv2-devel

%description
A granular delay effect written in Rust. The effect can be compiled
to a lv2 or vst plugin. This plugin has been written primarily to run
on Mod devices. And because I mainly use this for guitar it's just
mono for now.

%prep
%autosetup -n dm-GrainDelay-%{commit0}

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
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-bf8e8f71-1
- initial spec 
