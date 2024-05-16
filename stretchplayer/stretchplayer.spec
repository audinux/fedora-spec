# Tag: Player
# Type: Standalone
# Category: Audio, Tool

# Global variables for github repository
%global commit0 5e807a87cfad84c648d873107bfc91eef3648a4a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: stretchplayer
Version: 0.0.1.%{shortcommit0}
Release: 1%{?dist}
Summary: Variable speed audio plater
URL: https://github.com/smbolton/stretchplayer
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/smbolton/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:  stretchplayer-fix-cast.patch
Patch1:  stretchplayer-remove-inline.patch
Patch2:  stretchplayer-disable-mpg123.patch

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: rubberband-devel

%description
StretchPlayer is an audio file player that allows you to change the
speed of the song without changing the pitch.  It will also allow you
to transpose the song to another key (while also changing the speed).
This is a very powerful tool for musicians who are learning to play a
pre-recorded song.  You can:

 * Time Stretch (50% to 150% of song speed)
 * Pitch shift (up or down 1 octave)
 * A/B repeat

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%cmake

%cmake_build

%install

%cmake_install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README.txt INSTALL.txt BUGS.txt
%license COPYING*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/icons/*
%exclude %{_datadir}/%{name}/%{name}.desktop

%changelog
* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update for Fedora 33

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- update for Fedora 29

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial release
