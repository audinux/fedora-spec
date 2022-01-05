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
| tascar              | https://github.com/HoerTech-gGmbH/tascar/ |
| midieditor          | https://github.com/markusschwenk/midieditor/ |
| seq66               | https://github.com/ahlstromcj/seq66 |
| drops               | https://github.com/clearly-broken-software/drops |
| audiveris           | https://github.com/Audiveris/audiveris.git |
| Teragon audio       | http://teragonaudio.com/software.html |
|                     | - Kickmaker: http://static.teragonaudio.com/downloads/KickMaker/KickMaker.zip |
|                     | - BeatCounter: https://github.com/teragonaudio/BeatCounter/archive/refs/tags/2.1.tar.gz |
|                     | - ExtraNotes: http://static.teragonaudio.com/downloads/ExtraNotes/ExtraNotes.zip |
|                     | - HiLoFilter: http://static.teragonaudio.com/downloads/HiLoFilter/HiLoFilter.zip |
|                     | - NotNotchFilter: http://static.teragonaudio.com/downloads/NotNotchFilter/NotNotchFilter.zip |
|                     | - ChaosChimp: http://static.teragonaudio.com/downloads/ChaosChimp/ChaosChimp.zip |
|                     | - MrsWatson: http://static.teragonaudio.com/downloads/MrsWatson/MrsWatson.zip |
|                     | - all: https://launchpad.net/~kxstudio-debian/+archive/ubuntu/plugins/+sourcefiles/teragonaudio-plugins/5:20140325.3/teragonaudio-plugins_20140325.3.tar.gz |
| ProM                | https://github.com/DISTRHO/ProM |
| Cardinal            | https://github.com/DISTRHO/Cardinal |
| loop192             | https://github.com/jean-emmanuel/loop192 |
| fat1.lv2            | https://github.com/x42/fat1.lv2 |
| loopor              | https://github.com/stevie67/loopor |
| flute.lv2           | https://github.com/timowest/flute-lv2 |
| lv2file             | https://github.com/jeremysalwen/lv2file |
| harmonizer.lv2      | https://github.com/dsheeler/harmonizer.lv2 |
| inscore             | https://inscore.grame.fr |
| Gwion               | https://github.com/Gwion |
| Amati               | https://github.com/glocq/Amati |
| Pure language       | https://agraef.github.io/pure-lang |
| Freeze              | https://github.com/taylordotfish/freeze |
| Aether              | https://github.com/Dougal-s/Aethe |
| Delay Architect     | https://github.com/jpcima/DelayArchitect |
| HISE                | https://github.com/christophhart/HISE.git |
| ORCHESTOOLS-PIANO-S | https://github.com/ilirbajri/ORCHESTOOLS-PIANO-S |
| CollisionDrive      | https://github.com/brummer10/CollisionDrive |
| QuatumVerb          | https://github.com/QVbDev/quantumVerb |
| Gammou              | https://github.com/aliefhooghe/Gammou |
| Livecode-This       | https://github.com/gilfuser/livecode-this |
| SpleeterRT          | https://github.com/james34602/SpleeterRT |
| Spek                | https://github.com/alexkay/spek |
| sndpeek             | https://www.gewang.com/software/sndpeek |
| fmit                | https://github.com/gillesdegottex/fmit |
| Mousai              | https://github.com/SeaDve/Mousai |
| audioprism          | https://github.com/vsergeev/audioprism |
| friture             | https://github.com/tlecomte/friture |
| reMID.lv2           | https://github.com/ssj71/reMID.lv2 |
| MiniGBS             | https://github.com/baines/MiniGBS |
| protrekkr           | https://github.com/hitchhikr/protrekkr |
| monique-monosynth   | https://github.com/surge-synthesizer/monique-monosynth |
| mclk.lv2            | https://github.com/x42/mclk.lv2 |
| Schrammel_OJD       | https://github.com/JanosGit/Schrammel_OJD |
| EasySSP             | https://github.com/automatl/audio-dsp-multi-visualize/ |

## Cleanup
Remove mv-6pm or 6pm. Both are normally the same package

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

## Fix debug generation:

| Package                        | Comment |
|--------------------------------|---------|
| purr-data/purr-data.spec       | has a pure binary dependency |
| improviz/improviz.spec         | (Cabal ...) |
| processing/processing.spec     | precompiled java package -> noarch ... |
| ams-lv2/lvtk.spec              | static library |
| picoloop/picoloop.spec         | complex ... |
| orca/orca.spec                 | really special build system |
| zrythm/ztoolkit                | it's a static library ... |
| zrythm/zrythm                  | embedded glibc problem |
| ossia/ossia-score.spec         | don't build anymore. Wait for next release |

## Tag list:

### Tag:

Analyzer, Compressor, Emulator, Delay, Drum, Jack, Alsa
Editor, Legacy, Live, Effect, Gate, Graphic, Guitar, Amp Simul
Delay, Overdrive, Cabinet, Equalizer, Convolution, Octaver
MIDI, Tablature, Phaser, Tape, Tracker, Reverb
Sfz, Sf2, Sf3, Monitoring, Video, Organ, PM, Sequencer
Keyboard, Library, Live, OSC, Mixer, Modular, Rack, Sampler, Session

### Type:

Devel, IDE, Language, DSSI, LV2, LADSPA, Standalone, VST, VST3, Presets, Rack, Language

### Category:

Audio, DAW, Effect, Synthesizer, MIDI, Programming, Sampler, Sequencer
Graphic, Tool, Session Mngmt

## ZITA:

zita-avc1-0.1.0.tar.bz2
zita-jclient-0.4.2.tar.bz2
zita-audiotools-1.0.0.tar.bz2
zita-jacktools-1.5.3.tar.bz2        Requires zita-jclient, zita-convolver and zita-audiotools
g2reverb-0.7.1.tar.bz2
hoafilt.tar.bz2

## Add desktop files

dgedit
drumgizmo
sfizz
horgand
improviz
juce
cadence
carla

## Add *.sh files

## To be fixed:

None

## regular update

Stopped at mammut
