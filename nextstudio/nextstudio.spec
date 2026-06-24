# Status: active
# Tag: Jack, Alsa, Distortion
# Type: Plugin, Standalone, VST3
# Category: Effect

Name: nextstudio
Version: 0.0.2a
Release: 1%{?dist}
Summary: Digital Audio Workstation built with JUCE and Tracktion Engine
License: AGPL-3.0-or-later
URL: https://github.com/BaraMGB/NextStudio
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./nextstudio-source.sh <TAG>
#        ./nextstudio-source.sh v0.02-alpha

Source0: NextStudio.tar.gz
Source1: nextstudio-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: libatomic
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel
BuildRequires: ladspa-devel
BuildRequires: desktop-file-utils

%description
NextStudio is a Digital Audio Workstation designed for music production, recording, editing,
and mixing. Built with JUCE and Tracktion Engine.

%prep
%autosetup -n NextStudio

%build

%set_build_flags
export CXXFLAGS="-include cstdint -Wno-template-body $CXXFLAGS"

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/App/NextStudio_artefacts/NextStudio  %{buildroot}/%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra App/resources/Themes %{buildroot}/%{_datadir}/%{name}/
cp -ra App/resources/Samples %{buildroot}/%{_datadir}/%{name}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/
install -m 644 resources/nextstudio.png %{buildroot}/%{_datadir}/icons/hicolor/apps/256x256/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 resources/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 resources/nextstudio.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENCE.md
%{_bindir}/*
%{_datadir}/%{name}/Themes/*
%{_datadir}/%{name}/Samples/*
%{_datadir}/icons/hicolor/apps/256x256/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*
%changelog
* Tue Jun 23 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.2-alpha-1
- Initial spec file
