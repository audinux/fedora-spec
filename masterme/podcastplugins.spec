# Status: active
# Tag: Editor
# Type: Standalone; Plugin, LADSPA, VST3, CLAP, LV2, VST
# Category: Audio, Effect

Name: podcastplugins
Version: 1.0.0
Release: 1%{?dist}
Summary: speech enhancement audio plugins for podcasters
License: GPL-3.0-or-later
URL: https://github.com/trummerschlunk/PodcastPlugins
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./podcastplugins-source.sh <TAG>
#        ./podcastplugins-source.sh 1.0.0

Source0: PodcastPlugins.tar.gz
Source1: podcastplugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: faust
BuildRequires: boost-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel

Requires: license-%{name}

%description
Podcast Plugins are easy-to-use plugins for speech enhancement, specifically designed
for podcasters who can't or don't want to dig deeper into the craft of sound engineering.

%package -n license-%{name}
Summary:  License and documentation for %{name}
License:  GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n ladspa-%{name}
Summary:  LADSPA version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n ladspa-%{name}
LADSPA version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n PodcastPlugins

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
install -m 755 -d %{buildroot}/%{_libdir}/ladspa/

for PLUGIN in pp-master pp-track
do
    cp bin/$PLUGIN %{buildroot}/%{_bindir}/
    cp bin/$PLUGIN.clap %{buildroot}/%{_libdir}/clap/
    cp -ra bin/$PLUGIN.lv2 %{buildroot}/%{_libdir}/lv2/
    cp -ra bin/$PLUGIN.vst3 %{buildroot}/%{_libdir}/vst3/
    cp bin/$PLUGIN-vst.so %{buildroot}/%{_libdir}/vst/
    cp bin/$PLUGIN-ladspa.so %{buildroot}/%{_libdir}/ladspa/
done

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%files -n ladspa-%{name}
%{_libdir}/ladspa/*

%changelog
* Fri Apr 04 2025 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial version of the spec
