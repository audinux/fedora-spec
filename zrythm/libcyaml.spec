# Tag: Library
# Type: Devel
# Category: Programming

Name: libcyaml
Version: 1.2.0
Release: 2%{?dist}
Summary: C library for reading and writing YAML
License: ISC
Packager: Alexandros Theodotou
URL: https://github.com/tlsa/libcyaml/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/tlsa/libcyaml/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: libyaml-devel

%description
LibCYAML is a C library for reading and writing structured YAML documents.
It is written in ISO C11 and licensed under the ISC licence.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_lib}

%install

mkdir -p %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_includedir}
%make_install PREFIX=/usr LIBDIR=%{_lib}

%files
%{_libdir}/*

%files devel
%{_includedir}/*

%changelog
* Wed Jun 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Sat Jun 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Adjustment for Fedora

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Adjustment for Fedora

* Mon Feb 4 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- Bump to official v0.1.0 release

* Tue Jan 22 2019 Alexandros Theodotou <alex at zrythm dot org> 0.1.0-1
- RPM release
