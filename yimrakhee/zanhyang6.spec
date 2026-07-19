# Status: active
# Tag: Distortionverb
# Type: Standalone, Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}
%global commit0 c172e6bf28888cd31a97bc927296a6251f517ba0

Name: zanhyang6
Version: 0.8.7
Release: 1%{?dist}
Summary: Reverb Rack plugin for Linux
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/zanhyang6
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/zanhyang6/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

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
This plugin provides six meticulously crafted reverb algorithms ranging from physical acoustic modeling to
atmospheric shimmers, all wrapped in a sleek, hardware-accelerated GUI with interactive real-time visualizers.
The 6 Reverb Engines:
- RM (Room): Dense, natural room acoustics with energy preservation and velvet noise early reflections
- HA (Hall): Lush, expansive concert hall with dynamic wander modulation and deep spatial imaging
- PL (Plate): Physical modeling plate reverb with high-tension dispersion and metallic friction rattling
- SP (Spring): Dynamic resonant helices with adjustable tension, dynamic wobble, and tube-like overdrive
- VD (Vintage Digital): Retro 80s/90s digital reverb with adjustable AD/DA Lo-Fi decimation, chorus,
  and raw matrix density
- SH (Shimmer): Ethereal, ascending aurora reverb with pristine pitch-shifting, huge atmospheric tails,
  and glowing particle visualization

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
rustup-init -y --no-modify-path --default-toolchain 1.88.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.88.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/zanhyang6.vst3/Contents/%{_target}/
cp -ra target/release/libzanhyang6.so %{buildroot}/%{_libdir}/vst3/zanhyang6.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libzanhyang6.so %{buildroot}/%{_libdir}/clap/zanhyang6.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/zanhyang6 %{buildroot}/%{_bindir}/

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
* Sun Jul 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.7-1
- update to 0.8.7-1

* Sat Jul 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.6-1
- Initial spec file
