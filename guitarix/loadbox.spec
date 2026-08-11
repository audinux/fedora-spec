# Status: active
# Tag: Audio, AI, Amp Simul
# Type: Plugin, CLAP, VST3, VST2, LV2
# Category: Audio, Tool

Name: loadbox
Version: 0.1.0
Release: 1%{?dist}
Summary: A lightweight stereo Impulse Response and NAM profile loader plugin
License: BSD-3-Clause
URL: https://github.com/brummer10/loadbox
ExclusiveArch: x86_64 

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh loadbox v0.1.0

Source0: loadbox.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: ncurses
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: lv2-devel
BuildRequires: libsigc++20-devel
BuildRequires: zita-resampler-devel
BuildRequires: libsndfile-devel

%description
A lightweight stereo Impulse Response and NAM profile loader plugin, split out from NeuralRack.
Features:
* True stereo processing: independent IR/NAM slot per channel, with a switchable Stereo / Mix mode
* Per-channel and master gain, plus a mix control between channels in Mix mode
* Available as CLAP, VST2 and VST3

%package -n license-%{name}
Summary: License and documentation for %{name}
License: BSD-3-Clause

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst2-%{name}
Summary: VST2 version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n vst2-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: BSD-3-Clause
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n loadbox

%build

%set_build_flags

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp -ra bin/LoadBox.clap     %{buildroot}%{_libdir}/clap/
cp -ra bin/LoadBoxVST3.vst3 %{buildroot}%{_libdir}/vst3/
cp -ra bin/LoadBoxvst.so    %{buildroot}%{_libdir}/vst/

%files -n license-%{name}
%doc README.md

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst2-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Aug 10 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- Initial spec file
