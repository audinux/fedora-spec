# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    plumbing.lv2
Version: 0.1.3
Release: 1%{?dist}
Summary: LV2 Plumbing Plugins
License: GPLv2+
URL:     https://github.com/x42/plumbing.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/plumbing.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel

%description
A small set of plugins for routing audio and MIDI data,
intended to be used with Ardour3's linear processor chain.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Thu May 11 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- update to 0.1.3-1

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
