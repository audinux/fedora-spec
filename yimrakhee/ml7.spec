# Status: active
# Tag: Limiter
# Type: Standalone, Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}
%global commit0 b454dd433573edca9b7b7484a9db72d3c41d6deb

Name: ml7
Version: 0.0.1
Release: 1%{?dist}
Summary: ML7 is a modern, highly optimized mastering limiter audio plugin
License: GPL-3.0-or-later
URL: https://codeberg.org/yimrakhee/ml7
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://codeberg.org/yimrakhee/ml7/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

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
ML7 is a modern, highly optimized mastering limiter audio plugin (CLAP / VST3) built in Rust using the nih-plug
and egui frameworks.
It is designed from the ground up to provide peak protection, oversampling fidelity, and strict EBU R128
compliant metering.

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

install -m 755 -d %{buildroot}%{_libdir}/vst3/ml7.vst3/Contents/%{_target}/
cp -ra target/release/libml7.so %{buildroot}/%{_libdir}/vst3/ml7.vst3/Contents/%{_target}/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra target/release/libml7.so %{buildroot}/%{_libdir}/clap/ml7.clap

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra target/release/ml7 %{buildroot}/%{_bindir}/

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
* Fri Jun 26 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
