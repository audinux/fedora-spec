# Status: active
# Tag: Effect, Delay
# Type: Plugin, Standalone, LV2, VST3
# Category: Effect

Name: sirial
Version: 1.1.2
Release: 1%{?dist}
Summary: Rhythmic Delay
License: GPL-3.0-or-later
URL: https://github.com/tiagolr/sirial
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./ripplerx-source.sh <PROJECT> <TAG>
#        ./ripplerx-source.sh sirial v1.1.1

Source0: sirial.tar.gz
Source1: ripplerx-source.sh

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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

Requires: license-%{name}

%description
Sirial is a Rhythmic Delay where each tap can be placed and configured with different
amplitudes and feedback giving total control on how the delay responds and the patterns
it creates.
It is loosely based on EchoBoy Tap mode, with the novelty that it uses serial delay
lines instead of delay taps, this hybrid approach enables the versatility of multi-tap
delays with the natural decay (optional) and coloring of standard delays,
producing a more pleasant and realistic sound.
The main advantage of using serial delay lines is that any effects on the feedback path,
like damping, are applied on each tap like normal delays, it also enables natural decay
over the taps and allows for classic modes like Ping-Pong or cross feedback.
This comes at a cost of complexity and CPU usage, not that the serial delay lines are
expensive its just that multiple taps on a single delay line are extremely cheap.
This plug-in doesn't include many effects since applying them on each tap can be
prohibitively costly, for example feedback pitch-shift or saturation would be computed
each sample for 16 delay lines * 2 channels. The effects included are only pre or post
delay, any pre or post FX can be added outside the plug-in in any DAW.
If you are looking for a typical delay with more FXs and modes checkout QDelay.
Features:
* 16 Serial Delay Lines allows to build intricate delay patterns
* Intuitive UI to configure the taps offset and amplitude
* Stereo Taps with different offsets for left and right channels
* Ping-Pong Mode where the feedback is crossed on each tap
* Modulation with 5 modes: Sine, Tri, Square, Rand S&H and Rand Walk.
* Delay Reverse mode
* Basic Effects like damping, saturation and diffusion
* Ducking with controls for threshold, amount, attack and release

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n sirial

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Sirial_artefacts/VST3/*  %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/Sirial_artefacts/LV2/*  %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}%{_bindir}/
cp -ra %{__cmake_builddir}/Sirial_artefacts/Standalone/*  %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Mar 22 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- Initial spec file
