# Tag: Effect, Distortion
# Type: Plugin, VST, VST3, LV2, CLAP
# Category: Audio, Effect

Name: wstd-manglr
Version: 1.0.1
Release: 1%{?dist}
Summary: Modular distortion plugin
License: GPL-3.0-only
URL: https://github.com/Wasted-Audio/wstd-manglr

Vendor:       Audinux
Distribution: Audinux

# ./wstd-source.sh <project> <tag>
# ./wstd-source.sh wstd-manglr v1.0.1

Source0: wstd-manglr.tar.gz
Source1: hvcc-Makefile
Source2: wstd-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: hvcc
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: dssi-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
Modular distortion plugin

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.
Requires: %{name}

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%package -n clap-%{name}
Summary: CLAP version of the %{name} plugin.
Requires: %{name}

%description -n clap-%{name}
CLAP version of the %{name} plugin.

%package -n vst-%{name}
Summary: VST2 version of the %{name} plugin.
Requires: %{name}

%description -n vst-%{name}
VST2 version of the %{name} plugin.

%package -n vst3-%{name}
Summary: VST3 version of the %{name} plugin.
Requires: %{name}

%description -n vst3-%{name}
VST3 version of the %{name} plugin.

%prep
%autosetup -n %{name}

cp %{SOURCE1} Makefile

%build

%set_build_flags

%make_build PLUGIN=wstd_manglr PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp -ra wstd_manglr/bin/WSTD_MANGLR.lv2 %{buildroot}/%{_libdir}/lv2/
cp wstd_manglr/bin/WSTD_MANGLR-vst.so %{buildroot}/%{_libdir}/vst/
cp -ra wstd_manglr/bin/WSTD_MANGLR.vst3 %{buildroot}/%{_libdir}/vst3/
cp wstd_manglr/bin/WSTD_MANGLR.clap %{buildroot}/%{_libdir}/clap/

%files
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial version of the spec file
