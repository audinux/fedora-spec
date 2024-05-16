# Tag: Editor, Audio, Tool
# Type: Standalone
# Category: Standalone
# Category: Audio, Tool

Name: samplehive
Version: 0.8.4
Release: 1%{?dist}
Summary: A simple, modern audio sample browser/manager
License: GPL-2.0-or-later
URL: https://gitlab.com/samplehive/sample-hive
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/samplehive/sample-hive/-/archive/v%{version}-alpha.1/sample-hive-v%{version}-alpha.1.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
BuildRequires: yaml-cpp-devel
BuildRequires: taglib-devel
BuildRequires: sqlite-devel
%if 0%{?fedora} <= 38
BuildRequires: wxGTK3-devel
%else
BuildRequires: wxGTK-devel
%endif
BuildRequires: desktop-file-utils

%description
SampleHive let’s you manage your audio samples in a nice and simple way,
just add a directory where you store all your samples, or drag and drop
a directory on it to add samples to it, and it will help sort, search,
play and view some information about the sample. You can also drag and
drop from SampleHive to other applications.

%prep
%autosetup -n sample-hive-v%{version}-alpha.1

%build

%meson
%meson_build

%install

%meson_install

%files
%doc README.org
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Jul 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.8.4-1
- Initial version
