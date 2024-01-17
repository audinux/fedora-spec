# Tag: Jack, Organ
# Type: Standalone
# Category: Audio, Synthesizer

Name:    azr3-jack
Version: 1.2.3
Release: 2%{?dist}
Summary: This JACK program is a port of the free VST plugin AZR-3
URL:     http://ll-plugins.nongnu.org/azr3/
License: GPL

Vendor:       Audinux
Distribution: Audinux

Source:  https://download.savannah.gnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
Source1: azr3.png
Patch1:  0001-fix-sigc-namespace.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: cairomm-devel
BuildRequires: glibmm24-devel
BuildRequires: gtkmm24-devel
BuildRequires: pango-devel
BuildRequires: desktop-file-utils

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

%prep

%autosetup -p1 -n azr3-jack-%{version}

%build
%set_build_flags

export CXXFLAGS="$CXXFLAGS -I/usr/include/gtkmm-2.4 -I/usr/include/glibmm-2.4/ -I/usr/lib64/glibmm-2.4/include"

%configure
%make_build

%install
%make_install prefix=%{_usr} libdir=%{_libdir}

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
Icon=/usr/share/pixmaps/azr3.png
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
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/azr3
%{_datadir}/pixmaps/azr3.png
%{_datadir}/applications/azr3-jack.desktop
%dir %{_datadir}/azr3-jack
%{_datadir}/azr3-jack/presets
%{_datadir}/azr3-jack/*.png
%{_mandir}/man1/azr3.1*
%exclude %{_docdir}/azr3-jack/*

%changelog
* Fri Nov 05 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-2
- install desktop file

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.3-1
- update for Fedora 29

* Wed Sep 13 2017 Initial release
- initial release
