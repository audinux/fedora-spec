# Status: active
# Tag: Audio, Tool
# Type: Standalone
# Category: Audio, Tool

Name: tascar
Version: 0.234.4
Release: 1%{?dist}
Summary: TASCAR is a collection of tools for creating spatially dynamic acoustic scenes in different render formats
License: GPL2
URL: http://tascar.org/
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/HoerTech-gGmbH/tascar/archive/refs/tags/release_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 0001-fix-config.mk.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: doxygen
BuildRequires: xxd
BuildRequires: boost-devel
BuildRequires: libsndfile-devel
BuildRequires: pkgconfig(jack)
BuildRequires: fftw-devel
BuildRequires: eigen3-devel
BuildRequires: liblo-devel
BuildRequires: gsl-devel
BuildRequires: xerces-c-devel
BuildRequires: freetype-devel
BuildRequires: gtkmm30-devel
BuildRequires: glibmm24-devel
BuildRequires: cairomm-devel
BuildRequires: pangomm-devel
BuildRequires: libsigc++20-devel
BuildRequires: atkmm-devel
BuildRequires: gtksourceviewmm3-devel
BuildRequires: libltc-devel
BuildRequires: portaudio-devel
BuildRequires: matio-devel
BuildRequires: libsamplerate-devel
BuildRequires: libcurl-devel
BuildRequires: libxml++30-devel
BuildRequires: libmysofa-devel
BuildRequires: CUnit-devel

%description
TASCAR is a collection of tools for creating spatially dynamic acoustic scenes in different render formats

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup -p1 -n %{name}-release_%{version}

mkdir bin
ln -s /usr/bin/true bin/git

%build

export PATH=`pwd`/bin:$PATH

%make_build

%install

%make_install

install -d 755 %buildroot/%{_datadir}/%{name}/examples/
cp -r examples/* %buildroot/%{_datadir}/%{name}/examples/

%ifarch x86_64 amd64 aarch64
install -d 755 %buildroot/%{_libdir}/
mv %buildroot/usr/lib/* %buildroot/%{_libdir}/
%endif

# Cleanup
rm %buildroot/%{_bindir}/*.mk
rm -rf %buildroot/builddir

%files
%license LICENSE
%doc README.md release.md changelog
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%{name}/examples/*

%files devel
%{_includedir}/tascar/*
%{_libdir}/*.so

%changelog
* Tue Sep 30 2025 Yann Collette <ycollette.nospam@free.fr> - 0.234.5-1
- update to 0.234.5-1 - remove unused dep

* Tue Sep 09 2025 Yann Collette <ycollette.nospam@free.fr> - 0.234.4-1
- update to 0.234.4-1

* Sun May 18 2025 Yann Collette <ycollette.nospam@free.fr> - 0.234.3-1
- update to 0.234.3-1

* Sun Feb 16 2025 Yann Collette <ycollette.nospam@free.fr> - 0.234.2-1
- update to 0.234.2-1

* Sun Jan 12 2025 Yann Collette <ycollette.nospam@free.fr> - 0.234.0-1
- update to 0.234.0-1

* Wed Oct 23 2024 Yann Collette <ycollette.nospam@free.fr> - 0.233.2-1
- update to 0.233.2-1

* Thu Oct 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.233.1-1
- update to 0.233.1-1

* Fri Jul 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.232.2-1
- update to 0.232.2-1

* Wed May 01 2024 Yann Collette <ycollette.nospam@free.fr> - 0.232.1-1
- update to 0.232.1-1

* Mon Apr 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.232.0-1
- update to 0.232.0-1

* Wed Apr 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.231.2-1
- update to 0.231.2-1

* Thu Apr 11 2024 Yann Collette <ycollette.nospam@free.fr> - 0.231.1-1
- update to 0.231.1-1

* Fri Mar 22 2024 Yann Collette <ycollette.nospam@free.fr> - 0.231.0-1
- update to 0.231.0-1

* Thu Sep 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.230.0-1
- update to 0.230.0-1

* Fri Jan 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.229.0-1
- update to 0.229.0-1

* Tue Dec 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.228.3-1
- update to 0.228.3-1

* Sun Feb 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.223.0-1
- initial version of the spec file
