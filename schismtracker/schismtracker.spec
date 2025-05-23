# Status: active
# Tag: Tracker, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: schismtracker
Version: 20250415
Release: 2%{?dist}
Summary: Module tracker software for creating music
License: GPL-3.0-or-later
URL: https://github.com/schismtracker/schismtracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/schismtracker/schismtracker/archive/refs/tags/%{version}.tar.gz#/schismtracker-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: python
BuildRequires: perl-open
BuildRequires: SDL2-devel
BuildRequires: libXext-devel
BuildRequires: flac-devel
BuildRequires: utf8proc-devel
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

%build

autoreconf --force --install
mkdir auto
%configure
%make_build

%install
%make_install

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
* Wed Apr 16 2025 Yann Collette <ycollette dot nospam at free dot fr> - 20250415-2
- update to 20250415-2

* Fri Mar 14 2025 Yann Collette <ycollette dot nospam at free dot fr> - 20250313-2
- update to 20250313-2

* Thu Mar 06 2025 Yann Collette <ycollette dot nospam at free dot fr> - 20250305-2
- update to 20250305-2

* Thu Dec 26 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20241226-2
- update to 20241226-2

* Mon Oct 21 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20241021-2
- update to 20241021-2

* Tue Sep 10 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240909-2
- update to 20240909-2

* Sat Aug 10 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240809-1
- update to 20240809

* Sun Jun 30 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240630-1
- update to 20240630

* Sun Jun 16 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240614-1
- update to 20240614

* Sun Jun 09 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240609-1
- update to 20240609

* Thu May 30 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240529-1
- update to 20240529

* Fri May 24 2024 Yann Collette <ycollette dot nospam at free dot fr> - 20240523-1
- update to 20240523

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

