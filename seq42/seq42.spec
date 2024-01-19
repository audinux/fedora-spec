# Tag: Sequencer, MIDI
# Type: Standalone
# Category: Audio, Sequencer, MIDI

Name: seq42
Version: 2.1.3
Release: 1%{?dist}
Summary: MIDI sequencer
License: GPL
URL: https://github.com/Stazed/seq42

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Stazed/seq42/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm30-devel
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

%description
It's a fork of seq24 (which is a fork of the original seq24),
but with a greater emphasis on song editing (as opposed to live looping)
and some enhancements. seq24 is great for sequence editing and live looping,
but I found it cumbersome to edit songs as the number of sequences
grew (I would quickly reach a point where there were more sequence rows
in the song editor than would fit on my screen without scrolling, which
made it difficult to keep track of the whole song).

%prep
%autosetup -n %{name}-%{version}

sed -i -e "/NEWS /,+1d" CMakeLists.txt

%build

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/seq42/examples/
cp seq42usr.example %{buildroot}/%{_datadir}/seq42/examples/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Apr 08 2023 Yann Collette <ycollette.nospam@free.fr> - 2.1.3-1
- udate to 2.1.3-1

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 2.1.2-1
- udate to 2.1.2-1

* Tue Apr 19 2022 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-1
- udate to 2.1.1-1

* Mon Mar 21 2022 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-1
- udate to 2.1.0-1

* Mon Mar 14 2022 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- udate to 2.0.0-1

* Mon May 03 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.4-1
- initial version
