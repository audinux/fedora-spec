# Tag: Library
# Type: Devel
# Category: Programming

%define commit0 85af0c9a4ce345395f1dde641a4b6e7b254ecd5e

Name: libtimecode
Version: 0.1.0
Release: 1%{?dist}
Summary: Deal with A/V timecode and framerates
License: GPL-2.0-or-later
URL: https://github.com/x42/libtimecode
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/x42/libtimecode/archive/%{commit0}.zip#/%{name}-%{commit0}.zip

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
Timecode and Framerate manipulation functions.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package static
Summary:  Static library for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static library for %{name}.

%prep
%autosetup -n %{name}-%{commit0}

autoreconf --force --install

%build

%set_build_flags
export OPTIMIZATIONS="$CFLAGS"

%configure

%make_build PREFIX=%{_prefix} STRIP=true

%install

%make_install PREFIX=%{_prefix} STRIP=true

%files
%doc README.md
%{_libdir}/*.so.*
%{_mandir}/*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files static
%{_libdir}/*.a

%changelog
* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
