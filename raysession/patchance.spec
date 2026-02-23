# Status: active
# Tag: Session, OSC, Jack
# Type: Standalone
# Category: Session Mngmt

Name: patchance
Version: 1.3.1
Release: 1%{?dist}
Summary: Jack Patchbay GUI
License: GPL-2.0-or-later
URL: https://github.com/Houston4444/Patchance
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./source-houston4444.sh <project> <tag>
#        ./source-houston4444.sh Patchance v1.3.1

Source0: Patchance.tar.gz
Source1: source-houston4444.sh

BuildArch: noarch

BuildRequires: python3-pyqt6-devel
BuildRequires: python3
BuildRequires: qtchooser
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: gtk-update-icon-cache
BuildRequires: desktop-file-utils

Requires(pre): python3-pyqt6
Requires(pre): python3-pyliblo3
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

export PATH=/usr/lib64/qt6/libexec:$PATH

%make_build PREFIX=/usr LRELEASE=lrelease-qt6 RCC=/usr/lib64/qt6/libexec/rcc

%install

export PATH=/usr/lib64/qt6/libexec:$PATH

%make_install PREFIX=/usr LRELEASE=lrelease-qt6 RCC=/usr/lib64/qt6/libexec/rcc

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
%dir %{_datadir}/patchance/
%{_datadir}/patchance/HoustonPatchbay/*
%{_datadir}/patchance/locale/*
%{_datadir}/patchance/src/*

%changelog
* Sat Feb 21 2026 Yann Collette <ycollette.nospam@free.fr> - 1.3.1-1
- update to 1.3.1-1

* Mon Nov 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- update to 1.3.0-1

* Sat Jul 29 2023 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Sun Jan 22 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- update to 1.0.0-1

* Mon Jan 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
