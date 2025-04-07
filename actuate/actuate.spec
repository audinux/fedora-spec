# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: actuate
Version: 1.3.9
Release: 1%{?dist}
Summary: Synthesizer, Sampler, Granulizer written in Rust with Nih-Plug and egui
License: GPL-3.0-or-later
URL: https://github.com/ardura/Actuate
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ardura/Actuate/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: xcb-util-wm-devel
Buildrequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: alsa-lib-devel

%description
A Subtractive and Additive Synthesizer, Sampler, and Granulizer
built in Rust + Nih-Plug Written by Ardura

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
%autosetup -n Actuate-%{version}

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
rustup-init -y --no-modify-path --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle Actuate --profile release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra target/bundled/Actuate.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra target/bundled/Actuate.clap %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Mar 31 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.9-1
- update to 1.3.9-1

* Fri Feb 28 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.8-1
- update to 1.3.8-1

* Fri Jan 17 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.7-1
- update to 1.3.7-1

* Tue Dec 31 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.6-1
- update to 1.3.6-1

* Thu Oct 17 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-1
- update to 1.3.5-1

* Sat Oct 05 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-1
- update to 1.3.4-1

* Mon Sep 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.3-1
- update to 1.3.3-1

* Fri Sep 06 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-1
- Initial spec file
