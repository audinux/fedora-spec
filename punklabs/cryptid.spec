# Tag: Jack, Synthesizer, Drum
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: onetrick-cryptid
Version: 1.0.2
Release: 1%{?dist}
Summary: An FM drum synth with the cold clanging heart of a DX7 in the fearsome frame of an 808.
License: GPL-3.0-or-later
URL: https://punklabs.com/ot-cryptid
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Source0: https://punklabs.com/content/projects/ot-cryptid/downloads/OneTrick-CRYPTID-Source-v{version}.zip
Source0: https://punklabs.com/content/projects/ot-cryptid/downloads/OneTrickCRYPTID-Source-v1.0.2.zip

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
Whispers of a dreaded drum machine with the cold clanging heart of a DX7
in the fearsome frame of a TR-808 echo in dusty backrooms of backstreet
recording studios.
A contraption conjured under cover of darkness in the heinous pursuit of
chart topping tracks, known only as the DX-808.

It's time to bring the beast out of the shadows! Allow us to present the
world's most accurate recreation of an FM drum synth skeptics say never
actually existed. Using a DX7 emulator of our own design, we forged each
facet of the CRYPTID, reconstructing its wretched inner-workings. From the
"Log Drum" Toms to the "Wood Block" Cowbell. Blow that Samba Whistle and
hit the Gong! Do you want to believe?

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

sed -i -e "s/OneTrick CRYPTID/OneTrick_CRYPTID/g" bundler.toml

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

cargo xtask bundle onetrick_cryptid --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 'target/bundled/OneTrick_CRYPTID' %{buildroot}/%{_bindir}/

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
* Thu Jul 25 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to 1.0.2-1

* Sat Mar 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial spec file
