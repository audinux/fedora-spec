# Tag: Tool, Audio, Editor
# Type: Standalone
# Category: Tool, Audio

Summary: A sound editor
Name: eko
Version: 7.1.0
Release: 1%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/psemiletov/eko

Source:	https://github.com/psemiletov/eko/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Vendor:       Audinux
Distribution: Audinux

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: portaudio-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qt5compat-devel
# for joystick
BuildRequires: kernel-headers
BuildRequires: libxkbcommon-x11-devel
BuildRequires: desktop-file-utils

%description
EKO is a simple sound editor

%prep
%autosetup -n %{name}-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cp desktop/eko.desktop %{buildroot}/%{_datadir}/applications/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/docs/
cp -ra docs/* %{buildroot}/%{_datadir}/%{name}/docs/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README
%license COPYING LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/%{name}/docs/*

%changelog
* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 7.1.0-1
- initial version of the spec

