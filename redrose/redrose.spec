# Status: active
# Tag: Editor, Tablature, MIDI, Alsa, Jack, Pipewire
# Type: Standalone
# Category: Sequencer, Tool

Name: redrose
Version: 0.5.52
Release: 2%{?dist}
Summary: ABC notation music integrated environment
License: GPL-3.0
URL: http://brouits.free.fr/redrose
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/be1/redrose/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: patchelf
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

# Use a fluidsynth default SF2 file
sed -i -e "s|/usr/share/sounds/sf2/default-GM.sf2|/usr/share/sounds/sf2/default.sf2|g" app/config.h.in
# Force the build of libabc as a static library
sed -i -e "s|add_library(abc \${SRCS} \${HEADERS})|add_library(abc STATIC \${SRCS} \${HEADERS})|g" abc/CMakeLists.txt

%build

%cmake
%cmake_build

%install

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
* Sun Jan 18 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.52-2
- update to 0.5.52-2

* Mon Jan 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.51-2
- update to 0.5.51-2

* Sun Jan 11 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.50-2
- update to 0.5.50-2

* Wed Jan 07 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.49-2
- update to 0.5.49-2

* Mon Jan 05 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.48-2
- update to 0.5.48-2

* Wed Dec 31 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.47-2
- update to 0.5.47-2

* Mon Dec 29 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.45-2
- update to 0.5.45-2

* Fri Dec 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.44-2
- update to 0.5.44-2: fix installation

* Wed Dec 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.5.44-1
- Initial development
