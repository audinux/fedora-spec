# Status: active
# Tag: Jack, Alsa
# Type: Language
# Category: Audio, Synthesizer, Graphic, Programming

%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif

Name: csound
Version: 6.18.1
Release: 12%{?dist}
Summary: A sound synthesis language and library
URL: https://csound.com/index.html
License: LGPLv2+

Source0: https://github.com/csound/csound/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/csound/manual/releases/download/6.18.0/Csound6.18.0_manual_html.zip

Patch1: 0001-Add-support-for-using-xdg-open-for-opening-help.patch
Patch2: 0002-Default-to-PulseAudio.patch
Patch3: 0003-use-standard-plugins-path.patch
Patch4: 0004-fix-naming-conflicts.patch
Patch5: 0005-OSC-types.patch
Patch6: 0006-python312.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
BuildRequires: swig
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel
BuildRequires: CUnit-devel
BuildRequires: dssi-devel
BuildRequires: eigen3-devel
BuildRequires: gettext-devel
%if %{JAVA}
BuildRequires: java-devel
BuildRequires: jpackage-utils
%endif
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

%package -n python3-csound
%{?python_provide:%python_provide python3-csound}
Summary: Python Csound development files and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-csound
Contains Python language bindings for developing Python applications that
use Csound.

%if %{JAVA}
%package java
Summary: Java Csound support
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-headless
Requires: jpackage-utils

%description java
Contains Java language bindings for developing and running Java
applications that use Csound.
%endif

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
License: GFDL
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description manual
Canonical Reference Manual for Csound.

%prep
%autosetup -p1
# setup the manual
%setup -q -T -D -a 1

# Fix end of line encodings
%define fix_line_encoding() \
  sed -i.orig 's/\\r\\n/\\n/;s/\\r/\\n/g' %1; \
  touch -r %1.orig %1; \
  rm -f %1.orig;

for csd in $(find html/examples -name \*.csd); do
  %fix_line_encoding $csd
done

# Fix spurious executable bits
find html/examples -type f -print0 | xargs -0 chmod a-x

%build
%if "%{_libdir}" == "%{_prefix}/lib64"
    %global uselib64 ON
%else
    %global uselib64 OFF
%endif

# Terrible hack
%ifarch %{arm}
sed -i 's*//#define PFFFT_SIMD_DISABLE*#define PFFFT_SIMD_DISABLE*' OOps/pffft.c
%endif

JAVA_VAL=OFF
%if %{JAVA}
JAVA_VAL=ON
%endif
%cmake -DUSE_LIB64:BOOL=%{uselib64} \
       -DFAIL_MISSING:BOOL=ON \
       -DBUILD=BUILD_PYTHON_INTERFACE:BOOL=ON \
       -DBUILD_JAVA_INTERFACE:BOOL=${JAVA_VAL} \
       -DBUILD_LUA_INTERFACE:BOOL=OFF \
       -DSWIG_ADD_LIBRARY:BOOL=OFF \
       -DPYTHON_MODULE_INSTALL_DIR:STRING="%{python3_sitearch}" \
%ifarch %{x86}
       -DHAS_SSE2:BOOL=OFF \
       -DHAS_FPMATH_SSE:BOOL=OFF \
%endif
%ifarch %{arm}
       -DHAVE_NEON:BOOL=OFF \
%endif
       -DBUILD_STK_OPCODES:BOOL=ON \
       -DBUILD_LINEAR_ALGEBRA_OPCODES:BOOL=OFF \
       -DUSE_PORTMIDI:BOOL=OFF \
       -DNEED_PORTTIME:BOOL=OFF \
       -DBUILD_P5GLOVE_OPCODES:BOOL=OFF \
       -DBUILD_WEBSOCKET_OPCODE:BOOL=OFF \
       -DBUILD_TESTS:BOOL=OFF

%cmake_build

%install
%cmake_install

%if %{JAVA}
# Fix the Java installation
install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/%{name}/java/csnd.jar .)
%endif

# Help the debuginfo generator
ln -s ../csound_orclex.c Engine/csound_orclex.c
ln -s ../csound_prelex.c Engine/csound_prelex.c

rm -rf %{buildroot}%{_datadir}/cmake/Csound/
rm -rf %{buildroot}%{_datadir}/samples/

%find_lang %{name}6

%ldconfig_scriptlets

%ldconfig_scriptlets -n python3-csound

%check
# make csdtests

%files -f %{name}6.lang
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
%{_bindir}/cs-envext
%{_bindir}/cs-extract
%{_bindir}/cs-extractor
%{_bindir}/het_export
%{_bindir}/het_import
%{_bindir}/hetro
%{_bindir}/lpanal
%{_bindir}/lpc_export
%{_bindir}/lpc_import
%{_bindir}/makecsd
%{_bindir}/cs-mixer
%{_bindir}/pvanal
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_bindir}/pvlook
%{_bindir}/cs-scale
%{_bindir}/cs-scot
%{_bindir}/scsort
%{_bindir}/sdif2ad
%{_bindir}/cs-sndinfo
%{_bindir}/cs-srconv
%{_bindir}/cs-src_conv
%{_libdir}/lib%{name}64.so.6.0
%dir %{_libdir}/%{name}/plugins-6.0
%{_libdir}/%{name}/plugins-6.0/libampmidid.so
%{_libdir}/%{name}/plugins-6.0/libarrayops.so
%{_libdir}/%{name}/plugins-6.0/libcontrol.so
%{_libdir}/%{name}/plugins-6.0/libdoppler.so
%{_libdir}/%{name}/plugins-6.0/libfractalnoise.so
%{_libdir}/%{name}/plugins-6.0/libftsamplebank.so
%{_libdir}/%{name}/plugins-6.0/libipmidi.so
%{_libdir}/%{name}/plugins-6.0/libjoystick.so
%{_libdir}/%{name}/plugins-6.0/liblfsr.so
%{_libdir}/%{name}/plugins-6.0/libmixer.so
%{_libdir}/%{name}/plugins-6.0/libpadsynth.so
%{_libdir}/%{name}/plugins-6.0/libpvsops.so
%{_libdir}/%{name}/plugins-6.0/librtalsa.so
%{_libdir}/%{name}/plugins-6.0/librtpulse.so
%{_libdir}/%{name}/plugins-6.0/libscansyn.so
%{_libdir}/%{name}/plugins-6.0/libsignalflowgraph.so
%{_libdir}/%{name}/plugins-6.0/libstdutil.so
%{_libdir}/%{name}/plugins-6.0/libtrigenvsegs.so
%{_libdir}/%{name}/plugins-6.0/liburandom.so
%{_libdir}/%{name}/plugins-6.0/libbformdec2.so
%{_libdir}/%{name}/plugins-6.0/libdeprecated.so
%{_libdir}/%{name}/plugins-6.0/librtjack.so
   
%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}64.so
%{_libdir}/libcsnd6.so

%files -n python3-csound
%{_libdir}/libcsnd6.so.6.0
#%%{_libdir}/%%{name}/plugins-6.0/libpy.so
#%%{python3_sitearch}/_csnd*
#%%{python3_sitearch}/csnd*
%{python3_sitearch}/*csound.py*
%{python3_sitearch}/__pycache__/

%if %{JAVA}
%files java
%{_libdir}/lib_jcsound6.so
%{_libdir}/lib_jcsound.so.1
%{_libdir}/csnd6.jar
%{_javadir}/csnd.jar
%endif

%files dssi
%{_libdir}/%{name}/plugins-6.0/libdssi4cs.so

%files osc
%{_libdir}/%{name}/plugins-6.0/libosc.so

%files portaudio
%{_libdir}/%{name}/plugins-6.0/librtpa.so

%files manual
%doc html/

%changelog
* Tue Oct 08 2024 Yann Collette <ycollette.nospam@free.fr> - 6.18.1-12
- update to 6.18.1-12

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.16.2-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.16.2-7
- Stop building java parts on i686 (#2104031)

* Mon Oct 17 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.16.2-6
- Fix FTBFS (properly remove spurious x bits) (#2113161)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.16.2-4
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 6.16.2-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 6.16.2-1
- Update to 0.16.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 6.15.0-4
- Rebuild for fluidsynth soname

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.15.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.15.0-1
- Update to 6.15.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 6.14.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.14.0-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.14.0-1
- Update to 6.14.0

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 6.13.0-7
- Rebuild against fluidsynth2
- Fix FTBFS RHBZ#1794443

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.13.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.13.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.13.0-3
- Move to python3, upstream seems to have fixed it with the current release
- Minor cleanups

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.13.0-1
- Update to Csound 6.13.0

* Sun Jun  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.12.2-1
- Update to Csound 6.12.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 6.10.0-2
- Fix upgrade path

* Sun Feb 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 6.10.0-1
- Update to Csound 6.10.0
- Obsolete javadocs support (deprecated upstream)
- Packaging updates from Hlöðver Sigurðsson

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.03.2-16
- Python 2 binary package renamed to python2-csound
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 6.03.2-12
- Rebuild for LuaJIT 2.1.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Kalev Lember <klember@redhat.com> - 6.03.2-9
- Rebuilt for libwiiuse soname bump

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 6.03.2-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.03.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 6.03.2-4
- Rebuild for boost 1.57.0

* Tue Sep 30 2014 Dan Horák <dan[at]danny.cz> - 6.03.2-3
- luajit available only on selected arches

* Wed Sep 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 6.03.2-2
- Fix separation of jack into it's subpackage

* Tue Sep 16 2014 Jerry James <loganjerry@gmail.com> - 6.03.2-1
- Update to 6.03.2
- Fix installation
- Fix license handling
- Add wiimote subpackage, wiiuse-devel BR, and bluez-libs-devel BR (bz 1142457)

* Fri Aug 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 6.03.1-1
- Update to 6.03.1
- Spec file fixups

* Mon Jul 28 2014 Jerry James <loganjerry@gmail.com> - 6.03.0-1
- Update to 6.03.0 (bz 1094866; fixes bzs 1057580, 1067182, and 1106095)
- Change project URL to github page
- Update BRs and reorganize for readability
- Bring back the manual sources; the manual subpackage has the GFDL license
- Obsolete the -gui and -tk subpackages (no longer supported upstream)
- Add -csoundac, -lua, -portaudio, and -stk subpackages
