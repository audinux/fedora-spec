# Status: active
# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global app_id com.giadamusic.Giada

Name: giada
Version: 1.3.1
Release: 2%{?dist}
Summary: Your hardcore loop machine
License: GPL-3.0-or-later AND MIT AND BSD-2-Clause
URL: https://www.giadamusic.com
ExclusiveArch: x86_64 aarch64

# LICENSING NOTE:
#
# The upstream source, when downloaded from the main website (i.e.,
# %%{url}/data/giada-%%{version}-src.tar.gz), contains excerpts from the
# Steinberg VST 3 SDK, which has additional restrictions on top of the GPLv3
# that make it unsuitable for distribution in Fedora. See
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/FMFIZU22AP36J3DOUVCXUPHQ3MNDN5P6/.
#
# These problematic components may be filtered from the upstream source archive
# using a script to produce a distributable source archive. At one point, this
# package followed that approach. Now we use the GitHub release tarball; since
# the problematic components (vst3sdk and juce) are git submodules, they are
# not included in the automatically-generated release tarball.
#
# Note that this means Giada will *not* be built with VST3 support in Fedora.
# (The situation for VST2 is even worse, as it is available only under a
# proprietary license.)

# Usage: ./giada-source.sh <TAG>
#        ./giada-source.sh 1.3.1

Source0: giada.tar.gz
Source1: giada-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: cmake(fmt)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(freetype2)
BuildRequires: cmake(nlohmann_json)
BuildRequires: libcurl-devel
BuildRequires: libsamplerate-devel
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: json-static
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: appstream

Requires: hicolor-icon-theme

%description
Giada is an open source, minimalistic and hardcore music production tool.
Designed for DJs, live performers and electronic musicians.

%prep
%autosetup -n %{name}

%build

%set_build_flags
export CFLAGS="${CFLAGS} $(pkgconf --cflags nlohmann_json)"
export CXXFLAGS="${CXXFLAGS} $(pkgconf --cflags nlohmann_json)"
export LDFLAGS="${CXXFLAGS} $(pkgconf --libs nlohmann_json)"

%cmake \
    -DWITH_VST2:BOOL=OFF \
    -DWITH_VST3:BOOL=ON \
    -DWITH_TESTS:BOOL=OFF
%cmake_build

%install 

%cmake_install

# Cleanup
rm -rf %{buildroot}/%{_includedir}
rm -rf %{buildroot}/%{_bindir}/JUCE-*
rm -rf %{buildroot}/usr/lib/cmake/JUCE-*

rm %{buildroot}/%{_bindir}/fltk-config
rm %{buildroot}/%{_libdir}/libfltk*
rm -rf %{buildroot}/%{_datadir}/fltk/
rm -f %{buildroot}/%{_datadir}/man/man1/fltk-config.1*
rm -f %{buildroot}/%{_datadir}/man/man3/fltk.3*

%check 
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop

#appstream-util validate-relax \
#    %{buildroot}/%{_metainfodir}/%{app_id}.metainfo.xml

#appstreamcli validate --no-net \
#    %{buildroot}/%{_metainfodir}/%{app_id}.metainfo.xml

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/giada
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg

%changelog
* Sat Nov 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-2
- update to 1.3.1-2

* Sun Sep 14 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- update to 1.3.0-2

* Fri Aug 29 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-2
- update to 1.2.1-2 - removed unused dep

* Sat Jun 28 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update to 1.2.1-1

* Mon Apr 21 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Fri Feb 07 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Thu Oct 24 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

