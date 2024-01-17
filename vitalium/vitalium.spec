%define _lto_cflags %{nil}

%global commit0 65f1fe6c8917de717fe0d30f58b326f1f602ebdd
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    vitalium
Version: 1.0.0
Release: 1%{?dist}
Summary: A LV2 / VST3 / standalone wavetable synth
License: GPL-2.0-or-later
URL:     https://vital.audio

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mtytel/vital/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(jack)
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: libsecret-devel

%description
Vitalium is a powerful wavetable synthesizer with realtime modulation feedback
vitalium is a MIDI enabled polyphonic music synthesizer with an easy to use
parameter modulation system with real-time graphical feedback.

%prep
%autosetup -n vital-%{commit0}

# Disable VST
sed -i -e "s/vst vst3/vst3/g" Makefile
sed -i -e "s/install_vst install_vst3/install_vst3/g" Makefile
sed -i -e "s/install_effects_vst install_effects_vst3/install_effects_vst3/g" Makefile
# Disable installation of icons
sed -i -e "s/standalone install_icons/standalone/g" Makefile
# Rename executable
find . -name "Makefile*" -exec sed -i -e "s/[vV]ial/vitalium/g" {} \;
# remove icon from desktop
sed -i -e "/Icon=/d" standalone/vital.desktop

unzip %{SOURCE1}

%build

# %set_build_flags
# %make_build CONFIG=Release STRIP=true LIBDIR=%{_libdir} PROGRAM=vitalium LIB_PROGRAM=Vitalium LIB_PROGRAM_FX=VitaliumFX
make DESTDIR=%{buildroot} CONFIG=Release CXXFLAGS=-I`pwd`/VST_SDK/VST2_SDK STRIP=true LIBDIR=%{_libdir} standalone vst3 lv2

%install

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_libdir}/vst3/vitalium.vst3/Contents/x86_64-linux/
mkdir -p %{buildroot}%{_libdir}/lv2/vitalium.lv2/
mkdir -p %{buildroot}%{_datadir}/applications/

cp standalone/builds/linux/build/vitalium %{buildroot}%{_bindir}/

cp plugin/builds/linux_vst/build/vitalium.vst3/Contents/x86_64-linux/vitalium.so %{buildroot}%{_libdir}/vst3/vitalium.vst3/Contents/x86_64-linux/

cp -ra plugin/builds/linux_lv2/vitalium.lv2/* %{buildroot}%{_libdir}/lv2/vitalium.lv2/

install -m644 standalone/vital.desktop %{buildroot}%{_datadir}/applications/vitalium.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst3/*
%{_datadir}/applications/*

%changelog
* Wed Feb 24 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial build
