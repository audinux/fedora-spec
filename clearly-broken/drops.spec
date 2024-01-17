# Tag: Sampler
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    drops
Version: 1.0.b2
Release: 1%{?dist}
Summary: Sampler plugin
URL:     https://github.com/clearly-broken-software/drops
License: GPL3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./clearly-broken-source.sh <PROJECT> <TAG>
#        ./clearly-broken-source.sh drops v1.0-beta2

Source0: drops.tar.gz
Source1: clearly-broken-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: ladspa-devel
BuildRequires: lv2-devel
BuildRequires: freetype-devel
BuildRequires: cairo-devel
BuildRequires: libglvnd-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: libsndfile-devel
BuildRequires: desktop-file-utils

%description
Sampler plugin

%package -n vst3-drops
Summary: VST3 sampler plugin

%description -n vst3-drops
A VST3 sampler plugin

%package -n lv2-drops
Summary: LV2 sampler plugin

%description -n lv2-drops
A LV2 sampler plugin

%prep

%autosetup -n drops

%build

%set_build_flags

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} SKIP_STRIPPING=true VERBOSE=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/drops.lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp bin/drops %{buildroot}/%{_bindir}/
cp bin/drops-vst.so %{buildroot}/%{_libdir}/vst3/
cp -ra bin/drops.lv2/* %{buildroot}/%{_libdir}/lv2/drops.lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n lv2-drops
%{_libdir}/lv2/*

%files -n vst3-drops
%{_libdir}/vst3/*

%changelog
* Fri Mar 04 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.b2-1
- Initial spec file
