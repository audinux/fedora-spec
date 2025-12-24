# Status: active
# Tag: Editor, Tablature, Alsa, MIDI
# Type: Standalone
# Category: Sequencer, Tool

Name: redrose
Version: 0.5.44
Release: 1%{?dist}
Summary: ABC notation music integrated environment
License: GPL-3.0
URL: http://brouits.free.fr/redrose
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/be1/redrose/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: libsmf-devel
BuildRequires: libspectre-devel
BuildRequires: fluidsynth-devel
BuildRequires: drumstick-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: abcMIDI
Requires: abcm2ps
Requires: fluid-soundfont-gm

%description
ABC music notation integrated environment

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s|/usr/share/sounds/sf2/default-GM.sf2|/usr/share/sounds/sf2/default.sf2|g" app/config.h.in

%build

%cmake
%cmake_build

%Install

%cmake_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/fr.free.brouits.redrose.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/mime/packages/redrose.xml
%{_datadir}/%{name}/locale/*.qm

%changelog
* Wed Dec 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.44-1
- Initial development
