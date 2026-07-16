# Status: active
# Tag: Filter
# Type: Plugin, LV2, CLAP
# Category: Audio, Effect

Name: ToneShiftEQ
Version: 0.5.0
Release: 1%{?dist}
Summary: ToneShiftEQ is a modern 12-band equalizer designed for precise spectral shaping, mixing, mastering, and corrective audio processing.
License: GPL-2.0-or-later
URL: https://github.com/brummer10/ToneTwistPlugs
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./brummer10-source.sh ToneShiftEQ v0.5.0

Source0: ToneShiftEQ.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: git
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: vim-common

Requires: license-%{name}

%description
ToneShiftEQ is a modern 12-band equalizer designed for precise spectral shaping, mixing, mastering, and corrective audio processing.
It can operate in two different modes:
- Master -> Master -> Perfect linear-phase response with 128 samples of latency, ideal for mastering and critical processing.
- Live -> Zero-latency processing with slight phase deviation, optimized for real-time performance and live use.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-2.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-2.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n ToneShiftEQ

%build

%set_build_flags
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%make_build STRIP=true
%make_build STRIP=true clap lv2

%install

install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 bin/toneshifteq %{buildroot}/%{_bindir}/

cp -ra bin/*.lv2 %{buildroot}%{_libdir}/lv2/
cp -ra bin/*.clap %{buildroot}%{_libdir}/clap/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Wed Jul 15 2026 Yann Collette <ycollette.nospam@free.fr> - 0.5.0-1
- update to 0.5.0-1

* Wed Jul 01 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial spec file
