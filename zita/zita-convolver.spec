# Tag: Jack, Convolution
# Type: Standalone
# Category: Audio, Tool

Summary: convolver function
Name:    zita-convolver
Version: 4.0.3
Release: 2%{?dist}
License: GPL
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/

Vendor:       Audinux
Distribution: Audinux

Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: fftw-devel

%description
This function is used to modify IR data while the convolver
is actually running. It does not use any memory allocation
nor modify internal data structures, and only data in already
existing partitions can be modified this way.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%prep
%autosetup

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|ldconfig||' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
pushd source
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%files
%doc AUTHORS README*
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Sat Jun 15 2019 Yann Collette <ycollette.nospam@free.fr> - 4.0.3-2
- fix package

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 4.0.3-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 4.0.3-1
- Initial build.
