# Tag: Audio, Tool
# Type: Standalone
# Category: Audio, Tool

Name: tascar
Version: 0.232.1
Release: 1%{?dist}
Summary: TASCAR is a collection of tools for creating spatially dynamic acoustic scenes in different render formats
License: GPL2
URL: http://tascar.org/
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/HoerTech-gGmbH/tascar/archive/refs/tags/release_%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
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
BuildRequires: gtksourceviewmm-devel
BuildRequires: libglademm24-devel
BuildRequires: libltc-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: portaudio-devel
BuildRequires: matio-devel
BuildRequires: libsamplerate-devel
BuildRequires: libcurl-devel
BuildRequires: libxml++30-devel

%description
TASCAR is a collection of tools for creating spatially dynamic acoustic scenes in different render formats

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package static
Summary:  Static libraries for %{name}
Requires: %{name} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for %{name}.

%prep
%autosetup -n %{name}-release_%{version}

%build

%cmake
%cmake_build

%install

%cmake_install

install -d 755 %buildroot/%{_datadir}/%{name}/examples/
cp -r examples/* %buildroot/%{_datadir}/%{name}/examples/

%ifarch x86_64 amd64 aarch64
mv %buildroot/usr/lib/* %buildroot/%{_libdir}/
%endif

%files
%license LICENSE
%doc README.md release.md changelog
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/
%{_datadir}/%{name}/examples/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/*

%files static
%{_libdir}/*.a

%changelog
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
