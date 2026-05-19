# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

%global real_version 0.4.0-beta
# Godot export templates are upstream prebuilt binaries and do not
# contain GNU build IDs.
%global _missing_build_ids_terminate_build %{nil}
%global debug_package %{nil}
%global godot_version 4.6.2

Name: SoundThread
Version: 0.4.0b
Release: 2%{?dist}
Summary: Experimental sound design workstation
License: MIT
URL: https://github.com/j-p-higgins/SoundThread

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/refs/tags/v%{real_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: godot_templates.zip
Source2: soundthread.svg
Source3: prepare_godot.sh

BuildRequires: godot
BuildRequires: unzip
BuildRequires: desktop-file-utils

Requires: cdp-compat

%description
SoundThread is a Godot-based experimental sound design environment.

%prep
%autosetup -n %{name}-%{real_version}

sed -i -e "s|export_path=\".*\"|export_path=\"build/SoundThread\"|g" export_presets.cfg

%build

PWD=`pwd`

export HOME=$PWD
export XDG_DATA_HOME=$PWD/.local/share

mkdir -p $PWD/.local/share/godot/export_templates/%{godot_version}.stable
unzip %{SOURCE1} -d $PWD/.local/share/godot/export_templates/%{godot_version}.stable

mkdir build

godot --headless --path . --editor --quit
godot --headless --path . --export-release Linux

%install

install -m755 -d %{buildroot}/%{_bindir}
install -m755 build/SoundThread %{buildroot}/%{_bindir}/SoundThread

install -m755 -d %{buildroot}/%{_datadir}/%{name}/examples/
cp -ra examples/* %{buildroot}/%{_datadir}/%{name}/examples/

# Install icon
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=soundthread
Comment=Node based GUI for The Composers Desktop Project
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
%{_bindir}/SoundThread
%{_datadir}/%{name}/examples/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Tue May 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.0b-2
- update to 0.4.0b-2 - use cdp-compat

* Tue May 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.0b-1
- initial version of the spec
