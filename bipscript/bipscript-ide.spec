# Tag: Jack, Alsa
# Type: Standalone, IDE
# Category: Audio, Programming

Name:    bipscript-ide
Version: 0.17
Release: 1%{?dist}
Summary: An IDEA for bipscript
URL:     https://gitlab.domainepublic.net/bipscript/ide/
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.domainepublic.net/bipscript/ide/-/archive/v%{version}/ide-v%{version}.tar.gz
Source1: bipscript-version.h

BuildRequires: gcc gcc-c++ sed
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtsvg-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: libatomic
BuildRequires: desktop-file-utils

Requires: bipscript

%description
An IDE for bipscript

%prep
%autosetup -n ide-v%{version}

cp %{SOURCE1} version.h

%build

%qmake_qt5 bipscript-ide.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bipscript-ide %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/icons/
install -m 644 icon.png %{buildroot}/%{_datadir}/icons/bipscript-ide.png

#
# Write desktop files
#
cat > bipscript-ide.desktop <<EOF
[Desktop Entry]
Name=BipScript IDE
GenericName=IDE for BipScript
Comment=IDE for BipScript
Exec=bipscript-ide
Icon=bipscript-ide
Type=Application
Categories=AudioVideo;Audio;Development;
Terminal=false
EOF

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 bipscript-ide.desktop %{buildroot}%{_datadir}/applications/bipscript-ide.desktop

# install polyphon.desktop properly.
desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/bipscript-ide.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/bipscript-ide.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%changelog
* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.17-1
- update to 0.17-1

* Sat Jul 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.13-1
- update to 0.13-1

* Sat Apr 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.12-1
- Initial spec file
