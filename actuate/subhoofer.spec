# Status: active
# Tag: Effect, Equalizer
# Type: Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: subhoofer
Version: 2.2.3
Release: 1%{?dist}
Summary: Sub and Bass Enhancement plugin
License: GPL-3.0-or-later
URL: https://github.com/ardura/Subhoofer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ardura/Subhoofer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: xcb-util-wm-devel
BuildRequires: python3
Buildrequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)

%description
Subhoofer is a sub and bass enhancement plugin aimed at being a
lightweight replacement for other subharmonic generation plugins.
Use it to make your bass audible on small speakers or extend the
sub range in bass signals! You can also beef up guitars, add bass
to other instruments, presence to vocals etc. Experiment!

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentations for %{name}

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
%autosetup -n Subhoofer-%{version}

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
rustup-init -y --no-modify-path --default-toolchain 1.92.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.92.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle Subhoofer --profile release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra target/bundled/Subhoofer.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra target/bundled/Subhoofer.clap %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Jan 07 2026 Yann Collette <ycollette.nospam@free.fr> - 2.2.3-1
- update to 2.2.3-1

* Mon Nov 11 2024 Yann Collette <ycollette.nospam@free.fr> - 2.2.2-1
- Initial spec file
