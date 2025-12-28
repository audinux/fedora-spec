# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3, LV2, CLAP
# Category: Audio, Synthesizer

%global commit0 aa23b122b5f51bc28218791f4a961043e1d86ba3

Name: obxf
Version: 0.1
Release: 2%{?dist}
Summary: OB-Xf is a continuation and modernatization of the last open source release of OB-Xd by 2DaT and later discoDSP
License: GPL-3.0-only
URL: https://github.com/surge-synthesizer/OB-Xf
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/surge-synthesizer/OB-Xf/archive/%{commit0}.zip#/%{name}-%{version}.zip
Patch0: obxf-0001-remove-Werror.patch
Patch1: obxf-0002-remove-fetchcontent-for-fmt.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: fmt-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: chrpath

Requires: license-%{name}

%description
OB-Xf is a continuation of the last open source version of OB-Xd by 2DaT and later discoDSP,
bringing together several efforts going on in the audio space and combining them inside
the Surge Synth Team infrastructure.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-only

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-only
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -p1 -n OB-Xf-%{commit0}

%build

%set_build_flags

export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=redundant-move//g"`

%cmake -DGIT_COMMIT_HASH="00000000"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/clap/

cp -ra %{__cmake_builddir}/OB-Xf_artefacts/Standalone/* %{buildroot}/%{_bindir}/
cp -ra %{__cmake_builddir}/OB-Xf_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/OB-Xf_artefacts/LV2/* %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/OB-Xf_artefacts/CLAP/* %{buildroot}/%{_libdir}/clap/

chrpath --delete `find %{buildroot}/usr/%{_lib}/vst3/ -name "*.so"`
chrpath --delete `find %{buildroot}/usr/%{_lib}/lv2/ -name "*.so"`
chrpath --delete `find %{buildroot}/usr/%{_lib}/clap/ -name "*.clap"`
chrpath --delete `find %{buildroot}/usr/bin/ -executable -type f`

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md HISTORY.md
%license LICENSE

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Aug 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Try to fix a dependency problem

* Fri Aug 01 2025 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
