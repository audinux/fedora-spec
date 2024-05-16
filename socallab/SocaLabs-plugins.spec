# Tag: Compressor, Emulator, Delay, Analyzer
# Type: Plugin, VST, VST3
# Category: Audio, Effect, Synthesizer

# spec file for package slPlugins
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/

Name: SocaLabs-plugins
Version: 20220502
Release: 6%{?dist}
Summary: Various VST/VST3 Plugins from SocaLabs.com
License: BSD-3-Clause
URL: https://github.com/FigBug/slPlugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./socalab-source.sh <tag>
# ./socalab-source.sh 20a0b31169f54e942e22b4ac74fcc2788d72ea16

Source0: slPlugins.tar.gz
Source4: socalab-source.sh

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libcurl-devel
BuildRequires: ladspa-devel

Requires: alsa

%description
SocaLabs Audio Plugins: https://SocaLabs.com/

- Synth: Commodore 64 SID, Nintendo Entertainment System RP2A03, Gameboy PAPU,
         Sega Master System SN76489, SFX8, Voc Vocal Synth
- Effect: Compressor, Delay, Mverb 2020, Sample Delay
- Analyzer: Oscilloscope, Spectrum Analyzer
- Developer tool: AB Tester, Add & Invert, Channel Mute, Compensated Delay, Huge Gain
- Math:  Tone Generator

%package -n vst-%{name}
Summary: Various VST2 Plugins from SocaLabs.com

%description -n vst-%{name}
https://socalabs.com/

SocaLabs Audio Plugins - VST2 format

%package -n vst3-%{name}
Summary: Various VST3 Plugins from SocaLabs.com

%description -n vst3-%{name}
https://socalabs.com/

SocaLabs Audio Plugins - VST3 format

%package -n lv2-%{name}
Summary: Various LV2 Plugins from SocaLabs.com

%description -n lv2-%{name}
https://socalabs.com/

SocaLabs Audio Plugins - LV2 format

%prep
%autosetup -n slPlugins

%build

%set_build_flags

export CXXFLAGS="-std=c++20 -include utility -include cmath $CXXFLAGS"

%cmake
%cmake_build

%install

mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/vst/
mkdir -p %{buildroot}%{_libdir}/vst3/
mkdir -p %{buildroot}%{_libdir}/lv2/
mkdir -p %{buildroot}%{_libdir}/clap/

PLUGIN_LIST="ABTester \
	     AddInvert \
	     ChannelMute \
	     CompensatedDelay \
	     Compressor \
	     Delay \
	     Expander \
	     Gate \
	     HugeGain \
	     Limiter \
	     Maths \
	     Oscilloscope \
	     PitchTrack \
	     SampleDelay \
	     SFX8 \
	     SpectrumAnalyzer \
	     ToneGenerator"

for PLUGIN in $PLUGIN_LIST
do
    cp -ra %{__cmake_builddir}/plugins/$PLUGIN/"$PLUGIN"_artefacts/Standalone/* %{buildroot}%{_bindir}/
    cp -ra %{__cmake_builddir}/plugins/$PLUGIN/"$PLUGIN"_artefacts/LV2/* %{buildroot}%{_libdir}/lv2/
    cp -ra %{__cmake_builddir}/plugins/$PLUGIN/"$PLUGIN"_artefacts/VST/* %{buildroot}%{_libdir}/vst/
    cp -ra %{__cmake_builddir}/plugins/$PLUGIN/"$PLUGIN"_artefacts/VST3/* %{buildroot}%{_libdir}/vst3/
done

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/

%files -n vst3-%{name}
%{_libdir}/vst3/

%files -n lv2-%{name}
%{_libdir}/lv2/

%changelog
* Wed Oct 11 2023 Yann Collette <ycollette.nospam@free.fr> - 20200512-6
- update to 20a0b31169f54e942e22b4ac74fcc2788d72ea16

* Fri May 20 2022 Yann Collette <ycollette.nospam@free.fr> - 20200512-5
- update to 77b4a8d6bf8da4407fc6de7b9074f68985d33ef8

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-5
- fix debug build

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-1
- Initial release
