# Tag: Synthesizer
# Type: LV2
# Category: Synthesizer

# Global variables for github repository
%global commit0 df67460fc344f94db4306d4ee21e4207e657bbee
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    ryukau
Version: 0.0.1.%{shortcommit0}
Release: 3%{?dist}
Summary: Some audio plugins (LV2 and VST) from ruykau
License: GPLv2+
URL:     https://github.com/ryukau/LV2Plugins/

Vendor:       Audinux
Distribution: Audinux

# ./ryukau-source.sh <tag>
# ./ryukau-source.sh df67460fc344f94db4306d4ee21e4207e657bbee

Source0: ryukau.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
Some audio plugins (LV2 and VST) from ruykau

%prep
%autosetup -n %{name}

# Too expensive to compile
#sed -i -e "/CubicPadSynth/d" Makefile
#sed -i -e "/LightPadSynth/d" Makefile
##ed -i -e "/L4Reverb/d" Makefile

# Remove some non generic flags
#for Flags in mavx512f mfma mavx512vl mavx512bw mavx512dq mavx512f mavx2 mfma msse4.1 msse2
#do
#  for Files in `find . -name Makefile -exec grep -l $Flags {} \;`
#  do
#    sed -i -e "s/-$Flags//g" $Files
#  done
#done
#for Files in `find . -name Makefile -exec grep -l "std=c++17" {} \;`
#do
#  sed -i -e "s/-std=c++17/-O2 -std=c++17/g" $Files
#done

%build

%set_build_flags

export CXXFLAGS="$CXXFLAGS -include array"
%make_build PREFIX=/usr LIBDIR=%{_lib} VERBOSE=1 SKIP_STRIPPING=true LDFLAGS="%{build_ldflags} -ldl" -j1

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2
install -m 755 -d %{buildroot}/%{_libdir}/vst

cp bin/EnvelopedSine       %{buildroot}/%{_bindir}/
cp bin/EsPhaser            %{buildroot}/%{_bindir}/
cp bin/FDNCymbal           %{buildroot}/%{_bindir}/
cp bin/IterativeSinCluster %{buildroot}/%{_bindir}/
cp bin/SevenDelay          %{buildroot}/%{_bindir}/
cp bin/SyncSawSynth        %{buildroot}/%{_bindir}/
cp bin/TrapezoidSynth      %{buildroot}/%{_bindir}/
cp bin/WaveCymbal          %{buildroot}/%{_bindir}/

cp -r bin/EnvelopedSine.lv2/*       %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2/
cp -r bin/EsPhaser.lv2/*            %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2/
cp -r bin/FDNCymbal.lv2/*           %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2/
cp -r bin/IterativeSinCluster.lv2/* %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2/
cp -r bin/SevenDelay.lv2/*          %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2/
cp -r bin/SyncSawSynth.lv2/*        %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2/
cp -r bin/TrapezoidSynth.lv2/*      %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2/
cp -r bin/WaveCymbal.lv2/*          %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2/

cp bin/EnvelopedSine-vst.so       %{buildroot}/%{_libdir}/vst/
cp bin/EsPhaser-vst.so            %{buildroot}/%{_libdir}/vst/
cp bin/FDNCymbal-vst.so           %{buildroot}/%{_libdir}/vst/
cp bin/IterativeSinCluster-vst.so %{buildroot}/%{_libdir}/vst/
cp bin/SevenDelay-vst.so          %{buildroot}/%{_libdir}/vst/
cp bin/SyncSawSynth-vst.so        %{buildroot}/%{_libdir}/vst/
cp bin/TrapezoidSynth-vst.so      %{buildroot}/%{_libdir}/vst/
cp bin/WaveCymbal-vst.so          %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*

%changelog
* Sun May 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-df67460f-3
- update to df67460f

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-fae2ad4b-2
- fix debug build and update to fae2ad4b

* Wed Feb 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6bcd263e-1
- Initial spec file for 6bcd263e
