# Status: active
# Tag: Effect, Overdrive
# Type: Plugin, VST
# Category: Audio, Effect

%global debug_package %{nil}

%global commit0 2eeb7ce2e838c1668e0eeac4eeef9f40e0310c91

Name: wild-blossom-plugins
Version: 0.0.1
Release: 1%{?dist}
Summary: A saturation plugin.
License: GPL-3.0-or-later
URL: https://gitlab.com/wild-blossom-audio/wild-blossom-plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/wild-blossom-audio/wild-blossom-plugins/-/archive/%{commit0}/wild-blossom-plugins-%{commit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
Wild Blossom Saturator

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n wild-blossom-plugins-%{commit0}

%build

%set_build_flags

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
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp -vfr target/release/libwild_blossom_saturator.so %{buildroot}/%{_libdir}/vst/

%files -n vst-%{name}
%license LICENSE
%{_libdir}/vst/*

%changelog
* Wed Feb 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
