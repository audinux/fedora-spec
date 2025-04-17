# Status: active
# Tag: MIDI
# Type: Standalone
# Category: MIDI

%global commit0 665f0976775d06bc4a3680228b998a5956c7461b

Summary: QMidiControl is a virtual MIDI control pad
Name: qmidicontrol
Version: 0.0.1
Release: 1%{?dist}
License: GPLv2+
URL: https://sourceforge.net/projects/alsamodular/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/code-snapshots/git/a/al/alsamodular/qmidicontrol.git.git/alsamodular-qmidicontrol.git-665f0976775d06bc4a3680228b998a5956c7461b.zip
Source1: qmidicontrol-configure.ac
Source2: qmidicontrol.jpg

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: desktop-file-utils

%description
QMidiControl is a virtual MIDI control pad

%prep
%autosetup -n alsamodular-qmidicontrol.git-%{commit0}

cp %{SOURCE1} configure.ac

%build

autoreconf --install

%configure

%make_build

%install

%make_install

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/qmidicontrol.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=qmidicontrol
Exec=qmidicontrol
Icon=qmidicontrol
Comment=MIDI Control surface
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/qmidicontrol.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/qmidicontrol.desktop

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/qmidicontrol/*

%changelog
* Thu Apr 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial build
