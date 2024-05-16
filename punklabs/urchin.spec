# Tag: Jack, Synthesizer, Drum
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: onetrick-urchin
Version: 1.0.0
Release: 1%{?dist}
Summary: A hybrid drum synth that models the gritty lo-fi sound of beats from vintage records without sampling.
License: GPL-3.0-or-later
URL: https://punklabs.com/ot-urchin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://punklabs.com/content/projects/ot-urchin/downloads/OneTrickURCHIN-Source-v%{version}.zip


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
A hybrid drum synth that models the gritty lo-fi sound of beats from vintage
records without sampling.
It takes spectral and physically modeled drums, running them through simulated
studio reverb, a vinyl or tape player, and finally a digital sampler.
The result is a fat and saturated drum machine that creates a vibe of sampling
with the control of a synthesizer.

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

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
# rustup-init -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env
# rustup target list
# cargo build --release --bin hexosynth_jack

%ifarch x86_64
rustup-init -y --default-toolchain 1.76.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --default-toolchain 1.76.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo xtask bundle onetrick_urchin --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 'target/bundled/OneTrick URCHIN' %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/*.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/*.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.txt
%license COPYING.txt
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Mar 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
