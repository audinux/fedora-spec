#
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
#

# Global variables for github repository
%global commit0 8479da129a8bb955870ad3059a22e8f8802630ca
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Tag: Compressor, Emulator, Delay, Analyzer
# Type: Plugin, VST, LV2
# Category: Audio, Effect, Synthesizer

Name:    SocaLabs-plugins
Version: 20200512
Release: 5%{?dist}
Summary: Various VST/LV2 Plugins from SocaLabs.com
License: BSD-3-Clause
URL:     https://github.com/FigBug/slPlugins

Source0: https://github.com/FigBug/slPlugins/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: generate-lv2-ttl.py
Source2: LV2.mak.in
Source3: AppConfig.h.in

BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libcurl-devel
BuildRequires: ladspa-devel
BuildRequires: JUCE
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: lv2-devel
BuildRequires: python3-devel
BuildRequires: python-unversioned-command

Requires: alsa

%description
SocaLabs Audio Plugins: https://SocaLabs.com/

- Synth: Commodore 64 SID, Nintendo Entertainment System RP2A03, Gameboy PAPU,
Sega Master System SN76489, SFX8, Voc Vocal Synth
- Effect: Compressor, Delay, Mverb 2020, Sample Delay
- Analyzer: Oscilloscope, Spectrum Analyzer
- Developer tool: AB Tester, Add & Invert, Channel Mute, Compensated Delay, Huge Gain
- Math:  Tone Generator


%package -n lv2-%{name}
Summary: Various LV2 Plugins from SocaLabs.com (LV2)

%description -n lv2-%{name}
https://socalabs.com/

SocaLabs Audio Plugins

%package -n vst-%{name}
Summary: Various VST Plugins from SocaLabs.com (VST)

%description -n vst-%{name}
https://socalabs.com/

SocaLabs Audio Plugins

%prep
%autosetup -n slPlugins-%{commit0}

%build

%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

export CURRENT_PATH=`pwd`

mkdir -p bin/vst
mkdir -p bin/lv2
mkdir -p bin/standalone

mkdir -p $CURRENT_PATH/bin/standalone/
mkdir -p $CURRENT_PATH/bin/vst/
mkdir -p $CURRENT_PATH/bin/lv2/

Projucer --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE/modules

cat ci/pluginlist.txt | while read PLUGIN; do
  PLUGIN=$(echo $PLUGIN|tr -d '\n\r ')

  mkdir -p plugins/$PLUGIN/JuceLibraryCode
  cp %{SOURCE3} plugins/$PLUGIN/JuceLibraryCode/
  cp %{SOURCE2} plugins/$PLUGIN
  cp %{SOURCE1} plugins/$PLUGIN
  
  lv2uri="https://socalabs.com/$PLUGIN/"
  sed "s/_lv2uri_pattern_/${lv2uri//\//\\/}/g" plugins/$PLUGIN/JuceLibraryCode/AppConfig.h.in >plugins/$PLUGIN/JuceLibraryCode/AppConfig.h
  sed "s/_juce_target_/$PLUGIN/g" plugins/$PLUGIN/LV2.mak.in >plugins/$PLUGIN/LV2.mak
  
  sed -i -e 's/pluginFormats="buildVST,buildAU"/pluginFormats="buildStandalone,buildVST"/' plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e 's/buildStandalone="0"/buildStandalone="0"/' plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e 's/JUCEOPTIONS/JUCEOPTIONS JUCE_JACK="1"/'   plugins/$PLUGIN/$PLUGIN.jucer
  
  Projucer --resave plugins/$PLUGIN/$PLUGIN.jucer
  
  echo "include ../../LV2.mak" >> plugins/$PLUGIN/Builds/LinuxMakefile/Makefile
  
  cd plugins/$PLUGIN/Builds/LinuxMakefile
  
  %make_build CONFIG=Release CFLAGS="%{build_cflags}" CXXFLAGS="-std=c++11 %{build_cxxflags}" STRIP=true
  
  cp ./build/$PLUGIN        $CURRENT_PATH/bin/standalone/
  cp ./build/$PLUGIN.so     $CURRENT_PATH/bin/vst/
  cp -r ./build/$PLUGIN.lv2 $CURRENT_PATH/bin/lv2/
  
  cd ../../../..
done

%install

mkdir -p %{buildroot}%{_bindir}
install bin/standalone/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_libdir}/vst
cp bin/vst/*.so %{buildroot}%{_libdir}/vst/

mkdir -p %{buildroot}%{_libdir}/lv2
cp -r bin/lv2/*.lv2 %{buildroot}%{_libdir}/lv2/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/

%files -n vst-%{name}
%{_libdir}/vst/

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-5
- fix debug build

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-1
- Initial release
