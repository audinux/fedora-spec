# Tag: Audio, Editor, Tool
# Type: Standalone
# Category: Tool, Audio

Summary: Replaygain functionality for WAV audio files
Name: wavegain
Version: 1.3.2
Release: 1%{?dist}
License: LGPL
URL: https://github.com/MestreLion/wavegain
ExclusiveArch: x86_64 

Source:	https://github.com/MestreLion/wavegain/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Vendor:       Audinux
Distribution: Audinux

BuildRequires: gcc
BuildRequires: make
BuildRequires: alsa-lib-devel

%description
WaveGain is an application of the ReplayGain algorithms to standard PCM wave
files. Calculated gain adjustments are applied directly to the audio data,
instead of just writing metadata as traditionally done for other formats
like MP3, FLAC and Ogg Vorbis.

The replaygain values can also be added as metadata in a custom RIFF chunk
named 'gain'. This could theoretically allow WAV files to have same lossless
functionality as other formats where audio data is not altered. But since no
current players are aware of this "standard", the metadata is used only by
WaveGain for the "--undo-gain" feature, which is lossy.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "/CFLAGS  += -m32/d" Makefile
sed -i -e "/CFLAGS +=/d" Makefile
sed -i -e "s/install -s/install/g" Makefile

%build

%set_build_flags

%make_build

%install

%make_install prefix=/usr

install -m 755 -d %{buildroot}/%{_mandir}/man1/
cp debian/wavegain.1 %{buildroot}/%{_mandir}/man1/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
cp -ra doc/manual/* %{buildroot}/%{_datadir}/%{name}/doc/

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/doc/*
%{_mandir}/man1/*

%changelog
* Thu May 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.2-1
- Initial version of the spec
