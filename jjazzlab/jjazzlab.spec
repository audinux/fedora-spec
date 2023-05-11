# Tag: MIDI
# TYpe: IDE, Standalone
# Category: Tool, MIDI, Sequencer

Name:     jjazzlab
Version:  3.2.1
Release:  2%{?dist}
Summary:  A complete Midi-based framework for automatic backing tracks generation.
URL:      https://github.com/jjazzboss/JJazzLab-X
License:  LGPL-3.0

Vendor:       Audinux
Distribution: Audinux

Source0: https://www.jjazzlab.com/pkg/JJazzLab-%{version}-Linux.zip
Source1: jjazzlab.png
Source2: README.md

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
%autosetup -n JJazzLab-%{version}-Linux

%install


install -dm 755 %{buildroot}/opt/jjazzlab/share/doc
cp -rav . %{buildroot}/opt/jjazzlab
cp %{SOURCE2} %{buildroot}/opt/jjazzlab/share/doc

install -dm 755 %{buildroot}/%{_bindir}/

ln -s /opt/jjazzlab/bin/jjazzlab %{buildroot}/%{_bindir}/jjazzlab

# Cleanup
rm -rf %{buildroot}/opt/jjazzlab/platform/modules/lib/aarch64

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
cp %{SOURCE1}  %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=jjazzlab
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
%doc /opt/jjazzlab/share/doc/README.md
%{_bindir}/*
/opt/jjazzlab/
%{_datadir}/icons/*
%{_datadir}/applications/*

%changelog
* Wed May 10 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-2
- install binary Distribution

* Sun Oct 16 2022 Yann Collette <ycollette.nospam@free.fr> - 3.2.1-1
- initial spec file
