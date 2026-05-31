# Status: active
# Tag: Sf2
# Type: Standalone
# Category: Audio, Tool

%global commit0 351a7d4aa73021e7d910c07600db4f5bcbeaa24d

Name: boutronique
Version: 0.0.1
Release: 1%{?dist}
Summary: Boutronique is a small desktop tool to helps identify and extract short, loopable samples from a loaded sound file
URL: https://boutronique.jmfavreau.info
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://forge.chapril.org/jmtrivial/boutronique/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-gui
BuildRequires: qt6-qtmultimedia-devel
BuildRequires: qt6-linguist
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

%description
Boutronique is a small desktop tool to helps identify and extract short, loopable samples from a loaded sound file.
The program provides a simple waveform view and graphical tools to mark, adjust and preview looping regions.
It is intended as a lightweight utility to make finding clean loops easier and to export them for use in other audio software.
Features:
- Load and display audio waveforms
- Select and preview looping regions
- Loop playback for selected parts
- Basic information display (duration, BPM planned)
- Export of selected audio regions for external use


%prep
%autosetup -n %{name}-%{commit0}

%build

lrelease-qt6 Boutronique.pro

%qmake_qt6 Boutronique.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 build/bin/release/Boutronique %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=%{name}
Icon=%{name}
Comment=Boutronique is a small desktop tool to helps identify and extract short, loopable samples from a loaded sound file
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 images/boutronique-logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --vendor '' \
        --add-category=Sequencer \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md AUTHORS.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
* Sun May 31 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
