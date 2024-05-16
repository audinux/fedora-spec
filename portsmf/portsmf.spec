# Tag: Library, MIDI
# Type: Devel
# Category: Programming

Summary: Port Standard MIDI File - portable library for reading/writing Standard MIDI Files
Name: portsmf
Version: 0.1
Release: 2%{?dist}
License: MIT-like
URL: http://sourceforge.net/p/portmedia/wiki/portsmf/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# svn co https://portmedia.svn.sourceforge.net/svnroot/portmedia/portsmf/trunk portsmf
Source0: %{name}.tar.xz
# Source0-md5:	654893b608c70230e0838725c563b86f
Patch0: %{name}-shared.patch
Patch1: %{name}-includes.patch

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libstdc++-devel
BuildRequires: libtool

%description
PortSMF is "Port Standard MIDI File", a cross-platform, C++ library
for reading and writing Standard MIDI Files.

%package devel
Summary:  Header files for portSMF library
Requires: %{name} = %{version}-%{release}
Requires: libstdc++-devel

%description devel
Header files for portSMF library.

%package static
Summary:  Static portSMF library
Requires: %{name}-devel = %{version}-%{release}

%description static
Static portSMF library.

%prep
%autosetup -p1 -n %{name}

%build

autoreconf -i
chmod a+x configure
%configure --includedir=%{_includedir}/portSMF

%make_build

%install

%make_install

rm -f %{buildroot}/%{_libdir}/libportSMF.la

%files
%doc README.txt changelog.txt
%license license.txt
%{_libdir}/libportSMF.so.*.*.*
%ghost %{_libdir}/libportSMF.so.0
%{_datadir}/doc/portsmf/license.txt

%files devel
%{_libdir}/libportSMF.so
%{_includedir}/portSMF

%files static
%{_libdir}/libportSMF.a

%changelog
* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 0.1-2
- Fix for Fedora 37

* Fri Apr 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial package for Fedora

* Sat Nov 09 2013 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/portsmf.git;a=log;h=master

* Sat Nov 09 2013 Jakub Bogusz <qboosh@pld-linux.org> ec3739a
- added includes patch (let public headers include required C++ headers)
- release .2

* Sat Jun 22 2013 Jakub Bogusz <qboosh@pld-linux.org> 0f56bd7
- new; patch to build as shared library

