# Status: active
# Tag: Analyzer, Graphic
# Type: Plugin, VST3, CLAP
# Category: Tool, Graphic

%global debug_package %{nil}

Name: scrollscope
Version: 1.4.2
Release: 1%{?dist}
Summary: A simple scrolling oscilloscope
License: GPL-3.0-or-later
URL: https://github.com/ardura/Scrollscope
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ardura/Scrollscope/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

Requires: license-%{name}

%description
This is an oscilloscope with a few different features

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
%autosetup -n Scrollscope-%{version}

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
rustup-init -y --no-modify-path --default-toolchain 1.78.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.78.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle scrollscope --profile release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra target/bundled/scrollscope %{buildroot}/%{_bindir}/
cp -ra target/bundled/scrollscope.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra target/bundled/scrollscope.clap %{buildroot}/%{_libdir}/clap/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Mar 27 2025 Yann Collette <ycollette.nospam@free.fr> - 1.4.2-1
- update to 1.4.2-1

* Wed Oct 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.4.1-1
- Initial spec file
