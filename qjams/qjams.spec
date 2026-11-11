# Status: active
# Tag: Effect
# Type: LV2
# Category: Effect

Name: qjams
Version: 1.0.1
Release: 1%{?dist}
Summary: Musician 12-track audio&video recording&jam DAW
License: GPL-2.0-or-later
URL: https://github.com/robw-nl/QJams
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/robw-nl/QJams/archive/refs/tags/QJams_v1.0.1.tar.gz

BuildRequires: gcc
BuildRequires: (ffmpeg-free-devel or ffmpeg-devel)
BuildRequires: gtk4-devel
BuildRequires: rubberband-devel
BuildRequires: libsndfile-devel
BuildRequires: libarchive-devel
BuildRequires: pkgconfig(jack)

%description
Bring backing tracks, multi-track recording, synchronized video, editing,
playlists and practice sessions together in one focused Linux application.
Build a backing track in seconds or complete composition or practice session
in minutes. Record yourself with synchronized video. Switch inputs while
recording.
Adjust levels while you play. Slow down your recordings to analyze your playing.
Stack your tracks safely with automatic clipping prevention. Edit what you need
without getting buried in a full-sized DAW.
I designed QJams around one core idea: start playing quickly or create a full
composition quickly, and keep the software out of the way. With its unique,
lightning-fast workflow, QJams is unlike any traditional DAW.
Built for guitarists. Ready for musicians. Made for Linux. Developed in C.

%prep
%autosetup -n QJams-QJams_v%{version}

%build

%set_build_flags

gcc *.c -I. $CFLAGS $LDFLAGS `pkg-config --cflags --libs gtk4 libavcodec libavformat libavutil libavdevice libavfilter libswscale libswresample rubberband sndfile libarchive jack` -lm -o qjams

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 qjams %{buildroot}/%{_bindir}/
%files
%doc README.md
%{_bindir}/*

%changelog
* Wed Nov 11 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- initial version of the spec
