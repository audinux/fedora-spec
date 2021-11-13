# Tag: Live
# Type: Standalone
# Category: Graphic

Name:    lebiniou
Version: 3.63.3
Release: 3%{?dist}
Summary: Audio spectrum visualizer
URL:     https://biniou.net/
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/lebiniou/lebiniou/-/archive/version-%{version}/lebiniou-version-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make sed
BuildRequires: autoconf automake libtool
BuildRequires: pulseaudio-libs-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libcaca-devel
BuildRequires: fftw-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: freetype-devel
BuildRequires: pandoc
BuildRequires: libsndfile-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: ImageMagick-devel
BuildRequires: ffmpeg-devel
BuildRequires: jansson-devel
BuildRequires: ulfius-devel
BuildRequires: ffmpeg-devel
BuildRequires: perl-podlators
BuildRequires: gtk-update-icon-cache
BuildRequires: python3-htmlmin
BuildRequires: desktop-file-utils

Requires(pre): lebiniou-data

%description
As an artist, composer, VJ or just fan, lebiniou allows you
to create live visuals based on your audio performances or
existing tracks.
As a listener, lebiniou allows you to watch an everlasting and
totally unseen creation reacting to the music.

%prep
%autosetup -n %{name}-version-%{version}

sed -i -e "s/LEBINIOU_LIBDIR=\"\$prefix\/lib\"/LEBINIOU_LIBDIR=\"\$prefix\/%{_lib}\"/g" configure.ac

%build

%set_build_flags

autoreconf --install

CFLAGS=" -I/usr/include/ffmpeg $CFLAGS"; export CFLAGS

%configure --prefix=%{_prefix} \
	   --without-cleancss \
	   --without-uglifyjs \
	   --enable-alsa \
	   --enable-pulseaudio \
	   --enable-sndfile \
	   --enable-caca \
	   --enable-jackaudio \
	   --libdir=%{_libdir}

%make_build

%install

%make_install

desktop-file-install                         \
  --add-category="AudioVideo"                \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/net.biniou.LeBiniou.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/net.biniou.LeBiniou.desktop

%files
%doc README.md AUTHORS ChangeLog THANKS
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Sat Nov 13 2021 Yann Collette <ycollette.nospam@free.fr> - 3.63.3-3
- update to 3.63.3-3

* Thu Nov 11 2021 Yann Collette <ycollette.nospam@free.fr> - 3.63.2-3
- update to 3.63.2-3

* Sun Nov 07 2021 Yann Collette <ycollette.nospam@free.fr> - 3.63.1-3
- update to 3.63.1-3

* Tue Nov 02 2021 Yann Collette <ycollette.nospam@free.fr> - 3.63.0-3
- update to 3.63.0-3

* Sat Sep 25 2021 Yann Collette <ycollette.nospam@free.fr> - 3.62.1-3
- update to 3.62.1-3

* Sun Sep 12 2021 Yann Collette <ycollette.nospam@free.fr> - 3.62.0-3
- update to 3.62.0-3

* Mon Aug 30 2021 Yann Collette <ycollette.nospam@free.fr> - 3.61.2-3
- update to 3.61.2-3

* Mon Aug 23 2021 Yann Collette <ycollette.nospam@free.fr> - 3.61.1-3
- update to 3.61.1-3

* Wed Aug 18 2021 Yann Collette <ycollette.nospam@free.fr> - 3.61.0-3
- update to 3.61.0-3

* Sat Jul 03 2021 Yann Collette <ycollette.nospam@free.fr> - 3.60.1-3
- update to 3.60.1-3

* Sun May 02 2021 Yann Collette <ycollette.nospam@free.fr> - 3.56.1-3
- update to 3.56.1-3

* Sat May 01 2021 Yann Collette <ycollette.nospam@free.fr> - 3.56.0-3
- update to 3.56.0-3

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 3.55.0-3
- update to 3.55.0-3

* Wed Feb 17 2021 Yann Collette <ycollette.nospam@free.fr> - 3.54.1-3
- update to 3.53.1-3

* Sun Feb 14 2021 Yann Collette <ycollette.nospam@free.fr> - 3.54.0-3
- update to 3.54.0-3

* Fri Jan 29 2021 Yann Collette <ycollette.nospam@free.fr> - 3.53.3-3
- update to 3.53.3-3

* Wed Jan 20 2021 Yann Collette <ycollette.nospam@free.fr> - 3.53.2-3
- update to 3.53.2-3

* Wed Jan 20 2021 Yann Collette <ycollette.nospam@free.fr> - 3.53.1-3
- update to 3.53.1-3

* Mon Jan 18 2021 Yann Collette <ycollette.nospam@free.fr> - 3.53-3
- update to 3.53-3

* Sun Jan 3 2021 Yann Collette <ycollette.nospam@free.fr> - 3.52-3
- update to 3.52-3

* Mon Dec 7 2020 Yann Collette <ycollette.nospam@free.fr> - 3.51-3
- update to 3.51-3

* Sat Oct 31 2020 Yann Collette <ycollette.nospam@free.fr> - 3.50-3
- update to 3.50-3

* Wed Aug 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.43.1-3
- update to 3.43.1-3

* Mon Jul 13 2020 Yann Collette <ycollette.nospam@free.fr> - 3.43-3
- update to 3.43

* Tue May 12 2020 Yann Collette <ycollette.nospam@free.fr> - 3.42.1-3
- update to 3.42.1

* Thu Apr 30 2020 Yann Collette <ycollette.nospam@free.fr> - 3.41-3
- update to 3.41

* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 3.40-3
- fix for Fedora 32

* Mon Feb 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.40-2
- update to 3.40

* Fri Dec 6 2019 Yann Collette <ycollette.nospam@free.fr> - 3.32-2
- fix path

* Fri Dec 6 2019 Yann Collette <ycollette.nospam@free.fr> - 3.32-1
- update to 3.32

* Fri May 17 2019 Yann Collette <ycollette.nospam@free.fr> - 3.31-1
- initial spec file
