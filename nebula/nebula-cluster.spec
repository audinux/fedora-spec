# Status: active
# Tag: Effect
# Type: Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: nebula-cluster
Version: 1.0.0
Release: 1%{?dist}
Summary: A free open-source dirt box plugin.
License: AGPL-3.0-or-later
URL: https://github.com/subhankardas15071992-cloud/Nebula-Cluster
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/subhankardas15071992-cloud/Nebula-Cluster/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Nebula Cluster is a free open-source dirt box plugin made by Nebula Audio.
It is built for one job: take clean, polite audio and give it weight, bite, heat, movement, and attitude.
Put it on drums, bass, synths, vocals, guitars, loops, rooms, buses, or anything that needs to stop behaving.

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
%autosetup -n Nebula-Cluster-%{version}

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

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/%{target}/
cp -vfr target/release/libnebula_cluster.so %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/%{target}/

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
cp -vfr target/release/libnebula_cluster.so %{buildroot}/%{_libdir}/clap/%{name}.clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu May 21 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
