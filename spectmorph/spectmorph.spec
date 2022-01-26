# Tag: MIDI
# Type: Plugin, LV2
# Category: Audio, Synthesizer

Name: spectmorph
Version: 0.5.2
Release: 1%{?dist}
Summary: SpectMorph is a free software project which allows to analyze samples of musical instruments, and to combine them (morphing)
URL: http://www.spectmorph.org
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: http://www.spectmorph.org/files/releases/spectmorph-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: glib2-devel
BuildRequires: lv2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libao-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
SpectMorph is a free software project which allows to analyze samples
of musical instruments, and to combine them (morphing). It can be used
to construct hybrid sounds, for instance a sound between a trumpet and
a flute; or smooth transitions, for instance a sound that starts as a
trumpet and then gradually changes to a flute. In its current version,
SpectMorph ships with many ready-to-use instruments which can be
combined using morphing. 

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

# Fix desktop file
sed -i -e "s/Icon=smjack.png/Icon=smjack/g" data/smjack.desktop
sed -i -e "s/Midi//g" data/smjack.desktop

# Disable some compilation flags
sed -i -e "s/-msse -msse2 -msse3 -mmmx//g" configure
sed -i -e "s/-O3/-O2/g" configure

%build

%configure --prefix=%{_prefix} --with-lv2 --with-jack --with-qt --libdir=%{_libdir}

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build VERBOSE=1

%install

%make_install

# install smjack.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/smjack.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/man/*
%{_datadir}/pixmaps/*
%{_datadir}/spectmorph/*

%files devel
%{_includedir}/%{name}/*

%changelog
* Wed  Jan 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
- update to 0.5.2-1

* Thu Feb 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.5.1-1
- update to 0.5.1-1

* Sat Aug 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to 0.5.0-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.1-1
- update for Fedora 29
- update to 0.4.1-1

* Tue Apr 10 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- Initial release
