# Tag: Plugin
# Type: Plugin, LV2, VST, VST3, CLAP, LADSPA
# Category: Audio, Effect

Name:    dpf-plugins
Version: 1.7
Release: 3%{?dist}
Summary: Collection of DPF-based plugins for packaging
License: GPL-2.0-or-later
URL:     https://github.com/DISTRHO/DPF-Plugins

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/DPF-Plugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

%description
Collection of DPF-based plugins ready for packaging.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n dssi-%{name}
Summary:  DSSI version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n dssi-%{name}
DSSI version of %{name}

%prep
%autosetup -n DPF-Plugins-%{version}

%build

%set_build_flags

%make_build PREFIX=%{_prefix} SKIP_STRIPPING=true

%install

%make_install PREFIX=%{_prefix} SKIP_STRIPPING=true

mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}

%files
%doc README.md
%license LICENSE
%{_bindir}/*

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
* Sun Apr 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.2.10-3
- Initial build
