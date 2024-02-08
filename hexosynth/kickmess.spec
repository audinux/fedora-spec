# Tag: Jack, Synthesizer, Drum
# Type: Plugin, VST
# Category: Audio, Synthesizer

%global debug_package %{nil}

%global commit0 e02760ca72031587007c33395419d5f67e2296d8

Name: kickmess
Version: 0.2.2
Release: 1%{?dist}
Summary: A kick drum synthesizer plugin
License: GPL-3.0-or-later
URL: https://github.com/WeirdConstructor/Kickmess

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/WeirdConstructor/Kickmess/archive/%{commit0}.zip#/Kickmess.zip

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
Kickmess is a port of the easy to use and good sounding Kicker plugin from
LMMS to a reusable audio plugin format on Linux (VST currently). The DSP code
has been ported, changed a bit and extended with some other functionality.

An extended version of Kickmess, with more oscillators and other functionality,
is available as Megamess plugin. It's built from the same code base, but with
a larger DSP core and extended GUI. It's useful for many kinds of percussion
synthesis, for synthesizing bass sounds and other fx sounds.

More features and changes might be added and before Version 1.0 is released
I will not guarantee that your presets will sound the same. After Version 1.0
significant changes will come with a change in the major version number.

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n Kickmess-%{commit0}

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
rustup-init -y --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --all-features --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp -vfr target/release/libkickmessvst.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license COPYING

%files -n vst-%{name}
%{_libdir}/vst/*


%changelog
* Wed Feb 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- Initial spec file
