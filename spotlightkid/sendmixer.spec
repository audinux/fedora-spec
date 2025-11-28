# Status: active
# Tag: Mixer
# Type: Plugin, LV2, VST3, CLAP
# Category: Audio, Tool

Name: sendmixer
Version: 0.2.0
Release: 1%{?dist}
Summary: A stereo channel strip with one master gain and two pre/post-fader sends
License: MIT
URL: https://github.com/SpotlightKid/sendmixer
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh sendmixer v0.2.0

Source0: sendmixer.tar.gz
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
A stereo channel strip plugin with one master gain and two pre/post-fader sends

%package -n license-%{name}
Summary: License and documentation for the sendmixer plugin.

%description -n license-%{name}
License and documentation for the sendmixer plugin.

%package -n lv2-%{name}
Summary: LV2 version of the sendmixer plugin.
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of the sendmixer plugin.

%package -n vst3-%{name}
Summary: VST3 version of the sendmixer plugin.
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of the sendmixer plugin.

%package -n clap-%{name}
Summary: CLAP version of the sendmixer plugin.
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of the sendmixer plugin.

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
* Fri Nov 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- Initial version of the spec file
