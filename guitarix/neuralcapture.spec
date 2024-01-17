# Tag: Tool, AI
# Type: Plugin, LV2, VST3, Stqndqlone
# Category: Audio, Tool

Name: neuralrecord
Version: 0.1.9
Release: 1%{?dist}
Summary: A Neural Record plug to make the process of cloning external soft/hardware a bit more comfortable
License: BSD
URL: https://github.com/brummer10/neuralrecord

Vendor:       Audinux
Distribution: Audinux

# ./brummer10-source.sh <project> <tag>
# ./brummer10-source.sh neuralcapture v0.1.9

Source0: neuralcapture.tar.gz
Source1: brummer10-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: libXext-devel
BuildRequires: SDL2-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libglvnd-devel
BuildRequires: libXrandr-devel
BuildRequires: vulkan-loader-devel
BuildRequires: liblo-devel
BuildRequires: libXcursor-devel
BuildRequires: cairo-devel
BuildRequires: libsndfile-devel

%description
A Neural Record plug to make the process of cloning external
soft/hardware a bit more comfortable

%package -n lv2-%{name}
Summary: LV2 version of the %{name} plugin.

%description -n lv2-%{name}
LV2 version of the %{name} plugin.

%package -n vst3-%{name}
Summary: VST3 version of the %{name} plugin.

%description -n vst3-%{name}
VST version of the %{name} plugin.

%prep
%autosetup -n neuralcapture

%build

%set_build_flags

%make_build SKIP_STRIPPING=true

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp bin/neuralrecord          %{buildroot}/%{_bindir}/
cp -ra bin/neuralrecord.lv2  %{buildroot}/%{_libdir}/lv2/
cp -ra bin/neuralrecord.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sat Nov 25 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.9-1
- update to 0.1.9-1

* Tue Oct 31 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.8-1
- update to 0.1.8-1

* Fri Oct 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.7-1
- update to 0.1.7-1

* Thu Oct 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.6-1
- update to 0.1.6-1

* Fri Sep 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.4-1
- update to 0.1.4-1

* Tue Sep 05 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.3-1
- update to 0.1.3-1

* Sat Sep 02 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.2-1
- update to 0.1.2-1

* Fri Sep 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1.1-1
- Initial spec file
