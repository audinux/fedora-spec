# Status: active
# Tag: Effect, Compressor, Delay, Overdrive, Reverb
# Type: Plugin, Standalone, VST3, CLAP
# Category: Audio, Effect

%global commit0 eac485b0be09725f41b5baeef5139015c24ae38c

Name: unplugged
Version: 0.0.1
Release: 1%{?dist}
Summary: A collection of VST plugins
License: AGPLv3-or-later
URL: https://github.com/unplugred/vsst
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/unplugred/vsts/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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

Requires: license-%{name}

%description
A collection of VST plugins:

- Everything Bundle: Think of the savings!
  grammy winning producers dont want you to know this simple trick!
  get the paid versions of all of my plugins at a funny price.
  also saves u a few clicks as u can bulk download everything.
- Prisma: Modular multiband distortion plugin.
  multiband distortion plugin for advanced tone shaping.
  up to four modules can be added to any one of the four bands.
  as of writing, there are 21 modules available to choose from.
  in the right hands the plugin can produce highly complex and intricate tones.
  common usecases include very harsh distortions being applied on a narrow band
  to create more subtle effects,
  and bass recordings being distorted on the higher frequencies without hurting
  the low end.
  also included is a single band version called prismon.
- CRMBL: Delay for insane people.
  a highly versitile delay plugin with a large feature-set,
  which in the right hands can produce highly textural results.
  among the features are pitch shifting on the feedback, asymetric ping pong,
  reverse delay, and more...
  the parameters are highly automatable and can produce a dub delay effect when
  automating the time parameter.
- ModMan: Adds movement.
  modulation effect that produces organic and ever changing randomized movements,
  based on a perlin noise algorithm.
  allows modulating a tape drift, low pass and its resonance, saturation, and amplitude.
  with this effect you can add movement to a pad, widen the stereo field, create
  a tape style effect, or experiment with bizzare settings to create interesting textures.
  its cool!
- SunBurnt: Multi-curve reverb delay.
  unique reverb plugin whose characteristics you can draw in the form of a curve.
  for example, you can have a reverse reverb with an oscillating lowpass, with a
  tail that starts panned left and ends up panned right.
  or, you could have a reverb with a tail that goes wub wub wub wub and the end of
  the tail is pitched up an octave.
  hold ctrl while dragging the length knob to sync to bpm.
  more chaotic and textural results can be achieved by reducing the density parameter,
  and the plugin can enter multi-tap delay mode by turning the density knob all the way down.
  due to the plugin's extensive use of convolution, it is somewhat cpu heavy.
  if youre experiencing problems, try increasing the buffer size!
- PNCH: Knob that makes ur stuff tight.
  a type of effect that causes added harmonics as well as a gating effect.
  compared to typical gates and expanders, this one does not use an envelope follower
  for the gating effect, resulting in gating without pumping
  the added harmonics might not be noticeable or even pleasant on an already dirty signal
  such as a guitar.
  as a result, this makes it great for applications such as removing humming on a direct
  guitar signal before applying heavy distortion.
  also sounds great on drum loops and results in a very choppy effect.
  APPLY BEFORE DISTORTION FOR IDEAL EFFECT.
- Magic Carpet: Three delays feedbacking into the atmosphere.
  three delay lines with a shared feedback path, makes a delay that starts sparse but
  continues to get denser with each feedback.
  the result is a very full-sounding delay with not a lot of gaps.
  can also be used to create noise by enabling noise mode via the right click menu,
  which raises the feedback to unstable levels (loud)  
- Diet Audio: Spectral gate.
  a spectral gate plugin with a unique sound, very good at separating transient
  information from the rest of the audio.
  two copies of the plugin can be used in order to process transients differently
  than the rest, for example by distorting only the transients.
  the plugin can also produce unique artifacts when used in fast release mode, which
  resemble mp3 compression.
- Red Bass: Low-end enchancer excellent for kicks and speech.
  sub oscillator sidechained to incoming signal.
  put a drum loop or a kick thats lacking some oompth in there and the result will be
  instantly thick.
  apply with caution if not in a proper mixing environment.
- Scope: Cool oscilloscope.
  a neat oscilloscope with a skewmorphic design inspired by the electron beam scopes
  of the past.
  included inside are:
  - advanced sync algorithm that produces stable waves
  - waveform mode in addition to stereo-field xy panorama mode
  - adjustable colors and customizability
- MPaint: A sampler from a popular video game.
  this one is a reproduction of a sampler present in a music making feature that was
  in a video game thats near and dear to my childhood.
  this plugin attempts to preserve the unique voice limitations of the original sampler,
  and the samples were recorded with a high quality reproduction of the soundcard of
  the originating console, preserving the unique artefacts of the digital to analog
  conversion of the original chip.
- Pisstortion: Advanced sinefold distortion plugin.
  a better attempt at achieving what plastic funeral tried to achieve.
  harsh and metallic fold distortion with a lot of controls and an innovative stereo
  widening algorithm.
  guarenteed to destroy any mix.
- VU: VU meter for your VU metering needs.
  very simple and to the point vu meter. has:
  - stereo and mono modes
  - scalable ui
  - adjustable rise and decay speed
  - adjustable nominal operation level (NoL)
  - peak indicator
- Plastic Funeral: Distortion that sounds like a laser beam.
  forget about warmth.
  this refreshing take on fold distortion gives off a harsh and metallic sound that is
  guaranteed to destroy any mix.
  this plugin has been mostly replaced by pisstortion.
- ClickBox: Randomized click generator.
  generates randomized digital clicks
  made after people complained i fixed the annoying clicking issue in my first vst,
  plastic funeral (why??)
  not useful for much but i made it so might as well put it out there.
  winner of the britpop awards plugin of the decade ????

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: AGPLv3-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: AGPLv3-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n license-%{name}
Summary: License and documentation for %{name}
License: AGPLv3-or-later

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n vsts-%{commit0}

sed -i -e "s/PRODUCT_NAME \"Red Bass\"/PRODUCT_NAME \"Red_Bass\"/g" plugins/redbass/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Plastic Funeral\"/PRODUCT_NAME \"Plastic_Funeral\"/g" plugins/plasticfuneral/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Magic Carpet\"/PRODUCT_NAME \"Magic_Carpet\"/g" plugins/magiccarpet/CMakeLists.txt
sed -i -e "s/PRODUCT_NAME \"Diet Audio\"/PRODUCT_NAME \"Diet_Audio\"/g" plugins/dietaudio/CMakeLists.txt

%build

%cmake
%cmake_build

%install

PLUGIN_LIST="plugins/crmbl/CRMBL_artefacts
plugins/prisma/prisma/Prisma_artefacts
plugins/prisma/prismon/Prismon_artefacts
plugins/pisstortion/Pisstortion_artefacts
plugins/modman/ModMan_artefacts
plugins/mpaint/MPaint_artefacts
plugins/redbass/RedBass_artefacts
plugins/plasticfuneral/PlasticFuneral_artefacts
plugins/sunburnt/SunBurnt_artefacts
plugins/vu/VU_artefacts
plugins/scope/Scope_artefacts
plugins/magiccarpet/MagicCarpet_artefacts
plugins/clickbox/ClickBox_artefacts
plugins/pnch/PNCH_artefacts
plugins/proto/Proto_artefacts
plugins/dietaudio/DietAudio_artefacts"

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_bindir}/

for Plugins in $PLUGIN_LIST
do
    cp -ra %{__cmake_builddir}/$Plugins/VST3/* %{buildroot}/%{_libdir}/vst3/
    cp -ra %{__cmake_builddir}/$Plugins/CLAP/* %{buildroot}/%{_libdir}/clap/
    cp -ra %{__cmake_builddir}/$Plugins/Standalone/* %{buildroot}/%{_bindir}/
done

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Sep 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
