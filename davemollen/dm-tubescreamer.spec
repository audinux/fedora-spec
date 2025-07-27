# Status: active
# Tag: Effect, Distortion
# Type: Plugin, LV2, CLAP, VST3
# Category: Effect

%global debug_package %{nil}

%global commit0 8095f1e478001bc59b001014b5f776d2ee50e129

Name: dm-TubeScreamer
Version: 0.0.7
Release: 2%{?dist}
Summary: An overdrive effect written in Rust modeled after the Ibanez Tube Screamer
URL: https://github.com/davemollen/dm-TubeScreamer
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-TubeScreamer/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
An overdrive effect written in Rust modeled after the Ibanez Tube Screamer

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

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -n dm-TubeScreamer-%{commit0}

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
cp target/release/libdm_tube_screamer.so dm-TubeScreamer.lv2/
cd ..

cd nih-plug
cargo xtask bundle dm_tube_screamer --release

%install

cd nih-plug/target/bundled

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr dm_tube_screamer.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr dm_tube_screamer.vst3 %{buildroot}/%{_libdir}/vst3/

cd ../../../lv2/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-TubeScreamer.lv2 %{buildroot}/%{_libdir}/lv2/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Tue May 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.6-2
- update to 0.0.6-2

* Tue Oct 08 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.6-1
- update to 0.0.6-1 - update to cf4f26c13f6090d3293eb6e52aa97b408db32e86

* Thu Oct 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.4-1
- Initial spec file
