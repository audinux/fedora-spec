# Status: active
Summary: efsw is a C++ cross-platform file system watcher and notifier.
Name: libefsw
Version: 1.4.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/SpartanJ/efsw
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/SpartanJ/efsw/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
efsw is a C++ cross-platform file system watcher and notifier.
It monitors the file system asynchronously for changes to files
and directories by watching a list of specified paths, and raises
events when a directory or file change.
It supports recursive directories watch, tracking the entire
sub directory tree.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package static
Summary: Static library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static library for %{name}.

%prep
%autosetup -n efsw-%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib*.so

%files devel
%{_includedir}/efsw/*
%{_libdir}/cmake/*

%files static
%{_libdir}/*.a

%changelog
* Tue Jun 04 2024 Yann Collette <ycollette dot nospam at free.fr> 1.4.0-1
- update to 1.4.0-1

* Sat May 08 2021 Yann Collette <ycollette dot nospam at free.fr> 1.1.0-1
- Initial release of spec file for 1.1.0-1
