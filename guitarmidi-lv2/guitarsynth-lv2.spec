Name:    guitarsynth
Version: 0.1
Release: 1%{?dist}
Summary: GuitarSynth is a set of wavetable synths controlled by a monophonic pitchdetector
URL:     https://github.com/geraldmwangi/GuitarSynth-DPF
License: LGPLv2+

Vendor:       Audinux
Distribution: Audinux

# Usage: ./guitarsynth-lv2-source.sh <TAG>
#        ./guitarsynth-lv2-source.sh master

Source0: GuitarSynth-DPF.tar.gz
Source1: guitarsynth-lv2-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: aubio-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel

%description
GuitarSynth is a set of wavetable synths controlled by a monophonic pitchdetector.
Actually it is not specific to guitars but can be used for any harmonic instrument
when playing single notes. This is a small petproject of mine to explore the
possibilities of pitchdetection for Guitars. It uses aubio for pitch detection,
but that will change as I want to write my own detector.

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.
Requires: %{name}

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%package -n vst-%{name}
Summary: VST2 version of the %{name} plugin.
Requires: %{name}

%description -n vst-%{name}
VST2 version of the %{name} plugin.

%package -n ladspa-%{name}
Summary: LADSPA version of the %{name} plugin.
Requires: %{name}

%description -n ladspa-%{name}
LADSPA version of the %{name} plugin.

%prep
%autosetup -n GuitarSynth-DPF

sed -i -e "s/-Wl,--strip-all//g" Makefile.mk
sed -i -e "s/-Wl,--strip-all//g" dpf/dgl/Makefile.mk

%ifarch aarch64
sed -i -e "s/-msse -msse2//g" Makefile.mk
sed -i -e "s/-msse -msse2//g" dpf/dgl/Makefile.mk
sed -i -e "s/-mfpmath=sse//g" Makefile.mk
sed -i -e "s/-mfpmath=sse//g" dpf/dgl/Makefile.mk
%endif

%build

%make_build

%install

install -d 755 %{buildroot}/%{_libdir}/lv2
install -d 755 %{buildroot}/%{_libdir}/vst
install -d 755 %{buildroot}/%{_libdir}/ladspa
install -d 755 %{buildroot}/%{_bindir}/

cp bin/GuitarSynth %{buildroot}/%{_bindir}/

cp bin/GuitarSynth-ladspa.so %{buildroot}/%{_libdir}/ladspa
cp -ra bin/GuitarSynth.lv2 %{buildroot}/%{_libdir}/lv2/
cp bin/GuitarSynth-vst.so %{buildroot}/%{_libdir}/vst

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%changelog
* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version of the spec file
