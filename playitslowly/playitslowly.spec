# Tag: Audio, Player
# Type: Standalone
# Category: Audio, Tool

%define commit0 f1d445f8ff410ee378f066441b39dff2adc7af7c

Name: playitslowly
Version: 1.0.0
Release: 1%{?dist}
Summary: Play it slowly is a software to play back audio files at a different speed or pitch.
URL: https://github.com/jwagner/playitslowly
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/jwagner/playitslowly/archive/%{commit0}.zip#/%{name}-%{version}.zip
# Patch0:  playitslowly_0001_force_gtk3.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: python3-gobject
Requires: python3-simplejson
Requires: pygtk2

%description
Play it slowly is a software to play back audio files at a different speed or pitch.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/ch.x29a.playitslowly.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info
%{_datadir}/applications/*
%{_datadir}/appdata/*
%{_usr}/lib/python%{python3_version}/site-packages/playitslowly-py3.1.install-info
%{_datadir}/icons/hicolor/128x128/*
%{_datadir}/icons/hicolor/32x32/*
%{_datadir}/icons/hicolor/scalable/*

%changelog
* Fri Oct 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- Initial release
