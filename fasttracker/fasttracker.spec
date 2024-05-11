# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: fasttracker2
Version: 1.83.1
Release: 3%{?dist}
Summary: Module tracker software for creating music
License: GPL-3.0-or-later
URL: https://16-bits.org/ft2.php

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/8bitbubsy/ft2-clone/archive/v%{version}.tar.gz#/ft2-clone-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
FastTracker 2 is a music tracker created by Fredrik "Mr. H" Huss
and Magnus "Vogue" Högdahl, two members of the demogroup Triton
(who later founded Starbreeze Studios) which set about releasing
their own tracker after breaking into the scene in 1992 and winning
several demo competitions.
The source code of FastTracker 2 is written in Pascal using Borland
Pascal 7 and TASM. The program works natively under MS-DOS.

%prep
%autosetup -n ft2-clone-%{version}

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install

%cmake_install

mv %{buildroot}/%{_bindir}/ft2-clone %{buildroot}/%{_bindir}/fasttracker2

# Write bash script to select audio driver

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa fasttracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp src/gfxdata/icon/ft2-clone.ico %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-jack
Exec=%{name}-jack
Icon=/usr/share/pixmaps/ft2-clone.ico
Comment=FastTrack2 tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-alsa
Exec=%{name}-alsa
Icon=/usr/share/pixmaps/ft2-clone.ico
Comment=FastTrack2 tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name-pulse
Exec=%{name}-pulse
Icon=/usr/share/pixmaps/ft2-clone.ico
Comment=FastTrack2 tracker
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-alsa.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-jack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-pulse.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-alsa.desktop

%files
%doc README.md
%license LICENSE LICENSES.txt
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Sat May 11 2024 Yann Collette <ycollette.nospam@free.fr> - 1.83.1-3
- update to 1.83.1-3

* Fri May 10 2024 Yann Collette <ycollette.nospam@free.fr> - 1.83-3
- update to 1.83-3

* Fri Apr 12 2024 Yann Collette <ycollette.nospam@free.fr> - 1.82-3
- update to 1.82-3

* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 1.81-3
- update to 1.81-3

* Tue Apr 09 2024 Yann Collette <ycollette.nospam@free.fr> - 1.80-3
- update to 1.80-3

* Mon Mar 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1.79.2-3
- update to 1.79.2-3

* Mon Mar 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1.78-3
- update to 1.78-3

* Tue Mar 12 2024 Yann Collette <ycollette.nospam@free.fr> - 1.77.1-3
- update to 1.77.1-3

* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 1.77-3
- update to 1.77-3

* Fri Feb 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.76-3
- update to 1.76-3

* Mon Jan 08 2024 Yann Collette <ycollette.nospam@free.fr> - 1.75-3
- update to 1.75-3

* Sat Dec 16 2023 Yann Collette <ycollette.nospam@free.fr> - 1.74-3
- update to 1.74-3

* Mon Oct 30 2023 Yann Collette <ycollette.nospam@free.fr> - 1.73-3
- update to 1.73-3

* Sat Oct 07 2023 Yann Collette <ycollette.nospam@free.fr> - 1.72-3
- update to 1.72-3

* Wed Oct 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1.71-3
- update to 1.71-3

* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1.70-3
- update to 1.70-3

* Fri Aug 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1.69-3
- update to 1.69-3

* Thu Jun 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.68-3
- update to 1.68-3

* Tue Apr 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.67-3
- update to 1.67-3

* Thu Apr 13 2023 Yann Collette <ycollette.nospam@free.fr> - 1.66-3
- update to 1.66-3

* Fri Mar 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.65-3
- update to 1.65-3

* Tue Jan 24 2023 Yann Collette <ycollette.nospam@free.fr> - 1.63-3
- update to 1.63-3

* Mon Nov 28 2022 Yann Collette <ycollette.nospam@free.fr> - 1.62-3
- update to 1.62-3

* Mon Nov 07 2022 Yann Collette <ycollette.nospam@free.fr> - 1.61-3
- update to 1.61-3

* Tue Oct 11 2022 Yann Collette <ycollette.nospam@free.fr> - 1.60-3
- update to 1.60-3

* Mon Oct 03 2022 Yann Collette <ycollette.nospam@free.fr> - 1.59-3
- update to 1.59-3

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 1.58-3
- update to 1.58-3

* Sun Sep 04 2022 Yann Collette <ycollette.nospam@free.fr> - 1.57-3
- update to 1.57-3

* Tue Jul 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.56-3
- update to 1.56-3

* Wed Jun 15 2022 Yann Collette <ycollette.nospam@free.fr> - 1.55-3
- update to 1.55-3

* Wed Apr 20 2022 Yann Collette <ycollette.nospam@free.fr> - 1.54-3
- update to 1.54-3

* Sun Apr 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1.53-3
- update to 1.53-3

* Sun Feb 27 2022 Yann Collette <ycollette.nospam@free.fr> - 1.52-3
- update to 1.52-3

* Tue Feb 01 2022 Yann Collette <ycollette.nospam@free.fr> - 1.51-3
- update to 1.51-3

* Wed Jan 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.50-3
- update to 1.50-3

* Mon Dec 13 2021 Yann Collette <ycollette.nospam@free.fr> - 1.49-3
- update to 1.49-3

* Mon Nov 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.48-3
- update to 1.48-3

* Sun May 23 2021 Yann Collette <ycollette.nospam@free.fr> - 1.47-3
- update to 1.47-3

* Fri Apr 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.46-3
- update to 1.46-3

* Thu Apr 01 2021 Yann Collette <ycollette.nospam@free.fr> - 1.45-3
- update to 1.45-3

* Thu Jan 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.43-3
- update to 1.43-3

* Sun Jan 3 2021 Yann Collette <ycollette.nospam@free.fr> - 1.42-3
- update to 1.42-3

* Thu Nov 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.41-3
- update to 1.41-3

* Sat Nov 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.40-3
- update to 1.40-3

* Sun Nov 08 2020 Yann Collette <ycollette.nospam@free.fr> - 1.39-3
- update to 1.39-3

* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.38-3
- update to 1.38-3

* Thu Oct 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.37-3
- update to 1.37-3

* Mon Oct 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.36-3
- update to 1.36-3

* Mon Sep 28 2020 Yann Collette <ycollette.nospam@free.fr> - 1.35-3
- update to 1.35-3

* Thu Sep 10 2020 Yann Collette <ycollette.nospam@free.fr> - 1.34-3
- update to 1.34-3

* Mon Sep 7 2020 Yann Collette <ycollette.nospam@free.fr> - 1.33-3
- update to 1.33-3

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.32-3
- update to 1.32-3

* Sun Aug 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.31-3
- update to 1.31-3

* Sun Aug 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.30-3
- update to 1.30-3

* Sun Aug 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.28-3
- update to 1.28-3

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.27-3
- update to 1.27-3

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.26-3
- update to 1.26-3

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.25-3
- update to 1.25-3

* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.24-3
- update to 1.24-3

* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.23-3
- update to 1.23-3

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.21-3
- update to 1.21-3

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.17-3
- update to 1.17-3

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.17-1
- update to 1.17

* Thu Apr 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.15-1
- update to 1.15

* Wed Mar 18 2020 Yann Collette <ycollette.nospam@free.fr> - 1.13-1
- update to 1.13

* Sat Mar 14 2020 Yann Collette <ycollette.nospam@free.fr> - 1.12-1
- update to 1.12

* Tue Mar 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10-1
- update to 1.10

* Sun Feb 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.09-1
- update to 1.09

* Sat Feb 8 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-1
- update to 1.08

* Fri Jan 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.07-1
- update to 1.07

* Thu Jan 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.06-1
- update to 1.06

* Sun Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.05-1
- update to 1.05

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.01-1
- update to 1.01

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b166-1
- update to 0.1b166

* Mon Aug 5 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b164-1
- update to 0.1b164

* Thu Feb 21 2019 Yann Collette <ycollette dot nospam at free dot fr> 0.1b137-1
- initial spec file
