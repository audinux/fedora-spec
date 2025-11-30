# Status: active
# Tag: Jack, Alsa, Effect
# Type: Plugin, Standalone, LADSPA, VST, LV2, VST3, CLAP
# Category: Audio, Effect

Name: cchorus
Version: 2.2.0
Release: 1%{?dist}
Summary: A versatile stereo chorus, multi-format audio effect plugin
License: MIT
URL: https://github.com/SpotlightKid/cchorus
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh cchorus v2.2.0

Source0: cchorus.tar.gz
Source1: spotlightkid-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: desktop-file-utils

%description
A versatile stereo chorus effect

%package -n license-%{name}
Summary: License and documentation for cchorus plugin.

%package -n ladspa-%{name}
Summary: LADSPA version of the cchorus plugin.
Requires: license-%{name}

%package -n lv2-%{name}
Summary: LV2 version of the cchorus plugin.
Requires: license-%{name}

%package -n vst-%{name}
Summary: VST version of the cchorus plugin.
Requires: license-%{name}

%package -n vst3-%{name}
Summary: VST3 version of the cchorus plugin.
Requires: license-%{name}

%package -n clap-%{name}
Summary: CLAP version of the cchorus plugin.
Requires: license-%{name}

%description -n license-%{name}
License and documetatnion for cchorus plugin.

%description -n ladspa-%{name}
LADSPA version of the cchorus plugin.

%description -n lv2-%{name}
LV2 version of the cchorus plugin.

%description -n vst-%{name}
VST version of the cchorus plugin.

%description -n vst3-%{name}
VST3 version of the cchorus plugin.

%description -n clap-%{name}
CLAP version of the cchorus plugin.

%prep
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Nov 30 2025 Yann Collette <ycollette.nospam@free.fr> - 2.2.0-1
- Initial version of the spec file
