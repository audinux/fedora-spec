# Status: active
# Tag: Guitar, Amp Simul
# Type: Standalone
# Category: Audio, Effect

Name: stompbox
Version: 0.1.16
Release: 1%{?dist}
Summary: Guitar amplification and effects pedalboard simulation
License: GPL-3.0-or-later
URL: https://github.com/mikeoliphant/stompbox

# ./mikeoliphant-source.sh <project> <tag>
# ./mikeoliphant-source.sh stompbox v0.1.16

Source0: stompbox.tar.gz
Source1: mikeoliphant-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
Stompbox is a guitar amplification and effects library.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: license-%{name}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}

%build

%cmake -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"
%cmake_build

%install

mkdir -p %{buildroot}/%{_libdir}/
cp %{__cmake_builddir}/stompbox-capi/libstompbox-capi.so %{buildroot}/%{_libdir}/

mkdir -p %{buildroot}/%{_includedir}/
cp stompbox-capi/StompboxCAPI.h %{buildroot}/%{_includedir}/

mkdir -p %{buildroot}/%{_bindir}/
cp %{__cmake_builddir}/stompbox-jack/stompbox-jack %{buildroot}/%{_bindir}/

%files
%{_bindir}/stompbox-jack

%files -n license-%{name}
%doc README.md CREDITS.md
%license LICENSE.md

%files devel
%{_includedir}/StompboxCAPI.h
%{_libdir}/libstompbox-capi.so

%changelog
* Wed Feb 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.16-1
- update to 0.1.16-1

* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.15-1
- Initial build
