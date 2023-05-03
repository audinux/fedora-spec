# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

%global __python %{__python3}

Name:    patchance
Version: 1.0.0
Release: 1%{?dist}
Summary: Jack Patchbay GUI

License: GPLv2+
URL:     https://github.com/Houston4444/Patchance

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh Patchance v1.0.0

Source0: Patchance.tar.gz
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
Patchance is one more JACK patchbay GUI for GNU/Linux systems,
but it could be adapted to Mac and Windows with little effort.
It is a direct alternative to Catia or Patchage.

%prep
%autosetup -n Patchance

# Fix desktop categories
sed -i -e "s/AudioVideo;//g" data/share/applications/patchance.desktop

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
%{_datadir}/patchance/
%{_datadir}/patchance/HoustonPatchbay/*
%{_datadir}/patchance/locale/*
%{_datadir}/patchance/src/*

%changelog
* Sun Jan 22 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0

* Mon Jan 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
