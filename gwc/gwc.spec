# Tag: Tool, Alsa, Editor
# Type: Standalone
# Category: Audio, Tool

%define gwc_version 0.22
%define gwc_subversion 06

Name:   gtk-wave-cleaner
Version: %{gwc_version}.%{gwc_subversion}
Release: 1%{?dist}
Summary: Gtk Wave Cleaner -- audio restoration application
License: GPL
URL:     https://gwc.sourceforge.net/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/AlisterH/gwc/releases/download/%{gwc_version}-%{gwc_subversion}/%{name}-%{gwc_version}-%{gwc_subversion}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: gtk2-devel
BuildRequires: libogg-devel
BuildRequires: lame-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: desktop-file-utils

%description
Gtk (formerly GNOME) Wave Cleaner (GWC) is a tool for cleaning up noisy audio files in
preparation for burning to CDs. The typical application is to record
the audio from vinyl LPs, 45s, 78s, etc, to a hard disk as a 16-bit,
stereo, 44.1khz wave formatted file and then use GWC to apply denoising
and declicking algorithms.

%prep
%autosetup -n %{name}-%{gwc_version}-%{gwc_subversion}

sed -i -e "/CFLAGS =/d" meschach/makefile.in

%build

%set_build_flags

export OPT_CFLAGS="-Wno-implicit-int -Wno-implicit-function-declaration $CFLAGS"
export CFLAGS="-Wno-implicit-int -Wno-implicit-function-declaration $CFLAGS"

%configure --enable-ogg --enable-mp3 --enable-pa
%make_build

%install

%make_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README Changelog gtk-wave-cleaner.html gtkrc-example.txt COPYING INSTALL TODO
%license COPYING
%{_bindir}/*
%{_datadir}/applications/gtk-wave-cleaner.desktop
%{_datadir}/icons/hicolor/128x128/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/16x16/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/22x22/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/24x24/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/256x256/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/32x32/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/64x64/apps/gtk-wave-cleaner.png
%{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/scalable/apps/gtk-wave-cleaner.svg

%changelog
* Sat Aug 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.22-06-1
- initial spec
