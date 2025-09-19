# Status: active
# Tag: Synthesizer, Modular
# Type: Plugin, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: node-sound
Version: 4.1.0
Release: 1%{?dist}
Summary: FOSS VST synth/effect based on nodes
License: MIT
URL: https://github.com/Lubba-64/node_sound
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Lubba-64/node_sound/archive/refs/tags/v%{version}.tar.gz#/node_sound-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: python3

Requires: license-%{name}

%description
A node based sound construction program written in rust.
I reserve the right to quit this project whenever, that
said I am still finding fun new things to add every now and then...

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n node_sound-%{version}

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
# rustup-init -y --no-modify-path --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain 1.85.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.85.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo run --bin xtask bundle node_sound_vst --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/*.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/*.clap %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Fri Sep 19 2025 Yann Collette <ycollette.nospam@free.fr> - 4.1.0-1
- update to 4.1.0-1

* Sun Sep 14 2025 Yann Collette <ycollette.nospam@free.fr> - 4.0.0-1
- update to 4.0.0-1

* Mon Aug 18 2025 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-1
- Initial spec file
