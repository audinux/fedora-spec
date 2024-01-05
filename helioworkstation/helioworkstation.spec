# Tag: Jack, Alsa, MIDI
# Type: Standalone
# Category: Audio, Sequencer

Name: helio-workstation
Version: 3.12.0
Release: 2%{?dist}
Summary: An audio sequencer
URL: https://github.com/helio-fm/helio-workstation
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./helioworkstation-source.sh 3.12

Source0: helio-workstation.tar.gz
Source1: helioworkstation-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: desktop-file-utils

%description
Helio Workstation is free and open-source music sequencer, designed to be used on all major platforms.

%prep
%autosetup -n %{name}

%build

%set_build_flags

export CXXFLAGS="-include utility $CXXFLAGS"

cd Projects/LinuxMakefile/
%make_build STRIP=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp -a Projects/LinuxMakefile/build/helio %{buildroot}/%{_bindir}/helio

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp -a Projects/Deployment/Linux/Debian/x64/usr/share/applications/Helio.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_datadir}/icons/
cp -ra Projects/Deployment/Linux/Debian/x64/usr/share/icons/* %{buildroot}%{_datadir}/icons/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc
cp -ra Docs/* %{buildroot}/%{_datadir}/%{name}/doc/

# install helioworkstation.desktop properly.
desktop-file-install --vendor '' \
        --add-category=AudioVideo \
        --add-category=X-Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/doc/*

%changelog
* Tue Dec 12 2023 Yann Collette <ycollette.nospam@free.fr> - 3.12.0-2
- update to 3.12.0-2

* Sun Apr 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.11.0-2
- update to 3.11.0-2

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 3.10.0-2
- update to 3.10.0-2

* Sun Feb 27 2022 Yann Collette <ycollette.nospam@free.fr> - 3.9.0-2
- update to 3.9.0-2

* Sat Nov 06 2021 Yann Collette <ycollette.nospam@free.fr> - 3.8.0-2
- update to 3.8.0-2

* Sat Aug 07 2021 Yann Collette <ycollette.nospam@free.fr> - 3.7.0-2
- update to 3.7.0-2

* Sun Jun 20 2021 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-2
- update to 3.6.0-2 - fix binary name

* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-1
- update to 3.6.0-1

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 3.4.0-1
- update to 3.4.0-1

* Sat Dec 26 2020 Yann Collette <ycollette.nospam@free.fr> - 3.3.0-1
- update to 3.3.0-1

* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- Initial spec file 3.1.0-1
