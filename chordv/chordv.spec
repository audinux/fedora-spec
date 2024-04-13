# Tag: Jack, Alsa, Editor
# Type: Standalone
# Category: Audio, Sequencer

Name:    chordv
Version: 1.2
Release: 1%{?dist}
Summary: ChordV provide an editor to define song and chord.
URL:     https://sourceforge.net/projects/chordv
License: GPL-3.0-only

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/chordv/files/chordv_%{version}.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
%if 0%{?fedora} >= 40
BuildRequires: podofo0.9-devel
%else
BuildRequires: podofo-devel
%endif
BuildRequires: libidn-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
ChordV provide an editor to define song and chord.

%prep
%autosetup -n src

sed -i -e "s/Application;Office;/AudioVideo/g" Install/chordV.desktop
sed -i -e "/Encoding=/d"  Install/chordV.desktop

%build

%qmake_qt5 chordV.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_datadir}/chordV/
install -m 644 Bd/Chord.db %{buildroot}/%{_datadir}/chordV/
install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/chordV %{buildroot}/%{_bindir}/
install -m 644 Images/chordv.svg %{buildroot}/%{_datadir}/chordV/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 Install/chordV.desktop %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/chordV/Français/
install -m 755 -d %{buildroot}/%{_datadir}/chordV/English/
cp -ra translations/Français/* %{buildroot}/%{_datadir}/chordV/Français/
cp -ra translations/English/* %{buildroot}/%{_datadir}/chordV/English/

install -m 644 Example/Français/demo.chop %{buildroot}/%{_datadir}/chordV/Français/
install -m 644 Example/English/demo.chop %{buildroot}/%{_datadir}/chordV/English/

install -m 755 -d %{buildroot}/%{_datadir}/chordV/Français/img/
install -m 755 -d %{buildroot}/%{_datadir}/chordV/English/img/

install -m 644 Docs/User/Français/pdf/doc.pdf  %{buildroot}/%{_datadir}/chordV/Français
install -m 644 Docs/User/Français/txt/doc.md %{buildroot}/%{_datadir}/chordV/Français
install -m 644 Docs/User/Français/html/doc.html %{buildroot}/%{_datadir}/chordV/Français
cp -ra Docs/User/Français/html/img/* %{buildroot}/%{_datadir}/chordV/Français/img/

install -m 644 Docs/User/English/pdf/doc.pdf  %{buildroot}/%{_datadir}/chordV/English/
install -m 644 Docs/User/English/txt/doc.md %{buildroot}/%{_datadir}//chordV/English/
install -m 644 Docs/User/English/html/doc.html %{buildroot}/%{_datadir}/chordV/English/
cp -ra Docs/User/English/html/img/* %{buildroot}/%{_datadir}/chordV/English/img/

# install konfyt.desktop properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/chordV.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/chordV.desktop

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Tue Jun 07 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial spec
