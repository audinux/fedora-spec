# Status: active
# Tag: DAW, Editor, Player
# Type: Standalone
# Category: Audio, DAW

Name: powertabeditor
Version: 2.0.21
Release: 4%{?dist}
Summary: View and edit guitar powertab tablature.
URL: https://github.com/powertab/powertabeditor
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/powertab/powertabeditor/archive/refs/tags/2.0.21.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qttools-devel
BuildRequires: alsa-lib-devel
BuildRequires: doctest-devel
%if 0%{?fedora} >= 40
BuildRequires: minizip-ng-compat-devel
%else
BuildRequires: minizip-ng-devel
%endif
BuildRequires: json-devel
BuildRequires: pugixml-devel
BuildRequires: rtmidi-devel
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Power Tab Editor is an easy to use cross-platform guitar tablature editor and viewer.
It is an open source, community-driven successor to the original Power Tab Editor 1.7.

A variety of file formats are supported, including .pt2, .ptb, .gp3, .gp4, .gp5, .gpx, and .gp

%prep
%autosetup -n powertabeditor-%{version}

%build

%set_build_flags

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications//powertabeditor.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications//powertabeditor.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/powertabeditor.metainfo.xml

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/metainfo/*
%{_datadir}/mime/*
%{_datadir}/powertab/

%changelog
* Thu Nov 21 2024 Yann Collette <ycollette.nospam@free.fr> - 2.0.21-4
- update to 2.0.21-4

* Mon Nov 04 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to 731b4fc5c6500fdc8095e00171e3859179ed2470

* Mon Jun 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to f6662dd3c63adeca417c750e689bf7d5cf3a2f01

* Fri Jun 07 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to 4544a987a5e271dd6ee76aec28a40ab1739798c9

* Fri Jul 08 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
