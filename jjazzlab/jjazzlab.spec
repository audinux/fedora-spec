# Tag: MIDI
# TYpe: IDE, Standalone
# Category: Tool, MIDI, Sequencer

Name:     jjazzlab
Version:  3.2.1
Release:  1%{?dist}
Summary:  A complete Midi-based framework for automatic backing tracks generation.
URL:      https://github.com/jjazzboss/JJazzLab-X
License:  LGPL-3.0

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jjazzboss/JJazzLab-X/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: jjazzlabx.zip
Source2: jjazzlabx

BuildArch: noarch

BuildRequires: unzip
BuildRequires: desktop-file-utils

Requires: java >= 1.5

%description
JJazzLab-X is a Midi-based framework dedicated to backing tracks
generation -some people talk about "play-along songs" or
“auto-accompaniment applications”. You type in chord symbols, select
a rhythm (style), then the application generates a complete backing
track with drums, bass, guitar, piano, strings, etc.

The objective is to develop a jam buddy able to quickly generate
intelligent and interesting backing tracks: realistic and non-boring
backing tracks which you can easily adjust to a specific song.

%prep
%autosetup -n JJazzLab-X-%{version}

%build

mkdir dist
cd dist
unzip %{SOURCE1}

rm -f platform/lib/*.dll
rm -f platform/lib/*.exe

%install

install -dm 755 %{buildroot}%{_bindir}
cp %{SOURCE2} %{buildroot}%{_bindir}

install -dm 755 %{buildroot}%{_datadir}/jjazzlab
cp -ra dist/jjazzlabx/etc %{buildroot}%{_datadir}/jjazzlab
cp -ra dist/jjazzlabx/jjazzlabx %{buildroot}%{_datadir}/jjazzlab
cp -ra dist/jjazzlabx/platform %{buildroot}%{_datadir}/jjazzlab

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 Graphics/logo-JJazzLabX.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=logo-JJazzLabX
Comment=JJazzLab Sequencer
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
%license LICENSE
%{_bindir}/*
%{_datadir}/jjazzlab/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*

%changelog
* Sun Oct 16 2022 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-1
- initial spec file
