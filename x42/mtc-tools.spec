# Tag: Video, Tool
# Type: Standalone
# Category: Tool

Name: mtc-tools
Version: 0.2.0
Release: 1%{?dist}
Summary: JACK MIDI Timecode tools
License: GPL-2.0-or-later
URL: https://github.com/x42/mtc-tools
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/mtc-tools/archive/refs/tags/v0.2.0.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libtimecode-devel
BuildRequires: pkgconfig(jack)

%description
Commandline tools to deal with MIDI Timecode (MTC) via http://jackaudio.org

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"
%make_build PREFIX=%{_prefix} STRIP=true

%install

%make_install PREFIX=%{_prefix} STRIP=true

%files
%doc README.md
%license COPYING
%{_bindir}/*
%{_mandir}/*

%changelog
* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial spec file
