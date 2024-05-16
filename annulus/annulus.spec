# Tag: Loop, Jack
# Type: Standalone
# Category: Audio, Sampler

%define commit0 e5bc560f957c7897c22b10171d4e57738bb17cf9

Name:    annulus
Version: 1.0.0
Release: 1%{?dist}
Summary: audio looping application
URL:     https://github.com/chronopoulos/annulus
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/chronopoulos/annulus/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: qt-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel

%description
Audio Looper for Live Performance.

%prep
%autosetup -n %{name}-%{commit0}

%build

%qmake_qt4 annulus.pro
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/annulus %{buildroot}%{_bindir}/

%files
%doc README.md
%{_bindir}/annulus

%changelog
* Fri Jan 20 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
