# Tag: Jack, Alsa, Overdrive
# Type: Plugin, Standalone, VST, LV2, DSSI
# Category: Audio, Effect

Name:    wolf-shaper
Version: 1.0.0
Release: 2%{?dist}
Summary: Wolf-shaper is a waveshaper plugin with a graph editor.
License: GPLv2+
URL:     https://github.com/pdesaulniers/wolf-shaper

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/wolf-plugins/wolf-shaper/releases/download/v%{version}/wolf-shaper-v%{version}-source.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
Wolf Shaper is a waveshaper plugin with a graph editor.

%package -n dssi-%{name}
Summary: DSSI version of the Wolf Shaper plugin.

%package -n lv2-%{name}
Summary: LV2 version of the Wolf Shaper plugin.

%package -n vst-%{name}
Summary: VST version of the Wolf Shaper plugin.

%package -n vst3-%{name}
Summary: VST3 version of the Wolf Shaper plugin.

%package -n clap-%{name}
Summary: CLAP version of the Wolf Shaper plugin.


%description -n dssi-%{name}
DSSI version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n lv2-%{name}
LV2 version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n vst-%{name}
VST version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n vst3-%{name}
VST3 version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%description -n clap-%{name}
CLAP version of the Wolf Shaper plugin.
Wolf Shaper is a waveshaper plugin with a graph editor.

%prep
%autosetup -n %{name}

%build

%set_build_flags

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/dssi/

cp %__cmake_builddir/bin/wolf-shaper %{buildroot}/%{_bindir}/
cp -ra %__cmake_builddir/bin/wolf-shaper.clap %{buildroot}/%{_libdir}/clap/
cp -ra %__cmake_builddir/bin/wolf-shaper-dssi %{buildroot}/%{_libdir}/dssi/
cp %__cmake_builddir/bin/wolf-shaper-dssi.so %{buildroot}/%{_libdir}/dssi/
cp -ra %__cmake_builddir/bin/wolf-shaper.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra %__cmake_builddir/bin/wolf-shaper.vst3 %{buildroot}/%{_libdir}/vst3/
cp %__cmake_builddir/bin/wolf-shaper-vst.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n dssi-%{name}
%{_libdir}/dssi/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Dec 29 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-2
- update to 0.1.8-2 - fix debug buid

* Wed Oct 2 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- update to 0.1.8-1

* Tue Apr 16 2019 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- Initial version of the spec file
