
# Status: active
# Tag: Drum, Sampler
# Type: Plugin, CLAP, VST3
# Category: Tool

%global debug_package %{nil}

Name: rustydrumgizmo
Version: 0.3.3
Release: 1%{?dist}
Summary: Rusty DrumGizmo is a modern Rust port of the acclaimed DrumGizmo acoustic drum sampler
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/rustydrumgizmo
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/rustydrumgizmo/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
Rusty DrumGizmo is a modern Rust port of the acclaimed DrumGizmo acoustic drum sampler.
Built with nih-plug and egui, it aims to bring the raw, multi-channel acoustic drum sounds
of the original DrumGizmo ecosystem into a memory-safe, optimized Rust architecture.

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
# cargo build --release

%ifarch x86_64
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/rusty_drumgizmo.vst3/Contents/%{_target}/
cp -ra target/release/librustydrumgizmo.so %{buildroot}/%{_libdir}/vst3/rusty_drumgizmo.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/librustydrumgizmo.so %{buildroot}/%{_libdir}/clap/rusty_drumgizmo.clap

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Jul 08 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update to 0.3.3-1

* Tue Jul 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-1
- update to 0.3.2-1

* Fri Jun 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
