# Tag: MIDI
# Type: Standalone
# Category: DAW, Audio

Name:    stargate
Version: 22.11.6
Release: 1%{?dist}
Summary: Digital audio workstations, instrument and effect plugins
License: GPLv3
URL:     http://github.com/stargateaudio/stargate/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/stargateaudio/stargate/archive/refs/tags/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: jq
BuildRequires: make
BuildRequires: libsndfile-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: python3-devel 
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

Requires: alsa-lib
Requires: fftw
Requires: lame
Requires: libsndfile
Requires: portaudio
Requires: portmidi
Requires: python3
Requires: python3-jinja2
Requires: python3-mido
Requires: python3-mutagen
Requires: python3-numpy
Requires: python3-psutil
Requires: python3-pyyaml
Requires: python3-pymarshal
Requires: python3-wavefile
Requires: (python3-qt6 or python3-qt5)
Requires: rubberband
Requires: vorbis-tools 

Recommends: ffmpeg 

%description
Stargate is digital audio workstations (DAWs), instrument and effect plugins

%prep
%autosetup -n %{name}-release-%{version}

%build

export PLAT_FLAGS=-fPIC

cd src
%make_build PIP=true

%install
cd src
export DONT_STRIP=1
%make_install PIP=true

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/stargate.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/stargate.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/stargate
%{_bindir}/stargate-engine
%{_bindir}/stargate-engine-dbg
%{_bindir}/stargate-sbsms
%{_datadir}/doc/stargate/copyright
%{_datadir}/applications/*
%{_datadir}/mime/*
%{_datadir}/pixmaps/*
%{_datadir}/stargate/*

%changelog
* Thu Nov 24 2022 Yann Collette <ycollette.nospam@free.fr> - 22.11.6-1
- update to 22.11.6-1

* Sun Nov 20 2022 Yann Collette <ycollette.nospam@free.fr> - 22.11.5-1
- update to 22.11.5-1

* Thu Nov 17 2022 Yann Collette <ycollette.nospam@free.fr> - 22.11.4-1
- update to 22.11.4-1

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 22.10.1-1
- update to 22.10.1-1

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> - 22.07.1-1
- update to 22.07.1-1

* Thu Mar 03 2022 Yann Collette <ycollette.nospam@free.fr> - 22.03.1-1
- update to 22.03.1-1

* Mon Jan 31 2022 Yann Collette <ycollette.nospam@free.fr> - 22.02.1-1
- update to 22.02.1-1

* Thu Jan 06 2022 Yann Collette <ycollette.nospam@free.fr> - 22.01.1-1
- update to 22.01.1-1

* Mon Dec 20 2021 Yann Collette <ycollette.nospam@free.fr> - 21.12.3-1
- update to 21.12.3-1

* Sun Dec 12 2021 Yann Collette <ycollette.nospam@free.fr> - 21.12.2-1
- update to 21.12.2-1

* Wed Dec 01 2021 Yann Collette <ycollette.nospam@free.fr> - 21.12.1-1
- update to 21.12.1-1

* Fri Nov 26 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.7-1
- update to 21.11.7-1

* Wed Nov 17 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.6-1
- update to 21.11.6-1

* Sun Nov 14 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.5-1
- update to 21.11.5-1

* Sat Nov 13 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.4-1
- update to 21.11.4-1

* Mon Nov 08 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.3-1
- update to 21.11.3-1

* Sun Nov 07 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.2-1
- update to 21.11.2-1

* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.1-1
- initial spec

