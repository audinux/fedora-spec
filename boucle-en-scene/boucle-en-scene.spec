# Status: active
# Tag: Sequencer, MIDI
# Type: Standalone
# Category: Audio, Sequencer, MIDI

%global debug_package %{nil}
# .NET single-file bundle: do not strip the executable
%global __strip /bin/true

# Bump this when the distro moves to a new .NET SDK generation
%global dotnet_version 10.0
%global dotnet_tfm     net%{dotnet_version}

Name: boucle-en-scene
Version: 0.6
Release: 1%{?dist}
Summary: A MIDI and audio loop launcher, for live performance or practice
License: GPL-3.0-or-later
URL: https://boucle-en-scene.fr
ExclusiveArch: x86_64 aarch64

Source0: https://boucle-en-scene.fr/telechargements/BoucleEnScene-%{version}.DEV-2026-11-11-source.tar.gz
Patch0: boucle-en-scene-0001-fix-path.patch

BuildRequires: gcc-c++
BuildRequires: dotnet-host
BuildRequires: dotnet-sdk-%{dotnet_version}
BuildRequires: mono-devel
BuildRequires: libgdiplus
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: dotnet-runtime-%{dotnet_version}
Requires: fluid-soundfont-gm

%description
A MIDI and audio loop launcher for live performance or practice.
It features a grid of tracks and scenes, loops that trigger in perfect synchronization,
keyboard-based recording, a note editor, and a built-in synthesizer.
It can be controlled via mouse, MIDI controller, computer keyboard, or a mobile phone app.

%prep
%autosetup -p1 -n BoucleEnScene-%{version}.DEV-2026-11-11-source

%build

%ifarch x86_64
./publish.sh linux-x64
mv publish/BoucleEnScene-linux-x64  publish/BoucleEnScene
%endif

%ifarch aarch64
./publish.sh linux-arm64
mv publish/BoucleEnScene-linux-arm64  publish/BoucleEnScene
%endif

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 publish/BoucleEnScene/BoucleEnScene %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/
cp -ra publish/BoucleEnScene/Controllers %{buildroot}/%{_datadir}/%{name}/
cp -ra publish/BoucleEnScene/Loops %{buildroot}/%{_datadir}/%{name}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 publish/BoucleEnScene/Images/icon.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=A MIDI and audio loop launcher, for live performance or practice
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
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/%{name}/Loops/*
%{_datadir}/%{name}/Controllers/*
%{_datadir}/applications/boucle-en-scene.desktop
%{_datadir}/pixmaps/boucle-en-scene.ico

%changelog
* Thu Nov 12 2026 Yann Collette <ycollette.nospam@free.fr> - 0.6-1
- Initial build
