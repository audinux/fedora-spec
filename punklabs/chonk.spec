# Status: active
# Tag: Jack, Synthesizer, Bass
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: onetrick-chonk
Version: 1.0.0
Release: 1%{?dist}
Summary: A physically modeled electric bass monosynth that produces a classic sound perfect for a wide variety of musical genres.
License: GPL-3.0-or-later
URL: https://punklabs.com/ot-chonk
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://punklabs.com/content/projects/ot-chonk/downloads/OneTrickCHONK-Source-v%{version}.zip

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
A physically modeled electric bass monosynth that produces a
classic sound perfect for a wide variety of musical genres.
It's powered by digital waveguide synthesis to simulate the
vibrations of a string. Different play styles like muting,
fingering, picking, or slap can be achieved with articulations.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -c -n %{name}-%{version}

sed -i -e "s/OneTrick CHONK/OneTrick_CHONK/g" bundler.toml

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
rustup-init -y --no-modify-path --default-toolchain 1.76.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.76.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle onetrick_chonk --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 'target/bundled/OneTrick_CHONK' %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/*.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/*.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
