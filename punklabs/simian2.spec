# Tag: Drum
# Type: Plugin, Standalone, VST3, CLAP
# Category: Drum, Synthesizer

%global debug_package %{nil}

Name: onetrick-simian2
Version: 2.0.2
Release: 1%{?dist}
Summary: An open source drum synth inspired by hexagonal classics like the Simmons SDS-V
License: GPL-3.0-or-later
URL: https://punklabs.com/ot-simian
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://punklabs.com/content/projects/ot-simian/downloads/OneTrickSIMIAN2-Source-v%{version}.zip

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
Crash into the 80s with an open source drum synth inspired by hexagonal classics
like the Simmons SDS-V. Thumping kicks, punchy snares, and sizzling cymbals
coalesce with its clacky claves and crunchy claps. Bring saccharine synthwave
sauce to your sublime soundscapes or drop indelable pewww pewww tom toms into
your new nu-disco.

Highly customizable voices with great dynamics, filter sweeps, saturation,
and drive that will literally flam your tracks. Toss [OT] SIMIAN into your DAW
and just see what happens.

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

sed -i -e "s/OneTrick SIMIAN2/OneTrick_SIMIAN2/g" bundler.toml

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

cargo xtask bundle onetrick_simian2 --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 'target/bundled/OneTrick_SIMIAN2' %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/*.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/*.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.txt CHANGELOG.txt
%license LICENSE.txt
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Jul 25 2024 Yann Collette <ycollette.nospam@free.fr> - 2.0.2-1
- Initial spec file
