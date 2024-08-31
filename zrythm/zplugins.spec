# Status: active
# Tag: Audio, Tool
# Type: Plugin, LV2
# Category: Audio, Tool

Name: zplugins
Version: 0.2.5
Release: 1%{?dist}
Summary: A collection of audio DSP LV2 plugins
License: GPL-2.0-or-later
URL: https://github.com/zrythm/ZPlugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zrythm/ZPlugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: ztoolkit
BuildRequires: meson
BuildRequires: lv2-devel
BuildRequires: librsvg2-devel
BuildRequires: libsndfile-devel
BuildRequires: guile22-devel

%description
A collection of audio DSP LV2 plugins

%prep
%autosetup -n ZPlugins-%{version}

%build

%set_build_flags

export CFLAGS="-fPIC $CFLAGS"

%meson -Dlv2dir=%{_lib}/lv2
%meson_build

%install

%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Oct 10 2022 Yann Collette <ycollette.nospam@free.fr> - 0.2.5-1
- update to 0.2.5-1

* Mon May 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2.4-1
- update to 0.2.4-1

* Sun Jan 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Sun Jan 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.2.1-1
- update to 0.2.1-1

* Tue Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- Initial build
