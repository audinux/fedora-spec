Name:    pipecontrol
Version: 0.2.4
Release: 1%{?dist}
Summary: osmid is a tool to bridge MIDI and OSC
URL:     https://github.com/llloret/osmid
License: GPLv2+

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
%{_datadir}/icons/pipecontrol.svg

%changelog
* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- Initial spec file
