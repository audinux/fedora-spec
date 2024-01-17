# Tag: Guitar, Jack
# Type: Standalone
# Category: Audio, Tool

Name: stomptuner
Version: 0.2
Release: 1%{?dist}
Summary: Tuner for Jack Audio Connection Kit
License: GPL-2.0-or-later
URL: https://github.com/brummer10/StompTuner

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh StompTuner v0.2

Source0: StompTuner.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: fftw-devel
BuildRequires: libsigc++20-devel
BuildRequires: zita-resampler-devel
BuildRequires: desktop-file-utils

%description
StompTuner, a Strobe Tuner in Stomp Box Format. The Strobe provide 2 indicators.
The outer ring have a accuracy of 1.0 Cent, the inner ring have a accuracy at 0.1 Cent.
The working frequency range is from 24 - 998 Hz. The reference Pitch could be selected
between 432 - 452 Hz.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n StompTuner

%build

%set_build_flags

%make_build SKIP_STRIPPING=true

%install

%make_install PREFIX=/usr LIBDIR=/usr/%{_lib}/ SKIP_STRIPPING=true

%files
%doc README.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Oct 26 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2-1
- Initial spec file
