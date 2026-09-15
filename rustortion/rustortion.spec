# Status: active
# Tag: Tool, Rack
# Type: Plugin, VST3, CLAP, Standalone
# Category: Audio, Effect, Tool

%global debug_package %{nil}

Name: rustortion
Version: 0.3.0
Release: 1%{?dist}
Summary: A low latency guitar amp simulator
License: MIT
URL: https://github.com/OpenSauce/rustortion
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/OpenSauce/rustortion/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: rustortion.png

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
A guitar and bass amp simulator built in Rust. Runs standalone with JACK,
or as a VST3/CLAP plugin in your DAW.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n common-%{name}
Summary: Common files for %{name}
License: MIT

%description -n common-%{name}
Common files for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}
Requires: common-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}
Requires: common-%{name}

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

cargo build --release
cargo xtask bundle rustortion-plugin --release

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 target/release/rustortion %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr target/bundled/Rustortion.vst3 %{buildroot}/%{_libdir}/vst3/
cp -vfr target/bundled/Rustortion.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -rav presets %{buildroot}/%{_datadir}/%{name}/
cp -rav impulse_responses %{buildroot}/%{_datadir}/%{name}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A low latency guitar amp simulator
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE

%files -n common-%{name}
%{_datadir}/%{name}/presets/*
%{_datadir}/%{name}/impulse_responses/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Tue Sep 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
