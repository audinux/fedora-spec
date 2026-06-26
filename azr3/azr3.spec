# Status: active
# Tag: Jack, Organ
# Type: Standalone
# Category: Audio, Synthesizer

Name: azr3-jack
Version: 2.0.0
Release: 2%{?dist}
Summary: This JACK program is a port of the free VST plugin AZR-3
URL: http://ll-plugins.nongnu.org/azr3/
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source: https://github.com/ycollet/azr3/archive/refs/tags/v2.0.0.tar.gz#/%{name}-%{version}.tar.gz
Source1: azr3.png

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm4.0-devel
BuildRequires: liblo-devel
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
This JACK program is a port of the free VST plugin AZR-3.
It is a tonewheel organ with drawbars, distortion and rotating speakers.
The original was written by Rumpelrausch Täips.
The organ has three sections, two polyphonic with 9 drawbars each
and one monophonic bass section with 5 drawbars. The two polyphonic
sections respond to events on MIDI channel 1 and 2, and an optional
keyboard split function makes the bass section listen to the lower keys
on channel 1.
The three sections have separate sustain and percussion switches as well
as separate volume controls,
and the two polyphonic sections have separate vibrato settings. All three
sections are mixed and sent through the distortion effect and the
rotating speakers simulator, where the modulation wheel can be used to
switch between fast and slow rotation, and the fast and slow rotation
speeds themselves can be changed separately for the lower and upper
frequencies.

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentations for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -n azr3-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications

install -m 644  %{S:1} %{buildroot}%{_datadir}/pixmaps/azr3.png

cat > %{buildroot}%{_datadir}/applications/azr3-jack.desktop << EOF
[Desktop Entry]
Name=AZR3-Jack
Comment=Organ VST bar to n channels.
Comment[it]=Organo VST a barre a n canali.
Exec=/usr/bin/azr3
Type=Application
Terminal=false
Icon=azr3
Categories=Audio;AudioVideo;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/azr3-jack.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/azr3
%{_datadir}/pixmaps/azr3.png
%{_datadir}/applications/azr3-jack.desktop
%{_datadir}/azr3-jack/presets
%{_datadir}/azr3-jack/*.png
%{_mandir}/man1/azr3.1*

%files -n license-%{name}
%doc AUTHORS ChangeLog README
%license COPYING

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Jun 26 2026 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-2
- update to 2.0.0 - lv2 version

* Fri Nov 05 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-2
- install desktop file

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-1
- update for Fedora 29

* Wed Sep 13 2017 Initial release
- initial release
