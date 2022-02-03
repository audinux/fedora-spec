Name:    seq42
Version: 1.1.4
Release: 1%{?dist}
Summary: MIDI sequencer
License: GPL
URL:     https://github.com/Stazed/seq42

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Stazed/seq42/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: lash-devel
BuildRequires: liblo-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig

%description
It's a fork of seq24 (which is a fork of the original seq24),
but with a greater emphasis on song editing (as opposed to live looping)
and some enhancements. seq24 is great for sequence editing and live looping,
but I found it cumbersome to edit songs as the number of sequences
grew (I would quickly reach a point where there were more sequence rows
in the song editor than would fit on my screen without scrolling, which
made it difficult to keep track of the whole song).

%prep
%autosetup -n %{name}-%{version}

%build

autoreconf -i

%configure
%make_build

%install

%make_install

%files
%doc ChangeLog INSTALL NEWS README.md TODO
%license COPYING

%{_bindir}/*
%{_datadir}/*

%changelog
* Mon May 03 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-1
- initial version
