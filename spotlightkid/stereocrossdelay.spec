# Status: active
# Tag: Effect
# Type: Plugin, LV2, VST, VST3, LADSPA, CLAP
# Category: Effect

Name: stereocrossdelay
Version: 0.2.0
Release: 2%{?dist}
Summary: A stereo delay plugin with feedback and cross-mixing 
License: MIT
URL: https://github.com/SpotlightKid/stereocrossdelay
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh stereocrossdelay v0.2.0

Source0: stereocrossdelay.tar.gz
Source1: spotlightkid-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: ladspa-devel

%description
A stereo delay plugin with feedback and cross-mixing

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentaion for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary: LADSPA version of %{name}
License: MIT
Requires: license-%{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: MIT
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s/-Wl,--strip-all//g" dpf/Makefile.base.mk

%ifarch aarch64
sed -i -e "s|-msse -msse2||g" dpf/Makefile.base.mk
sed -i -e "s|-mfpmath=sse||g" dpf/Makefile.base.mk
%endif

%build

%set_build_flags

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cd bin
cp -a stereocrossdelay-vst.so %{buildroot}/%{_libdir}/vst/
cp -a stereocrossdelay-ladspa.so %{buildroot}/%{_libdir}/ladspa/
cp -a stereocrossdelay.clap %{buildroot}/%{_libdir}/clap/
cp -ra stereocrossdelay.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra stereocrossdelay.vst3 %{buildroot}/%{_libdir}/vst3/
cd ..

%files -n license-%{name}
%doc README.md CHANGELOG.md
%license LICENSE.md

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Aug 04 2025 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-2
- fix package

* Thu Nov 14 2024 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update to 0.2.0-1

* Wed Dec 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
