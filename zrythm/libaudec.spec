Name:    libaudec-devel
Version: 0.3.4
Release: 1%{?dist}
Summary: libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
License: GPL-2.0-or-later
URL:     https://git.zrythm.org/zrythm/libaudec

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.zrythm.org/zrythm/libaudec/archive/v%{version}.tar.gz#/libaudec-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
%if 0%{?fedora} >= 36
Buildrequires: compat-ffmpeg4-devel
%else
BuildRequires: ffmpeg-devel
%endif
BuildRequires: meson

%description
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading
and resampling audio files, based on Robin Gareus' 'audio_decoder' code

%prep
%autosetup -n libaudec

%build

%meson
%meson_build 

%install 

%meson_install

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_includedir}/audec/*

%changelog
* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- update to 0.3.4-1

* Sat Feb 27 2021 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update to 0.3.3-1

* Sat Aug 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Sun May 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- update to 0.2.2-1

* Thu Mar 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
