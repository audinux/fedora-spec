Name:    wavetable
Version: 0.0.11
Release: 1%{?dist}
Summary: Wavetable synth
License: BSD-3-Clause
URL:     https://github.com/FigBug/Wavetable

Vendor:       Audinux
Distribution: Audinux

# ./figbug-source.sh <project> <tag>
# ./figbug-source.sh Wavetable 0.0.11

Source0: Wavetable.tar.gz
Source1: figbug-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel

%description
Wavetable synth

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: BSD-3-Clause
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: BSD-3-Clause
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n Wavetable

%build

%cmake
%cmake_build

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_bindir}/

install -m 755 -p %{__cmake_builddir}/Wavetable_artefacts/Standalone/Wavetable %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/Wavetable_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Wavetable_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Thu Sep 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.11-1
- update to 0.0.11-1

* Wed Sep 20 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.10-1
- update to 0.0.10-1

* Sun Sep 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.8-1
- update to 0.0.8-1

* Thu Sep 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.7-1
- update to 0.0.7-1

* Tue Sep 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.5-1
- Initial spec file
