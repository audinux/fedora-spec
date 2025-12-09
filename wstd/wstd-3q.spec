# Status: active
# Tag: Effect, Equalizer
# Type: Plugin, VST, VST3, LV2, CLAP
# Category: Audio, Effect

Name: wstd-3q
Version: 1.1.1
Release: 1%{?dist}
Summary: WSTD EQ but with separate outputs
License: GPL-3.0-or-later
URL: https://github.com/Wasted-Audio/wstd-3q
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./wstd-source.sh <project> <tag>
# ./wstd-source.sh wstd-3q v1.1.1

Source0: wstd-3q.tar.gz
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

%description
WSTD EQ but with separate outputs

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

jq '.dpf.plugin_formats |= map(select(. != "au"))' WSTD_3Q.json > tmp.$$.json && mv tmp.$$.json WSTD_3Q.json

%build

%set_build_flags

export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`

%make_build PLUGIN=wstd_3q PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp -ra bin/WSTD_3Q.lv2 %{buildroot}/%{_libdir}/lv2/
cp bin/WSTD_3Q-vst.so %{buildroot}/%{_libdir}/vst/
cp -ra bin/WSTD_3Q.vst3 %{buildroot}/%{_libdir}/vst3/
cp bin/WSTD_3Q.clap %{buildroot}/%{_libdir}/clap/

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
* Tue Dec 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Mon Nov 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- update to 1.1-1

* Wed Jan 24 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial version of the spec file
