# Status: active
# Tag: Synthesizer, Effects
# Type: Plugin, Standalone, VST3, CLAP
# Category: Synthesizer, Effects

%global debug_package %{nil}
%global commit0 d64b2ab9cfb94773c5ee4d0e72aef5921ee95d2d

Name: nih-plug
Version: 0.4.3
Release: 2%{?dist}
Summary: Rust VST3 and CLAP plugin framework and plugins - because everything is better when you do it yourself
License: ISC
URL: https://github.com/robbert-vdh/nih-plug
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/robbert-vdh/nih-plug/archive/%{commit0}.zip#/%{name}-%{version}.zip

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
Rust VST3 and CLAP plugin framework and plugins - because everything is better when you do it yourself

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  ISC

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  ISC
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  ISC
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n nih-plug-%{commit0}

sed -i -e "s/Soft Vacuum/Soft_Vacuum/g" bundler.toml
sed -i -e "s/Buffr Glitch/Buffr_Glitch/g" bundler.toml
sed -i -e "s/Loudness War Winner/Loudness_War_Winner/g" bundler.toml
sed -i -e "s/Puberty Simulator/Puberty_Simulator/g" bundler.toml
sed -i -e "s/Safety Limiter/Safety_Limiter/g" bundler.toml
sed -i -e "s/Spectral Compressor/Spectral_Compressor/g" bundler.toml

%build

%set_build_flags

export RUSTFLAGS="-g -O"

export CWD=`pwd`
export RUSTUP_HOME="$CWD/rustup"
export CARGO_HOME="$CWD/cargo"
# rustup-init -y --no-modify-path --default-toolchain=1.77.0-x86_64-unknown-linux-gnu
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

PLUGINS="buffr_glitch
         crisp
	 crossover
         diopser
         loudness_war_winner
         puberty_simulator
         safety_limiter
         spectral_compressor"

for Files in $PLUGINS 
do
    cargo xtask bundle $Files --release
done


%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

PLUGINS="Buffr_Glitch
         Crisp
         Crossover
         Diopser
         Loudness_War_Winner
         Puberty_Simulator
         Safety_Limiter
         Spectral_Compressor"

for Files in $PLUGINS 
do
    cp -vfr target/bundled/$Files.vst3 %{buildroot}/%{_libdir}/vst3/
    cp -vfr target/bundled/$Files.clap %{buildroot}/%{_libdir}/clap/
done

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Aug 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-2
- fix package

* Tue May 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.4.3-1
- Initial spec file
