Summary: GUI tool to split WAV, MP2 and MP3 files
Name:    wavbreaker
Version: 0.16
Release: 1%{?dist}
License: GPL-2.0-or-later
URL:     https://github.com/thp/wavbreaker

Vendor:       Audinux
Distribution: Audinux

Source:  https://github.com/thp/wavbreaker/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: mpg123-devel
BuildRequires: libao-devel
BuildRequires: desktop-file-utils

%description
This application's purpose in life is to take a WAV file and break it up into multiple WAV files.
It makes a clean break at the correct position to burn the files to an Audio CD without any dead
air between the tracks.
wavbreaker also supports breaking up MP2 and MP3 files without re-encoding meaning it's fast and
there is no generational loss. Decoding (using mpg123) is only done for playback and waveform
display.
The GUI displays a waveform summary of the entire file at the top. The middle portion displays a
zoomed-in view that allows you to select where to start playing and where it will make the break.
The bottom portion contains a list of track breaks. You may change file names and uncheck parts
that you do not want to have written out to disk when saving.
There is also a command line tool wavmerge to merge WAV files together. If you download a show
and don't like how it was tracked, you can merge them together with wavmerge and then break them
back up with wavbreaker. The wavmerge tool will only work on files that have the same format
(for example, 44.100 Hz sample rate, 16-bit sample size, etc.).

%prep
%autosetup

%build

%meson
%meson_build

%install

%meson_install

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/net.sourceforge.wavbreaker.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/net.sourceforge.wavbreaker.desktop

%files
%doc AUTHORS README.md CHANGELOG.md CONTRIBUTORS
%license COPYING
%{_bindir}/*
%{_datadir}/applications/net.sourceforge.wavbreaker.desktop
%{_datadir}/icons/hicolor/scalable/apps/net.sourceforge.wavbreaker.svg
%{_datadir}/locale/*
%{_mandir}/man1/*
%{_metainfodir}/net.sourceforge.wavbreaker.appdata.xml

%changelog
* Tue Jan 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.16-1
- update to 0.16-1

* Mon Apr 11 2022 Yann Collette <ycollette.nospam@free.fr> - 0.14-1
- initial build
