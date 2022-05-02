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

# Tag: Compressor, Emulator, Delay, Analyzer
# Type: Plugin, VST, VST3
# Category: Audio, Effect, Synthesizer

Name:    SocaLabs-plugins
Version: 20220502
Release: 5%{?dist}
Summary: Various VST/VST3 Plugins from SocaLabs.com
License: BSD-3-Clause
URL:     https://github.com/FigBug/slPlugins

Vendor:       Audinux
Distribution: Audinux

# ./socalab-source.sh <tag>
# ./socalab-source.sh 77b4a8d6bf8da4407fc6de7b9074f68985d33ef8

Source0: slPlugins.tar.gz
Source4: socalab-source.sh

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
# This build uses JUCE-6.1.*
BuildRequires: JUCE
BuildRequires: xorg-x11-server-Xvfb
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

%prep
%autosetup -n slPlugins

%build

%set_build_flags

export CXXFLAGS="-include utility $CXXFLAGS"
export CURRENT_PATH=`pwd`

mkdir -p $CURRENT_PATH/bin/standalone/
mkdir -p $CURRENT_PATH/bin/vst/
mkdir -p $CURRENT_PATH/bin/vst3/

#Projucer --set-global-search-path linux defaultJuceModulePath /usr/src/JUCE/modules

cat ci/pluginlist.txt | while read PLUGIN; do
  PLUGIN=$(echo $PLUGIN|tr -d '\n\r ')

  sed -i -e "s/pluginFormats=\"/pluginFormats=\"buildVST3,/g"       plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e "s/pluginFormats=\"/pluginFormats=\"buildStandalone,/g" plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e 's/buildStandalone="0"/buildStandalone="1"/g'           plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e 's/buildVST3="0"/buildVST3="1"/g'                       plugins/$PLUGIN/$PLUGIN.jucer
  sed -i -e 's/JUCEOPTIONS/JUCEOPTIONS JUCE_JACK="1"/g'             plugins/$PLUGIN/$PLUGIN.jucer

  Projucer --resave plugins/$PLUGIN/$PLUGIN.jucer
  
  cd plugins/$PLUGIN/Builds/LinuxMakefile
  sed -i -e 's/-Wl,--strip-all//g' Makefile
  
  %make_build CONFIG=Release STRIP=true 
  
  cp ./build/$PLUGIN                                     $CURRENT_PATH/bin/standalone/
  cp ./build/$PLUGIN.so                                  $CURRENT_PATH/bin/vst/
  cp ./build/$PLUGIN.vst3/Contents/%{_target}/$PLUGIN.so $CURRENT_PATH/bin/vst3/
  cd ../../../..
done

%install

mkdir -p %{buildroot}%{_bindir}
install bin/standalone/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_libdir}/vst
cp bin/vst/*.so %{buildroot}%{_libdir}/vst/

mkdir -p %{buildroot}%{_libdir}/vst3
cp bin/vst3/*.so %{buildroot}%{_libdir}/vst3/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/

%files -n vst3-%{name}
%{_libdir}/vst3/

%changelog
* Mon May 20 2022 Yann Collette <ycollette.nospam@free.fr> -
- update to 77b4a8d6bf8da4407fc6de7b9074f68985d33ef8

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-5
- fix debug build

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 20200512-1
- Initial release
