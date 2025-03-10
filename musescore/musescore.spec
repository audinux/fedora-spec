# Status: active
# Tag: Editor, Tablature, Jack, Alsa, MIDI
# Type: Standalone
# Category: DAW, Sequencer, Tool

#
# spec file for package musescore
#
# Copyright (c) 2023 SUSE LLC
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

%define _lto_cflags %{nil}

# Internal QML imports
%global __requires_exclude qmlimport\\((MuseScore|FileIO).*

%define rname          mscore
%define version_lesser 4.4
%define revision       12112024
%define docdir         %{_docdir}/%{name}
%define fontdir        %{_datadir}/fonts/%{name}

Name: mscore-mao
Version: 4.4.4
Release: 3%{?dist}
Summary: A WYSIWYG music score typesetter

# Licenses in MuseScore are a mess. To help other maintainers I give the following overview:
# Musescore code license is GPL-3.0 with font exception (see LICENSE.rtf in top dir)
# although some files mention GPL-2.0, probably for historical reasons
# Software in thirdparty is licensed under their own license
# thirdparty/beatroot: GPL 2.0 or later
# thirdparty/dr_libs: Public Domain OR MIT no attribution
# thirdparty/dtl: BSD
# thirdparty/flac: BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.2-only
# thirdparty/fluidsytn: LGPL-2.1
# thirdparty/freetype): FTL (we use system freetype)
# thirdparty/google_crashpad_client: Apache 2.0 (we don't build with this)
# thirdparty/googletest: BSD 3
# thirdparty/invaltree: MIT
# thirdparty/kddockwidgets: GPL-2.0-only OR GPL-3.0-only
# thirdparty/lame: LGPL 2
# thirdparty/opus and opusenc: BSD 3
# thirdparty/rtf2html: LGPL-2.1
# thirdparty/stb: MIT
# the soundfont we musescore uses (see below) is BSD 3
License: Apache-2.0 AND BSD-3-Clause AND FTL AND GPL-2.0-only AND SUSE-GPL-3.0-with-font-exception AND GPL-2.0-or-later AND GFDL-1.2-only AND LGPL-2.0-only AND LGPL-2.1-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL: https://musescore.org
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/musescore/MuseScore/archive/v%{version}/MuseScore-%{version}.tar.gz

# MuseScore expect to be able to download the latest version of its soundfonts
# They are downloaded from the link conteinde in CMakeLists.text
# They are newer versions than the one included in the MuseScore tarball itself
Source1: https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Changelog.md
Source2: https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_License.md
Source3: https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General_Readme.md
Source4: https://ftp.osuosl.org/pub/musescore/soundfont/MuseScore_General/MuseScore_General.sf3

# VST3
# Usage: ./vst3-source.sh <TAG>
#        ./vst3-source.sh v3.7.11_build_10
Source5: vst3sdk.tar.gz
Source6: vst3-source.sh

# For mime types
Source7: %{name}.xml

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: chrpath
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtnetworkauth-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qt5compat-devel
BuildRequires: qt6-qtscxml-devel
BuildRequires: harfbuzz-devel
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pulseaudio-libs-devel
BuildRequires: libogg-devel
BuildRequires: portaudio-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: ffmpeg-devel
BuildRequires: portmidi-devel
BuildRequires: fdupes
BuildRequires: steinberg-bravura-fonts-all
BuildRequires: steinberg-petaluma-fonts-all
BuildRequires: desktop-file-utils

Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols2
Requires: ( alsa-plugins-pulse if pulseaudio )
Requires: ( pipewire-alsa      if pipewire )
# For crashpad binary
# Requires: openssl1.1
Requires: gnu-free-sans-fonts
Requires: gnu-free-serif-fonts
Requires: steinberg-bravura-fonts-all
Requires: steinberg-petaluma-fonts-all
Requires: hicolor-icon-theme

%description
MuseScore is a graphical music typesetter. It allows for note entry on a
virtual note sheet. It has an integrated sequencer for immediate playing of the
score. MuseScore can import and export MusicXml and standard MIDI files.

%prep
%autosetup -n MuseScore-%{version}

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} share/sound/

# fix EOL encoding
sed 's/\r$//' fonts/bravura/OFL-FAQ.txt > tmpfile
touch -r fonts/bravura/OFL-FAQ.txt tmpfile
mv -f tmpfile fonts/bravura/OFL-FAQ.txt

sed 's/\r$//' thirdparty/rtf2html/README > tmpfile
touch -r thirdparty/rtf2html/README tmpfile
mv -f tmpfile thirdparty/rtf2html/README

sed 's/\r$//' thirdparty/rtf2html/README.ru > tmpfile
touch -r thirdparty/rtf2html/README.ru tmpfile
mv -f tmpfile thirdparty/rtf2html/README.ru

# Install VST3 files
tar xvfz %{SOURCE5}

%build

# TODO:
# find out what those do:
# BUILD_VIDEOEXPORT_MODULE:BOOL=ON -> requires ffmpeg-5 ...
# Fedora ships ffmpeg-6 via ffmpeg-devel and ffmpeg-4 via compat-ffmpeg4-devel
# Setting path to crashpad_handler: MUE_CRASHPAD_HANDLER_PATH
# fvar-tracking-assignments -> disable for link

CURRENT_PATH=`pwd`

%set_build_flags
 
%cmake \
       -DMUE_BUILD_UNIT_TESTS:BOOL=OFF \
       -DMUE_BUILD_CRASHPAD_CLIENT:BOOL=OFF \
       -DMUE_BUILD_VST_MODULE:BOOL=ON \
       -DMUE_BUILD_VIDEOEXPORT_MODULE:BOOL=OFF \
       -DMUE_BUILD_UPDATE_MODULE:BOOL=OFF \
       -DMUE_ENABLE_AUDIO_JACK:BOOL=ON \
       -DMUSE_COMPILE_USE_PCH:BOOL=OFF \
       -DMUSESCORE_BUILD_MODE=release \
       -DMUSESCORE_BUILD_NUMBER=1 \
       -DMUSESCORE_REVISION=%{revision} \
       -DVST3_SDK_PATH:PATH=$CURRENT_PATH/vst3sdk \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DX86_MAY_HAVE_SSE:BOOL=ON \
       -DX86_MAY_HAVE_SSE2:BOOL=ON \
       -DX86_MAY_HAVE_SSE4_1:BOOL=OFF \
       -DX86_MAY_HAVE_AVX:BOOL=OFF \
       -DOPUS_X86_PRESUME_SSE:BOOL=ON \
       -DOPUS_X86_PRESUME_SSE2:BOOL=ON

%cmake_build

%install

%cmake_install

# don't package kddockwidgets. It should not be installed
rm %{buildroot}/%{_libdir}/*.a

# unique names for font docs
mv fonts/edwin/README.md        fonts/edwin/README.md.edwin
mv fonts/edwin/LICENSE.txt      fonts/edwin/LICENSE.txt.edwin
mv fonts/leland/README.md       fonts/leland/README.md.leland
mv fonts/leland/LICENSE.txt     fonts/leland/LICENSE.txt.leland
mv fonts/finalebroadway/OFL.txt fonts/finalebroadway/OFL.txt.finalebroadway
mv fonts/finalemaestro/OFL.txt  fonts/finalemaestro/OFL.txt.finalemaestro

# also package additional demos
mkdir -p %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos
install -p -m 644 demos/*.mscz %{buildroot}%{_datadir}/%{rname}-%{version_lesser}/demos

# Remove opus devel files, they are provided by system
rm -rf %{buildroot}%{_includedir}/opus
rm -rf %{buildroot}%{_includedir}/gmock
rm -rf %{buildroot}%{_includedir}/gtest
rm -rf %{buildroot}%{_includedir}/kddockwidgets-qt6
rm -rf %{buildroot}%{_libdir}/cmake/GTest
rm -rf %{buildroot}%{_libdir}/cmake/KDDockWidgets-qt6
rm -rf %{buildroot}%{_libdir}/cmake/Opus
rm -rf %{buildroot}%{_libdir}/pkgconfig/gmock.pc
rm -rf %{buildroot}%{_libdir}/pkgconfig/gmock_main.pc
rm -rf %{buildroot}%{_libdir}/pkgconfig/gtest.pc
rm -rf %{buildroot}%{_libdir}/pkgconfig/gtest_main.pc
rm -rf %{buildroot}%{_libdir}/pkgconfig/opus.pc

# Delete crashpad binary
rm -f %{buildroot}%{_bindir}/crashpad_handler

# collect doc files
install -d -m 755 %{buildroot}/%{docdir}
install -p -m 644 thirdparty/beatroot/COPYING        %{buildroot}/%{docdir}/COPYING.beatroot
install -p -m 644 thirdparty/beatroot/README.txt     %{buildroot}/%{docdir}/README.txt.beatroot
install -p -m 644 thirdparty/dtl/COPYING             %{buildroot}/%{docdir}/COPYING.BSD.dtl
install -p -m 644 thirdparty/intervaltree/README     %{buildroot}/%{docdir}/README.intervaltree
install -p -m 644 thirdparty/rtf2html/ChangeLog      %{buildroot}/%{docdir}/ChangeLog.rtf2html
install -p -m 644 thirdparty/rtf2html/COPYING.LESSER %{buildroot}/%{docdir}/COPYING.LESSER.rtf2html
install -p -m 644 thirdparty/rtf2html/README         %{buildroot}/%{docdir}/README.rtf2html
install -p -m 644 thirdparty/rtf2html/README.mscore  %{buildroot}/%{docdir}/README.mscore.rtf2html
install -p -m 644 thirdparty/rtf2html/README.ru      %{buildroot}/%{docdir}/README.ru.rtf2html

install -p -m 644 tools/bww2mxml/COPYING             %{buildroot}/%{docdir}/COPYING.bww2mxml
install -p -m 644 tools/bww2mxml/README              %{buildroot}/%{docdir}/README.bww2mxml
install -p -m 644 share/sound/README.md              %{buildroot}/%{docdir}/README.md.sound
install -p -m 644 share/instruments/README.md        %{buildroot}/%{docdir}/README.md.instruments
install -p -m 644 share/wallpapers/COPYRIGHT         %{buildroot}/%{docdir}/COPYING.wallpaper

# Mime type
mkdir -p %{buildroot}%{_datadir}mime/packages
install -p -m 644 %{SOURCE7} %{buildroot}%{_datadir}/mime/packages/

# Install desktop file
desktop-file-install \
   --dir=%{buildroot}%{_datadir}/applications \
   --add-category="X-Notation" \
   --remove-category="Sequencer" \
   --remove-category="AudioVideoEditing" \
   --add-mime-type="audio/midi" \
   --add-mime-type="application/xml" \
   --set-key="Exec" --set-value='env XDG_CURRENT_DESKTOP="" KDE_FULL_SESSION="" DESKTOP_SESSION="" GDK_BACKEND=x11 mscore %F' \
   %{buildroot}%{_datadir}/applications/org.musescore.MuseScore.desktop

# Remove rpath in mscore
chrpath --delete %{buildroot}/%{_bindir}/mscore

%fdupes %{buildroot}/%{_prefix}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.musescore.MuseScore.desktop

%files
%doc %{docdir}/*
%license LICENSE.txt
%{_bindir}/%{rname}
%{_datadir}/metainfo/org.musescore.MuseScore.appdata.xml
%{_datadir}/applications/org.musescore.MuseScore.desktop
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%dir %{_datadir}/%{rname}-%{version_lesser}
%{_datadir}/%{rname}-%{version_lesser}/*
%{_mandir}/man1/*

%doc fonts/README.md
%doc fonts/bravura/bravura-text.md
%doc fonts/bravura/OFL-FAQ.txt
%doc fonts/bravura/OFL.txt
%doc fonts/gootville/readme.txt
%license fonts/campania/LICENSE
# see section 'unique names for font docs' above
%doc fonts/edwin/README.md.edwin
%license fonts/edwin/LICENSE.txt.edwin
%doc fonts/leland/README.md.leland
%license fonts/leland/LICENSE.txt.leland
%license fonts/finalebroadway/OFL.txt.finalebroadway
%license fonts/finalemaestro/OFL.txt.finalemaestro

%changelog
* Wed Dec 11 2024 Yann Collette <ycollette.nospam@free.fr> - 4.4.4-3
- update to 4.4.4-3
* Thu Oct 24 2024 Yann Collette <ycollette.nospam@free.fr> - 4.4.3-3
- update to 4.4.3-3
* Mon Sep 16 2024 Yann Collette <ycollette.nospam@free.fr> - 4.4.2-3
- update to 4.4.2-3
* Sun Sep 08 2024 Yann Collette <ycollette.nospam@free.fr> - 4.4.1-3
- update to 4.4.1-3
* Tue Aug 27 2024 Yann Collette <ycollette.nospam@free.fr> - 4.4.0-3
- update to 4.4.0-3
* Wed Jul 10 2024 Yann Collette <ycollette.nospam@free.fr> - 4.3.2-3
- update to 4.3.2-3
* Mon May 06 2024 Yann Collette <ycollette.nospam@free.fr> - 4.3.0-3
- update to 4.3.0-3 - remove -Wp,-D_GLIBCXX_ASSERTIONS during build
* Thu May 02 2024 Yann Collette <ycollette.nospam@free.fr> - 4.3.0-2
- update to 4.3.0-2
* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 4.2.1-2
- update to 4.2.1-2
* Mon Dec 18 2023 Yann Collette <ycollette.nospam@free.fr> - 4.2.0-2
- update to 4.2.0-2
* Thu Aug 03 2023 Yann Collette <ycollette.nospam@free.fr> - 4.1.1-2
- update to 4.1.1-2 - fix build
* Tue Aug 01 2023 Yann Collette <ycollette.nospam@free.fr> - 4.1.1-1
- update to 4.1.1-1
* Tue Aug 01 2023 Yann Collette <ycollette.nospam@free.fr> - 4.0.2-1
- update to 4.0.2-1 for Fedora Audinux
* Fri Apr 28 2023 Cor Blom <cornelis@solcon.nl>
- Add fix-for-latest-qt-declarative.patch to fix boo#1210932
* Thu Mar 16 2023 Michael Vetter <mvetter@suse.com>
- Update to 4.0.2:
  * Score corruption fixes
  - Multiple issues causing score corruption have been fixed
  - Part scores are now scanned for corruptions
  - There is now a more comprehensive system for alerting you
    when there are corruptions identified on your score (including
    a mechanism to help you avoid saving those corruptions)
  * Usability improvements
  - The Properties panel has been improved so it's possible to edit
    the visibility, colour and play settings of individual notes within chords
  - Toggling visibility of notes within chords now produces more predictable results
  - Images in frames can now be deleted
  - Parts can now be reset to their original layout
  - The UI is now easier to interact with when the user is holding the mouse unsteadily
  - The audio export process can now be cancelled
  - There's a new feature to save relevant diagnostic files (making it
    easier to get support from MuseScore developers)
  * Performance enhancements
  - Major improvements to how MuseScore handles with WASAPI (Benefits Windows users)
  * Bugs squashed and regressions repaired
  - Various crashes have been fixed (including numerous VST-related crashes)
  - Zoom controls in the status bar are easier to use and more intuitive
  - Various problems with the visual behaviour of the app on second monitors are now resolved
  - Text line spacing option has been reinstated in Properties
  - Some playback problems have been resolved, including when entering tablature
    notation, and when changing the tempo using the tempo slider
  - Multiple other minor bug fixes
  * A ton of engraving fixes and improvements
  - Multiple fixes to system-line objects
  - Several errors arising from setting notes to cue size are resolved
  - Fixes to the behaviour of system objects
  - Various fixes to the behaviour of stems
  - Voices now align correctly in 'full' tab staves
  - Sticking in percussion music no longer breaks slurs
  - Slurs now show correctly in parts when only some voices are displayed
  - Cross-page glissando lines have been finessed
  - Various collisions have been resolved (clefs and key signatures, accidentals and cross-staff beams)
- Add musescore-4.0.2-return.patch: to make the compiler happy
* Sat Mar 11 2023 Cor Blom <cornelis@solcon.nl>
- More licenses found, also include licenses for sources we don't
  build. The license line also applies to the SRPMs
* Wed Mar  8 2023 Cor Blom <cornelis@solcon.nl>
- Update Licenses
* Thu Mar  2 2023 Christophe Marin <christophe@krop.fr>
- Don't package the KDDockWidgets development files. It's only
  a third party library that cannot be used for anything.
- Update build constraints
- Spec cleanup
* Mon Jan 16 2023 Michael Vetter <mvetter@suse.com>
- Update to 4.0.1:
  * Fixed a crash on startup with specific VST instruments present
  * Fixed a crash on deleting particular staves
  * Fixed a hang on startup involving WASAPI
  * Fixed corruption on adding or removing beats or measures in certain cases
  * Fixed shortcuts using numeric keypad
  * Fixed issues involving system elements and parts
  * Fixed issues with playback start position
  * Fixed chord symbol playback on transposing staves
* Sun Jan  1 2023 Marcus Rueckert <mrueckert@suse.de>
- Fix audio playback support in muse score
  https://github.com/musescore/MuseScore/issues/11220#issuecomment-1365822403
  - Fix jack finder by backporting 0dde64eef84.patch:
    Though the jack code in Musescore seems to be unused and only
    alsa seems supported
  - Require alsa-plugins-pulse or pipewire-alsa to make playing out
    of the box
- prepare disabling the update check but it is currently not
  possible due to
  https://github.com/musescore/MuseScore/issues/15617
- cmake searches for ogg support: add proper BR
* Thu Dec 29 2022 Hans-Peter Jansen <hpj@urpla.net>
- Switch to RelWithDebInfo build
- Fix Leap build issue (missing -ldl)
- Add README.SUSE and referring notes
- Add 8 GB disk contraints
* Sat Dec 17 2022 Cor Blom <cornelis@solcon.nl>
- Do not build crashpad and remove the prebuilt crashpad binary
* Fri Dec 16 2022 Cor Blom <cornelis@solcon.nl>
- Remove explicit opus-devel require
* Fri Dec 16 2022 Cor Blom <cornelis@solcon.nl>
- Add Qt5QuickTemplate2 to BuildRequires
- Remove opus devel files and add requires to system files
* Thu Dec 15 2022 Cor Blom <cornelis@solcon.nl>
- Update to 4.0:
  Changes in interface, graving, soundsystem, mixer, everything
  See https://musescore.org/nl/node/337788
- Removed unused patches:
  * no-webview-in-startcentre.patch
  * use-system-qtwebengine-files.patch
* Sat Aug 27 2022 Cor Blom <cornelis@solcon.nl>
- Add soundfont and related files that cmake tries to
  download during build (MuseScore_General_Changelog.md,
  MuseScore_General_License.md, MuseScore_General_Readme.md,
  MuseScore_General.sf3) which contain newer versions of the
  MuseScore soundfont
* Tue Apr 27 2021 Cor Blom <cornelis@solcon.nl>
- Explicit cmake flag -DBUILD_WEBENGINE="OFF" is needed to build
  without qtwebengine
* Sun Apr 25 2021 Cor Blom <cornelis@solcon.nl>
- Do not build with qtwebengine on ppc64 and ppc64le
* Sun Apr 25 2021 Cor Blom <cornelis@solcon.nl>
- Change the GenericName in the desktop file to something that is
  really generic: Music score typesetter
* Sat Apr 24 2021 Cor Blom <cornelis@solcon.nl>
- Add no-webview-in-startcentre.patch to prevent that webview is
  used in startcentre (boo#1181604)
* Tue Feb  9 2021 Fabian Vogt <fabian@ritter-vogt.de>
- Add compatibility with qml-autoreqprov
* Tue Feb  9 2021 Dura-Kovács <balping314@gmail.com>
- Updated to 3.6.2
  * Fixed an issue with gap between staff and final barline with
    courtesy clef
  * Fixed an issue when removing spanners from measures
    outside of the rewrite range
  * Fixed an accessibility issue with the score migration dialog
  * Fixed a crash related to QtWebEngineProcess after update
  * Fixed an issue with timeline showing part name rather than
    instrument name
  * Fixed an issue with focus of dockable windows when visibility
    is toggled
  * Fixed an issue where custom gliss text reverts to default "gliss"
  * Added missing Flügelhorns to instrument ordering definitions
  * Fixed an issue where beams cannot be connected over quarter rests
  * Fixed an issue where staff spacers do not work on last
    system of page
  * Fixed an issue with broken swapping of notes/chords with
    Shift + Left/Right
  * Fixed an issue with incomplete import from ScoreScan XML file
  * Fixed an issue with unsaved default settings to pre-3.6 score
    after 'reset styles to default'
  * Fixed an issue with Banjo fifth string fret numbers
  * Fixed an issue where invisible breath marks impact layout
  * Fixed a crash during the opening of a score with a missing
    section break
  * Applying tremolo is now a toggle operation
  * Fixed an issue where the Mixer panel is not fully shown when opened
  * Fixed an issue where an empty rehearsal mark is not deleted
    after entering a system break
  * Fixed an issue where multi-measure rest numbers can collide
    with other elements
  * Fixed an issue where deleting a breath/caesura leads
    to the wrong note being selected
  * Fixed an issue when parts inherit non-default style from score
  * Fixed a crash when changing time signature at the beginning
    of a corrupted measure
  * Fixed an issue with unreadable chord symbols
  * Updated the close icon for Import Midi Panel (and Find/GoTo)
  * Fixed an issue with auto-sizing of vertical frames when dragging
    the height handle
* Fri Jan 29 2021 Balázs Dura-Kovács <balping314@gmail.com>
- Updated to 3.6.1
  * Fixed a crash on open of a file with start repeat in
    continuous view
  * Fixed an issue when switching tabs when opening a score while
    "Score migration dialog" is open
  * Fixed crashes when rearranging instrument positions and changing
    Ordering
  * Fixed an issue where the window is marked as modified, even when
    the last score is closed
  * Fixed a crash when opening scores with large orchestration
    created in older versions of MuseScore
  * Fixed an issue with incorrect order of Violins in
    Orchestra template
  * Fixed a crash when hiding palettes
  * Fixed an export failure when part name contains a slash
  * Fixed an issue where spacers do not function when vertical
    justification is enabled
  * Added an option to Copy SMuFL Symbol Code for symbols in
    Master Palette
  * Clef changes are no longer visible on hidden staves
  * Fixed an issue where first system indentation can cause
    measures to not fit on system
  * Fixed an issue with wrong key signatures upon
    "Reset Al Styles" in concert pitch scores
  * Display symbols' SMuFL name in Symbols Palette
  * Removed corner radius from new default rehearsal mark style
  * Fixed an issue where custom style defaults are ignored when
    creating new score from template
  * Fixed an issue where applying a key change to a selection causes
    a crash when transposing instruments are involved
  * Fixed an issue where an incomplete voice in local time signature
    leads to corruption upon import
  * Fixed an issue where swapping notes in a two-note tremolo causes
    corrupted tremolo, and crash
  * Fixed an issue where two-note tremolos display incorrectly
    on a stave with custom scale
  * Fixed an issue where measure number offset changes on reload
  * It is now possible to copy/paste the LetRing, PalmMute and
    Vibrato elements
  * The link on "Score migration dialog" now leads to Bilibili
    if using Chinese
- Removed enable-build-with-qt5.15 patch as building with
  QT 5.15 is now enabled by upstream
* Tue Jan 19 2021 Cor Blom <cornelis@solcon.nl>
- From Balázs Dura-Kovács:
- removed fonts/gootville/readme.txt executable bit fix, as it was
  fixed in upstream
- install new fonts, most of them are otf
- included additional third party licenses and readme files
- added MUSESCORE_REVISION and MUSESCORE_BUILD_CONFIG flags,
  so that Musescore wouldn't think it's a dev build
- tested on Tumbleweed with Qt 5.15.2. Couldn't reproduce issues
  with with palettes and migration window described here:
  https://github.com/musescore/MuseScore/pull/7119
* Fri Jan 15 2021 Cor Blom <cornelis@solcon.nl>
- Update to 3.6
  * Added the new default notation fonts "Leland"
  * Added the new default text font "Edwin"
  * Added a new dialog that suggests trying out the new engraving
    defaults
  * Added automatic score ordering and bracketing
  * Added automatic vertical justification of staves
  * Added Mountain Dulcimer instrument and 3-string tab presets
  * Added portamento for FLUID synthesiser
  * Added Petaluma notation font
  * Added mnemonics for "Save", "Save As" and "Resource Manager"
  * And other improvements and bugfixes, for details see:
    https://github.com/musescore/MuseScore/releases/tag/v3.6
- Remove correct-revision.patch
- Add enable-build-with-qt515.patch to enable build with Qt 5.15
* Sat Oct 17 2020 Cor Blom <cornelis@solcon.nl>
- Update to 3.5.2:
  * Fixed an unexpected page stretching in "Edit style" dialog
  * Fixed an issue with audio export on Windows, previously
    exporting to .FLAC or .OGG could result in an empty file that
    cannot be played
  * Fixed an issue of harmony playback preferences. Previously, the
    real value of "Chord symbol playback" was not taken into
    account until the first toggle of this setting
  * Fixed a potential crash that could occur when resizing the
    Piano Roll
* Wed Oct  7 2020 Cor Blom <cornelis@solcon.nl>
- Update to 3.5.1:
  * Bugfix release
    For details see
    https://github.com/musescore/MuseScore/releases/tag/v3.5.1
- Update use-qtmake-qt5.patch
* Wed Aug 19 2020 Cor Blom <cornelis@solcon.nl>
- Update to 3.5:
  * New features:
  - Option available in Preferences for playback of chord symbols
  - Mid-staff instrument changes now do almost everything
    automatically
  - Support for Orca (Linux) screenreader
  - Hairpins, voltas, and other lines now adapt anchor points
    when dragged
  - Splash screen displays progress messages while loading MuseScore
  - Diatonic pitch up/down (keep degree alterations) shortcuts
  - Select Similar Elements: Same Beat
  - New Score Wizard now automatically numbers instruments
  - Property for beam style of tremolo (all strokes attached to
    stem)
  - Style for hiding brackets which span to a single staff when
    empty staves are hidden
  - Properties and styles for measure number positioning, including
    cantered and below staff
  - Property and style for position of multimeasure rest numbers
  - Property for fretboard diagram rotation
  * Improvements and fixes.
    For details see :
    https://github.com/musescore/MuseScore/releases/tag/v3.5
- update correct-revision.patch
* Mon Apr 27 2020 Bernhard Wiedemann <bwiedemann@suse.com>
- Normalize timestamps in .workspace zip files
  to make package build reproducible (boo#1047218)
* Fri Feb  7 2020 Cor Blom <cornelis@solcon.nl>
- Update to 3.4.2:
  * Telemetry dialog was not accessible for visually impaired people
  * Drum input palette worked incorrectly due to the changes
    involving single click behaviour
  * MuseScore crashed when pressing numbers/letters in a different
    voice when inputting tabs
  * Hidden pedal items were no longer displayed
  * "L" letter could not be typed when entering text
- Remove 0001-fix-299654-Crash-on-startup-with-Qt-5.14.patch (part
  of tarball now)
- update correct-revision.patch
* Tue Jan 28 2020 Christophe Giboudeaux <christophe@krop.fr>
- Update to 3.4.1. Changes since 3.3.4:
  * MuseScore crashed after closing a menu bar pop-up window
    if no score is opened
  * Audio glitches on note input and playback happened on
    macOS and other platforms
  * Parts corruption happened on timewise delete of individual beats
  * Crash happened when undoing "Beam middle" setting on a single note
  * Pedal lines alignment applied to the whole system, not individual
    staff
  * "Don't play trill" option silenced the note playback
  * Slurs on small staves were displaced in some cases
  * Barline handles were drawn incorrectly after dragging one
  * Strings in the Part dialogue were ambiguous
  * Y Offset value of fretboards didn't restore after undoing
    the values being changed from Edit Mode
  * Replacing a note with an accidental left the accidental
    on the new note
  * Adding Intervals (above/below) didn't take into consideration
    the accidental toggle state
  * Multiple chord symbols attached to same note didn't copy as
    part of the range
  * Strings in fret diagrams without "X" or "O" displayed as "?" on Linux
  * MuseScore crashed when changing a triplet's rest's duration
  * Images attached to rests weren't imported from MuseScore 2
  * Tremolo Bar dialog had multiple UX issues
  * AppImage: system printers weren't available in the print dialog
- Check https://musescore.org/fr/handbook/developers-handbook/release-notes
  for the complete list of changes.
- Update correct-revision.patch
- Update use-system-qtwebengine-files.patch
- Add upstream patch 0001-fix-299654-Crash-on-startup-with-Qt-5.14.patch
* Wed Dec  4 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.3.4:
  Fixes:
  * Palette names were scrambled and nearly impossible to read
    (Windows 7)
  * Scale of palette was incorrect for high and low DPI displays
  * Courtesy accidentals disappeared after an octave change using
    Ctrl(Cmd)+Up/Down
  * Crash reports could not be sent
- Updated correct-revision.patch
* Tue Nov 26 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.3.3:
  Improvements:
  * Tie button behaves as a toggle now
  * Enable changing notes duration if selecting note stem, hook or
    a range
  * Visual improvements for palettes
  * Mark notes that are out of instrument range with red or yellow
    color even when they are selected
  * Save Online is now fully synchronised with the musescore.com
    upload page
  Fixes
  * Export Pdf on Mac with Muse Jazz Text was garbled and
    unreadable if no printers were setup on a machine
  * Entering notes with mouse failed in Italian TAB
  * Scoreview jumped back to start of score during note input on
    (auto)save
  * Sticking could not be copy-pasted
  * Extensions could not be installed on macOS Catalina
- Update correct-revision.patch
* Fri Nov 15 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.3.2:
  * "Save online" failed in some cases
- Add patches to make qtwebengine work: use-qtmake-qt5.patch and
  use-system-qtwebengine-files.patch
* Wed Nov 13 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.3.1:
  * MuseScore crashed on startup in some cases on Windows 7
  * Palettes were incorrectly placed when using multiple HighDPI
    monitors and scaling
  * Palettes disappeared on Ubuntu 18.04 in some cases
- Update correct-revision.patch
- Remove line from spec to remove rtf2html binary: it is no longer
  part of the source tarball
* Tue Nov  5 2019 Cor Blom <cornelis@solcon.nl>
- -DCMAKE_BUILD_TYPE=RELEASE need to be set explicitly
  (boo#1155809)
- Convert BuildRequires to pkgconfig style and updated them according
  to recommendations of upstream. It solves a couple of cmake errors
- Added reminder to look into qtwebengine support, which is not
  essential but nice to have. Enabling it gives a build error
* Mon Nov  4 2019 Cor Blom <cornelis@solcon.nl>
- Add libqt5-qtgraphicaleffects and libqt5-qtquickcontrols2 as
  requires (boo#1155704)
* Thu Oct 31 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.3.0:
  This is a major update with new functions. For details see the
  announcement: https://musescore.org/en/3.3
- Update correct-revision.patch to latest revision number
* Thu Jul 11 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.2.3:
  * Articulations didn't play properly in MDL instruments
  * Tuplets layout was broken in some cases
  * Fingering jumped unpredictably in some cases
  * Switching between workspaces erased the enabled plugins
  * Bugfixes. For details see https://musescore.org/en/3.2.3
- update correct-revision.patch
* Sun Jun 30 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.2.2:
  + Most important improvements:
  * Sticking (the process of assigning certain notes to either our
    left or right hand) as a new command
  * Make basic colors of the application including voice colors consistent
  * 7/8 time signature was added to advanced workspace and master
    palette
  * Avoid poor alignment of hairpins to dynamics bound to the segment
    before hairpin start
  * Add style settings allowing MDL templates to follow basic drum
    line notation rules better
  * Double/triple-clicking in a text editing mode now selects a
    word/paragraph respectively
  + Also numerous fixes, for details see github release page:
  * https://github.com/musescore/MuseScore/releases
- Update correct-revision.patch
* Fri Jun  7 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.1.0:
  New:
  * Single-note dynamics playback - long notes can play dynamic changes
  * Updated soundfont that supports single-note dynamics out of the box
  * High quality soundfont with better strings and synth instruments
    available as an extension in the Resource Manager
  * Option to completely disable Auto Placement
  * Elements can cross staves still participating in Auto Placement
  * Half-time/Double-time feature that shortens and lengthens rhythms
    on copy-pasting
  * Linearization feature that unrolls all repeats
  * Internal computational approach that allows creating 256th, 512th,
    1024th notes and any kind of compound tuplets
  * Online documentation for Plugin API is available
  Further:
  * Several improvements and a number of bugfixes
- Update correct-revision.patch
* Fri Mar 15 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.0.5:
  Improvements:
  * The whole chord sounds when iterating over notes with left-right
    arrows
  * Support more properties for fingering
  * Add more properties for Plugin API
  * Optimise New Score Wizard start time and layout calculations
  Fixes:
  * MuseScore 3.0.4 crashed on startup on macOS
  * Score margins and related staves positioning were calculated
    incorrectly
  * Spacers worked incorrectly when interacting with page borders
  * Measure counting was wrong when setting a custom offset value
  * Keyboard navigation in Single Page view worked incorrectly
  * MuseScore crashed on finishing work on Windows
  * MuseScore crashed when changing Time Signature in parts
  * MuseScore crashed when selecting a bracket in edit mode
* Fri Mar  1 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.0.4:
  Fixes:
  * All instruments played as piano in some specific cases
  * "Save online" login screen didn't work on Mac
  * Removing section break crashed the editor in some cases
  * Copying measure repeats didn't work
  * Brass Quartet and Brass Quintet templates couldn't be opened
- Update to 3.0.3:
  New
  * New crash report facility (this is disabled in our build for now)
  Improvements
  * Whole score playback can be turned on when in the Part tab
    using the mixer. Part playback works by default in in the Part tab
  * Improved global performance
  * Drag-and-drop user experience is improved
  Fixes
  * Caesuras and sections breaks didn't cause pauses in playback
  * Some properties were not properly saved
  * Fermatas over barlines could not be added
  * Articulations could not be added to grace notes
  * Redundant key/time signatures appeared in Page/Continuous view
    and Parts
  * Visibility was not properly applied
  * Ties failed to be copied-pasted in a score with parts
  * Keyboard navigation in Continuous View was broken
- Updated correct-revision.patch to reflect new version
* Fri Feb 15 2019 cornelis@solcon.nl
- Update to 3.0.2:
  * Improvements
    + Reworked login screen when using Save Online allows signing in via
    Facebook and Google and creating an account from within the editor
    + New easy fingering input mode and other fingering improvements
  * Fixes
    + Plugins framework didn't work
    + Grace notes displayed the wrong size in TAB staves
    + Default window size was too large on a multi-monitor setup
    + Color was not available as a text style setting, including issues with
    coloring lyrics for different voices
    + Slurs were not exported properly to MusicXML
    + Tempo text was not imported properly from MusicXML
- Updated correct-revision.patch
* Sat Jan 19 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.0.1:
  * Improvements
    + Redesign of New Score Wizard makes it easier to search
    templates, provides better score previews, and significantly
    improves accessibility for blind users
    + Reworked Mixer UI allows minimizing and making it dockable
    + Better automatic placement of hairpins and dynamics
    + Better import of 2.X scores
  * Fixes
    + Properties were not saved properly in a number of cases
    + Layout was broken after operations with measure rests and
    tuplets
    + Time signatures appeared incorrectly in some cases and might
    lead to crash
    + Using the implode tool on notes connected with slurs led to
    crashes
    + Editing a barline was applied incorrectly
    + Context menu on instrument names didn't appear
    + Pages with landscape orientation were cropped when printing
    + Playback went crazy on saving
    + Tempo was applied incorrectly in certain cases involving
    fermatas
    + Slurs were lost or detached in some cases
    + Autoplacement couldn't be switched off for stems and arpeggio
- Added correct-revision.patch: revision number in the source
  tarballs on github is wrong
* Fri Jan  4 2019 Cor Blom <cornelis@solcon.nl>
- Update to 3.0.0: A major feature release:
  * Musical notation
    + Automatic placement - potential collisions between elements
    are detected and resolved automatically, allowing you to easily
    create great-looking scores with little need for manual adjustment
    + Improved parts facility - link parts to specific voices within
    a staff
    + System dividers - automatically generate dividers between
    systems
    + Staff type changes - change staff size, number of lines, and
    other properties mid-score
    + Temporary and cutaway staves - staves may appear and disappear
    as needed, including the ability to have empty measures be
    completely invisible
    + MuseJazz font - give all elements in your scores a handwritten
    appearance
    + Named noteheads - automatically display pitch names in
    noteheads using a variety of different naming schemes
  * Usability
    + Tours - get online help automatically as you need it
    + Timeline - navigate using a graphical overview of the music
    structure of your score that shows rehearsal marks, changes of
    tempo, key, and time signature, etc.
    + Score comparison tool - easily view differences between
    versions of a score
    + Single page mode - vertically scrolling view of your score
    + Improved Inspector - control more element properties and set
    style defaults directly from the Inspector window, including new
    above/below placement settings
    + Palette search - enter a search term to quickly find any
    symbol
    + Timewise note input and editing - insert and deletes notes and
    rests within measures, automatically shifting subsequent music
    forwards or backwards
    + Next/previous element - Alt+Right/Left shortcuts to navigate
    through each element of your score
    + Auto-update - no longer necessary to download and install new
    versions from musescore.org
  * Playback
    + Improved Mixer - mute individual voices, collapse channels
    into a single column, assign MIDI ports and channels
    + Improved Piano Roll Editor - easier control of the playback
    parameters of each note in your score
    + Redesigned Play Panel - docked within main window
- Removed no longer necessary remove_diff_match_patch.diff: the library
  is replaced and removed because of a conflict in licensing.
- Removed now included fix-build-qt512.patch
* Thu Dec 27 2018 Cor Blom <cornelis@solcon.nl>
- Add fix-build-qt512.patch to fix build with Qt 5.12
* Mon Oct  1 2018 cornelis@solcon.nl
- Add remove_diff_match_patch.diff to solve license conflict: it
  removes the Apache licensed diff_patch_match library.
* Mon Sep 17 2018 Jan Engelhardt <jengelh@inai.de>
- Trim bias from description. Do not run fdupes over
  the default partition boundaries.
* Fri Sep 14 2018 Cor Blom <cornelis@solcon.nl>
- Cleaned up spec file a bit.
* Wed Aug  8 2018 dliw@posteo.net
- Update to 2.3.2
  * Release 2.3.2
    Released 31 July 2018
    For a complete description of what has changed for 2.3.2
    see https://musescore.org/en/handbook/developers-handbook/release-notes/release-notes-musescore-232
* Mon Jul 30 2018 dliw@posteo.net
- Update to 2.3.1
  * Release 2.3.1
    Released 6 July 2018
    For a complete description of what has changed for 2.3.1
    see https://musescore.org/en/handbook/developers-handbook/release-notes/release-notes-musescore-231
  * Release 2.3.0
    Released 29 June 2018
    For a complete description of what has changed for 2.3.0
    see https://musescore.org/en/handbook/developers-handbook/release-notes/release-notes-musescore-23
- Remove patch musescore-fix-include.patch (no longer needed)
* Sat Jun  9 2018 dliw@posteo.net
- Update to 2.2.1
  * Release 2.2.1
    Released 3 April 2018
    For a complete description of what has changed for 2.2.1
    see https://musescore.org/en/handbook/developers-handbook/release-notes/release-notes-musescore-221
  * Release 2.2.0
    Released 27 March 2018
    For a complete description of what has changed for 2.2.0
    see https://musescore.org/en/handbook/developers-handbook/release-notes/release-notes-musescore-22
  * Release 2.1.0
    Released 2 May 2017
    For a complete description of what has changed for 2.1.0
    see https://musescore.org/en/developers-handbook/release-notes/release-notes-musescore-2.1
  * Release 2.0.3
    Released 6 April 2017
    For a complete description of what has changed for 2.0.3
    see https://musescore.org/en/developers-handbook/release-notes/release-notes-musescore-2.0.3
- Clean up spec file
- Obsolete musescore-doc
- Fix build with Qt >= 5.11
  new patch musescore-fix-include.patch (from upstream)
* Fri Nov 13 2015 cornelis@solcon.nl
- add make-lame-optional.diff (backport from upstream) so that we
  can build without lame
- lowered Qt requires to 5.3.0 (as CMakefilelist has it)
* Tue Sep  1 2015 wbauer@tmo.at
- fix package dependencies (boo#943985)
* Tue Jul 21 2015 cgardner@suse.com
- Version 2.0.2, released July 2015.
* Wed Mar 25 2015 cgardner@suse.com
- Update to consistently require Qt5 (5.4.2) for all distros from this repo
  to reduce problems with mismatched Qt libraries preventing mscore from loading
* Mon Mar 23 2015 cgardner@suse.com
- Version 2.0, released 23 March 2014.  See
  http://musescore.org/en/node/50996
  This is the first major release of MuseScore since version 1.3
* Sun Oct 27 2013 schoett@gmx.de
- Install mime data file mscore.xml.
* Wed Feb 27 2013 cgardner@suse.com
- Version 1.3, released 27 Feb 2013.  See
  http://musescore.org/en/developers-handbook/release-notes/release-notes-musescore-1.3
  This release has a very limited number of bug fixes over 1.2.
* Thu Mar 15 2012 cgardner@suse.com
- Added /etc/modules-load.d/musescore.conf to load snd-seq on openSUSE 12+
* Tue Mar 13 2012 cgardner@suse.com
- Version 1.2, released 13 March 2012.  See
  http://musescore.org/en/developers-handbook/release-notes/release-notes-musescore-1.2
  As usual, a few new features and many bugfixes.
* Thu Jul 28 2011 cgardner@suse.com
- Version 1.1, released 27 July 2011.  See
  http://musescore.org/en/developers-handbook/release-notes-musescore-1.1
  Many new features, and more than 60 bugs fixed.
* Thu May 26 2011 cgardner@suse.de
- Fixed compiler problem introduced by gcc 4.6
* Tue Feb  8 2011 cgardner@novell.com
- Removed lilypond from BuildRequires.  It's clearly not needed.
  Thanks to Nicolas Froment for pointing this out.
* Mon Feb  7 2011 cgardner@novell.com
- First major release, version 1.0.  See http://musescore.org/en/node/9020
  Several new features, scores of bug fixes.
* Tue Oct  5 2010 cgardner@novell.com
- update to version 0.9.6.3, with the following bug fixes:
  * fix #6775: Seg. fault by double clicking any element twice
  * fix #7233: Transpose by diminished second doesn't work (0.9.6 branch regression)
  * fix #7232: D.S. after coda sign freezes playback
  * fix #7167: Time signature change causes triplets to corrupt score
  * fix #7211: Copy/Paste notes over rest of diff. durations in staves
  * fix #7142: Crescendo & delete measures problems
  * fix #7197: MuseScore fails to open MSCZ files with capitals
  * fix #6932: Changing notehead of a breve crash
  * fix #7077: Applying double-note tremolo to dotted notes fails and alter measure duration
  * fix #6937: Measure Properties should be modal dialog
  * fix #6888: When exchanging voice, voice 1 is removed
  * fix get keysig from plugin when concert pitch mode is set
  * fix #6735: C# for AltoSax in default soundfont is silent
  * add access to DPI and notehead, note boundingbox and note position from plugin framework
  * fix #7150: Changing soundfont does not work for audio export
* Tue Sep 14 2010 cgardner@novell.com
- update to version 0.9.6.2, with the following bug fixes:
  15.aug (la)
  * fix #6658: Natural in every keysig on mac PPC
  * fix #6508: Crash removing instrument with volta
  * fix #6706: Crash when inserting slurs from palette while editing text
  * fix #6740: Autosave works only the first time
  10.aug (ws)
  * fix repeat command (ctrl+r) for staves > 1
  6.aug (ws)
  * attempt to fix font problem (quarternote looks too big in text)
  5.aug (la)
  * fix #6479: Crash when closing score during playback
  * fix #6505: Mixer is not refreshed when scores are switched
  4.aug (la)
  * fix #6597: Close/reload crash on XP
  * fix #6624: Crash when deleting a tuplet from a MusicXML import
  * fix cursor move on repeatmeasure in plugin framework
  * fix instrument name containing flats for plugin framework
  14.jul (ws)
  * fix mouse wheel handling for mixer elements
* Thu Jul  8 2010 cgardner@novell.com
- update to version 0.9.6
  "branched" to multimedia project.
* Thu Nov 26 2009 lars@linux-schulserver.de
- update to version 0.9.5
* Wed Nov 19 2008 lars@linux-schulserver.de
- build for openSUSE-Education
- fix some failures detected by rpmlint
* Sat Oct 25 2008 jvrdld <jvrdld@opensuse.org>
- updated to version 0.9.3
* Sat Feb  9 2008 Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.9.1
* Mon Jul 30 2007 Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.6.1
  * This is a bugfix release fixing the midi import crash and adding
  some small usability enhancements.
* Sat Jul 28 2007 Carlos Goncalves <cgoncalves@opensuse.org>
- initial package
