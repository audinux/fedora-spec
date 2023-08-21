# Tag: MIDI, FM, Emulator
# Type: Plugin, VST, LV2
# Category: Audio, Synthesizer

Name:    rccomp
Version: 0.9
Release: 1%{?dist}
Summary: A compressor designed for classical music engineers
URL:     https://github.com/chmaha/RCComp
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# To get RCComp source code:
# ./rccomp-source.sh v0.9

Source0: RCComp.tar.gz
Source1: rccomp-source.sh

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
A compressor designed for classical music engineers

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

%prep
%autosetup -n RCComp

%build

%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} VERBOSE=true SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp -ra bin/*.lv2  %{buildroot}/%{_libdir}/lv2/
cp -ra bin/*.clap %{buildroot}/%{_libdir}/clap/


%files
%doc README.md
%license LICENSE

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Aug 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial spec file
