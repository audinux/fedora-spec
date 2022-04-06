# Global variables for github repository
%global commit0 aaf94dfb1fd598dee0f52ad7a644ca01029691c7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Analyzer
# Type: Standalone
# Category: Audio, Tool

Name:    tsunami
Version: 0.7.90.%{shortcommit0}
Release: 2%{?dist}
Summary: A simple but powerful audio editor
URL:     https://github.com/momentarylapse/tsunami
License: GPLv3

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/momentarylapse/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: gtk3-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel 
BuildRequires: libogg-devel 
BuildRequires: flac-devel
BuildRequires: fftw-devel
BuildRequires: libunwind-devel
BuildRequires: libsndfile-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
Tsunami is an open-source digital audio workstation (DAW).
It is designed for ease of use and not-looking-crappy™.

%prep
%autosetup -n %{name}-%{commit0}

sed -i -e "s/usr\/local/usr/g" static/michisoft-tsunami.desktop
sed -i -e "s|/usr/local/share|/usr/share|g" src/lib/hui/Application.cpp

%build

%meson
%meson_build

%install

%meson_install

# install desktop file properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/michisoft-tsunami.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/michisoft-tsunami.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/michisoft-tsunami.desktop
%{_datadir}/tsunami/*

%changelog
* Tue Jan 25 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.90-2
- Initial spec file + fix installation
