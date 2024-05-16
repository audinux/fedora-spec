# Tag: Editor
# Type: Standalone; Plugin, VST3, CLAP, LV2, VST
# Category: Audio, Effect

Name: master_me
Version: 1.2.0
Release: 1%{?dist}
Summary: automatic mastering plugin for live streaming, podcasts and internet radio
License: GPL-2.0-or-later
URL: https://github.com/trummerschlunk/master_me
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./masterme-source.sh <TAG>
#        ./masterme-source.sh 1.2.0

Source0: master_me.tar.gz
Source1: masterme-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: faust
BuildRequires: boost-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

%description
Automatic audio mastering plugin for live-streaming,
podcasting and internet radio stations.

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
VST2 version of %{name}

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
%autosetup -n %{name}

sed -i -e "s/FAUSTPP_USE_INTERNAL_BOOST=ON/FAUSTPP_USE_INTERNAL_BOOST=OFF/g" Makefile
sed -i -e "s/git clone/#git clone/g" Makefile

%build

%set_build_flags
%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/clap/

cp bin/master_me %{buildroot}/%{_bindir}/
cp bin/master_me.clap %{buildroot}/%{_libdir}/clap/
cp -ra bin/master_me-easy-presets.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra bin/master_me.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra bin/master_me.vst3 %{buildroot}/%{_libdir}/vst3/
cp bin/master_me-vst.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sun Apr 16 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- update to 1.2.0-1

* Wed Sep 28 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial version of the spec
