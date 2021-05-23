# Tag: DAW, Jack, Alsa, MIDI
# Type: Standalone
# Category: Audio, DAW, MIDI

Name:    helio-workstation
Version: 3.6.0
Release: 1%{?dist}
Summary: An audio sequencer
URL:     https://github.com/helio-fm/helio-workstation
License: GPLv2+

# ./helioworkstation-source.sh 3.6

Source0: helio-workstation.tar.gz
Source1: helioworkstation-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
%if 0%{?fedora} > 31
BuildRequires: libglvnd-devel
%else
BuildRequires: mesa-libGL-devel
%endif
BuildRequires: libX11-devel libXft-devel libXrandr-devel libXinerama-devel libXcursor-devel

%description
Helio Workstation is free and open-source music sequencer, designed to be used on all major platforms.

%prep
%autosetup -n %{name}

%build

%set_build_flags

cd Projects/LinuxMakefile/
%make_build STRIP=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp -a Projects/LinuxMakefile/build/Helio %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp -a Projects/Deployment/Linux/Debian/x64/usr/share/applications/Helio.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_datadir}/icons/
cp -ra Projects/Deployment/Linux/Debian/x64/usr/share/icons/* %{buildroot}%{_datadir}/icons/

install -m 755 -d %{buildroot}/%{_datadir}/doc/%{name}/
cp -ra Docs/* %{buildroot}/%{_datadir}/doc/%{name}/

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
%{_datadir}/doc/%{name}/*

%changelog
* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-1
- update to 3.6.0-1

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 3.4.0-1
- update to 3.4.0-1

* Sat Dec 26 2020 Yann Collette <ycollette.nospam@free.fr> - 3.3.0-1
- update to 3.3.0-1

* Tue Oct 6 2020 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- Initial spec file 3.1.0-1
