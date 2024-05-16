# Tag: Tracker, Jack, Alsa
# Type: Standalone
# Category: Audio, Sequencer

Name:    bintracker
Version: 0.2.0
Release: 1%{?dist}
Summary: A hackable Chiptune Audio Workstation
License: GPL-3.0-or-later
URL:     https://github.com/bintracker/bintracker
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bintracker/bintracker/archive/refs/tags/v%{version}-alpha1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: chicken
BuildRequires: make
BuildRequires: sqlite-devel
BuildRequires: desktop-file-utils

%description
A hackable Chiptune Audio Workstation for the 21st Century.

%prep
%autosetup -n %{name}-%{version}-alpha1

mkdir -p %{buildroot}/usr/lib/chicken/
export CHICKEN_INSTALL_REPOSITORY=%{buildroot}/usr/lib/chicken/

chicken-install srfi-13

%build

cd build
%make_build

%install

cd build
%make_install

%files
%doc README.md
%license LICENSE LICENSES.txt
%{_bindir}/*

%changelog
* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-alpha1-1
- initial spec file
