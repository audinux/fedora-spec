# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

%global __python %{__python3}

Name: patchichi
Version: 0.2.0
Release: 1%{?dist}
Summary: Abstract JACK Patchbay
License: GPL-2.0-or-later
URL: https://github.com/Houston4444/Patchichi

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh Patchichi v0.2.0

Source0: Patchichi.tar.gz
Source1: source-houston4444.sh

BuildArch: noarch

BuildRequires: python3-qt5-devel
BuildRequires: python3
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: gtk-update-icon-cache
BuildRequires: desktop-file-utils

Requires(pre): python3-qt5
Requires(pre): python3-pyliblo
Requires(pre): python3-pyxdg

%description
Patchichi is an abstract JACK patchbay GUI for GNU/Linux systems,
but it could be adapted to Mac and Windows with little effort.
The software it most closely resembles is probably Catarina, from
the Cadence suite.

%prep
%autosetup -n Patchichi

# Fix desktop categories
sed -i -e "s/AudioVideo;//g" data/share/applications/patchichi.desktop

%build

%make_build PREFIX=/usr LRELEASE=lrelease-qt5

%install

%make_install PREFIX=/usr LRELEASE=lrelease-qt5

desktop-file-install                         \
  --add-category="Audio;AudioVideo;Qt"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check

desktop-file-validate  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc readme.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/patchichi/
%{_datadir}/patchichi/HoustonPatchbay/*
%{_datadir}/patchichi/locale/*
%{_datadir}/patchichi/src/*

%changelog
* Mon Jan 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
