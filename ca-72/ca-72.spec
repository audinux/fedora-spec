# Status: active
# Tag: Synthesizer
# Type: Plugin, VST3, CLAP
# Category: Audio, Synthesizer

%global debug_package %{nil}

Name: ca-72
Version: 0.3.0
Release: 1%{?dist}
Summary: A  a synthesizer plug-in modelled from the circuit of a 1970s analogue synthesizer
License: GPL-3.0-or-later
URL: https://github.com/idlefoundry/ca-72
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/idlefoundry/ca-72/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: git
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
A synthesizer by Idle Foundry: monophonic like the instrument it models, or one whole instrument
per note with POLY. Its voice is modelled from the circuit of a 1970s analogue synthesizer, the
Minimoog Model D of about 1972-73 with the CA3046 ("old") oscillator board. Every board was
transcribed from the instrument's service documents into SPICE netlists and simulated in ngspice.
The real-time models were then derived from those simulations and tested against them, the factory
calibration procedures included.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CALP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}-%{version}

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

cargo xtask bundle ca72-plugin --profile bundle
cargo build --locked -p ca72-plugin --bin ca72-standalone --features standalone-production --profile bundle

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/bundle/ca72-standalone %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/CA-72.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/CA-72.clap %{buildroot}/%{_libdir}/clap/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 scripts/standalone/icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/com.idlefoundry.ca72.svg

# Install desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 scripts/standalone/CA-72.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/CA-72.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/CA-72.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files -n license-%{name}
%doc README.md docs/*
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Oct 29 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update to 0.3.0-1

* Tue Oct 20 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.8-1
- update to 0.2.8-1

* Mon Oct 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.7-1
- update to 0.2.7-1

* Mon Oct 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.6-1
- update to 0.2.6-1

* Sun Oct 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.5-1
- update to 0.2.5-1

* Sat Oct 17 2026 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- Initial spec file
