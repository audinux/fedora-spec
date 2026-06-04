# Status: active
# Tag: Effect, Equalizer
# Type: Plugin, VST, VST3, LV2, CLAP
# Category: Audio, Effect

Name: wstd-mseq
Version: 1.0.1
Release: 1%{?dist}
Summary: Simple nasty mid-side EQ plugin
License: GPL-3.0-or-later
URL: https://github.com/Wasted-Audio/wstd-mseq
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./wstd-source.sh <project> <tag>
# ./wstd-source.sh wstd-mseq v1.0.1

Source0: wstd-mseq.tar.gz
Source1: wstd-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: hvcc
BuildRequires: jq
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: ladspa-devel
BuildRequires: dssi-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

Requires: license-%{name}

%description
Simple nasty mid-side EQ plugin.

%package -n license-%{name}
Summary: License and documentation for %{name}.

%description -n license-%{name}
License and documentation for %{name}.

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%package -n clap-%{name}
Summary: CLAP version of the %{name} plugin.
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of the %{name} plugin.

%package -n vst-%{name}
Summary: VST2 version of the %{name} plugin.
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of the %{name} plugin.

%package -n vst3-%{name}
Summary: VST3 version of the %{name} plugin.
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of the %{name} plugin.

%prep
%autosetup -n %{name}

jq '.dpf.plugin_formats |= map(select(. != "au"))' WSTD_MSEQ.json > tmp.$$.json && mv tmp.$$.json WSTD_MSEQ.json

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%make_build PLUGIN=wstd_mseq PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp -ra bin/WSTD_MSEQ.lv2 %{buildroot}/%{_libdir}/lv2/
cp bin/WSTD_MSEQ-vst.so %{buildroot}/%{_libdir}/vst/
cp -ra bin/WSTD_MSEQ.vst3 %{buildroot}/%{_libdir}/vst3/
cp bin/WSTD_MSEQ.clap %{buildroot}/%{_libdir}/clap/

%files -n license-%{name}
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
* Thu Jun 04 2026 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial version of the spec file
