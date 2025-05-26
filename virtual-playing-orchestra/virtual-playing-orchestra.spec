# Status: active
# Tag: Presets
# Type: Presets
# Category: Synthesizer

Name: virtual-playing-orchestra
Version: 3.2.4
Release: 1%{?dist}
Summary: Orchestral sample library
License: Freely Available and CC-BY-SA Creative Commons Sampling Plus 1.0 and CC0 and CC-BY-NC and Public Domain
URL: http://virtualplaying.com/virtual-playing-orchestra/

# For a breakdown of the licensing, see http://virtualplaying.com/virtual-playing-orchestra/#licensing
# Sonatina Symphonic Orchestra http://sso.mattiaswestlund.net/
# - Creative Commons Sampling Plus 1.0 license.
# Mattias Westlund additional samples http://mattiaswestlund.net/samples/
# - Creative Commons Attribution-ShareAlike 3.0 Unported license
# No Budget Orchestra https://github.com/ssj71/No-Budget-Orchestra
# - Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
# VSCO 2 Community Edition http://vis.versilstudios.net/vsco-2.html
# - CC0 1.0 Universal (CC0 1.0) Public Domain Dedication License
# University of Iowa Electronic Music http://theremin.music.uiowa.edu/
# - "freely available"
# stamperadam https://freesound.org/people/stamperadam/
# - Creative Commons 0
# Philharmonia Orchestra http://www.philharmonia.co.uk/explore/make_music
# - Creative Commons Attribution-ShareAlike 3.0 Unported License

# E-mail from Paul Battersby - 2020-01-18:
# - The same license that applies to the wav files also applies to the .sfz
#   scripts because they were both originally part of the same source library.

Source0: https://archive.org/download/VirtualPlayingOrchestra31WaveFiles/Virtual-Playing-Orchestra3-1-wave-files.zip
Source1: http://virtualplaying.com/vp-downloads/Virtual-Playing-Orchestra3-2-4-standard-scripts.zip
Source2: http://virtualplaying.com/vp-downloads/Virtual-Playing-Orchestra3-2-4-performance-scripts.zip

BuildArch: noarch

BuildRequires: unzip

Requires: virtual-playing-orchestra-performance-scripts
Requires: virtual-playing-orchestra-standard-scripts
Requires: virtual-playing-orchestra-iowa
Requires: virtual-playing-orchestra-mattiaswestlund
Requires: virtual-playing-orchestra-nbo2
Requires: virtual-playing-orchestra-nbo
Requires: virtual-playing-orchestra-philharmonia
Requires: virtual-playing-orchestra-sso
Requires: virtual-playing-orchestra-stamperadam
Requires: virtual-playing-orchestra-vsco-2-ce

%description
This is a full, free orchestral sample library featuring section and solo
instruments for woodwinds, brass, strings and percussion.

%package iowa
Summary: Iowa sound library
License: Freely Available
URL: http://theremin.music.uiowa.edu/
Requires: virtual-playing-orchestra

%description iowa
University of Iowa Electronic Music sound library.

%package mattiaswestlund
Summary: Mattias Westlund additional samples
# Horns/license.txt
# ViolaSect/readme.txt
License: CC-BY-SA and Public Domain
URL: https://mattiaswestlund.net/samples/
Requires: virtual-playing-orchestra

%description mattiaswestlund
Additional samples from Mattias Westlund.

%package nbo
Summary: NBO sound library
License: CC-BY-SA
URL: https://www.bandshed.net/sounds/sfz/
Requires: virtual-playing-orchestra

%description nbo
No Budget Orchestra sound library.

%package nbo2
Summary: NBO sound library 2
# Violin/SoloViolin/license.txt
# Violin/ViolinSect/license.txt
# Trumpet/license.txt
# Cello/CelloSect/license.txt
License: CC-BY-SA and Creative Commons Sampling Plus 1.0 and CC0 and CC-BY and CC-BY-NC
URL: https://www.bandshed.net/sounds/sfz/
Requires: virtual-playing-orchestra

%description nbo2
No Budget Orchestra 2 sound library.

%package philharmonia
Summary: Philharmonia sound library
# License from the Wayback Machine:
# https://web.archive.org/web/20161206161554/http://www.philharmonia.co.uk/explore/sound_samples/viola
License: CC-BY-SA
URL: https://www.philharmonia.co.uk/explore/make_music
Requires: virtual-playing-orchestra

%description philharmonia
Philharmonia Orchestra sound library.

%package sso
Summary: SSO sound library
License: Creative Commons Sampling Plus 1.0
URL: https://sso.mattiaswestlund.net/
Requires: virtual-playing-orchestra

%description sso
Sonatina Symphonic Orchestra sound library.

%package stamperadam
Summary: Stamperadam sound library
License: CC0
URL: https://freesound.org/people/stamperadam/
Requires: virtual-playing-orchestra

%description stamperadam
Stamperadam sound library.

%package vsco-2-ce
Summary: VSCO 2 CE sound library
License: CC0
URL: https://vis.versilstudios.com/vsco-community.html
Requires: virtual-playing-orchestra

%description vsco-2-ce
Versilian Studios Chamber Orchestra 2 Community Edition sound library.

%package standard-scripts
Summary: Standard Orchestra scripts
Version: 3.2.4
Requires: virtual-playing-orchestra

%description standard-scripts
The Standard Orchestra uses key velocity (how fast you hit a key on your MIDI
controller) to control the volume. Articulations (sustain, staccato etc) are
placed in different tracks or are selected via key switches. Most virtual
instruments work this way.

%package performance-scripts
Summary: Performance Orchestra scripts
Version: 3.2.4
Requires: virtual-playing-orchestra

%description performance-scripts
The Performance Orchestra uses the MOD wheel to control volume. Key velocity
(how fast you hit a key on your MIDI controller) selects the articulation
(sustain, staccato etc) while still slightly affecting the volume. The
performance .sfz file names contain the string "-PERF".

%prep
%autosetup -n Virtual-Playing-Orchestra3
unzip %{SOURCE1} -d standard-scripts
unzip %{SOURCE2} -d performance-scripts

%build

# Merge license files in nbo2
echo "LICENSE nbo2" > libs/NoBudgetOrch2/LICENSE
find libs/NoBudgetOrch2 -name license.txt | while read f; do
  echo -e "\n\nLICENSE $f:" >> libs/NoBudgetOrch2/LICENSE
  cat "$f" >> libs/NoBudgetOrch2/LICENSE
done

%install

install -d %{buildroot}%{_datadir}/soundfonts/%{name}
cp -r libs %{buildroot}%{_datadir}/soundfonts/%{name}/

# Install standard-scripts
cp -r standard-scripts/Virtual-Playing-Orchestra3/. %{buildroot}%{_datadir}/soundfonts/%{name}/

# Install performance-scripts
cp -r performance-scripts/Virtual-Playing-Orchestra3/. %{buildroot}%{_datadir}/soundfonts/%{name}/

rm -rf %{buildroot}%{_datadir}/soundfonts/%{name}/Documentation

%files
%license Documentation/license.htm
%doc Documentation/change-log-Wave-Files.txt
%{_datadir}/soundfonts/%{name}/libs/Other

%files iowa
%license libs/Iowa/license.txt
%{_datadir}/soundfonts/%{name}/libs/Iowa

%files mattiaswestlund
%{_datadir}/soundfonts/%{name}/libs/Mattias-Westlund

%files nbo
%license libs/NoBudgetOrch/license.txt
%{_datadir}/soundfonts/%{name}/libs/NoBudgetOrch

%files nbo2
%license libs/NoBudgetOrch2/LICENSE
%{_datadir}/soundfonts/%{name}/libs/NoBudgetOrch2

%files philharmonia
%license libs/Philharmonia/license.txt
%{_datadir}/soundfonts/%{name}/libs/Philharmonia

%files sso
%doc libs/SSO/Samples/Horn/readme-PB.txt
%{_datadir}/soundfonts/%{name}/libs/SSO

%files stamperadam
%license libs/stamperadam/samples/celesta/_readme_and_license.txt
%{_datadir}/soundfonts/%{name}/libs/stamperadam

%files vsco-2-ce
%license libs/VSCO2-CE/LICENSE.txt
%{_datadir}/soundfonts/%{name}/libs/VSCO2-CE

%files standard-scripts
%license standard-scripts/Virtual-Playing-Orchestra3/Documentation/license.htm
%doc standard-scripts/Virtual-Playing-Orchestra3/Documentation/instrument-list* standard-scripts/Virtual-Playing-Orchestra3/Documentation/change-log-*.txt
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-normal-panned-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-normal-panned-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-KS-C6-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-KS-C6-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-KS-C6-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-KS-C6-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-KS-C2-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-KS-C2-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-accent-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-normal-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-staccato-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-sustain-DXF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Keys/celesta.sfz
%{_datadir}/soundfonts/%{name}/Percussion/bassdrum-snare-cymbals.sfz
%{_datadir}/soundfonts/%{name}/Percussion/bassdrum.sfz
%{_datadir}/soundfonts/%{name}/Percussion/cymbals.sfz
%{_datadir}/soundfonts/%{name}/Percussion/glockenspiel.sfz
%{_datadir}/soundfonts/%{name}/Percussion/misc.sfz
%{_datadir}/soundfonts/%{name}/Percussion/snare.sfz
%{_datadir}/soundfonts/%{name}/Percussion/timpani-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Percussion/timpani-hit-LR.sfz
%{_datadir}/soundfonts/%{name}/Percussion/timpani-hit-n-roll.sfz
%{_datadir}/soundfonts/%{name}/Percussion/timpani-hit.sfz
%{_datadir}/soundfonts/%{name}/Percussion/timpani-roll.sfz
%{_datadir}/soundfonts/%{name}/Percussion/tubular-bells.sfz
%{_datadir}/soundfonts/%{name}/Percussion/vibraphone-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Percussion/vibraphone-auto-damp.sfz
%{_datadir}/soundfonts/%{name}/Percussion/vibraphone-open.sfz
%{_datadir}/soundfonts/%{name}/Percussion/xylophone.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-pizzicato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-tremolo-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-pizzicato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/harp-KS-B7.sfz
%{_datadir}/soundfonts/%{name}/Strings/harp-KS-C0.sfz
%{_datadir}/soundfonts/%{name}/Strings/harp-dampened.sfz
%{_datadir}/soundfonts/%{name}/Strings/harp-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-FEMALE-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-FEMALE-sustain.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MALE-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MALE-sustain.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MIXED-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MIXED-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-accent-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-normal-mod-wheel-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-sustain-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-KS-C1.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-KS-C4.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-sustain.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-accent.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-normal-mod-wheel.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-sustain.sfz

%files performance-scripts
%license standard-scripts/Virtual-Playing-Orchestra3/Documentation/license.htm
%doc standard-scripts/Virtual-Playing-Orchestra3/Documentation/instrument-list* standard-scripts/Virtual-Playing-Orchestra3/Documentation/change-log-*.txt
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/all-brass-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-PERF-KS-A5.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/bass-trombone-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/french-horn-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trombone-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/trumpet-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-PERF-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Brass/tuba-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/1st-violin-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/2nd-violin-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-pizzicato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-tremolo-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF-pizzicato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/all-strings-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-PERF-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/bass-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/cello-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-PERF-tremolo.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-PERF-pizzicato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Strings/viola-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-FEMALE-PERF.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MALE-PERF.sfz
%{_datadir}/soundfonts/%{name}/Vocals/choir-MIXED-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-PERF-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-PERF-staccato-panned.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/all-woodwinds-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/alto-flute-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bass-clarinet-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/bassoon-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/clarinet-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-PERF-KS-C4.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-PERF-KS-C5.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-PERF-KS-C6.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/contrabassoon-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/english-horn-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/flute-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SEC-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/oboe-SOLO-PERF.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-PERF-KS-C2.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-PERF-KS-C3.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-PERF-staccato.sfz
%{_datadir}/soundfonts/%{name}/Woodwinds/piccolo-SOLO-PERF.sfz

%changelog
* Mon May 26 2025 Yann Collette <ycollette.nospam@free.fr> - 3.2.4-1
- update to 3.2.4-1

* Sun Apr  5 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.1-1
- Initial build
