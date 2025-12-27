# Status: active
# Tag: Plugin
# Type: Plugin, LV2, VST, VST3, CLAP, LADSPA, DSSI
# Category: Audio, Effect

%global commit0 3858414367d1fce1e2c5d949f4ed46dde10bbf5c

Name:    dpf-plugins
Version: 1.7
Release: 3%{?dist}
Summary: Collection of DPF-based plugins for packaging
License: GPL-2.0-or-later
URL:     https://github.com/DISTRHO/DPF-Plugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/DPF-Plugins/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: liblo-devel
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: projectM-mao-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

Conflicts: proms

%description
Collection of DPF-based plugins ready for packaging.
They come in LADSPA, DSSI, LV2, VST2, VST3 and CLAP formats.
The list of plugins/packs are:
- glBars
- Kars
- Max-Gen examples (MaBitcrush, MaFreeverb, MaGigaverb, MaPitchshift)
- Mini-Series (3BandEQ, 3BandSplitter, PingPongPan)
- ndc-Plugs (Amplitude Imposer, Cycle Shifter, Soul Force)
- MVerb
- Nekobi
- ProM

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n dssi-%{name}
Summary:  DSSI version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n dssi-%{name}
DSSI version of %{name}

%prep
%autosetup -n DPF-Plugins-%{commit0}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} SKIP_STRIPPING=true

%install

%make_install PREFIX=%{_prefix} SKIP_STRIPPING=true

mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%changelog
* Mon Aug 04 2025 Yann Collette <ycollette.nospam@free.fr> - 3.2.10-4
- update package + conflicts with prom

* Sun Apr 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.10-3
- Initial build
