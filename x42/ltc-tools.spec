# Tag: Video, Tool, Jack
# Type: Standalone
# Category: Tool

Name: ltc-tools
Version: 0.7.0
Release: 1%{?dist}
Summary: Tools to deal with linear-timecode (LTC)
License: GPL-2.0-or-later
URL: https://github.com/x42/ltc-tools
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/ltc-tools/releases/download/v%{version}/ltc-tools-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libltc-devel
BuildRequires: libsndfile-devel
BuildRequires: pkgconfig(jack)

%description
Commandline tools to deal with linear-timecode (LTC).

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
* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- Initial spec file
