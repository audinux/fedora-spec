## Add new packages

| Package             | URL|
|---------------------|----|
| osmid               | https://github.com/llloret/osmid |
| Squeezer            | https://github.com/mzuther/Squeezer |
| DAFx19-Gamelanizer  | https://github.com/lukemcraig/DAFx19-Gamelanizer |
| OwlSim              | https://github.com/pingdynasty/OwlSim |
| DeLooper            | https://github.com/sonejostudios/DeLooper |
| morphex             | https://github.com/MarcSM/morphex |
| mephisto            | https://open-music-kontrollers.ch/lv2/mephisto/ |
| zrythm - lsp-dsp    | add a devel package for zrythm |
| emissioncontrol2    | https://github.com/EmissionControl2/EmissionControl2 |
| regrader            | https://github.com/igorski/regrader |
| mapmap              | https://github.com/mapmapteam/mapmap |
| openshow            | https://github.com/mapmapteam/openshow |
| supercollider-study | https://github.com/rumblesan/super-collider-study |
| marsyas             | http://marsyas.info/ |
| vapoursynth         | http://www.vapoursynth.com/ |
|                     | https://github.com/dubhater/vapoursynth-fluxsmooth |
|			          | https://github.com/HolyWu/L-SMASH-Works |
|			 	      | https://github.com/dubhater/vapoursynth-mvtools |
|					  | https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Deblock |
| frequanalizer       | https://github.com/ffAudio/Frequalizer |
| NoiseTorch          | https://github.com/lawl/NoiseTorch |
| CadMus              | https://github.com/josh-richardson/cadmus |
| tangamp             | https://github.com/sadko4u/tamgamp.lv2 |
| tascar              | https://github.com/HoerTech-gGmbH/tascar/ |
| midieditor          | https://github.com/markusschwenk/midieditor/ |
| seq66               | https://github.com/ahlstromcj/seq66 |
| drops               | https://github.com/clearly-broken-software/drops |
| audiveris           | https://github.com/Audiveris/audiveris.git |
| Teragon audio       | http://teragonaudio.com/software.html |
|                     | - Kickmaker: http://static.teragonaudio.com/downloads/KickMaker/KickMaker.zip
|                     | - BeatCounter: http://static.teragonaudio.com/downloads/BeatCounter/BeatCounter.zip
|                     | - ExtraNotes: http://static.teragonaudio.com/downloads/ExtraNotes/ExtraNotes.zip
|                     | - HiLoFilter: http://static.teragonaudio.com/downloads/HiLoFilter/HiLoFilter.zip
|                     | - NotNotchFilter: http://static.teragonaudio.com/downloads/NotNotchFilter/NotNotchFilter.zip
|                     | - ChaosChimp: http://static.teragonaudio.com/downloads/ChaosChimp/ChaosChimp.zip
|                     | - MrsWatson: http://static.teragonaudio.com/downloads/MrsWatson/MrsWatson.zip

## Cleanup
Remove mv-6pm or 6pm. Both are normally the same package

## Todo for 34
- Socalab -> /usr/bin/ld: /usr/lib64/libglib-2.0.so.0: error adding symbols: DSO missing from command line
- error: 'numeric_limits' is not a member of 'std'
- kmidimon: needs drumstick-devel
- glava: <artificial>:(.text+0x1005): undefined reference to `glfwGetX11Window'
- ecasound: python3 missing

## Add source.sh file in spec file:
Source1: source.sh

## Add check section:
```
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*%{name}.*.xml
```

## Add distribution information
Vendor:       Audinux
Distribution: Audinux

## Check before packaging:
remove -march=native from Makefiles if it's present

## lvtk
fix pkgconfig file installation

## Fix debug generation:

| Package                        | Comment |
|--------------------------------|---------|
| purr-data/purr-data.spec       | has a pure binary dependency |
| improviz/improviz.spec         | (Cabal ...) |
| processing/processing.spec     | precompiled java package -> noarch ... |
| ams-lv2/lvtk.spec              | static library |
| psi-plugins                    | error with fedora 33 + lv2-devel |
| picoloop/picoloop.spec         | complex ... |
| orca/orca.spec                 | really special build system |
| performer/performer.spec       | ui_setlist.h missing - cmake 3.18 pb probably |
| socallab/SocaLabs-plugins.spec | build fails because of a default juce path / maybe use juce 5.4 ... |
| surge/stochas.spec             | jucaid compilation pb - maybe due tu %set_build_flags ... |
| zrythm/ztoolkit                | it's a static library ... |
| ossia/ossia-score.spec         | don't build anymore. Wait for next release |

## Fedora 33 - To be fixed:
performer -> cmake + ui_setlist.h missing - pb cmake 3.18 ...

Tag list:

Tag:

Analyzer, Compressor, Emulator, Delay, Analyzer, Drum, Jack, Alsa
Editor, Legacy, Live, Effect, Gate, Graphic, Guitar, Amp Simul
Delay, Overdrive, Cabinet, Equalizer, Convolution, Octaver
MIDI, Tablature, Phaser, Tape, Tracker, Analyzer, Reverb
Sfz, Sf2, Sf3, Monitoring, Video, Organ, PM, Sequencer
Keyboard, Library, Live, OSC, Mixer, Modular, Rack, Sampler, Session

Type:

Devel, IDE, Language, DSSI, LV2, LADSPA, Standalone, VST, VST3, Presets, Rack, Language

Category:

Audio, DAW, Effect, Synthesizer, MIDI, Programming, Sampler, Sequencer
Graphic, Tool, Session Mngmt

ZITA:

zita-avc1-0.1.0.tar.bz2
zita-jclient-0.4.2.tar.bz2
zita-audiotools-1.0.0.tar.bz2
zita-jacktools-1.5.3.tar.bz2        Requires zita-jclient, zita-convolver and zita-audiotools
g2reverb-0.7.1.tar.bz2
hoafilt.tar.bz2

