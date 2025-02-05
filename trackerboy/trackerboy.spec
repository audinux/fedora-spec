# Status: active
# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name: trackerboy
Version: 0.6.5
Release: 1%{?dist}
Summary: Game Boy / Game Boy Color music tracker
URL: https://github.com/stoneface86/trackerboy
ExclusiveArch: x86_64 aarch64
License: MIT

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/stoneface86/trackerboy/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: alsa-lib-devel
BuildRequires: rtmidi-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt6-qtbase-devel
BuildRequires: desktop-file-utils

%description
Trackerboy is a tracker program for producing music for the gameboy / gameboy color consoles.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 src/resources/icons/app/appicon.ico %{buildroot}/%{_datadir}/pixmaps/%{name}.ico

install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 644 src/%{name}.desktop %{buildroot}/%{_datadir}/applications/

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/examples/
cp -ra examples/* %{buildroot}/%{_datadir}/%{name}/examples/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/%{name}/examples/*

%changelog
* Wed Feb 05 2025 Yann Collette <ycollette.nospam@free.fr> - 0.6.5-1
- initial version of the spec file
