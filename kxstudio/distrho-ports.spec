%global gittag0 2021-03-15

# Tag: Guitar, Equalizer, Convolution, Amp Simul, Overdrive
# Type: Plugin, LV2
# Category: Audio, Synthesizer, Effect

Name:    DISTRHO-Ports
Version: 1.1.0
Release: 4%{?dist}
Summary: A set of LV2 plugins
License: GPLv2+
URL:     https://github.com/DISTRHO/DISTRHO-Ports

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/DISTRHO-Ports/archive/%{gittag0}.tar.gz#/%{name}-%{gittag0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fftw-devel
BuildRequires: cmake
BuildRequires: meson

%description
A set of LV2 plugins
- SwankyAmp: tube amplifier simulation
- Vitalium: Synthesizer
- Chow: digital distortion effect. Useful for mixing guitars, drums, even vocals when a heavily degraded sound is desired
- TAL Dub-3, Filter, NoiseMaker, Reverb and Vocoder.
- KlangFalter: convolution audio plugin, e.g. for usage as convolution reverb.
- ...

%prep
%autosetup -n %{name}-%{gittag0}

sed -i -e "/-Wl,--strip-all/d" meson.build

%build

%set_build_flags

%meson -Dbuild-lv2=true -Dbuild-vst3=true
%meson_build 

%install 

%meson_install

%files
%doc README.md
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_libdir}/vst3/*

%changelog
* Mon Mar 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.4-4
- update to 2021-03-15 (1.0.3)

* Fri Jan 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.3-4
- update to 2021-01-15 (1.0.3)

* Wed Dec 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-4
- update to 2020-12-27 (1.0.2)

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-4
- fix debug build

* Tue Jul 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-4
- update to 2020-07-14 (1.0.1)

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-4
- update to 7e62235e809e59770d0d91d2c48c3f50ce7c027a

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update to a82fff059baafc03f7c0e8b9a99f383af7bfbd79

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-2
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build
