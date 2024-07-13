# Tag: Guitar, Analyzer
# Type: Standalone
# Category: Audio, Tool

Name: specmatch
Version: 0.10.0
Release: 1%{?dist}
Summary: A tool to compare the spectrum of two Sound Files and generate a Impulse Response File from the different.
License: GPL-2.0-or-later
URL: https://github.com/brummer10/SpecMatch
BuildArch: noarch

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/SpecMatch/releases/download/v%{version}/specmatch-%{version}.tar.gz

BuildRequires: python3-build
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-pip

Requires: python3
Requires: python3-numpy
Requires: python3-matplotlib
Requires: python3-scipy
Requires: python3-soundfile
Requires: pkgconfig(jack)

%description
SpecMatch can be used to adapt the sound produced by a Guitarix setting to another recorded sound.

%prep
%autosetup -n %{name}-%{version}

# generate_buildrequires
# pyproject_buildrequires -x dev

%build

%pyproject_wheel

%install

%pyproject_install
%pyproject_save_files -l specmatch

%files  -f %{pyproject_files}
%{_bindir}/*

%changelog
* Sat Jul 13 2024 Yann Collette <ycollette.nospam@free.fr> - 0.10.0-1
- Initial build
