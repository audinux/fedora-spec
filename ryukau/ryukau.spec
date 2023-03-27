# Tag: Synthesizer
# Type: LV2
# Category: Synthesizer

# Global variables for github repository
%global commit0 e5eee4c3

Name:    ryukau
Version: 0.0.1.%{commit0}
Release: 4%{?dist}
Summary: Some audio plugins (LV2 and VST) from ruykau
License: GPLv2+
URL:     https://github.com/Wasted-Audio/ryukau_LV2Plugins

Vendor:       Audinux
Distribution: Audinux

# ./ryukau-source.sh <tag>
# ./ryukau-source.sh e5eee4c3

Source0: ryukau.tar.gz
Source11: ryukau-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: lv2-devel
BuildRequires: dssi-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel

%description
Some audio plugins (LV2 and VST) from ruykau

%package -n vst-%{name}
Summary:  VST version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

%ifarch aarch64
for Files in `find . -name Makefile`
do
  sed -i -e "s/-mavx512f -mfma -mavx512vl -mavx512bw -mavx512dq//g" $Files
done
%endif

%build

%set_build_flags

export CXXFLAGS="$CXXFLAGS -include array"
%make_build PREFIX=/usr LIBDIR=%{_lib} VERBOSE=1 SKIP_STRIPPING=true LDFLAGS="$LDFLAGS -ldl"

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CollidingCombSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CubicPadSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_3PoleLP.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_AudioToCv.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_CvToAudio.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_DelayLP3.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_DoubleFilter.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_ExpADSREnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_ExpLoopEnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_ExpPolyADEnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_Gate16.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_HoldFilter.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_Invert.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_LinearADSREnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_LinearMap.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_LongAllpass.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_Multiply.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_NaiveDelay.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_NestedLongAllpass.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_ParabolicADEnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PController.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope2.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope4.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PTRSaw.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_PTRTrapezoid.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_RampFilter.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_RateLimiter.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_Sin.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_StereoGain.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/CV_TimeInfo.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/FoldShaper.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/L3Reverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/L4Reverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/LatticeReverb.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/LightPadSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/ModuloShaper.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/OddPowShaper.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SoftClipper.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2
install -m 755 -d %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -r bin/CollidingCombSynth.lv2/* %{buildroot}/%{_libdir}/lv2/CollidingCombSynth.lv2
cp -r bin/CubicPadSynth.lv2/* %{buildroot}/%{_libdir}/lv2/CubicPadSynth.lv2
cp -r bin/CV_3PoleLP.lv2/* %{buildroot}/%{_libdir}/lv2/CV_3PoleLP.lv2
cp -r bin/CV_AudioToCv.lv2/* %{buildroot}/%{_libdir}/lv2/CV_AudioToCv.lv2
cp -r bin/CV_CvToAudio.lv2/* %{buildroot}/%{_libdir}/lv2/CV_CvToAudio.lv2
cp -r bin/CV_DelayLP3.lv2/* %{buildroot}/%{_libdir}/lv2/CV_DelayLP3.lv2
cp -r bin/CV_DoubleFilter.lv2/* %{buildroot}/%{_libdir}/lv2/CV_DoubleFilter.lv2
cp -r bin/CV_ExpADSREnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_ExpADSREnvelope.lv2
cp -r bin/CV_ExpLoopEnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_ExpLoopEnvelope.lv2
cp -r bin/CV_ExpPolyADEnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_ExpPolyADEnvelope.lv2
cp -r bin/CV_Gate16.lv2/* %{buildroot}/%{_libdir}/lv2/CV_Gate16.lv2
cp -r bin/CV_HoldFilter.lv2/* %{buildroot}/%{_libdir}/lv2/CV_HoldFilter.lv2
cp -r bin/CV_Invert.lv2/* %{buildroot}/%{_libdir}/lv2/CV_Invert.lv2
cp -r bin/CV_LinearADSREnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_LinearADSREnvelope.lv2
cp -r bin/CV_LinearMap.lv2/* %{buildroot}/%{_libdir}/lv2/CV_LinearMap.lv2
cp -r bin/CV_LongAllpass.lv2/* %{buildroot}/%{_libdir}/lv2/CV_LongAllpass.lv2
cp -r bin/CV_Multiply.lv2/* %{buildroot}/%{_libdir}/lv2/CV_Multiply.lv2
cp -r bin/CV_NaiveDelay.lv2/* %{buildroot}/%{_libdir}/lv2/CV_NaiveDelay.lv2
cp -r bin/CV_NestedLongAllpass.lv2/* %{buildroot}/%{_libdir}/lv2/CV_NestedLongAllpass.lv2
cp -r bin/CV_ParabolicADEnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_ParabolicADEnvelope.lv2
cp -r bin/CV_PController.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PController.lv2
cp -r bin/CV_PolyLoopEnvelope2.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope2.lv2
cp -r bin/CV_PolyLoopEnvelope4.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope4.lv2
cp -r bin/CV_PolyLoopEnvelope.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PolyLoopEnvelope.lv2
cp -r bin/CV_PTRSaw.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PTRSaw.lv2
cp -r bin/CV_PTRTrapezoid.lv2/* %{buildroot}/%{_libdir}/lv2/CV_PTRTrapezoid.lv2
cp -r bin/CV_RampFilter.lv2/* %{buildroot}/%{_libdir}/lv2/CV_RampFilter.lv2
cp -r bin/CV_RateLimiter.lv2/* %{buildroot}/%{_libdir}/lv2/CV_RateLimiter.lv2
cp -r bin/CV_Sin.lv2/* %{buildroot}/%{_libdir}/lv2/CV_Sin.lv2
cp -r bin/CV_StereoGain.lv2/* %{buildroot}/%{_libdir}/lv2/CV_StereoGain.lv2
cp -r bin/CV_TimeInfo.lv2/* %{buildroot}/%{_libdir}/lv2/CV_TimeInfo.lv2
cp -r bin/EnvelopedSine.lv2/* %{buildroot}/%{_libdir}/lv2/EnvelopedSine.lv2
cp -r bin/EsPhaser.lv2/* %{buildroot}/%{_libdir}/lv2/EsPhaser.lv2
cp -r bin/FDNCymbal.lv2/* %{buildroot}/%{_libdir}/lv2/FDNCymbal.lv2
cp -r bin/FoldShaper.lv2/* %{buildroot}/%{_libdir}/lv2/FoldShaper.lv2
cp -r bin/IterativeSinCluster.lv2/* %{buildroot}/%{_libdir}/lv2/IterativeSinCluster.lv2
cp -r bin/L3Reverb.lv2/* %{buildroot}/%{_libdir}/lv2/L3Reverb.lv2
cp -r bin/L4Reverb.lv2/* %{buildroot}/%{_libdir}/lv2/L4Reverb.lv2
cp -r bin/LatticeReverb.lv2/* %{buildroot}/%{_libdir}/lv2/LatticeReverb.lv2
cp -r bin/LightPadSynth.lv2/* %{buildroot}/%{_libdir}/lv2/LightPadSynth.lv2
cp -r bin/ModuloShaper.lv2/* %{buildroot}/%{_libdir}/lv2/ModuloShaper.lv2
cp -r bin/OddPowShaper.lv2/* %{buildroot}/%{_libdir}/lv2/OddPowShaper.lv2
cp -r bin/SevenDelay.lv2/* %{buildroot}/%{_libdir}/lv2/SevenDelay.lv2
cp -r bin/SoftClipper.lv2/* %{buildroot}/%{_libdir}/lv2/SoftClipper.lv2
cp -r bin/SyncSawSynth.lv2/* %{buildroot}/%{_libdir}/lv2/SyncSawSynth.lv2
cp -r bin/TrapezoidSynth.lv2/* %{buildroot}/%{_libdir}/lv2/TrapezoidSynth.lv2
cp -r bin/WaveCymbal.lv2/* %{buildroot}/%{_libdir}/lv2/WaveCymbal.lv2

install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/CollidingCombSynth  %{buildroot}/%{_bindir}/
cp bin/CubicPadSynth  %{buildroot}/%{_bindir}/
cp bin/EnvelopedSine  %{buildroot}/%{_bindir}/
cp bin/EsPhaser  %{buildroot}/%{_bindir}/
cp bin/FDNCymbal  %{buildroot}/%{_bindir}/
cp bin/FoldShaper  %{buildroot}/%{_bindir}/
cp bin/IterativeSinCluster  %{buildroot}/%{_bindir}/
cp bin/L3Reverb  %{buildroot}/%{_bindir}/
cp bin/L4Reverb  %{buildroot}/%{_bindir}/
cp bin/LatticeReverb  %{buildroot}/%{_bindir}/
cp bin/LightPadSynth  %{buildroot}/%{_bindir}/
cp bin/ModuloShaper  %{buildroot}/%{_bindir}/
cp bin/OddPowShaper  %{buildroot}/%{_bindir}/
cp bin/SevenDelay  %{buildroot}/%{_bindir}/
cp bin/SoftClipper  %{buildroot}/%{_bindir}/
cp bin/SyncSawSynth  %{buildroot}/%{_bindir}/
cp bin/TrapezoidSynth  %{buildroot}/%{_bindir}/
cp bin/WaveCymbal  %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp bin/CollidingCombSynth-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/CubicPadSynth-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/EnvelopedSine-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/EsPhaser-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/FDNCymbal-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/FoldShaper-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/IterativeSinCluster-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/L3Reverb-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/L4Reverb-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/LatticeReverb-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/LightPadSynth-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/ModuloShaper-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/OddPowShaper-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/SevenDelay-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/SoftClipper-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/SyncSawSynth-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/TrapezoidSynth-vst.so  %{buildroot}/%{_libdir}/vst/
cp bin/WaveCymbal-vst.so  %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%{_bindir}/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Sun Oct 09 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-e5eee4c3-4
- update to e5eee4c3

* Sun May 01 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-df67460f-3
- update to df67460f

* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-fae2ad4b-2
- fix debug build and update to fae2ad4b

* Wed Feb 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6bcd263e-1
- Initial spec file for 6bcd263e
