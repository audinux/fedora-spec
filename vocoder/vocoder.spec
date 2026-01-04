# Status: active
# Tag: Plugin
# Type: Plugin, LV2, CLAP, LADSPA
# Category: Audio, Effect

Name: vocoder
Version: 1.1.1
Release: 1%{?dist}
Summary: Simple LADSPA/LV2/CLAP vocoder plugin using DPF
License: GPL-2.0-or-later
URL: https://github.com/Stazed/vocoder
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./vocoder-source.sh <TAG>
#        ./vocoder-source.sh 1.1.1

Source0: vocoder.tar.gz
Source1: vocoder-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
Vocoder is a simple LADSPA/LV2/CLAP plugin for vocoding based on VocProc

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

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%prep
%autosetup -n %{name}

%build

%cmake -DPluginLibDir=%{_lib}
%cmake_build

%install

%cmake_install

%files
%doc README.md
%license COPYING

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%changelog
* Sun Jan 04 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- update to 1.1.1-1

* Tue Dec 23 2025 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0-1

* Mon Jan 22 2024 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
