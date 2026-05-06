# Status: active
# Tag: Devel
# Type: Devel
# Category: Programming

Summary: Bauer stereophonic-to-binaural DSP LADSPA plugins
Name: libbs2b
Version: 3.1.0
Release: 1%{?dist}
License: GPL-2.0
URL: https://bs2b.sourceforge.net
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/bs2b/files/libbs2b/%{version}/libbs2b-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: chrpath
BuildRequires: libsndfile-devel

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio records.

Recommended for headphone prolonged listening to disable superstereo
fatigue without essential distortions.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package static
Summary: Static library for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static library for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%configure
%make_build

%install

%make_install

chrpath --delete %{buildroot}/%{_bindir}/bs2bconvert
chrpath --delete %{buildroot}/%{_bindir}/bs2bstream

%files
%doc README
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a

%changelog
* Wed May 06 2026 Yann Collette <ycollette dot nospam at free.fr> 3.1.0-1
- Initial release of spec file for 3.1.0
