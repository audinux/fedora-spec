%global commit0 ae519c239b9e9a3beca10aa0f4551a15dde40c2e

Name:    midi2voice
Version: 1.0.0
Release: 1%{?dist}
Summary: Singing synthesis from MIDI file
License: GPL-2.0-or-later
URL:     https://github.com/mathigatti/midi2voice

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/mathigatti/midi2voice/archive/%{commit0}.zip#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-music21
Requires: python3-requests
Requires: python3-pyphen

%description
Singing synthesis from MIDI file 

%prep
%autosetup -n %{name}-%{commit0}

%build

%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/%{name}/*
%{python3_sitelib}/%{name}-1.0.4-py3.10.egg-info/*

%changelog
* Tue Jul 19 2022 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- initial release of the spec file
