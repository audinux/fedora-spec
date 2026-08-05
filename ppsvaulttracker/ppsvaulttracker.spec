# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: ppsvaulttracker
Version: 1.1.0
Release: 1%{?dist}
Summary: A modern VSTi tracker (FT2 heritage, VST3 hosting, MIDI+stems export)
License: AGPL-3.0-or-later
URL: https://github.com/gPTPPs/ppsvaulttracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/gPTPPs/ppsvaulttracker/archive/refs/tags/v%{version}-beta.tar.gz#/%{name}-%{version}.tar.gz
Source1: icon.png
Source2: icon_small.png

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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
BuildRequires: desktop-file-utils

%description
A modern VSTi tracker — by The Unborn / RetroVault
A pattern-based tracker in the FastTracker 2 / ProTracker lineage, hosting VST3 instruments and effects,
designed to compose full songs whose deliverables (MIDI + WAV stems) import cleanly into Ableton Live
for final arrangement and mastering.

%prep
%autosetup -n %{name}-%{version}-beta

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/PPsVaultTracker_artefacts/PPsVaultTracker %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/%{name}_small.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=ppsvaulttracker tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE THIRD_PARTY_LICENSES.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Wed Aug 05 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
