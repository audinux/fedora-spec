# Tag: Video
# Type: Standalone
# Category: Graphic, Tool

Name:    harvid
Version: 0.8.3
Release: 2%{?dist}
Summary: harvid -- HTTP Ardour Video Daemon
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

URL:     https://github.com/x42/harvid
Source0: https://github.com/x42/harvid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: libXrender-devel
BuildRequires: libX11-devel
BuildRequires: ffmpeg-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: vim-common
BuildRequires: libpng-devel

Requires: ffmpeg
Requires: xjadeo

%description
Harvid decodes still images from movie files and serves them via HTTP.
Its intended use-case is to efficiently provide frame-accurate data and
act as second level cache for rendering the video-timeline in Ardour - https://ardour.org.

%prep
%autosetup -n %{name}-%{version}

sed -i -e "19,21d" src/Makefile

%build

%make_build PREFIX=/usr -j1

%install

%make_install PREFIX=/usr

mkdir -p %{buildroot}/usr/bin
ln -s /usr/bin/ffmpeg %{buildroot}/usr/bin/ffmpeg_harvid 
ln -s /usr/bin/ffprobe%{buildroot}/usr/bin/ffprobe_harvid

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/*
%{_mandir}/*
%{_datadir}/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-2
- fix for Fedora 33

* Sun Dec 2 2018 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- initial spec file
