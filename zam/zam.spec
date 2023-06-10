# Tag: Jack, Compressor, Overdrive, Equalizer, Delay, Gate
# Type: Plugin, LV2, VST
# Category: Audio, Effect

Name:    zam-mao-plugins
Version: 4.1
Release: 4%{?dist}
Summary: Set of LV2 / VST / VST3 / CLAPS plugins
License: GPL-2.0-or-later AND ISC
URL:     http://www.zamaudio.com/

Vendor:       Audinux
Distribution: Audinux

# ./zam-source.sh 4.1
Source0: zam-plugins-%{version}.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libsamplerate-devel
BuildRequires: zita-convolver-devel

Obsoletes: zam-plugins
Obsoletes: zam < 4.0-4

%description
Zam LV2 set of plugins
Compressors, Limiters, Saturation, Tube emulation, 
Equalizers, Delay, Gates

%package -n ladspa-%{name}
Summary: Zam LADSPA plugin
Obsoletes: ladspa-zam-plugins
Obsoletes: ladspa-zam < 4.0-4

%description -n ladspa-%{name}
Zam LADSPA plugin

%package -n vst-%{name}
Summary: Zam VST plugin

%description -n vst-%{name}
Zam VST plugin

%package -n vst3-%{name}
Summary: Zam VST3 plugin

%description -n vst3-%{name}
Zam VST3 plugin

%package -n lv2-%{name}
Summary: Zam LV2 plugin
Obsoletes: lv2-zam-plugins
Obsoletes: lv2-zam < 4.0-4

%description -n lv2-%{name}
Zam LV2 plugin

%package -n clap-%{name}
Summary: Zam CLAP plugin

%description -n clap-%{name}
Zam CLAP plugin

%prep
%autosetup -n zam-plugins-%{version}

%build

%set_build_flags
%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true USE_SYSTEM_LIBS=1 all

%install 

%make_install PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true USE_SYSTEM_LIBS=1 install

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -a bin/*.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
for Files in bin/*.vst3
do
  cp -ra $Files %{buildroot}/%{_libdir}/vst3/
done

%files
%doc changelog README.md
%license COPYING
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/* 

%files -n ladspa-%{name}
%{_libdir}/ladspa/* 

%files -n vst-%{name}
%{_libdir}/vst/* 

%files -n clap-%{name}
%{_libdir}/clap/* 

%files -n vst3-%{name}
%{_libdir}/vst3/* 

%changelog
* Wed Dec 21 2022 Yann Collette <ycollette.nospam@free.fr> - 4.1-4
- update to 4.1-4

* Wed Dec 14 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0-4
- update to 4.0-4 - add lv2 sub-package

* Wed Dec 14 2022 Yann Collette <ycollette.nospam@free.fr> - 4.0-3
- update to 4.0-3

* Sun Dec 20 2020 Yann Collette <ycollette.nospam@free.fr> - 3.14-3
- update to 3.14

* Sun Jul 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.13-3
- fix debug build

* Sun Jul 19 2020 Yann Collette <ycollette.nospam@free.fr> - 3.13-2
- update to zam-plugins-3.13

* Sun Dec 15 2019 Yann Collette <ycollette.nospam@free.fr> - 3.12-2
- update to zam-plugins-3.12

* Tue Jun 4 2019 Yann Collette <ycollette.nospam@free.fr> - 3.11-2
- update to zam-plugins-3.11

* Tue Apr 30 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10-2
- update to zam-plugins-3.10-10-g7232969

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.10-2
- update for Fedora 29
- update to zam-plugins-3.10-10-g7232969.tar.xz

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 3.10
- update version to 3.10

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build
