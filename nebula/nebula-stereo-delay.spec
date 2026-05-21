# Status: active
# Tag: Effect, Delay
# Type: Plugin, VST3, CLAP
# Category: Effect

%global debug_package %{nil}

Name: nebula-stereo-delay
Version: 1.1.0
Release: 1%{?dist}
Summary: A stereo delay engine forged in double-precision
License: AGPL-3.0-or-later
URL: https://github.com/subhankardas15071992-cloud/Nebula-Stereo-Delay
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/subhankardas15071992-cloud/Nebula-Stereo-Delay/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
Most delay plugins process audio in 32-bit floating point. That's fine — until you stack feedback,
filters, and crossfeed into a regenerative loop. Each pass through the feedback network erodes a
little more resolution, a little more air, a little more life from your sound.
The repeats don't decay — they decompose.
Nebula Stereo Delay runs its entire DSP engine in 64-bit double precision. Every delay line read,
every biquad filter, every crossfeed blend, every feedback calculation — all f64, from input to output.
The only place f32 exists is the final handoff to your DAW. The result? Repeats that decay gracefully,
not digitally.
Tail after tail of crystalline echo that keeps its shape through hundreds of feedback cycles.
This isn't a gimmick. It's engineering.

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
%autosetup -n Nebula-Stereo-Delay-%{version}

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
cp -vfr target/release/libnebula_stereo_delay.so %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/%{target}/

# Create moduleinfo.json (optional but recommended for VST3 SDK 3.7+)
cat > %{buildroot}/%{_libdir}/vst3/%{name}.vst3/Contents/moduleinfo.json <<EOF
{
    "Name": "%{name}",
    "Version": "%{version}",
    "Description": "%{name} by subhankardas15071992-cloud",
    "Vendor": "subhankardas15071992-cloud",
    "SDKVersion": "3.7.9",
    "Compatibility": {
        "PlugInCategory": "Fx|Delay"
    }
}
EOF

install -m 755 -d %{buildroot}/%{_libdir}/clap/%{name}.clap/
cp -vfr target/release/libnebula_stereo_delay.so %{buildroot}/%{_libdir}/clap/%{name}.clap/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu May 21 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
