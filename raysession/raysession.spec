# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

%global __python %{__python3}

Name:    raysession
Version: 0.13.1
Release: 2%{?dist}
Summary: A JACK session manager

License: GPLv2+
URL:     https://github.com/Houston4444/RaySession

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh RaySession v0.13.1

Source0: RaySession.tar.gz
Source1: source-houston4444.sh

BuildArch: noarch

BuildRequires: python3-qt5-devel
BuildRequires: python3
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: gtk-update-icon-cache
BuildRequires: desktop-file-utils

Requires(pre): python3-qt5
Requires(pre): python3-pyliblo
Requires(pre): python3-pyxdg

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour, Carla,
QTractor, Non-Timeline, etc... It uses the same API as Non Session Manager, so
programs compatible with NSM are also compatible with Ray Session.
As Non Session Manager, the principle is to load together audio programs, then
be able to save or close all documents together.

%prep
%autosetup -n RaySession

# Fix desktop categories
sed -i -e "s/AudioVideo;//g" data/share/applications/raysession.desktop
# Fix permission on executable python script
chmod a+x src/shared/jacklib.py

%build

%make_build PREFIX=/usr LRELEASE=lrelease-qt5

%install

%make_install PREFIX=/usr LRELEASE=lrelease-qt5

# Cleanup and redo symbolic links
rm %{buildroot}/usr/bin/ray_git
rm %{buildroot}/usr/bin/ray-jack_checker_daemon
rm %{buildroot}/usr/bin/ray-jack_config_script
rm %{buildroot}/usr/bin/ray-pulse2jack

ln -s /usr/share/raysession/src/bin/ray_git                 %{buildroot}/usr/bin/ray_git
ln -s /usr/share/raysession/src/bin/ray-jack_checker_daemon %{buildroot}/usr/bin/ray-jack_checker_daemon
ln -s /usr/share/raysession/src/bin/ray-jack_config_script  %{buildroot}/usr/bin/ray-jack_config_script  
ln -s /usr/share/raysession/src/bin/ray-pulse2jack          %{buildroot}/usr/bin/ray-pulse2jack

desktop-file-install                         \
  --add-category="Audio;AudioVideo;Qt"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --add-category="System"                    \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ray-jack_checker.desktop

desktop-file-install                         \
  --add-category="System"                    \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ray-jackpatch.desktop

desktop-file-install                         \
  --add-category="System"                    \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ray-network.desktop

%check

desktop-file-validate  %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-jack_checker.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-jackpatch.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-network.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/raysession/*
%{_sysconfdir}/xdg/raysession/client_templates/*

%changelog
* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.13.1-2
- update to 0.13.1-2

* Tue Sep 27 2022 Yann Collette <ycollette.nospam@free.fr> - 0.13.0-2
- update to 0.13.0-2

* Sat Jan 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.12.2-2
- update to 0.12.2-2

* Wed Dec 29 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12.1-2
- update to 0.12.1-2

* Sun Dec 19 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to 0.12.0-2 - add a missing dependency

* Sat Dec 18 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-1
- update to 0.12.0-1

* Sat Aug 28 2021 Yann Collette <ycollette.nospam@free.fr> - 0.11.1-1
- update to 0.11.1-1

* Thu Aug 05 2021 Yann Collette <ycollette.nospam@free.fr> - 0.11.0-1
- update to 0.11.0-1

* Thu Feb 4 2021 Yann Collette <ycollette.nospam@free.fr> - 0.10.1-1
- update to 0.10.1-1

* Tue Nov 10 2020 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- update to 0.10.0-1

* Sat Aug 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.2-1
- update to 0.9.2-1

* Wed Jul 29 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-1
- update to 0.9.1-1

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- update to 0.9.0-1

* Wed Jun 17 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- update to 0.8.3-1

* Thu Nov 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- update to 0.8.2-1

* Thu Oct 24 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Tue Oct 15 2019 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.2-1
- update to 0.7.2-1

* Sat May 4 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- Initial spec file
