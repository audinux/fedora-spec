# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

Name: cable
Version: 0.9.17
Release: 1%{?dist}
Summary: Application to dynamically modify Pipewire and Wireplumber settings at runtime
License: GPL-3.0-or-later
URL: https://github.com/magillos/Cable
BuildArch: noarch

Source0: https://github.com/magillos/Cable/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-packaging
BuildRequires: python3-Cython
BuildRequires: python3-build

Requires: python3-pyqt6
Requires: python3-alsa
Requires: jack_delay
Requires: python-jack-client

Provides: %{name} = %{version}-%{release}

%description
Application to dynamically modify Pipewire and Wireplumber settings at runtime,
such as quantum, sample rate, latency offset, services restart and more.
It features side-by-side and graph style connections managers (uses Python Jack
Client so will not list Pipewire items), pw-top wrapper, simple ALSA mixer
and jack_delay GUI.

%prep
%autosetup -n Cable-%{version}

sed -i -e "s|/usr/share/cable/connection-manager\.py|/usr/lib/python3.13/site-packages/cables/connection_manager\.py|g" cable_core/process.py

%build

%py3_build

%install

%py3_install

# Install the icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -Dm644 jack-plug.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/jack-plug.svg

# Install the desktop entry
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -Dm644 com.github.magillos.cable.desktop %{buildroot}/%{_datadir}/applications/com.github.magillos.cable.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{__python3_sitelib}/graph/*
%{__python3_sitelib}/cables/*
%{__python3_sitelib}/cable_core/*
%{__python3_sitelib}/Cable.py
%{__python3_sitelib}/cable-%{version}-py%{python3_version}.egg-info/*
%{__python3_sitelib}/__pycache__/Cable.*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*

%changelog
* Mon Jun 02 2025 Yann Collette <ycollette.nospam@free.fr> - 0.9.18-1
- initial spec
