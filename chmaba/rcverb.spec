# Tag: Effect, Reverb
# Type: Plugin, VST3, LV2
# Category: Audio, Effect

Name:    rcverb
Version: 1.0
Release: 1%{?dist}
Summary: A reverb suitable for classical music
URL:     https://github.com/chmaha/RCVerb
ExclusiveArch: x86_64 aarch64
License: GPL-3.0-or-later

Vendor:       Audinux
Distribution: Audinux

# To get RCVerb source code:
# ./rcverb-source.sh v1.0

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

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n RCVerb

%build

%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} VERBOSE=true SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp -ra bin/*.lv2  %{buildroot}/%{_libdir}/lv2/
cp -ra bin/*.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Aug 21 2023 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file
