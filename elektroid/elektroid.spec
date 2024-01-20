# Tag: Tool
# Type: Standalone
# Category: Tool, MIDI. Audio

Name: elektroid
Summary: Sample and MIDI device manager
Version: 3.0
Release: 1%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/dagargo/elektroid

Vendor:       Audinux
Distribution: Audinux

Source: https://github.com/dagargo/elektroid/releases/download/%{version}/elektroid-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: gettext-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtk3-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: json-glib-devel
BuildRequires: libzip-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Elektroid is a sample and MIDI device manager. It includes the
elektroid GUI application and the elektroid-cli CLI application.

%prep
%autosetup -n %{name}-%{version}

autoreconf --install --force

%build

%configure
%make_build

%install

%make_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/elektroid/
%{_datadir}/icons/hicolor/*
%{_datadir}/locale/*
%{_datadir}/metainfo/elektroid.appdata.xml
%{_datadir}/man/*

%changelog
* Sat Jan 20 2024 Yann Collette <ycollette.nospam@free.fr> - 3.0-1
- update to 3.0-1

* Wed Apr 26 2023 Yann Collette <ycollette.nospam@free.fr> - 2.5.2-1
- initial build
