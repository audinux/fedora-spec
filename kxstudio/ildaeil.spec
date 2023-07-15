Name:    Ildaeil
Version: 1.3
Release: 1%{?dist}
Summary: mini-plugin host as plugin
License: GPL-2.0-or-later
URL:     https://github.com/DISTRHO/Ildaeil

Vendor:       Audinux
Distribution: Audinux

# Usage: ./Ildaeil-source.sh <tag>
#        ./Ildaeil-source.sh v1.3

Source0: Ildaeil.tar.gz
Source1: Ildaeil-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: liblo-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fluidsynth-devel
BuildRequires: fftw-devel
BuildRequires: libsmf-devel
BuildRequires: mxml-devel
BuildRequires: non-ntk-devel
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: SDL2-devel
BuildRequires: cairo-devel
BuildRequires: dbus-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: rtaudio-devel
BuildRequires: libsndfile-devel

%description
DISTRHO Ildaeil is mini-plugin host working as a plugin, allowing one-to-one plugin format reusage.
The idea is to load it as a plugin inside your DAW and then the other "real" plugin inside Ildaeil.
This allows, for example, a VST3 host to load LV2 plugins.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

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

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n Ildaeil

%build

%set_build_flags

%make_build PREFIX=/usr SKIP_STRIPPING=true

%install 

%make_install PREFIX=/usr SKIP_STRIPPING=true

mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Jul 15 2023 Yann Collette <ycollette.nospam@free.fr> - 1.3-1
- update to 1.3-1

* Tue May 16 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2-1
- Initial build
