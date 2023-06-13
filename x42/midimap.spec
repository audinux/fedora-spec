# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    midimap.lv2
Version: 0.4.4
Release: 1%{?dist}
Summary: Rule based MIDI mapper plugin
License: GPL-2.0-or-later
URL:     https://github.com/x42/midimap.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/midimap.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: lv2-devel

%description
midimap.lv2 is a flexible MIDI event mapping plugin,
using a rule-based lookup-table, which is loaded from a config file.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%install 

%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2 fat1_VERSION=%{version} STRIP=true

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.4.4-1
- Initial spec file
