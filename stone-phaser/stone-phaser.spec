# Global variables for github repository
%global commit0 8ae2fc7544259525027ee4496e7fa0c7527f71e7
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    stone-phaser
Version: 0.1.2
Release: 2%{?dist}
Summary: A classic analog phaser effect
URL:     https://github.com/jpcima/stone-phaser
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

# ./stone-phaser-source.sh <tag>
# ./stone-phaser-source.sh v0.1.2

Source0: stone-phaser.tar.gz
Source1: stone-phaser-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel libXft-devel
BuildRequires: fltk-devel fltk-fluid
BuildRequires: cairo-devel libpng-devel

%description
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone. It has a color switch, which makes the phasing stronger when on, and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.

%package -n ladspa-stone-phaser
Summary: stone-phaser LADSPA plugin

%description -n ladspa-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone.
It has a color switch, which makes the phasing stronger when on,
and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser LADSPA plugin

%package -n vst-stone-phaser
Summary: stone-phaser VST plugin

%description -n vst-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone.
It has a color switch, which makes the phasing stronger when on,
and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser VST plugin

%package -n lv2-stone-phaser
Summary: stone-phaser LV2 plugin

%description -n lv2-stone-phaser
A classic analog phaser effect
This is an analog phaser with similarity to the Small Stone.
It has a color switch, which makes the phasing stronger when on,
and adds some feedback controls. A stereo variant of the phaser is included.
This effect is supported on MOD devices.
stone-phaser LV2 plugin

%prep

%autosetup -n stone-phaser

%ifarch aarch64
sed -i -e "s/-msse2//g" dpf/Makefile.base.mk
sed -i -e "s/-msse//g" dpf/Makefile.base.mk
%endif

%build

%set_build_flags

%if 0%{?fedora} >= 38
export CXXFLAGS="-include cstdint $CXXFLAGS"
%endif

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%files
%doc README.md
%license LICENSE

%files -n lv2-stone-phaser
%{_libdir}/lv2/*

%files -n vst-stone-phaser
%{_libdir}/vst/*

%files -n ladspa-stone-phaser
%{_libdir}/ladspa/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-2
- fix debug build

* Fri Oct 11 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- Initial spec file
