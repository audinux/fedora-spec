Name:    spek
Version: 0.8.4
Release: 1%{?dist}
Summary: Acoustic spectrum analyser
License: GPLv3+
URL:     https://github.com/alexkay/spek

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/alexkay/spek/releases/download/v%{version}/spek-%{version}.tar.xz

BuildRequires: gcc-c++ gcc
BuildRequires: autoconf automake
%if 0%{?fedora} >= 36
Buildrequires: compat-ffmpeg4-devel
%endif
BuildRequires: ffmpeg-devel
BuildRequires: wxGTK3-devel
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils

%description
Spek is an acoustic spectrum analyser written in C++.
It uses FFmpeg libraries for audio decoding and wxWidgets for the GUI.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%if 0%{?fedora} >= 36
export AVCODEC_CFLAGS="-I/usr/include/compat-ffmpeg4"
export AVFORMAT_CFLAGS="-I/usr/include/compat-ffmpeg4"
export AVUTIL_CFLAGS="-I/usr/include/compat-ffmpeg4"
export CFLAGS="-I/usr/include/compat-ffmpeg4 $CFLAGS"
export CXXFLAGS="-I/usr/include/compat-ffmpeg4 $CXXFLAGS"
export LDFLAGS="-L/%{_libdir}/compat-ffmpeg4 $LDFLAGS"
%else
export AVCODEC_CFLAGS="-I/usr/include/ffmpeg"
export AVFORMAT_CFLAGS="-I/usr/include/ffmpeg"
export AVUTIL_CFLAGS="-I/usr/include/ffmpeg"
export CFLAGS="-I/usr/include/ffmpeg $CFLAGS"
export CXXFLAGS="-I/usr/include/ffmpeg $CXXFLAGS"
%endif

%configure
%make_build

%install

%make_install

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md MANUAL.md
%license LICENCE.md
%{_bindir}/*
%{_datadir}/applications/spek.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/locale/*
%{_mandir}//man1/spek.1.gz

%changelog
* Tue Aug 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.8.5-1
- Initial development
