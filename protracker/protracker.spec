# Tag: Tracker, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Summary: Chiptune tracker for making chiptune-like music on a modern computer.
Name:    protracker2
Version: 1.48
Release: 4%{?dist}
License: BSD
URL:     https://16-bits.org/pt.php

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/8bitbubsy/pt2-clone/archive/v%{version}.tar.gz#/pt2-clone-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: SDL2-devel

%description
ProTracker2 is a chiptune tracker for making chiptune-like music on a modern computer.

Obsoletes: protracker

%prep
%autosetup -n pt2-clone-%{version}

%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build

%install

%cmake_install

mv %{buildroot}/%{_bindir}/pt2-clone %{buildroot}/%{_bindir}/protracker2

cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa protracker2
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p src/gfx/pt2-clone.ico %{buildroot}/%{_datadir}/icons/%{name}/%{name}.ico

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp release/effects.txt release/help.txt release/keybindings.txt release/LICENSES.txt release/other/protracker.ini %{buildroot}%{_datadir}/%{name}

# Create some desktop files
install -m 755 -d %{buildroot}%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=ProTracker Jack
Comment=Audio tracker
Exec=protracker-jack
Icon=protracker
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-jack.desktop

cat > %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=ProTracker PulseAudio
Comment=Audio tracker
Exec=protracker-pulse
Icon=protracker
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-pulse.desktop

cat > %{buildroot}/%{_datadir}/applications/%{name}-alsa.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=ProTracker Alsa
Comment=Audio tracker
Exec=protracker-alsa
Icon=protracker
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
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
%{_bindir}/protracker2
%{_bindir}/protracker2-jack
%{_bindir}/protracker2-pulse
%{_bindir}/protracker2-alsa
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{_datadir}/applications/*

%changelog
* Tue May 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1.48.0-4
- update to 1.48.0-4

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 1.47.0-4
- update to 1.47.0-4

* Sun Apr 10 2022 Yann Collette <ycollette.nospam@free.fr> - 1.46.0-4
- update to 1.46.0-4

* Thu Apr 07 2022 Yann Collette <ycollette.nospam@free.fr> - 1.44.0-4
- update to 1.44.0-4

* Thu Mar 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1.43.0-4
- update to 1.43.0-4

* Mon Mar 14 2022 Yann Collette <ycollette.nospam@free.fr> - 1.42.0-4
- update to 1.42.0-4

* Thu Feb 24 2022 Yann Collette <ycollette.nospam@free.fr> - 1.41.0-4
- update to 1.41.0-4

* Tue Feb 01 2022 Yann Collette <ycollette.nospam@free.fr> - 1.40.0-4
- update to 1.40.0-4

* Wed Jan 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.39.0-4
- update to 1.39.0-4

* Fri Dec 31 2021 Yann Collette <ycollette.nospam@free.fr> - 1.38.0-4
- update to 1.38.0-4

* Thu Oct 28 2021 Yann Collette <ycollette.nospam@free.fr> - 1.37.0-4
- update to 1.37.0-4

* Mon Oct 11 2021 Yann Collette <ycollette.nospam@free.fr> - 1.36.0-4
- update to 1.36.0-4 (fix2)

* Thu Sep 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.34.0-4
- update to 1.34.0-4

* Sat Sep 04 2021 Yann Collette <ycollette.nospam@free.fr> - 1.33.0-4
- update to 1.33.0-4

* Thu Aug 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.32.0-4
- update to 1.32.0-4

* Sun Jun 20 2021 Yann Collette <ycollette.nospam@free.fr> - 1.31.0-4
- update to 1.31.0-4

* Fri Apr 30 2021 Yann Collette <ycollette.nospam@free.fr> - 1.30.0-4
- update to 1.30.0-4

* Sun Mar 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.29.0-4
- update to 1.29.0-4

* Sun Jan 3 2021 Yann Collette <ycollette.nospam@free.fr> - 1.28.0-4
- update to 1.28.0-4

* Fri Dec 18 2020 Yann Collette <ycollette.nospam@free.fr> - 1.27.0-4
- update to 1.27.0-4

* Mon Nov 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.26.1-4
- update to 1.26.1-4 (1.26_fix)

* Wed Nov 18 2020 Yann Collette <ycollette.nospam@free.fr> - 1.25.1-4
- update to 1.25.1-4 (1.25_fix)

* Sun Oct 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.24-4
- update to 1.24-4

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.23-4
- fix for fedora 33

* Sat Sep 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.23-3
- update to 1.23-3

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.22-3
- update to 1.22-3

* Fri Jul 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.21-3
- update to 1.21-3

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.20-3
- update to 1.20-3

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.19-3
- update to 1.19-3

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 1.18-3
- update to 1.18-3

* Wed Jun 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.17-3
- update to 1.17-3

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.16-3
- update to 1.16-3

* Mon May 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.12-3
- update to 1.12-3

* Sat Apr 25 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10-3
- update to 1.10-3

* Fri Apr 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-3
- fix for Fedora 32

* Mon Apr 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.08-2
- update to 1.08-2

* Wed Apr 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.07-2
- update to 1.07-2

* Mon Feb 17 2020 Yann Collette <ycollette.nospam@free.fr> - 1.06-2
- update to 1.06-2

* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.04-2
- update to 1.04-2

* Fri Jan 24 2020 Yann Collette <ycollette.nospam@free.fr> - 1.03-2
- update to 1.03-2

* Mon Jan 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.02-2
- update to 1.02-2

* Sun Dec 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.01-2
- update to 1.01-2. Rename protracker to protracker2

* Sat Aug 17 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r191-2
- update to revision 191

* Wed Jul 17 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r188-2
- update to revision 188

* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-2
- Add pulse and jack script

* Thu Mar 14 2019 Yann Collette <ycollette dot nospam at free.fr> 2.3r167-1
- Initial release of spec file
