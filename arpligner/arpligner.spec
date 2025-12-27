# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST3, LV2
# Category: Audio, Synthesizer

%global commit0 901d3753cf8728217abc034251ada2d5fbc12ae6

Name: arpligner
Version: 0.0.1
Release: 1%{?dist}
Summary: A multi-track & polyphonic arpeggiator plugin that takes both chords and arp patterns as live MIDI data
License: MPL-2.0
URL: https://github.com/YPares/arpligner
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/YPares/arpligner/archive/901d3753cf8728217abc034251ada2d5fbc12ae6.zip#/%{name}-%{version}.zip

# Build with JUCE-7

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
# BuildRequires: JUCE7
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
Arpligner is a multi-track & polyphonic arpeggiator which will use your own
arpeggiation patterns (like 2Rule TugMidiSeq, LibreArp, Xfer Cthulhu, Reason
PolyStep Sequencer, or FL's VFX Sequencer).
It is packaged as VST3 & LV2 MIDI plugins and as a standalone application.

- Multi-track: Multiple arpeggiation patterns can play at the same time for
  a given chord, each one in its own track of your DAW, or on its own MIDI channel,
- Polyphonic: Each step can play several notes of a chord at the same time.
  "Steps" can also hold over an arbitrary length of time and overlap.
  So besides arpeggiation per se, you can do strumming or really any kind
  of "turning a plain block chord into something more interesting".

To achieve this, the big difference between Arpligner and the aforementioned
plugins is that Arpligner does very intentionally not come with its own
graphical interface for editing patterns. Instead it will rely on arp patterns
being fed to it as regular (and possibly live) MIDI data: you can thus make
use of your DAW piano rool and MIDI sequencing capabilities1, play those
patterns live, or use an external MIDI sequencer (software or hardware).

Therefore, you can use it as a regular arp, playing your chords against
pre-written patterns, or the opposite. Or both can be live data! That would be
having two keyboard players: one in charge of the chords and the other one in
charge of how to layout those chords2.

See https://youtu.be/IQ9GFEaS4Ag for an overview of the tool and the basic
features (this uses the original Lua script but the video remains valid).

Still experimental, please post issues here in case of bugs or questions,
or get in touch on Matrix (room #arpligner:gitter.im):
just click here to join the chat! :)

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MPL-2.0

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MPL-2.0
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MPL-2.0
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}-%{commit0}

%build

cd Builds/LinuxMakefile
%make_build

%install

cd Builds/LinuxMakefile/build

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra Arpligner  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra Arpligner.vst3  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra Arpligner.lv2  %{buildroot}/%{_libdir}/lv2/


%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Dec 17 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
