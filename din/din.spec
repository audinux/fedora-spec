# Status: active
# Tag: Jack, Alsa
# Type: Standalone
# Category: Audio, Synthesizer

%global din_vers_major 59
%global din_vers_minor 0
%global din_vers_patch 0
Summary: DIN is a synth of a 3rd kind
Name:    din
Version: %din_vers_major.%din_vers_minor.%din_vers_patch
Release: 1%{?dist}
License: GPL
URL:     https://dinisnoise.org/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://dinisnoise.org/files/din-%{din_vers_major}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: tcl-devel
BuildRequires: SDL-devel
BuildRequires: boost-devel
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils

%description
DIN is a synth of a 3rd kind.
It forgets history,
To not repeat it.
It doesnt hide analog music hardware,
In digital music software.
You had pulse, sine, triangle and sawtooth,
And went forth and made electronic music.

%package -n din-jack
Summary:  Jack version of the Din synthesiser
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: din

%description -n din-jack
Jack version of the Din synthesizer

%prep
%autosetup -n %{name}-%din_vers_major

# __line conflict with std c++ headers
sed -i -e "s/__line/__dinline/g" src/line.h

%build
%set_build_flags

# To select an api:
# __UNIX_JACK__
# __LINUX_ALSA__

mkdir build_jack
cd build_jack
CFLAGS="-D__UNIX_JACK__ $CFLAGS" CXXFLAGS="-DCONST=const -D__UNIX_JACK__ $CXXFLAGS" LDFLAGS="`pkg-config --libs jack` $LDFLAGS" ../configure --prefix=%{_prefix} --libdir=%{_libdir} --program-suffix=-jack

%if 0%{?fedora} >= 42
sed -i -e "s/-ltcl8.6/-ltcl/g" src/Makefile
%endif

%make_build

cd ..
mkdir build_alsa
cd build_alsa
CFLAGS="-D__LINUX_ALSA__ $CFLAGS" CXXFLAGS="-DCONST=const -D__LINUX_ALSA__ $CXXFLAGS" ../configure --prefix=%{_prefix} --libdir=%{_libdir}

%if 0%{?fedora} >= 42
sed -i -e "s/-ltcl8.6/-ltcl/g" src/Makefile
%endif

%make_build
cd ..

%install

cd build_jack
%make_install
cd ..

cd build_alsa
%make_install
cd ..

cp pixmaps/din.desktop pixmaps/din-jack.desktop

sed -i -e "s/Exec=din/Exec=din-jack/g" pixmaps/din-jack.desktop

desktop-file-install                         \
  --add-category=Audio                       \
  --add-category=AudioVideo                  \
  --delete-original                          \
  --remove-key=Encoding                      \
  --dir=%{buildroot}%{_datadir}/applications \
  pixmaps/din.desktop

desktop-file-install                         \
  --add-category=Audio                       \
  --add-category=AudioVideo                  \
  --delete-original                          \
  --remove-key=Encoding                      \
  --dir=%{buildroot}%{_datadir}/applications \
  pixmaps/din-jack.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/din.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/din-jack.desktop

%files
%doc AUTHORS CHANGELOG BUGS INSTALL NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/din.desktop
%{_datadir}/icons/hicolor/scalable/apps/din.svg
%{_datadir}/pixmaps/din.png

%files -n din-jack
%{_bindir}/din-jack
%{_datadir}/applications/din-jack.desktop

%changelog
* Sat Jan 18 2025 Yann Collette <ycollette dot nospam at free.fr> 59.0.0-1
- update to 59.0.0-1

* Mon Jan 22 2024 Yann Collette <ycollette dot nospam at free.fr> 58.0.0-1
- update to 58.0.0-1

* Sat Sep 16 2023 Yann Collette <ycollette dot nospam at free.fr> 57.0.0-1
- update to 57.0.0-1

* Mon Jan 16 2023 Yann Collette <ycollette dot nospam at free.fr> 56.0.0-1
- update to 56.0.0-1

* Sun Aug 21 2022 Yann Collette <ycollette dot nospam at free.fr> 54.0.0-1
- update to 54.0.0-1

* Sun Dec 12 2021 Yann Collette <ycollette dot nospam at free.fr> 52.0.0-1
- update to 52.0.0-1

* Wed Jul 14 2021 Yann Collette <ycollette dot nospam at free.fr> 51.1.1-1
- update to 51.1.1-1

* Wed May 19 2021 Yann Collette <ycollette dot nospam at free.fr> 50.2.0-1
- update to 50.2.0

* Sun Mar 14 2021 Yann Collette <ycollette dot nospam at free.fr> 50.0.0-1
- update to 50.0.0

* Sat Jan 2 2021 Yann Collette <ycollette dot nospam at free.fr> 49.1.0-1
- update to 49.1.0

* Fri Oct 23 2020 Yann Collette <ycollette dot nospam at free.fr> 48.0.0-1
- update to 48.0.0 and fix debug build

* Mon May 11 2020 Yann Collette <ycollette dot nospam at free.fr> 46.2.0-1
- Initial spec file
