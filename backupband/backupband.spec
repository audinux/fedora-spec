# Tag: Jack, Editor, Sequencer
# Type: Standalone
# Category: Audio, Synthesizer

%global commit0 21ef45e42c95fdd0484148ca7e9724ce52ca5c9b

Name:    backupband
Version: 04282023
Release: 1%{?dist}
Summary: An automatic orchestra
URL:     https://sourceforge.net/projects/backupband
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/code-snapshots/git/b/ba/backupband/code.git/backupband-code-%{commit0}.zip#/%{name}-%{version}.zip
Source1: https://sourceforge.net/projects/backupband/files/manual.zip
Source2: https://sourceforge.net/projects/backupband/files/extra_44k.zip
Source3: https://sourceforge.net/projects/backupband/files/instruments_44k.zip
Source4: https://sourceforge.net/projects/backupband/files/extra_48k.zip
Source5: https://sourceforge.net/projects/backupband/files/instruments_48k.zip
Source6: https://sourceforge.net/projects/backupband/files/backupband.zip

BuildRequires: gcc gcc-c++
BuildRequires: unzip
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: cairo-devel

%description
BackupBand is a music auto-arranger. It has a virtual drummer, bassist,
and rhythm guitarist. These 3 "musicians" follow your chord changes live
(as you play some MIDI instrument, such as a keyboard) and they play along
with you in perfect time. It's like having a live rhythm section
backing you up.

The rhythm section knows how to play in 60 different styles such as Rock,
Disco, HipHop, Heavy Metal, Reggae, Swing, various latin styles, etc.
You can also create your own styles for them to play.

The bassist plays a rickenbacker, fender precision, synth, and double (acoustic)
bass. The guitarist plays a les paul, steel string, and nylon string.
The drummer plays 6 kits. You can also create your own multi-sampled guitars,
basses, and kits for them to play.

%prep
%autosetup -n backupband-code-%{commit0}

# https://sourceforge.net/projects/backupband/files/manual.zip
# Docs
unzip %{SOURCE1}

# https://sourceforge.net/projects/backupband/files/extra_44k.zip
# Instruments
unzip %{SOURCE2}

# https://sourceforge.net/projects/backupband/files/instruments_44k.zip
# Instruments
unzip %{SOURCE3}

# https://sourceforge.net/projects/backupband/files/extra_48k.zip
# Instruments
unzip %{SOURCE4}

# https://sourceforge.net/projects/backupband/files/instruments_48k.zip
# Instruments
unzip %{SOURCE5}

# https://sourceforge.net/projects/backupband/files/backupband.zip
# Styles
unzip %{SOURCE6}

mv BackupBand BackupBandData

sed -i -e "s/DEBUGFLAGS=-O/DEBUGFLAGS=-O2 -g/g" Makefile

%build

make

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libexecdir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/

install -m 755 BackupBand %{buildroot}/%{_datadir}/%{name}/
install -m 755 BackupBandNoGui %{buildroot}/%{_datadir}/%{name}/
install -m 755 ConvertWave %{buildroot}/%{_datadir}/%{name}/
install -m 755 StyleEdit %{buildroot}/%{_datadir}/%{name}/

ln -s %{_datadir}/%{name}/BackupBand %{buildroot}%{_bindir}/BackupBand
ln -s %{_datadir}/%{name}/BackupBandNoGui %{buildroot}%{_bindir}/BackupBandNoGui
ln -s %{_datadir}/%{name}/ConvertWave %{buildroot}%{_bindir}/ConvertWave
ln -s %{_datadir}/%{name}/StyleEdit %{buildroot}%{_bindir}/StyleEdit

install -m 755 -d %{buildroot}/%{_libdir}/
install -m 755 libwavecmp.so %{buildroot}/%{_libdir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/Docs
cp -ra BackupBandData/Docs/* %{buildroot}/%{_datadir}/%{name}/Docs/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/Instruments
cp -ra BackupBandData/Instruments/* %{buildroot}/%{_datadir}/%{name}/Instruments/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/Styles
cp -ra BackupBandData/Styles/* %{buildroot}/%{_datadir}/%{name}/Styles/

%files
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Fri Apr 28 2023 Yann Collette <ycollette.nospam@free.fr> - 04272023-1
- Initial spec file
