# Status: active
# Tag: Tool, Graphic, Audio
# Type: Standalone
# Category: Audio, Tool

Name: pipecontrol
Version: 0.3.0
Release: 1%{?dist}
Summary: Pipewire control GUI program in Qt
URL: https://github.com/portaloffreedom/pipecontrol
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/portaloffreedom/pipecontrol/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: qt6-linguist
BuildRequires: pipewire-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtquickcontrols2-devel
BuildRequires: kf6-kirigami2-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
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
* Sun Mar 23 2025 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- update to 0.3.0-1

* Sat Mar 22 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.12-1
- update to 0.2.12-1

* Sun Oct 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.11-1
- update to 0.2.11-1

* Sat Apr 29 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.10-1
- update to 0.2.10-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- Initial spec file
