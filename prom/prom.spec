# Tag: Live, Video
# Type: Plugin, LV2, VST, VST3, CLAP
# Category: Effect

%global commit0 8686010aad8c5b7649cba7d820994b90998dbe53

Name: prom
Version: 0.0.1
Release: 2%{?dist}
Summary: ProjectM LV2 plugin
License: GPL-2.0-or-later
URL: https://github.com/DISTRHO/ProM

Vendor:       Audinux
Distribution: Audinux

Source0: ProM.tar.gz
Source1: source-prom.sh

# ./source-prom.sh <tag>
# ./source-prom.sh master

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: liblo-devel
BuildRequires: projectM-mao-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
A ProjectM LV2 plugin

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

%prep
%autosetup -n ProM

%build

%make_build PREFIX=/usr LIBDIR=%{_lib} SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_datadir}/ProM/data/
cp -ra plugins/ProM/projectM/presets %{buildroot}/%{_datadir}/ProM/data/
cp -ra plugins/ProM/projectM/fonts/ %{buildroot}/%{_datadir}/ProM/data/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra bin/ProM.clap %{buildroot}/%{_libdir}/clap/
rm -rf %{buildroot}/%{_libdir}/clap/ProM.clap/resources/presets
rm -rf %{buildroot}/%{_libdir}/clap/ProM.clap/resources/fonts
ln -s %{_datadir}/ProM/data/presets %{buildroot}/%{_libdir}/clap/ProM.clap/resources/presets
ln -s %{_datadir}/ProM/data/fonts %{buildroot}/%{_libdir}/clap/ProM.clap/resources/fonts

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra bin/ProM.lv2 %{buildroot}/%{_libdir}/lv2/
rm -rf %{buildroot}/%{_libdir}/lv2/ProM.lv2/resources/presets
rm -rf %{buildroot}/%{_libdir}/lv2/ProM.lv2/resources/fonts
ln -s %{_datadir}/ProM/data/presets %{buildroot}/%{_libdir}/lv2/ProM.lv2/resources/presets
ln -s %{_datadir}/ProM/data/fonts %{buildroot}/%{_libdir}/lv2/ProM.lv2/resources/fonts

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp -ra bin/ProM.vst %{buildroot}/%{_libdir}/vst/
rm -rf %{buildroot}/%{_libdir}/vst/ProM.vst/resources/presets
rm -rf %{buildroot}/%{_libdir}/vst/ProM.vst/resources/fonts
ln -s %{_datadir}/ProM/data/presets %{buildroot}/%{_libdir}/vst/ProM.vst/resources/presets
ln -s %{_datadir}/ProM/data/fonts %{buildroot}/%{_libdir}/vst/ProM.vst/resources/fonts

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra bin/ProM.vst3 %{buildroot}/%{_libdir}/vst3/
rm -rf %{buildroot}/%{_libdir}/vst3/ProM.vst3/Contents/Resources/presets
rm -rf %{buildroot}/%{_libdir}/vst3/ProM.vst3/Contents/Resources/fonts
ln -s %{_datadir}/ProM/data/presets %{buildroot}/%{_libdir}/vst3/ProM.vst3/Contents/Resources/presets
ln -s %{_datadir}/ProM/data/fonts %{buildroot}/%{_libdir}/vst3/ProM.vst3/Contents/Resources/fonts

%files
%doc README.md
%license LICENSE
%{_datadir}/ProM/
%{_datadir}/ProM/data/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Sun Oct 23 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to version 0.0.1-2

* Tue Oct 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial release
