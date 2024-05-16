# Tag: MIDI, Alsa
# Type: Standalone
# Category: MIDI, Tool
# GUIToolkit: Qt

%define	desktop_vendor planetccrma

Summary: ALSA MIDI monitor
Name: kmidimon
Version: 0.7.5
Release: 1%{?dist}
License: GPL
URL: https://kmetronome.sourceforge.net/kmidimon/
ExclusiveArch: x86_64 aarch64

Source0: https://sourceforge.net/projects/kmidimon/files/%{version}/kmidimon-%{version}.tar.bz2
Source1: kmidimon.desktop
Patch0: kmidimon-0001-remove-uninstall-target.patch
Patch1: kmidimon-0001-use-nullptr.patch

Vendor:       Planet CCRMA
Distribution: Planet CCRMA

Requires: hicolor-icon-theme

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: cmake gettext-devel
BuildRequires: kdelibs-devel
%if 0%{?fedora} >= 34
BuildRequires: drumstick0-devel
%endif
BuildRequires: alsa-lib-devel

%description
MIDI monitor for Linux using ALSA sequencer and KDE user interface.

%prep
%autosetup -p1

%build

%set_build_flags
export CXXFLAGS="-fPIC -I/usr/include/drumstick $CXXFLAGS"

%cmake
%cmake_build

%install

%cmake_install

# absolute symlink: /usr/share/doc/HTML/en/kmidimon/common -> /usr/share/doc/HTML/en/common
# absolute symlink: /usr/share/doc/HTML/ja/kmidimon/common -> /usr/share/doc/HTML/ja/common

rm %{buildroot}%{_datadir}/doc/HTML/en/kmidimon/common
rm %{buildroot}%{_datadir}/doc/HTML/ja/kmidimon/common

# desktop file categories
BASE="Application AudioVideo Audio"
XTRA="X-MIDI Midi"

mkdir -p %{buildroot}%{_datadir}/applications

desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{SOURCE1}

%{find_lang} kmidimon

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f kmidimon.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%license COPYING
%{_bindir}/kmidimon
%{_datadir}/doc/HTML/en/kmidimon
%{_datadir}/doc/HTML/ja/kmidimon
%{_datadir}/icons/hicolor/*/apps/kmidimon*
%{_datadir}/applications/%{desktop_vendor}-kmidimon.desktop
%{_datadir}/applications/kde4/kmidimon.desktop
%{_datadir}/kde4/apps/kmidimon
%{_mandir}/man1/kmidimon.1.gz
%{_mandir}/ja/man1/kmidimon.1.gz

%changelog
* Fri May 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.5-1
- update to 0.7.5-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> -
- update for Fedora 29

* Tue Jan 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- added documentation patch to build on fc14

* Tue Nov 24 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.1-1
- updated to version 0.7.1, updated post scripts

* Wed Jul 16 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- tweaked spec file for building on CentOS

* Tue Jul 14 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1
- add proper dependencies for building on fc9

* Fri Feb  1 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- built on CentOS

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.0-1
- updated to version 0.5.0
- updated desktop categories
- now builds with cmake

* Tue Dec 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-2
- spec file tweaks, build for fc6

* Thu Sep  7 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.1-1
- updated to 0.4.1

* Fri Aug 19 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3-1
- updated to version 0.3

* Wed May  4 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1-1
- initial build.
