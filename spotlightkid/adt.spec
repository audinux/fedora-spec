# Status: active
# Tag: Effect
# Type: Plugin, LV2, VST3, CLAP
# Category: Audio, Effect

Name: adt
Version: 0.2.2
Release: 1%{?dist}
Summary: Automatic double tracking plugin (not only) for vocals
License: MIT
URL: https://github.com/SpotlightKid/adt
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh adt v0.2.2

Source0: adt.tar.gz
Source1: spotlightkid-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: desktop-file-utils

%description
Automatic double tracking plugin (not only) for vocals
This plugin copies the input four times and pans the copies alternatively
left and right by a set amount, delays each by up to 100 ms and also
pitch-shifts each copy by up to 150 cents.
The maximum pan, delay and pitch-shift spread can be independently controlled
by parameters as well as the cutoff frequencies of a low- and high-pass
filter applied to the stereo ouput.

This effect can be used to thicken up lead or background vocals or other signals
that need more presence in the mix.

It can be used as either an insert effect or as a send effect in an auxilliary
bus by providing separate dry and wet signal gain parameters.

%package -n license-%{name}
Summary: License and documentation for the adt plugin.

%description -n license-%{name}
License and documentation for the adt plugin.

%package -n lv2-%{name}
Summary: LV2 version of the adt plugin.
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of the adt plugin.

%package -n vst3-%{name}
Summary: VST3 version of the adt plugin.
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of the adt plugin.

%package -n clap-%{name}
Summary: CLAP version of the adt plugin.
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of the adt plugin.

%prep
%autosetup -n %{name}

%build

%set_build_flags

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true

%files -n license-%{name}
%doc README.md
%license LICENSE.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Nov 27 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-1
- Initial version of the spec file
