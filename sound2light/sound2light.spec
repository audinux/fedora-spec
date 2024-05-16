# Tag: Audio, Tool, OSC
# Type: Standalone
# Category: Audio, Tool

Name: sound2light
Version: 0.0.3.1.0.2
Release: 2%{?dist}
Summary: A tool converting sound input to OSC trigger signals
URL: https://github.com/ETCLabs/Sound2Light
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/ETCLabs/Sound2Light/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-linguist
BuildRequires: alsa-lib-devel
BuildRequires: fftw-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
The Sound2Light tool converts live audio signals to trigger events
that can be sent as OSC messages. It can reproduce the sound-to-light
function of the NT/NTX consoles with systems of the Eos-, Cobalt-
and ColorSource-family. It can also be remotely controlled by OSC.

%prep
%autosetup -n Sound2Light-%{version}

%build

cd src

%qmake_qt5 S2L.pro
%make_build

%install

cd src

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 s2l %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 images/icons/etclogo.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Write desktop files
install -m 755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sound2Light
Exec=s2l
Icon=%{name}
Comment=A tool converting sound input to OSC trigger signals
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc src/README.md
%license src/LICENSE.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Fri Jan 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.3.1.0.2-2
- update to 0.0.3.1.0.2-2

* Mon Sep 12 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.3.1.0.2-1
- Initial spec file
