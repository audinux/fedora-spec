# Status: active
# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

Name: raysession
Version: 0.17.0
Release: 4%{?dist}
Summary: A JACK session manager

License: GPL-2.0-or-later
URL: https://github.com/Houston4444/RaySession
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh RaySession v0.17.0

Source0: RaySession.tar.gz
Source1: source-houston4444.sh

BuildArch: noarch

BuildRequires: python3
BuildRequires: python3-pyqt6-devel
BuildRequires: python3-QtPy
BuildRequires: python-jack-client
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: gtk-update-icon-cache
BuildRequires: desktop-file-utils

Requires(pre): python3-QtPy
Requires(pre): python-jack-client
Requires(pre): python3-pyqt6
Requires(pre): python3-pyliblo3
Requires(pre): python3-pyxdg
%if 0%{?fedora} >= 41
Requires(pre): python3-legacy-cgi
%endif

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour, Carla,
QTractor, Non-Timeline, etc... It uses the same API as Non Session Manager, so
programs compatible with NSM are also compatible with Ray Session.
As Non Session Manager, the principle is to load together audio programs, then
be able to save or close all documents together.

%prep
%autosetup -n RaySession

# Fix desktop categories
sed -i -e "s/AudioVideo;//g" data/share/applications/ray-alsapatch.desktop
sed -i -e "s/AudioVideo;//g" data/share/applications/ray-jack_checker.desktop
sed -i -e "s/AudioVideo;//g" data/share/applications/ray-jackpatch.desktop
sed -i -e "s/AudioVideo;//g" data/share/applications/ray-network.desktop
sed -i -e "s/AudioVideo;//g" data/share/applications/raysession.desktop

%build

%make_build PREFIX=/usr LRELEASE=lrelease-qt6 RCC=/usr/lib64/qt6/libexec/rcc

%install

%make_install PREFIX=/usr LRELEASE=lrelease-qt6 RCC=/usr/lib64/qt6/libexec/rcc

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
  %{buildroot}/%{_datadir}/applications/raysession.desktop

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

desktop-file-install                         \
  --add-category="System"                    \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/ray-alsapatch.desktop

# cleanup
rm -rf %{buildroot}/etc/bash_completion.d/ray_completion.sh

%check

desktop-file-validate  %{buildroot}/%{_datadir}/applications/raysession.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-jack_checker.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-jackpatch.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-network.desktop
desktop-file-validate  %{buildroot}/%{_datadir}/applications/ray-alsapatch.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/raysession/*
%dir %{_sysconfdir}/xdg/raysession/
%{_sysconfdir}/xdg/raysession/client_templates/*

%changelog
* Mon Nov 03 2025 Yann Collette <ycollette.nospam@free.fr> - 0.17.0-4
- update to 0.17.0-4

* Fri Sep 19 2025 Yann Collette <ycollette.nospam@free.fr> - 0.14.4-4
- update to 0.14.4-4 - use python3-pyliblo3

* Mon Nov 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.14.4-3
- update to 0.14.4-3

* Thu Nov 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.14.3-3
- update to 0.14.3-3 - add missing Requires for f41

* Sat Dec 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.14.3-2
- update to 0.14.3-2

* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.14.2-2
- update to 0.14.2-2

* Sat Sep 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.14.1-2
- update to 0.14.1-2

* Tue Sep 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.14.0-2
- update to 0.14.0-2

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
