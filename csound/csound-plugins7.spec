# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

Name: csound-plugins7
Version: 7.0.0
Release: 1%{?dist}
Summary: Csound plugins which were originally in the main repository, and for new plugins as well.
URL: https://github.com/csound/plugins
License: LGPL-2.1-or-later

# Usage: ./csound-plugins-source.sh <TAG>
#        ./csound-plugins-source.sh 7.0.0

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
BuildRequires: csound7-devel
BuildRequires: lame-devel
BuildRequires: wiiuse-devel

%description
Csound plugins which were originally in the main repository, and for new plugins as well.

%prep
%autosetup -n plugins

%build

# BUILD_CHUA_OPCODES=OFF -> disable eigen for now since it's not detected correctly

%cmake -DBUILD_HDF5_OPCODES=OFF \
       -DBUILD_TESTS:BOOL=OFF \
       -DBUILD_WEBSOCKET_OPCODE=ON \
       -DBUILD_CUDA_OPCODES= OFF \
       -DBUILD_WIIMOTE_OPCODES= ON \
       -DBUILD_PYTHON_OPCODES=ON \
       -DBUILD_HDF5_OPCODES=ON \
       -DBUILD_P5GLOVE_OPCODES=ON \
       -DBUILD_FAUST_OPCODES=ON \
       -DBUILD_OPENCL_OPCODES=ON \
       -DBUILD_LINEAR_ALGEBRA_OPCODES=ON \
       -DBUILD_STK_OPCODES=ON \
       -DBUILD_IMAGE_OPCODES=ON \
       -DBUILD_FLUID_OPCODES=ON \
       -DBUILD_CHUA_OPCODES=OFF \
       -DBUILD_DSSI_OPCODES=ON \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
       -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"


%cmake_build

%install

%cmake_install

mkdir -p %{buildroot}/%{_libdir}/csound/
mv %{buildroot}/usr/lib/csound/plugins64-7.0/ %{buildroot}/%{_libdir}/csound/plugins-7.0/

%files
%license LICENSE
%doc README.md
# {_libdir}/csound/plugins-7.0/libchua.so -> eigen not detect correctly
%{_libdir}/csound/plugins-7.0/libfaustcsound.so
%{_libdir}/csound/plugins-7.0/libimage.so
%{_libdir}/csound/plugins-7.0/libpy.so
#{_libdir}/csound/plugins-7.0/libwidgets.so
#{_libdir}/csound/plugins-7.0/libvirtual.so
%{_libdir}/csound/plugins-7.0/libstkops.so
%{_libdir}/csound/plugins-7.0/libwebsocketIO.so
#{_libdir}/csound/plugins-7.0/libmp3out.so
#{_libdir}/csound/plugins-7.0/libwiimote.so
%{_libdir}/csound/plugins-7.0/libfluidOpcodes.so
#{_libdir}/csound/plugins-7.0/libjackTransport.so
#{_libdir}/csound/plugins-7.0/libjacko.so
%{_libdir}/csound/plugins-7.0/libdssi4cs.so
%{_libdir}/csound/plugins-7.0/libhdf5ops.so
%{_libdir}/csound/plugins-7.0/liblinear_algebra.so
%{_libdir}/csound/plugins-7.0/stk/*

%changelog
* Thu Oct 29 2026 Yann Collette <ycollette.nospam@free.fr> - 7.0.0-1
- Initiali version of the spec
