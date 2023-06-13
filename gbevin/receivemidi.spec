# Tag: Alsa, MIDI
# Type: Standalone
# Category: MIDI, Tool

Name:    receivemidi
Version: 1.3.1
Release: 3%{?dist}
Summary: A command line tool to receive MIDI event
License: GPL-3.0-only
URL:     https://github.com/gbevin/ReceiveMIDI

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/%{version}.tar.gz#/ReceiveMIDI-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: libatomic

%description
Multi-platform command-line tool making it very easy to quickly
receive and monitor MIDI messages from MIDI devices on your computer.

%prep
%autosetup -n ReceiveMIDI-%{version}

%build

cd Builds/LinuxMakefile

%make_build STRIP=true CPPFLAGS="%{optflags}"

%install 

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -p build/receivemidi %{buildroot}/%{_bindir}/

%files
%doc README.md
%license COPYING.md
%{_bindir}/*

%changelog
* Wed Mar 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-3
- update to 1.3.1-3

* Thu Jan 19 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-3
- update to 1.3.0-3

* Sun Feb 20 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-3
- update to 1.2.0-3

* Sat Jan 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-3
- update to 1.1.0-3

* Sun Oct 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-3
- fix debug + install

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-2
- fix permission

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.6-1
- Initial spec file
