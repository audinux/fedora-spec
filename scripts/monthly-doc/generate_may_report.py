#!/usr/bin/env python3
"""Generate May 2026 monthly report ODT for Audinux Fedora repo."""

from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties, PageLayout, MasterPage
from odf.text import P, H, Span, LineBreak
from odf import dc
import datetime

doc = OpenDocumentText()

# ── Styles ──────────────────────────────────────────────────────────────────

def make_style(name, family, parent=None, tp_kwargs=None, pp_kwargs=None):
    s = Style(name=name, family=family)
    if parent:
        s.setAttribute("parentstylename", parent)
    if tp_kwargs:
        s.addElement(TextProperties(**tp_kwargs))
    if pp_kwargs:
        s.addElement(ParagraphProperties(**pp_kwargs))
    doc.styles.addElement(s)
    return s

make_style("Title", "paragraph",
           tp_kwargs=dict(fontsize="24pt", fontweight="bold", color="#1F497D"),
           pp_kwargs=dict(marginbottom="0.3cm", margintop="0.5cm"))

make_style("Heading1", "paragraph",
           tp_kwargs=dict(fontsize="16pt", fontweight="bold", color="#2E74B5"),
           pp_kwargs=dict(margintop="0.6cm", marginbottom="0.2cm"))

make_style("Heading2", "paragraph",
           tp_kwargs=dict(fontsize="13pt", fontweight="bold", color="#404040"),
           pp_kwargs=dict(margintop="0.4cm", marginbottom="0.15cm"))

make_style("Body", "paragraph",
           tp_kwargs=dict(fontsize="11pt"),
           pp_kwargs=dict(marginbottom="0.15cm"))

make_style("PkgName", "paragraph",
           tp_kwargs=dict(fontsize="12pt", fontweight="bold", color="#1F497D"),
           pp_kwargs=dict(margintop="0.3cm", marginbottom="0.05cm"))

make_style("URL_style", "paragraph",
           tp_kwargs=dict(fontsize="10pt", color="#0563C1"),
           pp_kwargs=dict(marginbottom="0.1cm"))

make_style("Mono", "paragraph",
           tp_kwargs=dict(fontsize="10pt", fontfamily="Courier New"),
           pp_kwargs=dict(marginbottom="0.05cm"))

make_style("UpdateItem", "paragraph",
           tp_kwargs=dict(fontsize="10pt"),
           pp_kwargs=dict(marginleft="0.5cm", marginbottom="0.05cm"))

# ── Helper ───────────────────────────────────────────────────────────────────

def p(text, style="Body"):
    el = P(stylename=style)
    el.addText(text)
    doc.text.addElement(el)

def h(text, level=1):
    style = "Heading1" if level == 1 else "Heading2"
    el = H(outlinelevel=level, stylename=style)
    el.addText(text)
    doc.text.addElement(el)

def pkg_entry(name, summary, url, description):
    p(f"● {name}", style="PkgName")
    p(description, style="Body")
    p(f"URL: {url}", style="URL_style")
    p("")

# ── Document metadata ────────────────────────────────────────────────────────
doc.meta.addElement(dc.Title(text="Audinux — Monthly Report May 2026"))
doc.meta.addElement(dc.Creator(text="Yann Collette"))
doc.meta.addElement(dc.Date(text="2026-06-05"))

# ══════════════════════════════════════════════════════════════════════════════
# Title
# ══════════════════════════════════════════════════════════════════════════════
p("Audinux — Monthly Report", style="Title")
p("May 2026  |  Maintainer: Yann Collette", style="Body")
p("")

# ══════════════════════════════════════════════════════════════════════════════
# 1. Summary
# ══════════════════════════════════════════════════════════════════════════════
h("1. Summary")
p(
    "During May 2026, the Audinux repository saw significant activity: "
    "32 new packages were introduced across standalone applications, LV2/VST3/CLAP plugins, "
    "LADSPA plugins, VCV Rack modules, and system utilities. "
    "In addition, approximately 88 package updates were pushed, covering audio synthesizers, "
    "effects, sequencers, DAW environments, and supporting libraries. "
    "Weekly snapshots of BespokeSynth and LMMS were kept up to date throughout the month."
)
p("")

# ══════════════════════════════════════════════════════════════════════════════
# 2. New Packages
# ══════════════════════════════════════════════════════════════════════════════
h("2. New Packages Added")
p(
    "The following packages were introduced for the first time in the Audinux repository "
    "during May 2026. Each entry includes a short description and the upstream source URL."
)
p("")

# ── 2.1 Standalone Applications & Tools ──────────────────────────────────────
h("2.1  Standalone Applications & Tools", level=2)

pkg_entry(
    "boutronique",
    "Sample extraction desktop tool",
    "https://boutronique.jmfavreau.info",
    "Boutronique is a small desktop utility designed to help musicians identify and "
    "extract short, loopable samples from a loaded sound file. It provides an intuitive "
    "waveform view and simple loop-point editing."
)

pkg_entry(
    "cdp8  (Composer's Desktop Project v8)",
    "Electroacoustic composition suite",
    "https://composersdesktop.com/index.html",
    "The Composer's Desktop Project (CDP) is a well-established suite of over 200 "
    "command-line programs for electroacoustic and computer music composition. "
    "Version 8 introduces new spectral-processing and granular-synthesis tools. "
    "A companion soundthread package provides an experimental graphical front-end."
)

pkg_entry(
    "soundthread",
    "Experimental sound design workstation",
    "https://github.com/j-p-higgins/SoundThread",
    "SoundThread is an experimental graphical workstation oriented towards sound design "
    "and synthesis exploration. It follows an unconventional patching paradigm intended "
    "for creative and live-performance use."
)

pkg_entry(
    "audio-topology-profile",
    "CPU topology-aware audio tuning",
    "https://github.com/audinux/audio-topology-profile",
    "A set of shell scripts and a systemd service that inspect the CPU topology at boot "
    "time and automatically apply PipeWire/JACK IRQ-affinity and scheduling profiles "
    "optimised for real-time audio workloads. Helps reduce xruns on multi-socket or "
    "hybrid-core systems."
)

pkg_entry(
    "qpitch",
    "Free autotune / pitch-correction plugin",
    "https://github.com/skynse/qpitch",
    "QPitch is a free, open-source pitch-correction plugin (VST3/LV2) that implements "
    "a real-time autocorrelation-based pitch detector coupled to a pitch-shifter. "
    "It provides a familiar 'autotune' workflow without proprietary dependencies."
)

# ── 2.2 Guitar / Instrument Plugins ──────────────────────────────────────────
h("2.2  Guitar & Instrument Plugins", level=2)

pkg_entry(
    "dsp4guitar",
    "Multi-effect processor for electric guitar (VST3/LV2)",
    "https://github.com/GizzZmo/DSP4Guitar",
    "DSP4Guitar is an all-in-one multi-effect plugin targeting electric guitar. "
    "It bundles common guitar-processing blocks (overdrive, cabinet simulation, chorus, "
    "delay, reverb) into a single patchable signal chain."
)

pkg_entry(
    "niner",
    "Monophonic analogue kick drum synthesizer (VST3/LV2)",
    "https://github.com/hyperfocusdsp/niner",
    "Niner is a monophonic kick drum synthesizer modelled after analogue circuitry. "
    "It features pitch-envelope, transient shaping, noise layer, and distortion controls, "
    "making it well-suited for electronic music production."
)

pkg_entry(
    "spiro",
    "Semi-modular synthesizer (VST3/LV2)",
    "https://github.com/p-o-l-e/spiro",
    "Spiro is an open-source semi-modular synthesizer plugin. Its architecture "
    "combines a dual-oscillator core with an integrated modulation matrix, built-in "
    "effects, and a patch memory system, aiming for a classic semi-modular workflow "
    "inside a DAW environment."
)

# ── 2.3 Effects & Processing Plugins ─────────────────────────────────────────
h("2.3  Effects & Processing Plugins", level=2)

pkg_entry(
    "nine-strip",
    "Channel-strip plugin based on Airwindows algorithms (VST3/LV2)",
    "https://github.com/blablack/nine-strip",
    "Nine-Strip is a comprehensive mixing channel strip built with the JUCE framework. "
    "It incorporates several well-regarded processing algorithms from the Airwindows "
    "collection — including high-quality EQ, saturation, and console-emulation stages — "
    "into a single, cohesive plugin interface."
)

pkg_entry(
    "spicefx",
    "Analogue-modelling saturation & cabinet simulator (VST3/LV2)",
    "https://github.com/DatanoiseTV/spice-oss",
    "SpiceFX is an analogue-modelling DSP plugin offering a wide palette of saturation "
    "and distortion models (tubes, transformers, tape) combined with cabinet-impulse "
    "simulation. It targets guitar, bass, and mix-bus colouring applications."
)

# ── 2.4 ClassicReverb RE series ───────────────────────────────────────────────
h("2.4  ClassicReverb RE Series (AnClark)", level=2)
p(
    "Three re-engineered implementations of the discontinued Kjaerhus Audio Classic Reverb "
    "were added. Each variant starts from the same open-source base and introduces "
    "different algorithmic enhancements."
)
p("")

pkg_entry(
    "classicreverb-re02",
    "Classic Reverb re-engineering — different timbre (VST3/LV2)",
    "https://github.com/AnClark/ClassicReverb-RE02",
    "RE02 focuses on a different timbre compared to the original, with a reworked "
    "early-reflections model that produces a brighter, more 'airy' spatial character."
)

pkg_entry(
    "classicreverb-re03",
    "Classic Reverb re-engineering — shaping controls (VST3/LV2)",
    "https://github.com/AnClark/ClassicReverb-RE03",
    "RE03 adds spectral shaping controls (pre-delay EQ, high/low damping curves) on top "
    "of the classic reverb tail, giving the user finer control over the reverb colour."
)

pkg_entry(
    "classicreverb-re04",
    "Classic Reverb re-engineering — general enhancements (VST3/LV2)",
    "https://github.com/AnClark/ClassicReverb-RE04",
    "RE04 is a general-purpose enhancement of the original Classic Reverb algorithm, "
    "improving the density and smoothness of the diffuse tail while retaining the "
    "familiar CPU-friendly footprint."
)

# ── 2.5 Nebula Plugin Series ──────────────────────────────────────────────────
h("2.5  Nebula Plugin Series", level=2)
p(
    "Four plugins from the Nebula series were packaged. They share a common branding "
    "and development style, each targeting a specific mixing or processing task."
)
p("")

pkg_entry(
    "nebula-cluster",
    "Distortion / dirt-box effect plugin (VST3/LV2)",
    "https://github.com/subhankardas15071992-cloud/Nebula-Cluster",
    "Nebula Cluster is a free, open-source distortion plugin described as a 'dirt box'. "
    "It provides harmonic saturation and clipping suitable for adding grit and aggression "
    "to synthesizers, drums, and guitars."
)

pkg_entry(
    "nebula-de-esser",
    "High-performance de-esser plugin (VST3/LV2)",
    "https://github.com/subhankardas15071992-cloud/Nebula-De-Esser",
    "Nebula De-Esser is a precision de-essing plugin targeting sibilance removal in "
    "vocal recordings. It uses a dynamic side-chain approach with adjustable frequency "
    "detection and gain-reduction depth."
)

pkg_entry(
    "nebula-delay",
    "Delay effect plugin (VST3/LV2)",
    "https://github.com/subhankardas15071992-cloud/Nebula-Delay",
    "Nebula Delay is a clean, general-purpose stereo delay plugin with tempo-sync, "
    "feedback, and tone-shaping controls."
)

pkg_entry(
    "nebula-stereo-delay",
    "Double-precision stereo delay engine (VST3/LV2)",
    "https://github.com/subhankardas15071992-cloud/Nebula-Stereo-Delay",
    "Nebula Stereo Delay extends the standard delay with a double-precision internal "
    "processing path and independent left/right time and feedback controls, enabling "
    "wide ping-pong and complex polyrhythmic delay patterns."
)

# ── 2.6 LADSPA Plugin Collection ─────────────────────────────────────────────
h("2.6  LADSPA Plugin Collection", level=2)
p(
    "A batch of classic and niche LADSPA plugins was added to expand the repository's "
    "legacy plugin coverage."
)
p("")

pkg_entry(
    "ladspa-bs2b  /  libbs2b",
    "Bauer stereophonic-to-binaural DSP",
    "https://bs2b.sourceforge.net/",
    "The bs2b library and LADSPA plugin implement the Bauer stereophonic-to-binaural "
    "DSP algorithm, which cross-feeds stereo channels to improve headphone listening "
    "comfort and reduce ear fatigue."
)

pkg_entry(
    "ladspa-clipper",
    "Hard-clipping LADSPA plugin",
    "http://quitte.de/dsp/",
    "A minimalist hard clipper LADSPA plugin without aliasing protection. Intended for "
    "deliberate digital saturation and lo-fi distortion effects."
)

pkg_entry(
    "ladspa-foo-plugins",
    "Limiter and dynamics processor LADSPA plugins",
    "http://www.studionumbersix.com/foo/",
    "The 'foo' plugin collection provides a transparent brickwall limiter and a special "
    "dynamics processor targeting broadcast and mastering use cases."
)

pkg_entry(
    "ladspa-lemux",
    "OpenMSX-based LADSPA instrument plugins",
    "http://lumatec.be/joost",
    "lemux is a set of LADSPA instrument plugins that emulate sound chips and synthesis "
    "methods found in openMSX emulated devices, recreating retro computer audio timbres."
)

pkg_entry(
    "ladspa-lgv",
    "Luis Garrido's LADSPA plugin collection",
    "https://sourceforge.net/projects/ladspa-lgv/",
    "A small collection of LADSPA audio-effect plugins by Luis Garrido, including "
    "various filters, modulators, and utility processors."
)

pkg_entry(
    "ladspa-njl",
    "NJL LADSPA plugin",
    "http://users.ecs.soton.ac.uk/njl98r/code/audio/",
    "NJL is a niche LADSPA plugin suite developed at the University of Southampton, "
    "providing signal-processing tools oriented towards academic and experimental audio."
)

pkg_entry(
    "ladspa-trigger",
    "Trigger LADSPA plugin",
    "https://sourceforge.net/projects/ladspa-trigger/",
    "A LADSPA plugin that generates trigger pulses or gate signals from audio transients, "
    "useful for driving MIDI note events or envelope followers from drum tracks."
)

pkg_entry(
    "ladspa-wubflip",
    "WubFlip LADSPA effect plugin",
    "http://www.alexs.org/ladspa/",
    "WubFlip is a creative LADSPA effect plugin that produces bass-modulation and "
    "filter-flip effects commonly associated with dubstep and electronic music styles."
)

# ── 2.7 VCV Rack Module Libraries ─────────────────────────────────────────────
h("2.7  VCV Rack Module Libraries", level=2)
p(
    "Six new VCV Rack v2 module libraries were packaged, expanding the Rack plugin "
    "ecosystem available through Audinux."
)
p("")

pkg_entry(
    "rack-v2-Astravox",
    "Astravox VCV Rack modules",
    "https://github.com/JackArkyDev/Astravox",
    "Astravox provides a set of VCV Rack v2 modules focused on spectral and additive "
    "synthesis techniques."
)

pkg_entry(
    "rack-v2-BCNmodular",
    "BCNmodular VCV Rack modules",
    "https://github.com/santifort-commits/BCNmodular",
    "BCNmodular is a collection of utility and modulation VCV Rack modules developed "
    "in Barcelona, offering LFOs, envelope generators, and signal-routing helpers."
)

pkg_entry(
    "rack-v2-SphericalSoundSocietyFree",
    "Spherical Sound Society free VCV Rack modules",
    "https://github.com/spherical-sound-society/VCV-Free",
    "The free tier of the Spherical Sound Society's VCV Rack library, featuring "
    "granular, spectral, and spatial-audio processing modules."
)

pkg_entry(
    "rack-v2-swv-guitar-tools",
    "SWV guitar tools for VCV Rack",
    "https://github.com/shortwavlabs/vcv-guitar-collection",
    "A collection of VCV Rack modules from Shortwave Labs oriented towards guitar and "
    "string-instrument processing — including pitch detection, chord voicing, and "
    "strumming pattern generators."
)

pkg_entry(
    "rack-v2-VostokInstruments",
    "Vostok Instruments VCV Rack modules",
    "https://github.com/Vostok-Instruments/Vostok_VCVRack",
    "Vostok Instruments offers VCV Rack modules inspired by Soviet-era synthesizer "
    "designs, including oscillators, filters, and sequencers with a distinctive "
    "vintage character."
)

pkg_entry(
    "rack-v2-WaveOfHormuz",
    "Wave of Hormuz VCV Rack modules",
    "https://github.com/quaternionmedia/waveofhormuz",
    "Wave of Hormuz is a set of experimental VCV Rack modules exploring unconventional "
    "signal-processing concepts including quaternion-based modulation and generative "
    "pattern generation."
)

# ══════════════════════════════════════════════════════════════════════════════
# 3. Package Updates
# ══════════════════════════════════════════════════════════════════════════════
h("3. Package Updates")
p(
    "88 individual spec-file updates were committed during May 2026. "
    "The table below lists each updated package together with its latest version "
    "reached during the month."
)
p("")

updates = [
    ("airwindows",          "last master snapshot"),
    ("amplitron",           "0.1.304"),
    ("atlas-06-synthetizer","0.0.1-2"),
    ("bespokesynth",        "weekly snapshot"),
    ("carla",               "updated"),
    ("clap (headers)",      "1.2.8"),
    ("din",                 "64"),
    ("drumgroovepro",       "1.0.0"),
    ("fasttracker2",        "2.19"),
    ("figbug",              "1.1.5"),
    ("freeeq8 (gearbear99)","2.3.0"),
    ("gearmulator",         "2.2.6"),
    ("giada",               "1.4.1"),
    ("hvcc",                "0.16.0"),
    ("infernal-synth",      "2.1.3"),
    ("jack-link",           "0.2.7"),
    ("jamulus",             "3.12.1"),
    ("js80p",               "4.0.2"),
    ("juce",                "8.0.13"),
    ("kernel-audio-tuned",  "1.0-4"),
    ("kernel-lqx",          "6.19.14-lqx1"),
    ("kernel-xanmod",       "6.19.14-xan1"),
    ("guitarmidi-lv2",      "2.1"),
    ("lmms",                "weekly snapshot"),
    ("magda-core",          "0.9.2"),
    ("maolan",              "0.1.0"),
    ("moddevices",          "1.0.4"),
    ("nebula-delay",        "1.2.0"),
    ("nebula-stereo-delay", "1.2.0"),
    ("neuralrack (guitarix)","0.3.3"),
    ("niner",               "0.7.9"),
    ("noise-suppression",   "1.21"),
    ("non-mixer-xt",        "2.0.15"),
    ("noteahead",           "3.1.0"),
    ("openwurli",           "0.5.1"),
    ("polyphone",           "2.6.0"),
    ("rack v2 (various)",   "multiple"),
    ("rakarrack-plus",      "2.0.15"),
    ("redrose",             "0.6.11"),
    ("rerdavies plugins",   "1.2.77"),
    ("rokerpack",           "1.1.0"),
    ("saugns",              "0.5.7b"),
    ("schismtracker",       "20260524 snapshot"),
    ("seq66",               "0.99.24"),
    ("spiro",               "updated"),
    ("splash",              "0.12.2"),
    ("stompbox / stompboxui","0.2.2"),
    ("supercollider",       "3.14.0"),
    ("ultramaster-kr106",   "2.5.13"),
    ("vimix",               "0.9.1"),
    ("vmpc",                "0.9.11"),
    ("yadaw",               "0.8.5"),
    ("zl-equalizer",        "1.2.0"),
]

h("3.1  Updated Package List", level=2)
for name, ver in updates:
    p(f"  • {name:<30s}→  {ver}", style="UpdateItem")

p("")

# ══════════════════════════════════════════════════════════════════════════════
# 4. Other Notable Work
# ══════════════════════════════════════════════════════════════════════════════
h("4. Other Notable Work")

p(
    "Beyond new packages and version bumps, the following infrastructure and maintenance "
    "tasks were completed during May:"
)
p("")
p("  • repo_check.sh updated to track the new boutronique and nine-strip packages.",
  style="UpdateItem")
p("  • Templates improved for more consistent spec-file generation.", style="UpdateItem")
p("  • Git clone strategy adjusted: removed --depth=1 to ensure tags are available "
  "for version detection during builds.", style="UpdateItem")
p("  • atlas-06-synthetizer desktop file corrected and shallow-clone strategy updated.",
  style="UpdateItem")
p("  • cdp8 layout fixes applied to ensure correct file placement after installation.",
  style="UpdateItem")
p("  • aarch64 support removed from a package that lacked upstream cross-compilation "
  "support.", style="UpdateItem")
p("  • Source download scripts fixed for several packages.", style="UpdateItem")
p("  • A README added to clarify repository structure for new contributors.",
  style="UpdateItem")
p("")

# ══════════════════════════════════════════════════════════════════════════════
# Footer
# ══════════════════════════════════════════════════════════════════════════════
p("")
p("─" * 60, style="Body")
p(f"Generated: 2026-06-05  |  Audinux Fedora Repository  |  Maintainer: Yann Collette",
  style="Body")

# ── Save ──────────────────────────────────────────────────────────────────────
out = "/Users/ycollette/repositories/github/fedora-spec/audinux-may2026-report.odt"
doc.save(out)
print(f"Saved: {out}")
