# Global variables for github repository
%global commit0 ad624e7e46b043183d3ab669e6cf54cba887e1a6
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    postfish
Version: 2005.01.01
Release: 2%{?dist}
Summary: The Postfish is a digital audio post-processing, restoration, filtering and mixdown tool.
License: GPLv2+
URL:     https://gitlab.xiph.org/xiph/postfish

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.xiph.org/xiph/%{name}/-/archive/%{commit0}/postfish-%{commit0}.tar.gz
Source1: postfish.png
Source2: Makefile.postfish

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: libao-devel
BuildRequires: gzip
BuildRequires: perl

%description
The Postfish is a digital audio post-processing, restoration, filtering and mixdown tool.
It works as a linear audio filter, much like a rack of analog effects.
The first stage of the filter pipeline provides a bank of configurable per-channel processing filters for up to 32 input channels.
The second stage provides mixdown of the processed input audio into a group of up to eight output channels.
The third stage applies processing filters to the output group post-mixdown.

The Postfish is a stream filter; feed it audio from a list of files or input stream, and it renders audio to standard out, as well as
optionally providing a configurable audio playback monitor via a sound device.
If the input audio is being taken from files, Postfish also provides simple forward/back/cue seeking and A-B looping control.
The next major update of Postfish will also include automation to allow mixdown settings to be 'recorded' and applied automatically during rendering.

%prep
%autosetup -n postfish-%{commit0}

cp %{SOURCE2} Makefile

%build

%set_build_flags

%make_build all

%install

mkdir -p %{buildroot}%{_sysconfdir}/postfish/
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/man/man1/
mkdir -p %{buildroot}%{_datadir}/applications/

install -m 755 postfish %{buildroot}%{_bindir}/
install -m 644 %{S:1} %{buildroot}%{_datadir}/pixmaps/postfish.png
install -m 644 postfish.1 %{buildroot}%{_datadir}/man/man1/postfish.1
gzip %{buildroot}%{_datadir}/man/man1/postfish.1
install -m 644 postfish-wisdomrc %{buildroot}%{_sysconfdir}/postfish-wisdomrc

cat > %{buildroot}%{_datadir}/applications/postfish.desktop << EOF
[Desktop Entry]
Name=PostFish
Comment=Digital audio post-processing tool.
Exec=/usr/bin/postfish
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/postfish.png
Categories=AudioVideo;
EOF

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/*
%{_sysconfdir}/*

%changelog
* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 2005.01.01-2
- fix debug build + update to gitlab version

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2005.01.01-1
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 2005.01.01-1
- switch to 19646

* Wed Sep 13 2017 Yann Collette <ycollette.nospam@free.fr> - 2005.01.01-1
- Initial version
