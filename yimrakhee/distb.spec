# Status: active
# Tag: Distortion
# Type: Standalone, Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: distb
Version: 0.2.0
Release: 1%{?dist}
Summary: A modern, aggressive bass distortion plugin
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/distb
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/distb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
A modern, aggressive bass distortion plugin (GNU GPLv3)
Designed to cut through the heavy metal or modern rock mixes, it preserves transient
attack while saturating the signal with rich, asymmetrical tube-style soft clipping.
Sculpt your distortion character before it hits the drive circuit, and keep your
low-end foundation rock solid.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}

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
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/distb.vst3/Contents/%{_target}/
cp -ra target/release/libdistb.so %{buildroot}/%{_libdir}/vst3/distb.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libdistb.so %{buildroot}/%{_libdir}/clap/distb.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/distb %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Mar 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
