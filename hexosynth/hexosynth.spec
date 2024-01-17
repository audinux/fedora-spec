# Tag: Jack, Synthesizer, Modular
# Type: Plugin, Standalone, VST, VST3, CLAP
# Category: Audio, Synthesizer

%global commit0 5ddd8a3ee5c2b0868d10d79c20c372d670fb97c9

Name: hexosynth
Version: 0.9.9
Release: 1%{?dist}
Summary: A hexagonal modular synthesizer plugin.
License: GPL-3.0-or-later
URL: https://github.com/WeirdConstructor/HexoSynth

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/WeirdConstructor/HexoSynth/archive/%{commit0}.zip#/hexosynth.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: rust
BuildRequires: cargo
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: python3

%description
Flashy Synthesia Like Software

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CALP version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}


%prep
%autosetup -n HexoSynth-%{commit0}

%build

%set_build_flags
export RUSTFLAGS="-g -O"

mkdir build
mkdir build/vst3
mkdir build/clap
mkdir build/vst

# Build jack standalone
./_build_release.sh
cp release/hexosynth_jack build/
cp target/release/libhexosynth.so build/vst/

# Build VTS3 and CLAP part
cd nih_plug
./build.sh
cd ..
cp -rav nih_plug/target/bundled/hexosynth_plug.vst3 build/vst3/
cp -rav nih_plug/target/bundled/hexosynth_plug.clap build/clap/

# Build standard audio
cd cpal_standalone
cargo build --release
cd ..
cp cpal_standalone/target/release/hexosynth_jack build/hexosynth

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 build/hexosynth_jack %{buildroot}/%{_bindir}/
install -m 755 build/hexosynth %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/hexosynth/examples/
cp -ra misc_patches/* %{buildroot}/%{_datadir}/hexosynth/examples/

install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 build/vst//libhexosynth.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr build/vst3/hexosynth_plug.vst3 %{buildroot}/%{_libdir}/vst3/
cp -vfr build/clap/hexosynth_plug.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.md
%license COPYING
%{_bindir}/hexosynth_jack
%{_bindir}/hexosynth
%{_datadir}/hexosynth/
%{_datadir}/hexosynth/examples/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Aug 21 2022 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Initial spec file
