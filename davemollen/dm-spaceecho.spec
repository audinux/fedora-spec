# Status: active
# Tag: Effect, Delay
# Type: Plugin, LV2, CLAP, VST3
# Category: Effect

%global debug_package %{nil}

%global commit0 40c759fd529802a179ba1d7f74714fbc0593e276

Name: dm-Spaceecho
Version: 0.1.5
Release: 1%{?dist}
Summary: A delay and reverb effect inspired by Space Echo devices written in Rust
URL: https://github.com/davemollen/dm-SpaceEcho
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/davemollen/dm-SpaceEcho/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
A delay and reverb effect inspired by Space Echo devices written in Rust

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

%autosetup -n dm-SpaceEcho-%{commit0}

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
cp target/release/libdm_space_echo.so dm-SpaceEcho.lv2/
cd ..

cd nih-plug
cargo xtask bundle dm_space_echo --release

%install

cd nih-plug/target/bundled

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr dm_space_echo.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr dm_space_echo.vst3 %{buildroot}/%{_libdir}/vst3/

cd ../../../lv2/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -vfr dm-SpaceEcho.lv2 %{buildroot}/%{_libdir}/lv2/

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
* Wed Aug 20 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-1
- update to 0.1.5-1

* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- update to 0.1.4-1

* Tue May 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- update to 0.1.3-1

* Thu Oct 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- Initial spec file
