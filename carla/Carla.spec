# Tag: Tool, Rack
# Type: Plugin, VST3, LV2, Standalone
# Category: Audio, Effect, Synthesizer, Tool

%define _lto_cflags %{nil}

%global pname carla

Name: Carla-mao
Version: 2.5.8
Release: 3%{?dist}
Summary: Audio plugin host
Epoch:   1
License: GPLv2+ and BSD and Boost and ISC and MIT and zlib
URL: https://github.com/falkTX/Carla

Source0: https://github.com/falkTX/Carla/archive/v%{version}.tar.gz#/Carla-%{version}.tar.gz
Patch0: Carla-libdir.patch
Patch1: Carla-single-libs-path.patch
Patch2: Carla-0001-fix-prototype.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-winpthreads-static
BuildRequires: mingw64-winpthreads-static
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(mxml)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: python3-qt5-base
BuildRequires: python3-magic
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(zlib)
BuildRequires: wine-devel
# BuildRequires: glibc-devel(x86-32)
# BuildRequires: wine-devel(x86-32)
# BuildRequires: libstdc++-devel(x86-32)
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: python3-qt5
Requires: python3-qt5-webkit
Requires: python3-pyliblo
Requires: python3-tornado
Requires: hicolor-icon-theme
Requires: shared-mime-info
Requires: wine-core

Provides: Carla-mao = %{version}

# Dont provide or require internal libs. Using new rpm builtin filtering,
# see https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Private_Libraries
%global _privatelibs libjack[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
Carla is a fully-featured audio plugin host, with support for many audio drivers
and plugin formats.
It's open source and licensed under the GNU General Public License, version 2 or
later.
Features:
* LADSPA, DSSI, LV2 and VST plugin formats
* SF2/3 and SFZ sound banks
* Internal audio and midi file player
* Automation of plugin parameters via MIDI CC
* Remote control over OSC
* Rack and Patchbay processing modes, plus Single and Multi-Client if using
  JACK
* Native audio drivers (ALSA, DirectSound, CoreAudio, etc) and JACK
* Export any Carla loadable plugin or sound bank as an LV2 plugin
* Plugin bridge support (such as running 32bit plugins on a 64bit Carla, or
  Windows plugins on Linux)
* Run JACK applications as audio plugins
* Transport controls, sync with JACK Transport or Ableton Link

Carla is also available as an LV2 plugin for MacOS and Linux, and VST plugin for
Linux.

This package of Carla includes the wine bridge.

%package devel
Summary: Header files to access Carla's API
Requires: %{name} = %{version}-%{release}
Provides: Carla-mao-devel = %{version}

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package -n vst-%{name}
Summary: CarlaRack and CarlaPatchbay VST plugins
Requires: %{name} = %{version}-%{release}
Provides: vst-Carla-mao-devel = %{version}

%description -n vst-%{name}
This package contains Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack.

%package -n lv2-%{name}
Summary: LV2 plugin
Requires: %{name} = %{version}-%{release}
Provides: lv2-Carla-mao-devel = %{version}

%description -n lv2-%{name}
This package contains the Carla LV2 plugin.

%prep
%setup -n Carla-%{version}

%patch 0 -p0
%patch 1 -p0
%if 0%{?fedora} >= 41
%patch 2 -p1
%endif

# remove windows stuff
rm -rf data/{macos,windows}

# E: wrong-script-interpreter /usr/lib64/python3/dist-packages/carla_backend.py /usr/bin/env python3
find . -type f \( -name "*.py" \) -exec sed -i "s|#!/usr/bin/env python3|#!%{__python3}|g" {} \;
sed -i "s|#!/usr/bin/env python3|#!%{__python3}|" source/frontend/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}
sed -i "s|#!/usr/bin/env python|#!%{__python3}|" source/frontend/widgets/paramspinbox.py

# fix libdir path
sed -i "s|/lib/carla|/%{_lib}/carla|" data/{carla,carla-control,carla-database,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack,carla-settings}

# Fix metainfo install dir
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata/studio.kx.carla.appdata.xml|$(DESTDIR)$(PREFIX)/share/metainfo/studio.kx.carla.appdata.xml|g' Makefile
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata|$(DESTDIR)$(PREFIX)/share/metainfo|g' Makefile

%build
%set_build_flags

# list build configuration, no need for optflags or -j
make features

%make_build SKIP_STRIPPING=true NOOPT=true V=1

export CFLAGS=
export CXXFLAGS=
export LDFLAGS=
#make win32 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++
make win64 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++

#make wine32
make wine64

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Create a vst directory
install -m 755 -d %{buildroot}/%{_libdir}/vst/

# E: non-executable-script /usr/share/carla/paramspinbox.py 644 /usr/bin/env python
find %{buildroot} -type f \( -name "*.py" \) -exec chmod a+x {} \;

# E: non-executable-script /usr/share/carla/carla 644 /usr/bin/python3
chmod a+x %{buildroot}%{_datadir}/%{pname}/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}

# fix perm due rpmlint W: unstripped-binary-or-object /usr/lib64/carla/libcarla_interposer-jack-x11.so
find %{buildroot}%{_libdir} -name '*.so' -exec chmod +x '{}' ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files
%doc README.md
%license doc/GPL.txt doc/LGPL.txt
%{_bindir}/%{pname}
%{_bindir}/%{pname}-control
%{_bindir}/%{pname}-database
%{_bindir}/%{pname}-jack-multi
%{_bindir}/%{pname}-jack-single
%{_bindir}/%{pname}-patchbay
%{_bindir}/%{pname}-rack
%{_bindir}/%{pname}-settings
%{_bindir}/%{pname}-single
%{_bindir}/%{pname}-jack-patchbayplugin
%{_bindir}/%{pname}-osc-gui
%{_libdir}/%{pname}/
%{_datadir}/applications/%{pname}-control.desktop
%{_datadir}/applications/%{pname}.desktop
%{_datadir}/applications/%{pname}-jack-multi.desktop
%{_datadir}/applications/%{pname}-jack-single.desktop
%{_datadir}/applications/%{pname}-patchbay.desktop
%{_datadir}/applications/%{pname}-rack.desktop
%{_datadir}/%{pname}/
%{_datadir}/icons/hicolor/*/apps/%{pname}*.png
%{_datadir}/icons/hicolor/*/apps/%{pname}*.svg
%{_datadir}/mime/packages/%{pname}.xml
%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files -n vst-%{name}
%{_libdir}/vst/

%files -n lv2-%{name}
%dir %{_libdir}/lv2
%{_libdir}/lv2/carla.lv2/

%files devel
%{_includedir}/%{pname}/
%{_libdir}/pkgconfig/%{pname}-standalone.pc
%{_libdir}/pkgconfig/%{pname}-utils.pc
%{_libdir}/pkgconfig/%{pname}-native-plugin.pc
%{_libdir}/pkgconfig/%{pname}-host-plugin.pc

%changelog
* Thu Jan 18 2024 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.8-3
- Update to 2.5.8-3

* Sun Oct 01 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.7-3
- Update to 2.5.7-3

* Fri Aug 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.6-3
- Update to 2.5.6-3 - add missing requires

* Sun Jun 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.5-3
- Update to 2.5.5-3 - add missing requires

* Sun Jun 04 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.5-1
- Update to 2.5.5-1

* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.4-1
- Update to 2.5.4-1

* Sun Jan 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.3-1
- Update to 2.5.3-1

* Mon Oct 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.2-1
- Update to 2.5.2-1

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1:2.5.0-1
- Update to 2.5.0-1

* Sun Jul 17 2022 Yann Collette <ycollette.nospam@free.fr> - 1:2.4.4-1
- Update to 2.4.4-1

* Sat Apr 16 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.3-1
- Update to 2.4.3 + add wine bridge

* Sat Mar 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-2
- Add Carla-refresh-plugin-crash.patch

* Sun Feb 20 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.2-1
- Update to 2.4.2
- Add Carla-single-libs-path.patch

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.1-3
- Add Carla-expression-error.patch

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.1-1
- Update to 2.4.1

* Fri Aug 20 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.4.0-1
- Update to 2.4.0

* Mon Aug 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.2-1
- Update to 2.3.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.1-1
- Update to 2.3.1-1

* Wed Jul 14 2021 Scott Talbert <swt@techie.net> - 1:2.3.0-5
- Replace python3-qt5-devel BD with python3-qt5-base (for pyuic5)

* Wed Jun 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-4
- Rebuilt for fluidsynth-2.2.1

* Tue Jun 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-3
- Add Carla-libdir.patch

* Wed May 26 2021 Jan Beran <jaberan@redhat.com> - 1:2.3.0-2
- Add carla.appdata.xml file

* Thu Apr 15 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.3.0-1
- Update to 2.3.0

* Thu Feb 18 2021 Neal Gompa <ngompa13@gmail.com> - 1:2.2.0-4
- Drop explicit dep on jack-audio-connection-kit

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 1:2.2.0-2
- Add missing #includes for gcc-11

* Sun Sep 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0-1
- Update to 2.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.0-0.1.rc1
- Update to 2.2.0-0.1.rc1

* Sat May 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2-0.1.beta1
- Update to 2.2-0.1.beta1

* Fri May 15 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2-0.1.20200514gitf100892
- Update to 2.2-0.1.20200514gitf100892
- Add ExcludeArch ppc64le due PowerPC is no longer supported by JUCE

* Tue Apr 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.1-2
- Add epoch to allow update

* Tue Apr 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1:2.1-1
- Update to 2.1-1

* Wed Apr 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1-6.rc2
- Update to 2.1-6.rc2

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1-5.beta1.git74eef49
- Rebuild against fluidsynth2

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1-4.beta1.git74eef49
- Update to 2.1-4.beta1.git74eef49
- Add Carla-gcc10-include.patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3.beta13322c9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.1-2.beta1.git3322c9f
- Update to 2.1-2.beta1.git3322c9f
- Dropped BR  non-ntk-fluid
- Dropped BR  pkgconfig(ntk)

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.1-1.beta1.git3322c9f
- Update to 2.1-1.beta1.git3322c9f

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.11.20190501git41f81a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.10.20190501git41f81a8
- Update to 2.0.0-0.10.20190501git41f81a8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.9.20181225git2f3a442
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.8.20181225git2f3a442
- Filtering private libs

* Sat Jan 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.7.20181225git2f3a442
- Add RR python3-pyliblo fixes (RHBZ#1663630)

* Fri Jan 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.6.20181225git2f3a442
- Add RR jack-audio-connection-kit fixes (RHBZ#1663319) and (RHBZ#1663357)

* Tue Dec 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.5.20181225git2f3a442
- Update to 2.0.0-0.5.20181225git2f3a442
- Rework of Carla-bswap.patch

* Fri Dec 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.4.20181212git51f2073
- Add lv2-carla subpkg
- Take ownership of lv2/
- Add BR desktop-file-utils
- Add Carla-bswap.patch
- Remove upstream optimisation options

* Thu Dec 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.3.20181212git51f2073
- Use correct directory in subpgk vst
- Make build verbose V=1
- Fix debug symbols extraction / stripping

* Wed Dec 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.2.20181212git51f2073
- Add subpkg vst
- Remove group tag
- Remove old BR qt-devel
- New git release use correct desktop files
- Use macro %%{_lib} libdir fix
- Use %%{__python3} macro
- Use %%{_datadir}/%%{pname}/

* Tue Dec 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-0.1.20181212git51f2073
- Initial build
