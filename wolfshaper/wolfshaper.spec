# Tag: Jack, Alsa, Overdrive
# Type: Plugin, Standalone, VST, LV2, DSSI
# Category: Audio, Effect

Name:    wolf-shaper
Version: 0.1.8
Release: 2%{?dist}
Summary: Wolf-shaper is a waveshaper plugin with a graph editor.
License: GPLv2+
URL:     https://github.com/pdesaulniers/wolf-shaper

Vendor:       Audinux
Distribution: Audinux

# ./wolfshapper-source.sh <tag>
# ./wolfshapper-source.sh v0.1.8

Source0: wolf-shaper.tar.gz
Source1: wolfshaper-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel

%description
Wolf Shaper is a waveshaper plugin with a graph editor.

%package -n dssi-%{name}
Summary: DSSI version of the Wolf Shaper plugin.

%package -n lv2-%{name}
Summary: LV2 version of the Wolf Shaper plugin.

%package -n vst-%{name}
Summary: VST version of the Wolf Shaper plugin.

%description -n dssi-%{name}
DSSI version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n lv2-%{name}
LV2 version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n vst-%{name}
VST version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%prep
%autosetup -n %{name}

%ifarch x86_64
sed -i -e "s/\$(PREFIX)\/lib/\$(PREFIX)\/lib64/g" Makefile
%endif

%build

%set_build_flags

%make_build PREFIX=/usr SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr SKIP_STRIPPING=true

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-2
- update to 0.1.8-2 - fix debug buid

* Wed Oct 2 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- update to 0.1.8-1

* Tue Apr 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- Initial version of the spec file
