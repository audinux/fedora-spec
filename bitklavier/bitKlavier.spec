#
# spec file for package bitKlavier
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Konstantin Voinov konstantin.voinov@gmail.com
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: bitKlavier
Version: 3.4
Release: 112%{?dist}
Summary: The prepared digital piano
License: GPL-3.0-only
URL: https://github.com/Princeton-CDH/bitKlavier
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Princeton-CDH/bitKlavier/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: Builds.tar.gz
# Source2: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source2: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Patch0: 01-bitKlavier-fix-dirpath.patch
Patch1: 02-bitKlavier-fix-std-max-types.patch

BuildRequires: gcc-c++
BuildRequires: JUCE7
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

Requires: license-%{name}

%description
http://bitklavier.com/

Developed by Dan Trueman and Michael Mulshine.
bitKlavier takes inspiration from John Cage's prepared piano, but instead of screws and
erasers we place a reconfigurable collection of digital machines between the virtual strings of the digital piano.

Manual http://manyarrowsmusic.com/bitKlavier/bitKlavier_Manual.pdf

You also need to download a resource package with samples and galleries:
https://www.dropbox.com/s/tvhad1ecsoycvx6/bK_2.6_installerResources.zip?dl=0

Unzip and put the content of Resources folder to your ~/Documents
it contains:
-- a "galleries" in your Documents folder; galleries saved here will automatically show up in bitKlavier
-- a "music" folder, containing PDFs of sheet music for bitKlavier
-- a "pianos" folder, for individual pianos
-- a "preparations" folder, with subfolders for each preparation type, for individual preparations
-- a "samples" folder with the core piano samples for bitKlavier
-- a "soundfonts" folder; soundfonts placed here will automatically show up in bitKlavier
-- a "doc" folder; the manual and relevant papers are included here

%package -n license-%{name}
Summary: License and documentations for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentations for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
http://bitklavier.com/

Developed by Dan Trueman and Michael Mulshine.
bitKlavier takes inspiration from John Cage's prepared piano, but instead of screws and
erasers we place a reconfigurable collection of digital machines between the virtual strings of the digital piano.

Manual http://manyarrowsmusic.com/bitKlavier/bitKlavier_Manual.pdf

You also need to download a resource package with samples and galleries:
https://www.dropbox.com/s/tvhad1ecsoycvx6/bK_2.6_installerResources.zip?dl=0

Unzip and put the content of Resources folder to your ~/Documents
it contains:
-- a "galleries" in your Documents folder; galleries saved here will automatically show up in bitKlavier
-- a "music" folder, containing PDFs of sheet music for bitKlavier
-- a "pianos" folder, for individual pianos
-- a "preparations" folder, with subfolders for each preparation type, for individual preparations
-- a "samples" folder with the core piano samples for bitKlavier
-- a "soundfonts" folder; soundfonts placed here will automatically show up in bitKlavier
-- a "doc" folder; the manual and relevant papers are included here

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
http://bitklavier.com/

Developed by Dan Trueman and Michael Mulshine.
bitKlavier takes inspiration from John Cage's prepared piano, but instead of screws and
erasers we place a reconfigurable collection of digital machines between the virtual strings of the digital piano.

Manual http://manyarrowsmusic.com/bitKlavier/bitKlavier_Manual.pdf

You also need to download a resource package with samples and galleries:
https://www.dropbox.com/s/tvhad1ecsoycvx6/bK_2.6_installerResources.zip?dl=0

Unzip and put the content of Resources folder to your ~/Documents
it contains:
-- a "galleries" in your Documents folder; galleries saved here will automatically show up in bitKlavier
-- a "music" folder, containing PDFs of sheet music for bitKlavier
-- a "pianos" folder, for individual pianos
-- a "preparations" folder, with subfolders for each preparation type, for individual preparations
-- a "samples" folder with the core piano samples for bitKlavier
-- a "soundfonts" folder; soundfonts placed here will automatically show up in bitKlavier
-- a "doc" folder; the manual and relevant papers are included here

%prep
%autosetup -p1

unzip %{SOURCE2}

cd bk_JUCE/bitKlavier
tar xvfz %{SOURCE1}

%build

%set_build_flags

export LDFLAGS="-z muldefs $MDFLAGS"
export CPPFLAGS="-I`pwd`/VST_SDK/VST2_SDK/"

cd bk_JUCE/bitKlavier

%make_build -C Builds/LinuxMakefile CONFIG=Release

%install

cd bk_JUCE/bitKlavier

install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 -d %{buildroot}/%{_libdir}/vst
install -m 755 -d %{buildroot}/%{_libdir}/vst3

install -m 755 Builds/LinuxMakefile/build/%{name}    %{buildroot}%{_bindir}/
install -m 755 Builds/LinuxMakefile/build/%{name}.so %{buildroot}%{_libdir}/vst/
cp -r Builds/LinuxMakefile/build/*.vst3              %{buildroot}%{_libdir}/vst3/

%files
%{_bindir}/%{name}

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst-%{name}
%{_libdir}/vst/%{name}.so

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Tue Sep 24 2024 Yann Collette <ycollette.nospam@free.fr> - 3.4-1
- first build for audinux

* Sat Oct  7 2023 kv@kott.no-ip.biz
- Update to version 3.4:
  * Update README.md
  * added Cami to authors
  * fixed text resolution display for pedalGainSlider
  * Fix ios and pianoiterator bug
  * Add pedalGain slider to setting
  * new fix from Synchronic holdTime problem
  * fixed bug where holdTime in Snchronic wasn't working
  * merge with pianoIterator
  * Fixed iterator toggle save; moved iterator button to gallery
    dropdown fixed multiple iterator windows bug
  * in PluginProcessor, line 801, i'm not sure why we are avoiding
    piano = 0? it's not loading in bK as expected, when we move back
    to it, so i have removed that in the conditional, which i think
    means that the 'else' will never be reached, but let me know if
    i'm missing something. it seems to be working as expected now
  * fixed iterator boundaries, so it doesn't crash when exceeding
    max # pianos, and wraps around, going forward or backwards
  * Fix up and down crash , Fix pianoIterator window open on change crash
  * add iterator up/down keymap to preset
  * Remoivng submodules
  * REmoving submodule
  * fixed some bugs with galleries loading lite
  * add listener funcionality to send clicks to main view
  * Add saving and loading features
  * fixed bug where the globalSampleType wasn't being set properly. at least i think i fixed it
  * updated createInputStream from deprecated form
  * cleaned up some compiler warnings
  * removed share Facebook stuff, deprecated
  * updated v# to 3.3.6
  * finished implementation of keymap->ignoreNoteOff
  * add back-end stuff for keymap->ignoreNoteOff functionality
  * fixed one more 0 slider
  * fixed bug where gain sliders were showing exponential format 0's
  * fixed bug where Tuning spiral view was updating the offsets of sounding
    pitches before their pitches had actually changed, in non-spring modes
  * Fix tuning increment broken
  * Fix Audio contstants for cTuningfundamentalOffset
  * fixing some of the zero displays in BKSingleSliders
  * mod bug checking
  * updated to 3.3.3
  * Fix reading custom samples
  * updated to v3.2.2
  * Fix preset global soundset
  * Fix preset saving and load for global soundfonts
  * Fix Preferences button
  * Fix gui for ios compressor
  * Fix iOS UI issues
  * Fix TuningView on IOS
  * Add look for sample files in filesearchpaths
  * Fix compilation on labeledSlider
  * Compressor GUI fix for IOS
  * Update README.md
  * Fix soundfont global load
* Sun Mar 26 2023 kv@kott.no-ip.biz
- Update to version 3.3:
  * Remov MTS connection button from tab2 and 3
  * Move MTSMaster button
  * change to v3.0 for release
  * changed dBFS to dB in resonanceViewController, to be consistent with other preps
  * changed to v3.2.9
  * Menu Fix
  * updated XCode project settings
  * updated version to rc2
  * Add Zenodo DOI badge & link
* Mon Jun  6 2022 Konstantin Voinov <kv@kott.no-ip.biz>
- Update to 3.1
- New Features and Changes
  * Resonance "add" and "ring" targeting via Keymap
  * Resonance display of Held and Ringing keys
  * ability to set and Modify static Held keys in Resonance
  * numerous bug fixes and some optimizations to Resonance; it
    should perform better than the initial release
  * Sostenuto pedal support
  * Keymap "toggle" mode; essentially, noteOff messages are ignore,
    so keys become switches
  * Keymap "sostenuto" mode; the sustain pedal behaves like a
    sostenuto pedal
  * Scala tuning format import (SCL and KBM) (big thanks to the
    Surge folks (Tuning Library and Tuning Workbench Synth) for
    their open source library and their assistance getting it
    integrated with bitKlavier)
  * new Mac installer that is notarized, so shouldn't trigger
    "unknown developer" and "damaged" messages
* Wed Sep  8 2021 Konstantin Voinov <kv@kott.no-ip.biz>
- Update to 3.0
  * Resonance preparation
  * Equalizer on mixed output
  * new sample libraries (download separately)
* Sun Jul 25 2021 Konstantin Voinov <kv@kott.no-ip.biz>
- Update to 2.9.0
- New Features and Changes
  * Velocity curves in Keymap
  * Updates to back-end velocity handling
  * Direct-from-Disk sample playback
  * Flexible resource paths for samples folders
  * Ability to open any sample folder with consistently named audio files for playback
- Manual
  * Updated manual for v2.9: bitKlavier_Manual.pdf
- Bug Fixes
  * many bug fixes, and new bugs!
* Sat Jan 30 2021 Konstantin Voinov <kv@kott.no-ip.biz>
- add quick crash fix
* Sat Jan 30 2021 Konstantin Voinov <kv@kott.no-ip.biz>
- Update to v2.8
  * Modification smoothing
  * Modification incrementing
  * Modification alternating
  * Velocity filtering in Direct
  * Blendrónic input gain sliders for Direct, Synchronic, and Nostalgic
  * All gain sliders changed to logarithmic dBFS scaling
- New in v2.7
  * Undo
  * Harmonizer mappings in Keymap
  * “Ignore sustain” option in Keymap
  * “Use as sustain pedal” option in Keymap
- New in v2.8
  * SoundFonts can be assigned to individual preparations
  * Piano and Gallery menus are now sorted alphabetically
  * New “music” folder that includes Mikroetudes, Nostalgic Synchronic, and the new Machines for Listening (by Dan) PDFs now part of the installer
* Sun May 17 2020 Konstantin Voinov <kv@kott.no-ip.biz>
- Initial upload
  * bitKlavier v2.5.2
  New Features and Changes
  - Active preparation highlighting: preparations that are currently active will blink, making it easier to track what is going on in a complex Piano
  - Active keys in selected Keymap will be displayed on main (bottom) keyboard, to make it easier to track prepared keys
  - ToolTips can be turned on/off (they were always on before)
  - Transposition "uses Tuning" option in Direct, Nostalgic, Synchronic; prior to this, transposition values were always interpreted literally, relative to main note; now they can be filtered by whatever Tuning is connected, so that a Tuning system can prevail in an entire preparation without micromanaging transposition values.
  * Bug Fixes
  - many bug fixes, and new bugs!
  - Multislider (in Synchronic and Blendrónic) completely rewritten, should behave much better now, and will also save "gaps" in the slider values now
  - bug fixes that were causing crashes with menus in plugin formats, some SoundFont loading bugs
  - bug fixes with Nostalgic; envelopes for overlapping reverse and undertow notes were not behaving properly, and now do
  - bug fix where Synchronic was not retaining its state across Piano changes
  * Manual
  - Updated manual for v2.5.2: bitKlavier_Manual.pdf http://manyarrowsmusic.com/bitKlavier/bitKlavier_Manual.pdf
  See full changelog: https://github.com/Princeton-CDH/bitKlavier/releases
