# Tag: Organ
# Type: Standalone
# Category: Audio, Sampler

%define revision 2330

Name:    GrandOrgue
Version: 0.3.1.%{revision}
Release: 4%{?dist}
Summary: A sample based pipe organ simulator.
License: GPLv2+
URL:     https://sourceforge.net/projects/ourorgan

Vendor:       Audinux
Distribution: Audinux

# ./GrandOrgue-source.sh <rev>
# ./GrandOrgue-source.sh 2330

Source0: ourorgan-%{revision}.tar.gz
Source1: GrandOrgue-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: wxGTK3-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: systemd-devel
BuildRequires: wavpack-devel
BuildRequires: fftw-devel

%description
GrandOrgue is a sample based pipe organ simulator.

%prep
%autosetup -n ourorgan-%{revision}

%build

%cmake -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-3.0 \
       -DLIBINSTDIR=%{_lib}

%cmake_build

%install

%cmake_install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README AUTHORS
%license license.txt
%{_bindir}/%{name}
%{_bindir}/GrandOrgueTool
%{_datadir}/*
%{_libdir}/*

%changelog
* Thu Oct 22 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-4
- fix debug build

* Wed Sep 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-3
- fix for fedora 33

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to release 2330

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-2
- update to release 2294

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to release 2242

* Mon Jun 01 2015 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- Initial version
