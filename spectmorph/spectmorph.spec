# Tag: MIDI
# Type: Plugin, LV2, VST, CLAP
# Category: Audio, Synthesizer

Name: spectmorph
Version: 0.6.1
Release: 3%{?dist}
Summary: SpectMorph is a free software project which allows to analyze samples of musical instruments, and to combine them (morphing)
URL: http://www.spectmorph.org
ExclusiveArch: x86_64 
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/swesterfeld/spectmorph/archive/refs/tags/%{version}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gettext
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: glibc-common
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: glib2-devel
BuildRequires: lv2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libao-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: simde-devel
BuildRequires: chrpath
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

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%setup -n spectmorph-%{version}

# Fix desktop file
sed -i -e "s/Icon=smjack.png/Icon=smjack/g" data/smjack.desktop
sed -i -e "s/Midi//g" data/smjack.desktop
sed -i -e "/AM_ICONV/d" configure.ac

%build

%set_build_flags

# Disable some flags to avoid segmentation fault
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Wp,-D_FORTIFY_SOURCE=2//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Wp,-D_GLIBCXX_ASSERTIONS//g"`
export CFLAGS=`echo $CFLAGS | sed -e "s/-Wp,-D_FORTIFY_SOURCE=2//g"`
export CFLAGS=`echo $CFLAGS | sed -e "s/-Wp,-D_GLIBCXX_ASSERTIONS//g"`

%if 0%{?fedora} >= 38
export CXXFLAGS="-include cstdint $CXXFLAGS"
%endif

./autogen.sh

%configure --with-lv2 --with-jack --with-qt
%make_build VERBOSE=1 CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS"

%install

%make_install

chrpath --delete %{buildroot}/%{_libdir}/clap/SpectMorph.clap
chrpath --delete %{buildroot}/%{_libdir}/lv2/spectmorph.lv2/spectmorph_lv2.so
chrpath --delete %{buildroot}/%{_libdir}/vst/spectmorph_vst.so

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
%{_datadir}/spectmorph/

%files devel
%{_includedir}/%{name}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Nov 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.1-3
- update to 0.6.1-3

* Thu May 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- update to 0.6.0-3

* Mon Apr 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-3
- update to 0.5.2-3 - update to cfad5460c5ff9b5b58957093f1fdca665f9d43db

* Wed Mar 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-2
- update to 0.5.2-2 - update to 609a19e6aa4b097138a68ca0631801266d005258

* Wed Jan 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.2-1
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
