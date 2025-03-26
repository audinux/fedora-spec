# Status: active
# Tag: Synthesizer, Drum
# Type: Plugin, LV2, VST3
# Category: Synthesizer

%global commit0 2820a1d31c744ed1a21e572dfa4cf490719dc76b

Name: stegosaurus
Version: 0.0.1
Release: 1%{?dist}
Summary: Drum Synthesizer
License: GPL-2.0-or-later
URL: https://github.com/thunderox/stegosaurus/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./stegosaurus-source.sh <TAG>
#        ./stegosaurus-source.sh main
Source0: stegosaurus.tar.gz
Source1: stegosaurus-source.sh

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: liblo-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: rtaudio-devel
BuildRequires: SDL2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: cairo-devel

%description
ThunderOx Drum synth plugin

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n dssi-%{name}
Summary:  DSSI version of %{name}
License:  GPL-2.0-or-later
Requires: license-%{name}

%description -n dssi-%{name}
DSSI version of %{name}

%prep
%autosetup -n %{name}

%build

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/dssi/

install -m 755 bin/stegosaurus %{buildroot}/%{_bindir}/

cp -ra bin/stegosaurus.lv2  %{buildroot}/%{_libdir}/lv2/
cp -ra bin/stegosaurus.vst  %{buildroot}/%{_libdir}/vst/
cp -ra bin/stegosaurus-dssi %{buildroot}/%{_libdir}/dssi/
install -m 755 bin/stegosaurus-dssi.so %{buildroot}/%{_libdir}/dssi/

%files
%{_bindir}/*

%files -n license-%{name} 
%doc README.md
%license LICENSE

%files -n lv2-%{name} 
%{_libdir}/lv2/*

%files -n vst-%{name} 
%{_libdir}/vst/*

%files -n dssi-%{name} 
%{_libdir}/dssi/*

%changelog
* Tue Mar 25 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec
