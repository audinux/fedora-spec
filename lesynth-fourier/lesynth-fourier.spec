# Status: active
# Tag: Synthesizer
# Type: Plugin, LV2, CLAP, VST3
# Category: Synthesizer

%global debug_package %{nil}

Name: lesynth-fourier
Version: 1.1.0
Release: 1%{?dist}
Summary: A powerful Fourier synthesizer VST3 audio plugin built in Rust using the nih-plug framework
URL: https://github.com/hlavnjak/lesynth-fourier
ExclusiveArch: x86_64 aarch64
License: Apache-2.0

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/hlavnjak/lesynth-fourier/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: rustup
BuildRequires: libglvnd-devel
BuildRequires: libXcursor-devel
BuildRequires: python3
BuildRequires: xcb-util-wm-devel

%description
A powerful Fourier synthesizer VST3 audio plugin built
in Rust using the nih-plug framework.
LeSynth - Fourier generates harmonic sounds through
Fourier synthesis with customizable amplitude and
phase curves for each harmonic.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: Apache-2.0

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: Apache-2.0
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep

%autosetup -n %{name}-%{version}

%build

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init --no-modify-path -y --default-toolchain=1.76.0-x86_64-unknown-linux-gnu
# rustup-init --no-modify-path -y --default-toolchain=nightly-x86_64-unknown-linux-gnu
# source cargo/env

%ifarch x86_64
rustup-init --no-modify-path -y --default-toolchain nightly-x86_64-unknown-linux-gnu
%endif
%ifarch aarch64
rustup-init --no-modify-path -y --default-toolchain nightly-aarch64-unknown-linux-gnu
%endif
source cargo/env

cargo build --release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/LeSynthFourier.vst3/Contents/%{_target}/
cp target/release/liblesynth_fourier.so %{buildroot}/%{_libdir}/vst3/LeSynthFourier.vst3/Contents/%{_target}/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Jul 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- update to 0.1.4-1

* Tue May 06 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to 0.1.0-1

* Thu Oct 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- Initial spec file
