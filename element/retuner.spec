# Status: active
# Tag: Pitch
# Type: Plugin, LV2, VST3, CLAP
# Category: Effect

Name: retuner
Version: 1.1.0
Release: 1%{?dist}
Summary: reTuner pitch shifter
URL: https://github.com/kushview/retuner
ExclusiveArch: x86_64 aarch64
License: GPL3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./element-source.sh <PROJECT> <TAG>
#        ./element-source.sh retuner 1.1.0
Source0: retuner.tar.gz
Source1: element-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: pandoc
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils

%description
reTuner is a precision audio pitch shifting plugin designed to convert
music between different tuning standards.
It allows you to seamlessly shift the pitch of audio from one reference
frequency (e.g., A440) to another (e.g., A432), preserving the character
and formants of the original recording.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep

%autosetup -n retuner

%build

%cmake
%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Audio \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/retuner.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/retuner.desktop

%files
%{_bindir}/retuner
%{_datadir}/applications/retuner.desktop
%{_datadir}/icons/hicolor/512x512/apps/retuner.png

%files -n license-%{name}
%doc README.md
%license LICENSE.txt
%{_datadir}/retuner/LICENSE.txt
%{_datadir}/retuner/manual.html

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Jan 07 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- First version of the spec
