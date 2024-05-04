# Tag: Tracker, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: schismtracker
Version: 20240503
Release: 2%{?dist}
Summary: Module tracker software for creating music
License: GPL-3.0-or-later
URL: https://github.com/schismtracker/schismtracker

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/schismtracker/schismtracker/archive/refs/tags/%{version}.tar.gz#/schismtracker-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: SDL2-devel
BuildRequires: libXext-devel
BuildRequires: python
BuildRequires: desktop-file-utils

%description
Schism Tracker is a free and open-source reimplementation of [Impulse
Tracker](https://github.com/schismtracker/schismtracker/wiki/Impulse-Tracker),
a program used to create high quality music without the requirements of
specialized, expensive equipment, and with a unique "finger feel" that is
difficult to replicate in part. The player is based on a highly modified
version of the [Modplug](https://openmpt.org/legacy_software) engine, with a
number of bugfixes and changes to [improve IT].

%prep
%autosetup -n %{name}-%{version}

sed -i -e "/-qv 1.2.1/,+2d" configure.ac

%build

%set_build_flags
export LDFLAGS="$LDFLAGS -lXext"

autoreconf --force --install
mkdir auto
%configure
%make_build

%install
%make_install

# Remove last action entry
head -n-3 %{buildroot}/%{_datadir}/applications/schism.desktop > %{buildroot}/%{_datadir}/applications/schism.desktop.tmp
rm %{buildroot}/%{_datadir}/applications/schism.desktop
mv %{buildroot}/%{_datadir}/applications/schism.desktop.tmp %{buildroot}/%{_datadir}/applications/schism.desktop

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS NEWS INSTALL README.md
%license COPYING
%{_bindir}/schismtracker
%{_datadir}/pixmaps/*
%{_datadir}/man/*
%{_datadir}/applications/*

%changelog
* Sat May 04 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240503-1
- update to 20240503

* Sat Apr 27 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240426-1
- update to 20240426

* Tue Apr 09 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240409-1
- update to 20240409

* Sat Mar 09 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240308-1
- update to 20240308

* Tue Jan 30 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240129-1
- update to 20240129

* Sun Oct 29 2023 Yann Collette <ycollette dot nospam at free dot fr> - 20231029-1
- update to 20231029

* Thu Sep 07 2023 Yann Collette <ycollette dot nospam at free dot fr> - 20230906-1
- update to 20230906

* Tue Nov 01 2022 Yann Collette <ycollette dot nospam at free dot fr> - 20221020-1
- update to 20221020

* Sun Aug 07 2022 Yann Collette <ycollette dot nospam at free dot fr> - 20220807-1
- update to 20220807

* Tue Jan 25 2022 Yann Collette <ycollette dot nospam at free dot fr> - 20220125-1
- update to 20220125

* Wed Nov 17 2021 Yann Collette <ycollette dot nospam at free dot fr> - 20211116-1
- update to 20211116

* Thu May 27 2021 Yann Collette <ycollette dot nospam at free dot fr> - 20210525-1
- update to 20210525

* Tue May 12 2020 Yann Collette <ycollette dot nospam at free dot fr> - 20200412-1
- update to 20200412

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free dot fr> - 20190805-1
- update to 20190805

* Mon Aug 5 2019 Yann Collette <ycollette dot nospam at free dot fr> - 20190722-1
- update to 20190722

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20181223-1
- update to 20181223

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180810-1
- update to Fedora 29

* Sat Aug 11 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180810-1
- update to latest version

* Mon May 14 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180513-1
- update to latest version

* Sat Apr 14 2018 Yann Collette <ycollette dot nospam at free dot fr> - 20180209-1
- Initial version of the package

