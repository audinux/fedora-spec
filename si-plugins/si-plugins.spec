# Tag: MIDI, FM, Emulator
# Type: Plugin, VST, LV2
# Category: Audio, Synthesizer

Name:    si-plugins
Version: 0.3.0
Release: 1%{?dist}
Summary: Shermann Innovations plugin series
URL:     https://github.com/guysherman/si-plugins
License: MIT

Vendor:       Audinux
Distribution: Audinux

# ./si-plugins-source.sh v0.3.0

Source0: si-plugins.tar.gz
Source1: si-plugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: jack-audio-connection-kit-devel
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
Shermann Innovations plugin series

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  MIT
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  MIT
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  MIT
Requires: %{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n dssi-%{name}
Summary:  DSSI version of %{name}
License:  MIT
Requires: %{name}

%description -n dssi-%{name}
DSSI version of %{name}

%prep
%autosetup -n si-plugins

sed -i -e "s/-Wl,--strip-all//g" Makefile.mk

%ifarch aarch64
sed -i -e "s/-msse2//g" Makefile.mk
sed -i -e "s/-msse2//g" dpf/dgl/Makefile.mk
sed -i -e "s/-msse//g" Makefile.mk
sed -i -e "s/-msse//g" dpf/dgl/Makefile.mk
sed -i -e "s/-mfpmath=sse//g" Makefile.mk
sed -i -e "s/-mfpmath=sse//g" dpf/dgl/Makefile.mk
%endif

%build

%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} VERBOSE=true

%install

ls bin

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 -d %{buildroot}/%{_libdir}/dssi/

cp -ra bin/*.lv2       %{buildroot}/%{_libdir}/lv2/
cp -ra bin/*-vst.so    %{buildroot}/%{_libdir}/vst/
cp -ra bin/*-ladspa.so %{buildroot}/%{_libdir}/ladspa/
cp -ra bin/*-dssi      %{buildroot}/%{_libdir}/dssi/
cp -ra bin/*-dssi.so   %{buildroot}/%{_libdir}/dssi/

cp -ra bin/si-d1 %{buildroot}/%{_bindir}/
cp -ra bin/si-d2 %{buildroot}/%{_bindir}/
cp -ra bin/si-h1 %{buildroot}/%{_bindir}/
cp -ra bin/si-h2 %{buildroot}/%{_bindir}/
cp -ra bin/si-l1 %{buildroot}/%{_bindir}/
cp -ra bin/si-l2 %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE_DPF  LICENSE_SIPLUGINS
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%changelog
* Sat Aug 19 2023 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
