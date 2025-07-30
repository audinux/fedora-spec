# Status: active
# Tag: Tool, AI
# Type: Plugin, LV2, VST3, Standalone
# Category: Audio, Tool

Name: neuralrack
Version: 0.2.0
Release: 1%{?dist}
Summary: NeuralRack is a Neural Model and Impulse Response File loader for Linux
License: BSD-3-Clause
URL: https://github.com/brummer10/NeuralRack
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh NeuralRack v0.2.0

Source0: NeuralRack.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: xxd
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: libX11-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: portaudio-devel

Requires: license-%{name}

%description
NeuralRack is a Neural Model and Impulse Response File loader for Linux/Windows.

It supports *.nam files with the Neural Amp Modeler engine, or *.json or .aidax
files with the RTNeural engine.

NeuralRack emulate a simple guitar effect chain with a pedal, a EQ a Amplifier
and a Stereo Cabinet.

Optional, NeuralRack could run the complete process in buffered mode to reduce the dsp load.
The resulting latency will be reported to the host so that it could be compensated.
For information the resulting latency will be shown on the GUI.

NeuralRack supports resampling when needed to match the expected sample rate of the
loaded models. Both models and the IR Files may have different expectations regarding
the sample rate.

%package -n license-%{name}
Summary: License and documentation for %{name}.

%description -n license-%{name}
License and documentation for %{name}

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%prep
%autosetup -n NeuralRack

%build

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/Neuralrack.lv2 %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_bindir}/
cp -a bin/Neuralrack %{buildroot}/%{_bindir}/

%files
%{_bindir}/Neuralrack

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Tue Jul 29 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Tue Jun 10 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.19-1
- update to 0.1.19-1

* Wed May 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- update to 0.1.8-1

* Tue May 20 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- update to 0.1.7-1

* Sat Apr 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.6-1
- update to 0.1.6-1

* Thu Apr 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.5-1
- update to 0.1.5-1

* Wed Apr 02 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- update to 0.1.4-1

* Wed Mar 26 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- update to 0.1.3-1

* Mon Mar 24 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
