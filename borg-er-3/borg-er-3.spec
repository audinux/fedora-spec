# Status: active
# Tag: Synthesizer
# Type: Standalone
# Category: Synthesizer

Name: borg-er-3
Version: 1.0.4
Release: 1%{?dist}
Summary: A JACK synthesizer
URL: https://github.com/mrbid/Borg-ER-3/
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mrbid/Borg-ER-3/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(jack)
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Mx44 is a polyphonic multichannel midi realtime software synthesizer.

%prep
%autosetup -n Borg-ER-3-%{version}

sed -i -e "s|Categories=Utility;Audio|Categories=Audio;AudioVideo|g" borg.AppDir/borg.desktop

%build

%set_build_flags

gcc $CFLAGS main.c -Ofast -lSDL2 -lm -o borg

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 borg %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/
install -m 644 borg.AppDir/borg512x512.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 borg.AppDir/borg.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/mime/packages/
install -m 644 borg.AppDir/usr/share/metainfo/com.voxdsp.borg.appdata.xml %{buildroot}/%{_datadir}/mime/packages/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/borg.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/borg.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/mime/packages/com.voxdsp.borg.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/icons/hicolor/512x512/apps/*
%{_datadir}/applications/*
%{_datadir}/mime/packages/*

%changelog
* Thu May 08 2025 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- inital release
