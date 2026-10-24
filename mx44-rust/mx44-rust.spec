# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, VST3, CLAP
# Category: Synthesizer

%global debug_package %{nil}

Name: mx44-rust
Version: 1.0.0
Release: 1%{?dist}
Summary: A clone of the old Mx44 synthesizer in Rust.
License: GPL-3.0-or-later AND GPL-2.0-or-later
URL: https://github.com/ycollet/Mx44-rust
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/Mx44-rust/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
BuildRequires: desktop-file-utils

Requires: license-%{name}
Requires: common-%{name}

%description
A standalone Rust synthesizer inspired by Jens M Andreasen's Mx44.
This is a new implementation, not an emulation or a source-compatible port.
It replaces GTK2, x86 MMX and the JACK-only audio path with an egui editor,
portable floating-point DSP, CPAL audio and midir MIDI input.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later AND GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n common-%{name}
Summary: Common files for %{name}
License: GPL-3.0-or-later AND GPL-2.0-or-later

%description -n common-%{name}
Common files for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later AND GPL-2.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later AND GPL-2.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Mx44-rust-%{version}

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

cargo build --release
cargo xtask bundle mx44-plugin --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra target/bundled/mx44-rust.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra target/bundled/mx44-rust.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
cp -ra presets/* %{buildroot}/%{_datadir}/%{name}/presets/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp assets/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 assets/%{name}.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files -n license-%{name}
%doc README.md
%license COPYING COPYING-GPL3

%files -n common-%{name}
%{_datadir}/%{name}/presets/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Oct 24 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Fri Oct 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
