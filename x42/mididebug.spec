# Tag: Alsa, Jack
# Type: Plugin, LV2
# Category: Audio, Tool

Name:    mididebug.lv2
Version: 0.3.4
Release: 1%{?dist}
Summary: MIDI Message Generator
License: GPLv2+
URL:     https://github.com/x42/mididebug.lv2

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/mididebug.lv2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: lv2-devel

%description
mididebug.lv2 is an instrumention tool to generate arbitrary MIDI
messages up to 3 bytes in length. It's mainly intented for
http://moddevices.com/ but works in any LV2 plugin-host.

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
* Wed May 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.4-1
- Initial spec file
