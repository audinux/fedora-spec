# Status: active
# Tag: Effect, Distortion
# Type: Plugin, CLAP, VST3
# Category: Effect

%global debug_package %{nil}

%global commit0 ee2f626c982eaeb57d8756d76432c04092a780fa

Name: zmann
Version: 0.0.1
Release: 1%{?dist}
Summary: Explore a range of instruments, designed to elevate your audio production experience.
URL: https://github.com/zmann-org/zmann
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zmann-org/zmann/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
Explore a range of instruments, designed to elevate your audio production experience.
Collection of VST plugins.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-only

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep

%autosetup -n zmann-%{commit0}

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

cargo xtask bundle toybox --release
cargo xtask bundle orchestron --release
cargo xtask bundle bells --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp -vfr target/bundled/Toybox.clap %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/Toybox.vst3 %{buildroot}/%{_libdir}/vst3/

cp -vfr target/bundled/Orchestron.clap %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/Orchestron.vst3 %{buildroot}/%{_libdir}/vst3/

cp -vfr target/bundled/Bells.clap %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/Bells.vst3 %{buildroot}/%{_libdir}/vst3/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Oct 12 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
