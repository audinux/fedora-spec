# Status: active
# Tag: Tool, Editor
# Type: Standalone
# Category: Audio, Tool

Name: samplecat
Version: 0.3.4
Release: 1%{?dist}
Summary: SampleCat is a a program for cataloguing and auditioning audio samples
URL: https://ayyi.github.io/samplecat/
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# Usage: ./samplecat-source.sh <TAG>
#        ./samplecat-source.sh v0.3.4

Source0: samplecat.tar.gz
Source1: samplecat-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gettext
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: libyaml-devel
BuildRequires: fftw-devel
BuildRequires: (ffmpeg-devel or ffmpeg-free-devel)
BuildRequires: sqlite-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: cairo-devel
BuildRequires: ladspa-devel
BuildRequires: gtkglext-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: graphene-devel
BuildRequires: desktop-file-utils

%description
SampleCat is a program for cataloguing and auditioning audio samples.

SampleCat is available under the GNU General Public License and runs mainly on GNU/Linux systems.
It is written in C and uses the GTK graphics library. MySql and Sqlite can be used for the database.

Currently, most basic functionality is in place and working.

%prep
%autosetup -n %{name}

%build

./autogen.sh

%configure
%make_build

%install

%make_install

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp icons/samplecat.xpm %{buildroot}/%{_datadir}/pixmaps/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
cp icons/samplecat.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=SampleCat
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

# install smjack.desktop properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/pixmaps/*
%{_mandir}/*
%{_sysconfdir}/*

%changelog
* Tue Jul 15 2025 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- Initial release
