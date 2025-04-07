# Status: active
# Tag: MIDI, Synthesizer
# Type: Standalone, VST3
# Category: Audio, Synthesizer

Name: aeolus_plugin
Version: 0.2.1
Release: 4%{?dist}
Summary: Pipe organ synthesizer
License: GPL-3.0-or-later
URL: https://github.com/Archie3d/aeolus_plugin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source_aeolus_plugin.sh <tag>
#        ./source_aeolus_plugin.sh master

Source0: aeolus_plugin.tar.gz
Source1: source_aeolus_plugin.sh
Patch0: aeolus_plugin-0001-aarch64.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: libcurl-devel
BuildRequires: freetype-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: simde-devel
BuildRequires: desktop-file-utils

%description
Pipe organ emulator using additive synthesis as a VST plugin
(or a stand-alone executable).

Aeolus was originally developed by Fons Adriaensen and presented in 2004.
The original implementation is Linux only and can be found here (or across
Linux distribution packages). At present it looks like Aeolus development
has been mostly abandoned (but Organnery picked up the original Aeolus
project to make it run on a Raspberry Pi).

This project leverages the wavetable systhesis part of the original Aeolus,
improves on it, and delivers it as a standard VST plugin using JUCE
framework, so that it can be run in Windows/macOS VST3/AU hosts.

This implementation contains additional improvements to the sound
generation including

- pipes chiff noise on attack;
- new pipe models;
- convolutional reverb.

The original binary format for the pipe models and the organ configuration
has been translated (partially) to JSON.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
vst3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%setup -n %{name}

%ifarch aarch64
%patch 0 -p1
%endif

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_datadir}/Aeolus/doc/

cp -ra %{__cmake_builddir}/Aeolus_artefacts/Standalone/* %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Aeolus_artefacts/VST3/Aeolus.vst3 %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Aeolus_artefacts/LV2/Aeolus.lv2 %{buildroot}%{_libdir}/lv2/
cp -ra docs/* %{buildroot}%{_datadir}/Aeolus/doc/
cp -ra Resources/* %{buildroot}%{_datadir}/Aeolus/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 Resources/icons/icon256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/Aeolus.png
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -m 644 Resources/icons/icon64.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/Aeolus.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/Aeolus.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Aeolus
Exec=Aeolus
Icon=Aeolus
Comment=Aeolus Pipe Organ
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/Aeolus.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Aeolus.desktop

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/*
%{_datadir}/Aeolus/
%{_datadir}/icons/hicolor/256x256/*
%{_datadir}/icons/hicolor/64x64/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Sep 02 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- update to 0.2.1-1

* Sat Feb 24 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-3
- update to 0.2.0-3 - update to 50494c1db8a88b4c17254fb40fc8f948b8046a8f

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Fri Oct 28 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.12-1
- update to last master

* Fri Oct 28 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.12-1
- Initial spec file
