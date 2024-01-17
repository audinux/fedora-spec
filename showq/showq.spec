# Global variables for github repository
%global commit0 b17f99891895109663c7fddb32e93de59ee91d1f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    showq
Version: 0.0.1
Release: 1%{?dist}
Summary: MIDI controlable audio player
License: GPL
URL:     https://github.com/evandelisle/showq

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: libxml++-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: libuuid-devel
BuildRequires: meson

%description
ShowQ is audio / MIDI trigger software for theatre productions.

%prep
%autosetup -n %{name}-%{commit0}

%build

%meson
%meson_build

%install

%meson_install

%files
%doc changes README.md doc/howto
%license COPYING
%{_bindir}/*

%changelog
* Mon Dec 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial version
