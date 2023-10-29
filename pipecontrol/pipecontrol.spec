Name:    pipecontrol
Version: 0.2.11
Release: 1%{?dist}
Summary: Pipewire control GUI program in Qt
URL:     https://github.com/portaloffreedom/pipecontrol
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portaloffreedom/pipecontrol/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: pipewire-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: kf5-kirigami2-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: desktop-file-utils

%description
Pipewire control GUI program in Qt-QML using Kirigami2 (KDE)

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/PipeControl.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/PipeControl.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/PipeControl.desktop
%{_datadir}/icons/hicolor/scalable/apps/

%changelog
* Sun Oct 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.11-1
- update to 0.2.11-1

* Sat Apr 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.10-1
- update to 0.2.10-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- Initial spec file
