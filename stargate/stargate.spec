# Tag: MIDI, Sequencer
# Type: Standalone
# Catagory: DAW, Audio, Sequencer

%define __provides_exclude_from ^%{_usr}/lib/stargate/.*$
%global __python %{__python3}

Name:    stargate
Version: 21.11.1
Release: 1%{?dist}
Summary: Digital audio workstations, instrument and effect plugins
License: GPLv3
URL:     http://github.com/stargateaudio/stargate/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/stargateaudio/stargate/archive/stargate-%{version}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: jq
BuildRequires: libsndfile-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: python3-devel 
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
%autosetup

# Deactivate automatic installation of wavefile and pymarshal
sed -i -e "s/ py_vendor commit_hash/ commit_hash/g" Makefile
sed -i -e "s/cp -r sg_py_vendor/cp -r /g" Makefile
# Relocate lib dir into lib64 on 64 bits architecture
%ifarch x86_64 amd64
# sed -i -e "s/'lib'/'%{_lib}'/g" sglib/lib/path/linux.py
%endif

%build
%make_build

%install
export DONT_STRIP=1
%make_install

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
%{_bindir}/stargate
%{_bindir}/stargate-engine
%{_bindir}/stargate-engine-dbg
%{_bindir}/stargate-paulstretch
%{_bindir}/stargate-sbsms
%{_datadir}/
%{_usr}/lib/stargate

%changelog
* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> - 21.11.1-1
- initial spec

