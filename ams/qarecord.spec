# Status: active
# Tag: Tool, Tape, Jack
# Type: Standalone
# Category: Tool, Audio

%global commit0 49995a3c6402fcdb4ac8698c22bc22d9843ea868

Summary: Audio recording tool
Name: qarecord
Version: 0.0.1
Release: 1%{?dist}
License: GPLv2+
URL: https://sourceforge.net/projects/alsamodular/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/code-snapshots/git/a/al/alsamodular/qarecord.git.git/alsamodular-qarecord.git-%{commit0}.zip
Source1: qarecord-configure.ac

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: desktop-file-utils

%description
QARecord is a simple but solid recording tool.
It works well with stereo and multichannel recordings,
supporting ALSA and JACK interfaces and in both 16 bit
and 32 bit mode.
By using a large ringbuffer for the captured data,
buffer overruns are avoided. It has a Qt based GUI with
graphical peak meters.

%prep
%autosetup -p1 -n alsamodular-qarecord.git-%{commit0}

cp %{SOURCE1} configure.ac

%build

%set_build_flags

export LDFLAGS="`pkg-config --libs jack` $LDFLAGS"

autoreconf --install

%configure

%make_build

%install

%make_install

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp src/pixmaps/qarecord_48.xpm %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/qarecord.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=qarecord
Exec=qarecord
Icon=qarecord_48
Comment=Audio recorder
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/qarecord.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/qarecord.desktop

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/qarecord/*
%{_mandir}/de/man1/qarecord.1.gz
%{_mandir}/fr/man1/qarecord.1.gz
%{_mandir}/man1/qarecord.1.gz

%changelog
* Thu Apr 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial build
