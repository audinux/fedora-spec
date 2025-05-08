# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

Name: csound-plugins
Version: 1.0.2
Release: 1%{?dist}
Summary: Csound plugins which were originally in the main repository, and for new plugins as well.
URL: https://github.com/csound/plugins
License: LGPLv2+

# Usage: ./csound-plugins-source.sh <TAG>
#        ./csound-plugins-source.sh 1.0.2

Source0: plugins.tar.gz
Source1: csound-plugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: eigen3-devel
BuildRequires: pkgconfig(jack)
BuildRequires: hdf5-devel
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: stk-devel
%if 0%{?fedora} >= 40
BuildRequires: intel-gmmlib-devel
%endif
BuildRequires: python3-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libwebsockets-devel
BuildRequires: fluidsynth-devel
BuildRequires: faust-devel
BuildRequires: csound-devel
BuildRequires: lame-devel
BuildRequires: wiiuse-devel

%description
Csound plugins which were originally in the main repository, and for new plugins as well.

%prep
%autosetup -n plugins

%build

%cmake -DBUILD_HDF5_OPCODES=OFF \
       -DBUILD_TESTS:BOOL=OFF \
       -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"

%cmake_build

%install

%cmake_install

mkdir -p %{buildroot}/%{_libdir}/csound/
mv %{buildroot}/usr/lib/csound/plugins64-6.0/ %{buildroot}/%{_libdir}/csound/plugins-6.0/

%files
%license LICENSE
%doc README.md
%{_libdir}/csound/plugins-6.0/libchua.so
%{_libdir}/csound/plugins-6.0/libfaustcsound.so
%{_libdir}/csound/plugins-6.0/libimage.so
%{_libdir}/csound/plugins-6.0/libpy.so
%{_libdir}/csound/plugins-6.0/libwidgets.so
%{_libdir}/csound/plugins-6.0/libvirtual.so
%{_libdir}/csound/plugins-6.0/libstkops.so
%{_libdir}/csound/plugins-6.0/libwebsocketIO.so
%{_libdir}/csound/plugins-6.0/libmp3out.so
%{_libdir}/csound/plugins-6.0/libwiimote.so
%{_libdir}/csound/plugins-6.0/libfluidOpcodes.so
%{_libdir}/csound/plugins-6.0/libjackTransport.so
%{_libdir}/csound/plugins-6.0/libjacko.so

%changelog
* Thu Oct 10 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- Initiali version of the spec
