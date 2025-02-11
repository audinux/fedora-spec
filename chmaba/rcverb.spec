# Status: active
# Tag: Effect, Reverb
# Type: Plugin, VST3, LV2, CLAP, LADSPA
# Category: Audio, Effect

%global commit0 5017507c204bb43f3eed0bacaac6fd227d4445c2

Name: rcverb
Version: 1.0
Release: 2%{?dist}
Summary: A reverb suitable for classical music
URL: https://github.com/chmaha/RCVerb
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# To get RCVerb source code:
# ./rcverb-source.sh main

Source0: RCVerb.tar.gz
Source1: rcverb-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libsamplerate-devel
BuildRequires: liblo-devel
BuildRequires: desktop-file-utils

%description
A reverb suitable for classical music

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%prep
%autosetup -n RCVerb

%build

%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} VERBOSE=true BUILD_LV2=true BUILD_VST3=true BUILD_LADSPA=true BUILD_CLAP=true SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/

cp -ra bin/rcverb.lv2  %{buildroot}/%{_libdir}/lv2/
cp -ra bin/rcverb.vst3 %{buildroot}/%{_libdir}/vst3/
cp bin/rcverb.clap %{buildroot}/%{_libdir}/clap/
cp bin/rcverb-ladspa.so %{buildroot}/%{_libdir}/ladspa/

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%changelog
* Tue Feb 11 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Mon Aug 21 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file
