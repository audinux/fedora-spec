# Tag: Drum
# Type: Standalone
# Category: Audio, Synthesizer

Name:    psindustrializer
Version: 0.2.7
Release: 1%{?dist}
Summary: Industrializer is a program for generating percussion sounds for musical purposes

License: GPL-2.0-only
URL:     https://sourceforge.net/projects/industrializer

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/industrializer/files/psindustrializer-%{version}.tar.xz
Source1: psindustrializer.appdata.xml
Source2: psindustrializer.desktop

BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pulseaudio-libs-devel
BuildRequires: audiofile-devel
BuildRequires: gtk2-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Industrializer is a program for generating percussion sounds for musical purposes.
This program is great for generating new techno and industrial sounds.
It also can produce chimes, bubbles, gongs, hammer hits on different materials and so on.

%prep
%autosetup

cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%configure
%make_build

%install

%make_install

# Cleanup
rm %{buildroot}%{_libdir}/*.la

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license COPYING
%doc README.md
%{_bindir}/*
%exclude %{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/locale/*
%{_datadir}/pixmaps/*
%{_datadir}/psindustrializer/

%changelog
* Mon Dec 13 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2.7-1
- Initial spec
