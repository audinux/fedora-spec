# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name: aloop
Version: 0.2
Release: 1%{?dist}
Summary: Audio File Looper for Linux
License: GPL-2.0-or-later
URL: https://github.com/brummer10/aloop
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/aloop/releases/download/v%{version}/aloop-v%{version}-src.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: libX11-devel
BuildRequires: libsndfile-devel
BuildRequires: portaudio-devel

%description
aloop is a audio file looper for Linux using PortAudio as backend (jack, pulse, alsa),
libsndfile to load sound files and zita-resampler to resample the files when needed.
The GUI is created with libxputty.

%prep
%autosetup -n %{name}-v%{version}

%build

%make_build STRIP=true

%install

%make_install STRIP=true

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Feb 03 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- update to 0.2-1

* Sat Feb 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
