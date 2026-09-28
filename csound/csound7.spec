# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

Name: csound7
Version: 7.0.0b17
Release: 2%{?dist}
Summary: A sound synthesis language and library
URL: https://csound.com
License: LGPL-2.1-or-later

# Usage: ./csound-source.sh <TAG>
#        ./csound-source.sh 7.0.0-beta.17

Source0: csound.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: doxygen
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
BuildRequires: swig
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel
BuildRequires: CUnit-devel
BuildRequires: dssi-devel
BuildRequires: eigen3-devel
BuildRequires: gettext-devel
BuildRequires: lame-devel
BuildRequires: libcurl-devel
BuildRequires: liblo-devel
BuildRequires: libpng-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pipewire-devel
BuildRequires: pkgconfig(jack)
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-tkinter
BuildRequires: python3-pygments

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...

%package devel
Summary: Csound development files and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains headers and libraries for developing applications that use Csound.

%package -n python3-csound7
%{?python_provide:%python_provide python3-csound}
Summary: Python Csound development files and libraries for CSound7
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-csound7
Contains Python language bindings for developing Python applications that
use Csound7.

%package dssi
Summary: Disposable Soft Synth Interface (DSSI) plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: dssi

%description dssi
Disposable Soft Synth Interface (DSSI) plugin for Csound

%package osc
Summary: Open Sound Control (OSC) plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description osc
Open Sound Control (OSC) plugin for Csound

%package portaudio
Summary: PortAudio plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description portaudio
PortAudio plugin for Csound

%package manual
Summary: Csound manual
License: GFDL-1.3-only
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description manual
Canonical Reference Manual for Csound.

%prep
%autosetup -n csound

sed -i -e "s|DESTINATION \"share/csound\"|DESTINATION \"%{_lib}/csound\"|g" CMakeLists.txt
sed -i -e "s|DESTINATION \${CMAKE_INSTALL_PREFIX}/share|DESTINATION \${CMAKE_INSTALL_PREFIX}/share/csound|g" CMakeLists.txt

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake -DUSE_LIB64:BOOL=ON \
       -DFAIL_MISSING:BOOL=ON \
       -DBUILD_PYTHON_INTERFACE:BOOL=ON \
       -DBUILD_DEPRECATED_OPCODES:BOOL=ON \
       -DBUILD_OSC_OPCODES:BOOL=ON \
       -DBUILD_DSSI_OPCODES:BOOL=ON \
       -DBUILD_DOCS:BOOL=ON \
       -DBUILD_PLUGINS:BOOL=ON \
       -DBUILD_TOOL:BOOL=ON \
       -DBUILD_TOOLS:BOOL=ON \
       -DBUILD_WITH_LTO:BOOL=ON \
       -DUSE_ALSA:BOOL=ON \
       -DUSE_JACK:BOOL=ON \
       -DUSE_PIPEWIRE:BOOL=ON \
       -DSWIG_ADD_LIBRARY:BOOL=ON \
       -DPYTHON_MODULE_INSTALL_DIR:STRING="%{python3_sitearch}" \
       -DUSE_AVX2:BOOL=OFF \
%ifarch %{arm}
       -DHAVE_NEON:BOOL=OFF \
%endif
       -DUSE_PORTMIDI:BOOL=OFF \
       -DNEED_PORTTIME:BOOL=OFF \
       -DBUILD_TESTS:BOOL=OFF \
       -DBUILD_PLUGINS:BOOL=ON \
       -DCMAKE_LIBRARY_PATH="`pkg-config --libs-only-L jack | sed -e 's/-L//g'`"

%cmake_build
%cmake_build -- doc

%install

%cmake_install

install -m 766 -d %{buildroot}/%{_mandir}/
cp -ra %{__cmake_builddir}/docs/man/man3 %{buildroot}/%{_mandir}/

install -m 766 -d %{buildroot}/%{_datadir}/doc/csound7-manual/
cp -ra %{__cmake_builddir}/docs/html %{buildroot}/%{_datadir}/doc/csound7-manual/

%find_lang %{name}

%ldconfig_scriptlets

%ldconfig_scriptlets -n python3-csound7

%files -f %{name}.lang
%license COPYING
%doc README.md Release_Notes
%{_bindir}/atsa
%{_bindir}/cs
%{_bindir}/csanalyze
%{_bindir}/csb64enc
%{_bindir}/csbeats
%{_bindir}/csdebugger
%{_bindir}/csound
%{_bindir}/cvanal
%{_bindir}/dnoise
%{_bindir}/envext
%{_bindir}/extract
%{_bindir}/extractor
%{_bindir}/het_export
%{_bindir}/het_import
%{_bindir}/hetro
%{_bindir}/lpanal
%{_bindir}/lpc_export
%{_bindir}/lpc_import
%{_bindir}/makecsd
%{_bindir}/mixer
%{_bindir}/mkir
%{_bindir}/pvanal
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_bindir}/pvlook
%{_bindir}/scale
%{_bindir}/scot
%{_bindir}/scsort
%{_bindir}/sdif2ad
%{_bindir}/smf_conv
%{_bindir}/sndinfo
%{_bindir}/src_conv
%{_bindir}/srconv
%{_libdir}/csound/plugins64-7.0/*.so
%exclude %{_libdir}/csound/plugins64-7.0/libdssi4cs.so
%exclude %{_libdir}/csound/plugins64-7.0/libosc.so
%exclude %{_libdir}/csound/plugins64-7.0/librtpa.so
%{_mandir}/man3/*
%{_datadir}/csound/samples/*

%files devel
%{_includedir}/csound/*
%{_libdir}/libcsound64.so
%{_libdir}/pkgconfig/csound.pc
%{_libdir}/csound/*.cmake

%files -n python3-csound7
%{_libdir}/libcsound64.so.7.0
%{python3_sitelib}/*csound.py*
%{python3_sitelib}/__pycache__/

%files dssi
%{_libdir}/csound/plugins64-7.0/libdssi4cs.so

%files osc
%{_libdir}/csound/plugins64-7.0/libosc.so

%files portaudio
%{_libdir}/csound/plugins64-7.0/librtpa.so

%files manual
%{_datadir}/doc/csound7-manual/*

%changelog
* Sun Sep 27 2026 Yann Collette <ycollette.nospam@free.fr> - 7.0.0b17-2
- update to 7.0.0b17-2 - fix the python package

* Sun Sep 27 2026 Yann Collette <ycollette.nospam@free.fr> - 7.0.0b17-1
- Initial version of the spec
