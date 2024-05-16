# Tag: Library
# Type: Devel
# Category: Programming

%global debug_package %{nil}

Summary: Game and tools oriented refactored version of GLU tesselator.
Name: libtess2
Version: 1.0.2
Release: 1%{?dist}
License: BSD
URL: https://github.com/memononen/libtess2
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/memononen/libtess2/archive/refs/tags/v%{version}.tar.gz#/libtess2-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: premake4
BuildRequires: make
BuildRequires: glfw-devel
BuildRequires: glew-devel

%description
This is refactored version of the original libtess which comes with the GLU
reference implementation. The code is good quality polygon tesselator and
triangulator. The original code comes with rather horrible interface and
its' performance suffers from lots of small memory allocations.
The main point of the refactoring has been the interface and memory
allocation scheme.

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
%autosetup -n %{name}-%{version}

%build

%set_build_flags
premake4 gmake
cd Build
%make_build config=release

%install

install -m 755 -d %{buildroot}/%{_includedir}/
install -m 755 -d %{buildroot}/%{_libdir}/

cp Include/tesselator.h %{buildroot}/%{_includedir}/
cp Build/libtess2.a     %{buildroot}/%{_libdir}/

%files
%doc README.md
%license LICENSE.txt

%files devel
%{_includedir}/tesselator.h

%files static
%{_libdir}/libtess2.a

%changelog
* Fri May 21 2021 Yann Collette <ycollette dot nospam at free.fr> 1.0.2-1
- Initial release of spec file for 1.0.2
