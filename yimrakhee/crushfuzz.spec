# Status: active
# Tag: Distortion
# Type: Standalone, Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: crushfuzz
Version: 0.2.0
Release: 1%{?dist}
Summary: Bitcrusher plugin for Guitar
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/crushfuzz
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/crushfuzz/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Bitcrusher plugin for Guitar.
Destructive digital artifacts with an Analog-style parallel mixing architecture.

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

install -m 755 -d %{buildroot}%{_libdir}/vst3/crushfuzz.vst3/Contents/%{_target}/
cp -ra target/release/libcrushfuzz.so %{buildroot}/%{_libdir}/vst3/crushfuzz.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libcrushfuzz.so %{buildroot}/%{_libdir}/clap/crushfuzz.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/crushfuzz %{buildroot}/%{_bindir}/

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
* Fri Feb 27 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Sat Feb 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-1
- update to 0.1.5-1

* Wed Feb 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
