# Tag: Jack, Alsa, Effect
# Type: Plugin, Standalone, VST, LV2, CLAP
# Category: Audio, Effect

Name: vswell
Version: 0.3.0
Release: 1%{?dist}
Summary: vSwell is a volume envelope audio effect plugin. In LV2, VST, VST3 and CLAP formats.
License: MIT
URL: https://github.com/GModal/vSwell

Vendor:       Audinux
Distribution: Audinux

# ./vswell-source.sh <tag>
# ./vswell-source.sh v0.3.0

Source0: vSwell.tar.gz
Source1: vswell-source.sh

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
vSwell is a volume envelope audio effect plugin.
The effect can be triggered by an audio signal, CV or a MIDI notein.
The plugin is provided in two versions:
 - vSwell: Mono, with a separate trigger input
 - vSwellST: Stereo, with selectable trigger channels

Plugins are provided in LV2, VST, VST3 and CLAP formats,
compiled for Linux environments. With a working hvcc environment,
the patch should compile for other systems.

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.
Requires: %{name}

%package -n vst-%{name}
Summary: VST version of the %{name} plugin.
Requires: %{name}

%package -n vst3-%{name}
Summary: VST3 version of the %{name} plugin.
Requires: %{name}

%package -n clap-%{name}
Summary: CLAP version of the %{name} plugin.
Requires: %{name}

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%description -n vst-%{name}
VST version of the %{name} plugin.

%description -n vst3-%{name}
VST3 version of the %{name} plugin.

%description -n clap-%{name}
CLAP version of the %{name} plugin.

%prep
%autosetup -n vSwell

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp -ra vSwell/bin/vSwell.lv2 %{buildroot}/%{_libdir}/lv2/
cp vSwell/bin/vSwell-vst.so %{buildroot}/%{_libdir}/vst/
cp -ra vSwell/bin/vSwell.vst3 %{buildroot}/%{_libdir}/vst3/
cp vSwell/bin/vSwell.clap %{buildroot}/%{_libdir}/clap/

cp -ra vSwellST/bin/vSwellST.lv2 %{buildroot}/%{_libdir}/lv2/
cp vSwellST/bin/vSwellST-vst.so %{buildroot}/%{_libdir}/vst/
cp -ra vSwellST/bin/vSwellST.vst3 %{buildroot}/%{_libdir}/vst3/
cp vSwellST/bin/vSwellST.clap %{buildroot}/%{_libdir}/clap/

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
* Wed Feb 15 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial version of the spec file
