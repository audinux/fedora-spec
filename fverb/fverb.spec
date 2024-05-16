# Tag: Reverb
# Type: Plugin, LV2
# Category: Audio, Effect

# Global variables for github repository
%global commit0 1b9e021b63a73a4bf86a6e4fb73200511391c691
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: fverb
Version: 0.0.1
Release: 1%{?dist}
Summary: Reverberation plugin
URL: https://github.com/jpcima/fverb
ExclusiveArch: x86_64 aarch64
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

# git clone https://github.com/jpcima/fverb
# # git checkout bells
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz fverb.tar.gz fverb/*
# rm -rf fverb

Source0: fverb.tar.gz

BuildRequires: gcc gcc-c++
BuildReauires: make
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: ladspa-devel
BuildRequires: lv2-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: desktop-file-utils

%description
Reverberation plugin

%package -n ladspa-fverb
Summary: LADSPA reverberation plugin

%description -n ladspa-fverb
A LADSPA reverberation plugin

%package -n vst-fverb
Summary: VST reverberation plugin

%description -n vst-fverb
A VST reverberation plugin

%package -n lv2-fverb
Summary: LV2 reverberation plugin

%description -n lv2-fverb
A LV2 reverberation plugin

%prep

%autosetup -n fverb

%build

%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" SKIP_STRIPPING=true VERBOSE=true

%install

%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" SKIP_STRIPPING=true VERBOSE=true

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%files -n lv2-fverb
%{_libdir}/lv2/*
%files -n vst-fverb
%{_libdir}/vst/*
%files -n ladspa-fverb
%{_libdir}/ladspa/*

%changelog
* Tue Jun 02 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
