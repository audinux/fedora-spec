Name: tutka
Version: 1.1.3
Release: 1%{?dist}
Summary: Tutka is a free tracker style MIDI sequencer

License: GPLv2	
URL: https://www.nongnu.org/tutka/	
Source0: http://download.savannah.gnu.org/releases/tutka/tutka-1.1.3.tar.xz
Source1: tutka.1

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: qt-devel
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils

%description
Tutka is a free (as in freedom) tracker style MIDI sequencer for GNU/Linux and Mac OS X.
It is similar to programs like SoundTracker, ProTracker and FastTracker except that it
does not support samples and is meant for MIDI use only. Tutka uses a custom XML based
file format for storing songs. Songs in OctaMED SoundStudio's MMD2 file format can
also be loaded and saved. 

%prep
%autosetup

sed -i -e "/-Werror/d" src/src.pro

%build
%qmake_qt4
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp src/tutka  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/
cp -r src/icons/* %{buildroot}/%{_datadir}/icons/hicolor/

install -m 755 -d %{buildroot}/%{_mandir}/man1/
install -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/

# Create some desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Tutka
Comment=MIDI Audio tracker
Exec=tutka
Icon=tutka
Terminal=false
Type=Application
Categories=Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/*
%{_mandir}/*

%changelog
* Wed Dec 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-1
- initial spec
