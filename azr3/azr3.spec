# Tag: Jack, Organ
# Type: Standalone
# Category: Audio, Synthesizer

Name:    azr3-jack
Version: 1.2.3
Release: 1%{?dist}
Summary: This JACK program is a port of the free VST plugin AZR-3
Group:   Applications/Multimedia
URL:     http://ll-plugins.nongnu.org/azr3/
License: GPL

Source:  https://download.savannah.gnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
Source1: azr3.png
Patch1:  0001-fix-sigc-namespace.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: cairomm-devel
BuildRequires: glibmm24-devel
BuildRequires: gtkmm24-devel
BuildRequires: lash-devel
BuildRequires: pango-devel
BuildRequires: desktop-file-utils

%description
This JACK program is a port of the free VST plugin AZR-3. It is a tonewheel organ with drawbars, distortion and rotating speakers. 
The original was written by Rumpelrausch Täips. The organ has three sections, two polyphonic with 9 drawbars each 
and one monophonic bass section with 5 drawbars. The two polyphonic sections respond to events on MIDI channel 1 and 2, 
and an optional keyboard split function makes the bass section listen to the lower keys on channel 1. 
The three sections have separate sustain and percussion switches as well as separate volume controls, 
and the two polyphonic sections have separate vibrato settings. All three sections are mixed and sent through the distortion effect 
and the rotating speakers simulator, where the modulation wheel can be used to switch between fast and slow rotation, 
and the fast and slow rotation speeds themselves can be changed separately for the lower and upper frequencies.

%prep

%setup -q -n azr3-jack-%{version}
%patch1 -p1 -b .nodevver

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} #CFLAGS="${CFLAGS:-%optflags}"
%{__make}

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

make DESTDIR=%{buildroot} install

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
Terminal=0
Icon=/usr/share/pixmaps/azr3.png
Categories=KDE;AudioVideo;
EOF

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
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
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Wed Sep 13 2017 Initial release
- initial release
