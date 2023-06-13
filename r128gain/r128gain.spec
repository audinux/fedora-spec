Name:    r128gain
Version: 1.0.7
Release: 1%{?dist}
Epoch:   1
Summary: r128gain is a multi platform command line tool to scan your audio files and tag them.
License: GPL-2.0-or-later
URL:     https://github.com/desbma/r128gain.git

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/desbma/r128gain/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-crcmod
Requires: python3-mutagen
Requires: python3-tqdm

%description
r128gain is a multi platform command line tool to scan your audio files and tag them with
loudness metadata (ReplayGain v2 or Opus R128 gain format), to allow playback of several
tracks or albums at a similar loudness level. r128gain can also be used as a Python module
from other Python projects to scan and/or tag audio files.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%{__python3} setup.py build

%install

%{__python3} setup.py install --root %{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/*
%{python3_sitelib}/%{name}-*.egg-info

%changelog
* Sun Mar 26 2023 Yann Collette <ycollette dot nospam at free.fr> 1.0.7-1
- update to 1.0.7-1

* Tue Aug 02 2022 Yann Collette <ycollette dot nospam at free.fr> 1.0.6-1
- update to 1.0.6-1

* Fri Oct 23 2020 Yann Collette <ycollette dot nospam at free.fr> 1.0.3-1
- update to 1.0.3 - fix debug build

* Thu Oct 10 2019 Yann Collette <ycollette dot nospam at free.fr> 0.9.3-1
- initial release of the spec file
