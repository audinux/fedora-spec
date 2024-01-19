# Tag: Editor
# Type: Standalone
# Category: Audio, Tool
# GUIToolkit: Qt5

Name: samplebrain
Version: 0.18.4
Release: 1%{?dist}
Summary: A custom sample mashing app designed by Aphex Twin
URL: https://gitlab.com/then-try-this/samplebrain
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/then-try-this/samplebrain/-/archive/%{version}_release/samplebrain-%{version}_release.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-linguist
BuildRequires: alsa-lib-devel
BuildRequires: portaudio-devel
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

%description
A custom sample mashing app designed by Aphex Twin.
Samplebrain chops samples up into a 'brain' of interconnected small
sections called blocks which are connected into a network by
similarity. It processes a target sample, chopping it up into blocks
in the same way, and tries to match each block with one in its brain
to play in realtime.
This allows you to interpret a sound with a different one. As we
worked on it (during 2015 and 2016) we gradually added more and more
tweakable parameters until it became slightly out of control.

%prep
%autosetup -n %{name}-%{version}_release

sed -i -e "/Encoding/d" desktop/samplebrain.desktop
sed -i -e "s/GNOME;Application;/Audio;AudioVideo/g" desktop/samplebrain.desktop

%build

%qmake_qt5 samplebrain.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 samplebrain %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 desktop/samplebrain.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 desktop/samplebrain.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/samplebrain/docs/
cp -ra docs/* %{buildroot}/%{_datadir}/samplebrain/docs/

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/samplebrain
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/samplebrain/
%{_datadir}/samplebrain/docs/*

%changelog
* Fri Oct 14 2022 Yann Collette <ycollette.nospam@free.fr> - 0.18.4-1
- update to 0.18.4-1

* Wed Sep 28 2022 Yann Collette <ycollette.nospam@free.fr> - 0.18-1
- Initial spec file
