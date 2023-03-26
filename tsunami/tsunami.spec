# Global variables for github repository
%global commit0 57999be98a2bc707bb8db83914f20215afee185e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: MIDI
# Type: Standalone
# Category: Audio, DAW

Name:    tsunami
# upstream version is in src/Tsunami.cpp
Version: 0.7.111.0.%{shortcommit0}
Release: 2%{?dist}
Summary: A simple but powerful audio editor
URL:     https://github.com/momentarylapse/tsunami
License: GPLv3

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/momentarylapse/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: gtk4-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel 
BuildRequires: libogg-devel 
BuildRequires: flac-devel
BuildRequires: fftw-devel
BuildRequires: libunwind-devel
BuildRequires: desktop-file-utils

%description
Tsunami is an open-source digital audio workstation (DAW).
It is designed for ease of use and not-looking-crappy™.

%prep
%autosetup -n %{name}-%{commit0}

%build

# Now tsunami's CMakeLists.txt set gtk4 by default.
# To use gtk3, change the BuildRequires, and add this argument to %%cmake:
# -DGTK4_OR_GTK3=gtk3

%if 0%{?fedora} >= 38
%cmake -DCMAKE_CXX_FLAGS="-include cstdio $CXXFLAGS"
%else
%cmake
%endif
%cmake_build

%install

%cmake_install

# install desktop file properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        --set-key=Exec --set-value=tsunami \
        --set-icon=tsunami \
        static/michisoft-tsunami.desktop

# desktop icon
install -Dm 644 static/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/tsunami.svg

# mime
install -Dm 644 static/michisoft-nami.xml %{buildroot}%{_datadir}/mime/packages/michisoft-nami.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/michisoft-tsunami.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/tsunami
%{_datadir}/tsunami/*
%{_datadir}/applications/michisoft-tsunami.desktop
%{_datadir}/icons/hicolor/scalable/apps/tsunami.svg
%{_datadir}/mime/packages/michisoft-nami.xml

%changelog
* Thu Feb 16 2023 Justin Koh <j@ustink.org> - 0.7.111.0-2
- update to 0.7.111.0-2

* Tue Jan 25 2022 Yann Collette <ycollette.nospam@free.fr> - 0.7.90-2
- Initial spec file + fix installation
