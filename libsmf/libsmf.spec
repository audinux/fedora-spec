%global realversion 1.3

Summary: LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files
Name:    libsmf
Version: 1.4
Release: 8%{?dist}
License: BSD
URL:     https://github.com/stump/%{name}

Vendor:       Audinux
Distribution: Audinux

Source0: %{url}/archive/%{name}-%{realversion}.tar.gz
Patch0: libsmf-0001-Fix-buffer-overflow-on-tempo-change-event.patch
Patch1: libsmf-0002-Fix-validity-checks-of-escaped-data.patch
Patch2: libsmf-0003-Fix-buffer-overflow-by-reducing-length-of-truncated-.patch
Patch3: libsmf-0004-Stop-parsing-tracks-after-the-first-failure.-Fixes-h.patch
Patch4: libsmf-0005-Handle-non-EOT-terminated-tracks.-Fixes-raised-asser.patch
Patch5: libsmf-0006-Fix-the-assertion-problem-is_sysex_byte-status.patch
Patch6: libsmf-0007-Fix-a-logic-error-in-Escape-event-handling.patch
Patch7: libsmf-0008-Fix-a-memory-leak-in-case-of-loading-failure.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: glib2-devel
BuildRequires: doxygen

%description
LibSMF is a BSD-licensed C library for handling SMF ("*.mid") files.
It transparently handles conversions between time and pulses,
tempo map handling etc. The only dependencies are C compiler and glib.
Full API documentation and examples are included.

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

%package doc
Summary:  Documentation for %{name}

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{name}-%{realversion}

%build
autoreconf --force --install
%configure
%make_build

doxygen doxygen.cfg

%install
%make_install

install -m 755 -d %{buildroot}/%{_datadir}/doc/%{name}/api/
cp -ra api/* %{buildroot}/%{_datadir}/doc/%{name}/api/

# Remove unnecessary file
rm %{buildroot}/%{_libdir}/libsmf.la

%files
%doc NEWS
%license COPYING
%{_bindir}/smfsh
%{_libdir}/libsmf.so.*
%{_datadir}/man/man1/smfsh.*

%files devel
%{_includedir}/smf.h
%{_libdir}/libsmf.so
%{_libdir}/pkgconfig/smf.pc

%files static
%{_libdir}/libsmf.a

%files doc
%{_datadir}/doc/%{name}/api/

%changelog
* Tue Jul 04 2023 Yann Collette <ycollette dot nospam at free.fr> 1.4-8
- update to 1.4-8

* Sun Nov 29 2020 Yann Collette <ycollette dot nospam at free.fr> 1.3-8
- add patches

* Sun Nov 29 2020 Yann Collette <ycollette dot nospam at free.fr> 1.3-6
- fix spec file + add doc subpackage

* Sun Nov 08 2020 Yann Collette <ycollette dot nospam at free.fr> 1.3-5
- fix spec file

* Fri Nov 06 2020 Yann Collette <ycollette dot nospam at free.fr> 1.3-4
- fix spec file

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-3
- update for Fedora 29

* Sat Jun 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-3
- update to commit 692e728

* Sat May 12 2018 Yann Collette <ycollette dot nospam at free.fr> 1.3-2
- update to commit fd5abd50

* Thu Jun 04 2015 Yann Collette <ycollette dot nospam at free.fr> 1.3-1
- Initial release of spec file for 1.3
