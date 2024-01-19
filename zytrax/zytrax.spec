# Tag: Jack, Alsa, Tracker
# Type: Standalone
# Category: Audio, Sequencer

# Global variables for github repository
%global commit0 97b79d17b390f70890928cebf74bb28acf32ecea
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: zytrax
Version: 0.9.0.%{shortcommit0}
Release: 3%{?dist}
Summary: Easy to use sequencer with an interface heavily inspired by 90's tracker software
URL: https://github.com/reduz/zytrax.git
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/reduz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: SConstruct-zytrax

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: scons
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(jack)
BuildRequires: gtkmm30-devel
BuildRequires: freetype-devel
BuildRequires: rtmidi-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libsndfile-devel

%description
While contemporary software that uses this approach exists, it
usually has a high entry barrier because it maintains compatibility
with old formats.

In contrast to this, ZyTrax starts afresh with an user friendly
approach (no hex numbers, pure plugin-based architecture, inlined
automation envelopes, smart automations, zoomable patterns and a
simple pattern/orderlist layout).

%prep
%autosetup -n %{name}-%{commit0}

cp %{SOURCE1} SConstruct

%build

export XDG_CURRENT_DESKTOP="kde"

%set_build_flags

export CXXFLAGS="-include cstdint $CXXFLAGS"

# scons --environment-overrides
scons

cat > zytrax.desktop << EOF
[Desktop Entry]
Name=Zytrax
Comment=An audio tracker
Exec=/usr/bin/zytrax
Type=Application
Terminal=0
Icon=/usr/share/pixmaps/zytrax.png
Categories=Audio;AudioVideo;
EOF

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/zytrax %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 zytrax.png %{buildroot}/%{_datadir}/pixmaps/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 zytrax.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/zytrax.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/zytrax.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/zytrax.desktop
%{_datadir}/pixmaps/zytrax.png

%changelog
* Sun Dec 05 2021 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-3
- rebuild

* Tue Oct 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-2
- fix debug build

* Sat Jun 08 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- Initial spec file 1.0alpha-1
