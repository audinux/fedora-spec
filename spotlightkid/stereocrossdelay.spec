# Tag: Effect
# Type: LV2
# Category: Effect

Name:    stereocrossdelay
Version: 0.1
Release: 1%{?dist}
Summary: A stereo delay plugin with feedback and cross-mixing 
License: MIT
URL:     https://github.com/SpotlightKid/stereocrossdelay

Vendor:       Audinux
Distribution: Audinux

# To get the sources:
# ./spotlightkid-source.sh <project> <tag>
# ./spotlightkid-source.sh stereocrossdelay b637627eda3189c3c2ff0f5512a78a76e7383285

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

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst-%{name}
VST2 version of %{name}

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
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/

cd bin
cp -a stereocrossdelay-vst.so %{buildroot}/%{_libdir}/vst/
cp -a stereocrossdelay-ladspa.so %{buildroot}/%{_libdir}/ladspa/
cp -ra stereocrossdelay.lv2 %{buildroot}/%{_libdir}/lv2/
cd ..

%files
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Wed Dec 27 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- Initial build
