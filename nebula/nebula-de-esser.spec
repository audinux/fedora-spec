# Status: active
# Tag: Effect
# Type: Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: nebula-de-esser
Version: 3.1.0
Release: 1%{?dist}
Summary: Nebula DeEsser is a high-performance de-esser plugin built for professionals who demand precision.
License: AGPL-3.0-or-later
URL: https://github.com/subhankardas15071992-cloud/Nebula-De-Esser
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/subhankardas15071992-cloud/Nebula-De-Esser/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Nebula DeEsser is a professional-grade de-esser plugin built entirely in Rust with 64-bit double-precision processing.
It delivers studio-quality results while maintaining zero compilation warnings and pure native builds across all platforms.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: AGPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: AGPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Nebula-De-Esser-%{version}

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
rustup-init -y --no-modify-path --default-toolchain 1.88.0-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init -y --no-modify-path --default-toolchain 1.88.0-aarch64-unknown-linux-gnu
%endif
source cargo/env

# cargo xtask bundle nebula_desser --release
cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/%{target}/
cp -vfr target/release/libnebula_desser.so %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/%{target}/

# Create moduleinfo.json (optional but recommended for VST3 SDK 3.7+)
cat > %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/moduleinfo.json <<EOF
{
    "Name": "%{name}",
    "Version": "%{version}",
    "Description": "%{name} by subhankardas15071992-cloud",
    "Vendor": "subhankardas15071992-cloud",
    "SDKVersion": "3.7.9",
    "Compatibility": {
        "PlugInCategory": "Fx"
    }
}
EOF

install -m 755 -d %{buildroot}/%{_libdir}/clap/%{name}.clap/
cp -vfr target/release/libnebula_desser.so %{buildroot}/%{_libdir}/clap/%{name}.clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu May 21 2026 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- Initial spec file
