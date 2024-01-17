# Tag: Jack, Alsa, Effect
# Type: Plugin, Standalone, VST, LV2, CLAP
# Category: Audio, Effect

Name:    chaffverb
Version: 0.2.3
Release: 1%{?dist}
Summary: An audio plugin utilizing pitch shifting, echo and reverb, for creating sounds from shimmers to whale songs.
License: MIT
URL:     https://github.com/GModal/ChaffVerb

Vendor:       Audinux
Distribution: Audinux

# ./chaffverb-source.sh <tag>
# ./chaffverb-source.sh v0.2.3

Source0: ChaffVerb.tar.gz
Source1: chaffverb-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: hvcc
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: dssi-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
An audio plugin utilizing pitch shifting, echo and reverb,
ChaffVerb can create sounds that vary from shimmers to whale songs.
Plugins are provided in LV2, VST, VST3 and CLAP formats, compiled
for Linux environments. With a working hvcc environment, the patch
should compile for other systems.

%package -n lv2-%{name}
Summary: LV2 version of the chaffverb plugin.
Requires: %{name}

%package -n vst-%{name}
Summary: VST version of the chaffverb plugin.
Requires: %{name}

%package -n vst3-%{name}
Summary: VST3 version of the chaffverb plugin.
Requires: %{name}

%package -n clap-%{name}
Summary: CLAP version of the chaffverb plugin.
Requires: %{name}

%description -n lv2-%{name}
LV2 version of the chaffverb plugin.

%description -n vst-%{name}
VST version of the chaffverb plugin.

%description -n vst3-%{name}
VST3 version of the chaffverb plugin.

%description -n clap-%{name}
CLAP version of the chaffverb plugin.

%prep
%autosetup -n ChaffVerb

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

cd ChaffVerb/bin

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra ChaffVerb.lv2 %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp ChaffVerb-vst.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra ChaffVerb.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp ChaffVerb.clap %{buildroot}/%{_libdir}/clap/

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
* Thu Jan 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.3-1
- update to 0.2.3-1

* Tue Jan 24 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- Initial version of the spec file
