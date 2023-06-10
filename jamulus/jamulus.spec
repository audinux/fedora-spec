# Tag: Jack
# Type: Standalone
# Category: Audio

%global v_major 3
%global v_minor 9
%global v_patch 1

Name:    jamulus
Version: %{v_major}.%{v_minor}.%{v_patch}
Release: 8%{?dist}
Summary: Internet jam session software
URL:     https://github.com/corrados/jamulus/
License: GPL-2.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/corrados/jamulus/archive/r%{v_major}_%{v_minor}_%{v_patch}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: libsndfile-devel
BuildRequires: opus-devel
BuildRequires: desktop-file-utils

%description
jamulus is a client / server software which allow to perform
real-time rehearsal over the internet. It uses Jack Audio Connection Kit
and Opus audio codec to manage the audio session. 

%prep
%autosetup -n %{name}-r%{v_major}_%{v_minor}_%{v_patch}

# Remove Opus source code, we use Opus library from Fedora
#rm -rf libs/opus

%build

%qmake_qt5 Jamulus.pro CONFIG+="noupcasename"
%make_build VERBOSE=1

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -p %{name} %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 -p linux/%{name}.desktop %{buildroot}%{_datadir}/applications/
install -m 644 -p linux/%{name}-server.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512/
install -m 644 -p src/res/io.jamulus.jamulus.png %{buildroot}/%{_datadir}/icons/hicolor/apps/512x512

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p src/res/io.jamulus.jamulusserver.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p src/res/io.jamulus.jamulus.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

install -m 755 -d %{buildroot}/%{_mandir}/man1
install -m 644 -p linux/Jamulus.1 %{buildroot}/%{_mandir}/man1

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-server.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-server.desktop

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-server.desktop
%{_datadir}/icons/hicolor/apps/512x512/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*

%changelog
* Tue Oct 18 2022 Yann Collette <ycollette.nospam@free.fr> - 3.9.1-8
- update to 3.9.1-8

* Sat Jul 30 2022 Yann Collette <ycollette.nospam@free.fr> - 3.9.0-8
- update to 3.9.0-8

* Tue Feb 22 2022 Yann Collette <ycollette.nospam@free.fr> - 3.8.2-8
- update to 3.8.2-8

* Tue Feb 22 2022 Yann Collette <ycollette.nospam@free.fr> - 3.8.1-8
- update to 3.8.1-8 - fix source

* Sat Oct 23 2021 Yann Collette <ycollette.nospam@free.fr> - 3.8.1-7
- update to 3.8.1-7

* Thu Jun 03 2021 Yann Collette <ycollette.nospam@free.fr> - 3.8.0-7
- update to 3.8.0-7

* Thu Mar 18 2021 Yann Collette <ycollette.nospam@free.fr> - 3.7.0-7
- update to 3.7.0-7

* Sat Dec 12 2020 Yann Collette <ycollette.nospam@free.fr> - 3.6.2-7
- update to 3.6.2-7

* Sun Nov 22 2020 Yann Collette <ycollette.nospam@free.fr> - 3.6.1-7
- update to 3.6.1-7

* Sun Oct 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-7
- update to 3.6.0-7

* Sun Oct 4 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.12-7
- update to 3.5.12-7

* Sun Sep 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.11-7
- update to 3.5.11-7

* Sun Aug 16 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.10-7
- update to 3.5.10-7

* Sun Jul 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.9-7
- update to 3.5.9-7

* Wed Jul 1 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.8-7
- update to 3.5.8-7

* Sun Jun 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.7-7
- update to 3.5.7-7

* Sat Jun 27 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.6-7
- update to 3.5.6-7 - fix opus enable-hardening problem

* Tue Jun 9 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.6-6
- update to 3.5.6-6

* Mon Jun 8 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-6
- fix spec file

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-5
- fix spec file

* Sat May 30 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-4
- fix debug package

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-3
- compile with fedora opus package
- fix install

* Thu May 28 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-2
- fix an executable right problem

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.5-1
- update 3.5.5-1

* Mon May 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-1
- update 3.5.4-1

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.3-1
- update 3.5.3-1

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.2-1
- update 3.5.2-1

* Mon Apr 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.1-1
- update 3.5.1-1

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.0-1
- update 3.5.0-1

* Sun Apr 12 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.7-1
- update 3.4.7-1

* Tue Mar 31 2020 Yann Collette <ycollette.nospam@free.fr> - 3.4.4-1
- update 3.4.4-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1
- update for Fedora 29

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 3.4.3-1

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.4.2-1

* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 3.4.1-1
- Initial release
