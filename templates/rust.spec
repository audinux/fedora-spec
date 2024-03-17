# Tag: Jack, Synthesizer, Modular
# Type: Plugin, Standalone, VST, VST3, CLAP
# Category: Audio, Synthesizer

%global debug_package %{nil}

%global commit0 d84e0357a98a8235b9383b1a3e913d065a7bad43

Name: hexosynth
Version: 0.9.9
Release: 1%{?dist}
Summary: A hexagonal modular synthesizer plugin.
License: GPL-3.0-or-later
URL: https://github.com/WeirdConstructor/HexoSynth

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/WeirdConstructor/HexoSynth/archive/%{commit0}.zip#/hexosynth.zip

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
Flashy Synthesia Like Software

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CALP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}


%prep
%autosetup -n HexoSynth-%{commit0}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
# rustup-init -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

# Build jack standalone
cd hexosynth_jack
cargo build --release --bin hexosynth_jack
cd ..

# Build VTS3 and CLAP part
cd hexosynth_plug
cargo +nightly xtask bundle hexosynth_plug --release
cd ..

# Build standard audio
cd hexosynth_cpal
cargo +nightly build --release --bin hexosynth_cpal
cd ..

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/hexosynth_jack %{buildroot}/%{_bindir}/
install -m 755 target/release/hexosynth_cpal %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/hexosynth_plug.vst3 %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/hexosynth_plug.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_datadir}/hexosynth/examples/
cp -ra misc_patches/* %{buildroot}/%{_datadir}/hexosynth/examples/

%files
%doc README.md CHANGELOG.md doc/hexosynth_wlambda_api.md
%license COPYING
%{_bindir}/hexosynth_jack
%{_bindir}/hexosynth_cpal
%dir %{_datadir}/hexosynth/
%{_datadir}/hexosynth/examples/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Feb 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Fix spec

* Sun Aug 21 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Initial spec file
