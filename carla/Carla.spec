# https://github.com/falkTX/Carla/commit/74eef49b626c362fbb70dd227f99534dd5014cc7

%global commit0 bd811fb1cedd330168c7712dfdade9665587ea07
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global pname   carla 
%global commitdate 20200201


# Tag: Jack, MIDI, Sfz, Sf2, Sf3, OSC
# Type: Standalone
# Category: Audio, Tool

Name:           Carla
Version:        2.1
#Release:        0.11.%%{commitdate}git%%{shortcommit0}%%{?dist}
Release:        5.rc1%{?shortcommit0}%{?dist}
Summary:        Audio plugin host
License:        GPLv2+ and BSD and Boost and ISC and MIT and zlib
URL:            https://github.com/falkTX/Carla

Vendor:       Audinux
Distribution: Audinux

# The entire source code is GPLv2+ except
# - BSD
# source/modules/lilv/lilv-0.24.0/waf
# source/modules/lilv/serd-0.24.0/waf
# source/modules/lilv/sord-0.16.0/waf
# source/modules/lilv/sratom-0.6.0/waf
# source/modules/audio_decoder/ffcompat.h
# source/modules/rtaudio/include/soundcard.h
# - Boost
# source/modules/hylia/link/asio/*
# - ISC
# source/jackbridge/*
# source/modules/dgl/*
# source/modules/distrho/*
# source/modules/lilv/*
# source/modules/water/buffers/AudioSampleBuffer.h
# source/modules/water/containers
# source/modules/water/files/*
# source/modules/water/maths/*
# source/modules/water/memory/*
# source/modules/water/midi/*
# source/modules/water/misc/*
# source/modules/water/streams/OutputStream.h
# source/modules/water/synthesisers/*
# source/modules/water/text/*
# source/modules/water/threads/*
# source/modules/water/xml/*
# source/utils/CarlaJuceUtils.hpp
# - MIT/Expat
# source/modules/rtaudio/RtAudio.cpp
# source/modules/rtaudio/RtAudio.h
# source/modules/rtmidi/RtMidi.cpp
# source/modules/rtmidi/RtMidi.h
# source/modules/sfzero/LICENSE
# - zlib
# source/modules/dgl/src/nanovg/LICENSE.txt
# source/modules/dgl/src/nanovg/fontstash.h
# source/modules/dgl/src/nanovg/nanovg.c
# source/modules/dgl/src/nanovg/nanovg.h
# source/modules/dgl/src/nanovg/nanovg_gl.h
# source/modules/dgl/src/nanovg/nanovg_gl_utils.h

Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         %{name}-gcc10-include.patch

BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-magic
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       jack-audio-connection-kit
Requires:       python3-qt5
Requires:       python3-pyliblo
Requires:       hicolor-icon-theme
Requires:       shared-mime-info


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
Features

    LADSPA, DSSI, LV2 and VST plugin formats
    SF2/3 and SFZ sound banks
    Internal audio and midi file player
    Automation of plugin parameters via MIDI CC
    Remote control over OSC
    Rack and Patchbay processing modes, plus Single and Multi-Client if using
    JACK
    Native audio drivers (ALSA, DirectSound, CoreAudio, etc) and JACK

In experimental phase / work in progress:

    Export any Carla loadable plugin or sound bank as an LV2 plugin
    Plugin bridge support (such as running 32bit plugins on a 64bit Carla, or
    Windows plugins on Linux)
    Run JACK applications as audio plugins
    Transport controls, sync with JACK Transport or Ableton Link

Carla is also available as an LV2 plugin for MacOS and Linux, and VST plugin for
Linux.

%package        devel
Summary:        Header files to access Carla's API
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package        vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    vst
This package contains Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack.

%package     -n lv2-%{pname}
Summary:        LV2 plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{pname}
This package contains the Carla LV2 plugin.

%prep
%autosetup -p 1 -n %{name}-%{commit0}

# remove windows stuff
rm -rf data/{macos,windows}

# E: wrong-script-interpreter /usr/lib64/python3/dist-packages/carla_backend.py /usr/bin/env python3
find . -type f \( -name "*.py" \) -exec sed -i "s|#!/usr/bin/env python3|#!%{__python3}|g" {} \;
sed -i "s|#!/usr/bin/env python3|#!%{__python3}|" source/frontend/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}
sed -i "s|#!/usr/bin/env python|#!%{__python3}|" source/frontend/widgets/paramspinbox.py

# fix libdir path
sed -i "s|/lib/carla|/%{_lib}/carla|" data/{carla,carla-control,carla-database,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack,carla-settings}

%build
%{set_build_flags}
# list build configuration, no need for optflags or -j
make features
%make_build SKIP_STRIPPING=true NOOPT=true V=1

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
%{_libdir}/%{pname}/
%{_datadir}/applications/%{pname}-control.desktop
%{_datadir}/applications/%{pname}.desktop
%{_datadir}/%{pname}/
%{_datadir}/icons/hicolor/*/apps/%{pname}*.png
%{_datadir}/icons/hicolor/*/apps/%{pname}*.svg
%{_datadir}/mime/packages/%{pname}.xml

%files vst
%{_libdir}/vst/

%files -n lv2-%{pname}
%dir %{_libdir}/lv2
%{_libdir}/lv2/carla.lv2/

%files devel
%{_includedir}/%{pname}/
%{_libdir}/pkgconfig/%{pname}-standalone.pc
%{_libdir}/pkgconfig/%{pname}-utils.pc
%{_libdir}/pkgconfig/%{pname}-native-plugin.pc

%changelog
* Sun Feb 9 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1-5.rc1.gitbd811fb1
- update to 2.1-5.rc1.gitbd811fb1

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
