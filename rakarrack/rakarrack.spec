# Tag: Guitar, Amp Simul
# Type: Plugin, VST
# Category: Audio, Effect
# LastSourceUpdate: 2010

Summary: Guitar Amplifier emulator
Name:    rakarrack
Version: 0.6.3
Release: 2%{?dist}
License: GPL
URL:     http://rakarrack.sourceforge.net/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ycollet/rakarrack/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: alsa-utils
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: libXpm-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: desktop-file-utils
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
This app was born after an informal conversation about effects for guitar using GNU/linux.
The major part of this apps are discontinued or simply not have new versions after few
years. Josep Andreu say on the IRC chat 'I can made an app based on the effects set
hiden on code of ZynAddSubFX (by Paul Nasca Octavian)'. Some time after here is the
result of our work...

This app has 42 effects:
  * EQ Lineal
  * Compressor
  * Distortion
  * Overdrive
  * Echo
  * Chorus
  * Phaser
  * Flanger
  * Reverb
  * Parametric EQ
  * Wah Wah
  * Alienwha
  * Harmonizer
  * etc.
The effects are procesed in cascade... The order of effects are configurable by the user.
The state of rack can be saved as 'presets'. Sets of presets can be stored as 'banks'.
The rack also has an integrated tuner and can receive MIDI control orders and can send MIDI
notes to MIDI devices like synthesizers.

%prep
%autosetup -n %{name}-%{version}

%build

./autogen.sh
%configure
%make_build

%install
%make_install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/rakarrack.desktop

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/doc/*
%{_datadir}/man/*
%{_datadir}/pixmaps/*
%{_datadir}/rakarrack/

%changelog
* Wed Nov 4 2020 Yann Collette <ycollette dot nospam at free.fr> 0.6.3-2
- update to 0.6.3-2

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- update for Fedora 29

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.5.1-1
- initial release
