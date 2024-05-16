# Tag: Synthesizer
# Type: Plugin, VST, LV2
# Category: Synthesizer

Name: string-machine
Version: 0.1
Release: 1%{?dist}
Summary: Digital model of electronic string ensemble instrument
URL: https://github.com/jpcima/string-machine
ExclusiveArch: x86_64 aarch64
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

# ./string-machine-source.sh <tag>
# ./string-machine-source.sh master

Source0: string-machine.tar.gz
Source1: string-machine-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: fltk-devel fltk-fluid
BuildRequires: cairo-devel
BuildRequires: libpng-devel

%description
This is a virtual-analog string ensemble synthesizer.

This implementation is based on a digital model designed by Peter Whiting.
The improvement of the model adds various abilities, in particular a
virtual-analog emulation of the bucket brigade delay circuit.

%package -n vst-%{name}
Summary: VST version of %{name}

%description -n vst-%{name}
VST version %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep

%autosetup -n string-machine

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

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Fri Nov 06 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial spec file
