# Tag: Guitar, Emulator, Overdrive, Amp Simul, Cabinet
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    GxPlugins
Version: 0.9
Release: 1%{?dist}
Summary: Guitarix LV2 plugins collection
License: GPLv2+
URL:     https://github.com/brummer10/GxPlugins.lv2

Vendor:       Audinux
Distribution: Audinux

# ./gxplugins-source.sh <tag>
# ./gxplugins-source.sh v0.9

Source0: GxPlugins.lv2.tar.gz
Source1: gxplugins-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: vim-common

%description
Large collection of guitar effects and simulations.

%package -n lv2-GxBottleRocket-plugin
Summary: Analogue simulation of a tube preamp
Group:   Applications/Multimedia
%description -n lv2-GxBottleRocket-plugin
LV2 Analogue simulation of a tube preamp from Guitarix

%package -n lv2-GxGuvnor-plugin
Summary: Overdrive/distortion pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxGuvnor-plugin
LV2 Overdrive/distortion pedal simulation from Guitarix

%package -n lv2-GxHotBox-plugin
Summary: Analogue simulation of a tube preamp with overdrive
Group:   Applications/Multimedia
%description -n lv2-GxHotBox-plugin
Analogue simulation of a tube preamp with overdrive and interactive tone control from Guitarix

%package -n lv2-GxHyperion-plugin
Summary: Simulation of the Hyperion Fuzz Pedal
Group:   Applications/Multimedia
%description -n lv2-GxHyperion-plugin
Simulation of the Hyperion Fuzz Pedal

%package -n lv2-GxQuack-plugin
Summary: Envelope controlled wah pedal with some extra features
Group:   Applications/Multimedia
%description -n lv2-GxQuack-plugin
Envelope controlled wah pedal with some extra features from Guitarix

%package -n lv2-GxSaturator-plugin
Summary: Saturation plugin
Group:   Applications/Multimedia
%description -n lv2-GxSaturator-plugin
A LV2 saturation plugin from Guitarix

%package -n lv2-GxSD1-plugin
Summary: Super Overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxSD1-plugin
Super Overdrive pedal simulation from Guitarix

%package -n lv2-GxSD2Lead-plugin
Summary: SD2 overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxSD2Lead-plugin
SD2 overdrive pedal simulation from Guitarix

%package -n lv2-GxSlowGear-plugin
Summary: Automatic pedal volume
Group:   Applications/Multimedia
%description -n lv2-GxSlowGear-plugin
Automatic pedal volume from Guitarix

%package -n lv2-GxSuperFuzz-plugin
Summary: Analog simulation of the UniVox SuperFuzz pedal
Group:   Applications/Multimedia
%description -n lv2-GxSuperFuzz-plugin
Analog simulation of the UniVox (*) SuperFuzz pedal as LV2 plugin from Guitarix

%package -n lv2-GxSuppaToneBender-plugin
Summary: Analog simulation of the Vox Suppa Tone Bender pedal
Group:   Applications/Multimedia
%description -n lv2-GxSuppaToneBender-plugin
Analog simulation of the Vox (*) Suppa Tone Bender pedal as LV2 plugin from Guitarix

%package -n lv2-GxSVT-plugin
Summary: Tube based Bass preamp simulation 
Group:   Applications/Multimedia
%description -n lv2-GxSVT-plugin
Tube based Bass preamp simulation from Guitarix

%package -n lv2-GxToneMachine-plugin
Summary: Analogous simulation of the Foxx Tone Machine Pedal
Group:   Applications/Multimedia
%description -n lv2-GxToneMachine-plugin
Analogous simulation of the Foxx(*) Tone Machine Pedal as LV2 plugin from Guitarix

%package -n lv2-GxUVox720k-plugin
Summary: Analog simulation of the UniVox 720k solid state amp
Group:   Applications/Multimedia
%description -n lv2-GxUVox720k-plugin
Analog simulation of the UniVox (*) 720k solid state amp as LV2 plugin from Guitarix

%package -n lv2-GxVBassPreAmp-plugin
Summary: Analog Simulation of the 1984 Vox Venue Bass 100 Pre Amp Section.
Group:   Applications/Multimedia
%description -n lv2-GxVBassPreAmp-plugin
Analog Simulation of the 1984 (*) Vox Venue Bass 100 Pre Amp Section from Guitarix

%package -n lv2-GxVintageFuzzMaster-plugin
Summary: Simulation of the Vintage Fuzz Master Pedal
Group:   Applications/Multimedia
%description -n lv2-GxVintageFuzzMaster-plugin
Simulation of the Vintage Fuzz Master Pedal from Guitarix

%package -n lv2-GxVmk2-plugin
Summary: ??
Group:   Applications/Multimedia
%description -n lv2-GxVmk2-plugin
?? from Guitarix

%package -n lv2-GxVoodoFuzz-plugin
Summary: Simulation impressed by the Voodoo Lab SuperFuzz pedal
Group:   Applications/Multimedia
%description -n lv2-GxVoodoFuzz-plugin
Simulation impressed by the Voodoo Lab (*) SuperFuzz pedal  from Guitarix

%package -n lv2-AxisFace-plugin
Summary: Simulation of the Axis Face Silicon Pedal
Group:    Applications/Multimedia
%description -n lv2-AxisFace-plugin
Simulation of the Axis Face Silicon Pedal from Guitarix

%package -n lv2-DOP250-plugin
Summary: Overdrive Preamp Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-DOP250-plugin
Overdrive Preamp Pedal simulation from Guitarix

%package -n lv2-Heathkit-plugin
Summary: Distortion Booster Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-Heathkit-plugin
Distortion Booster Pedal simulation from Guitarix

%package -n lv2-KnightFuzz-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-KnightFuzz-plugin
This is a really nasty Fuzz Pedal,
which act at lower/ moderate settings as a ultra dark fuzz,
when settings get cranked up, it becomes more and more high harmonics.  from Guitarix

%package -n lv2-liquiddrive-plugin
Summary: Liquid Drive provides a tonal response with a warm mild to aggressive overdrive
Group:   Applications/Multimedia
%description -n lv2-liquiddrive-plugin
Liquid Drive provides a tonal response with a warm mild to aggressive overdrive, which can do anything from Blues to Hard Rock. from Guitarix

%package -n lv2-maestro_fz1b-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-maestro_fz1b-plugin
Vintage Fuzz Pedal simulation from Guitarix

%package -n lv2-maestro_fz1s-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-maestro_fz1s-plugin
Vintage Fuzz Pedal simulation from Guitarix

%package -n lv2-MicroAmp-plugin
Summary: The MicroAmp is designed to be a transparent clean volume booster
Group:   Applications/Multimedia
%description -n lv2-MicroAmp-plugin
The MicroAmp is designed to be a transparent clean volume booster from Guitarix

%package -n lv2-quack-plugin
Summary: Envelope controlled wah pedal
Group:   Applications/Multimedia
%description -n lv2-quack-plugin
Envelope controlled wah pedal with some extra features from Guitarix

%package -n lv2-SunFace-plugin
Summary: A classic fuzz face with some light modifications
Group:   Applications/Multimedia
%description -n lv2-SunFace-plugin
A classic fuzz face with some light modifications

%package -n lv2-TubeDistortion-plugin
Summary: Simulation of a Tube based Distortion Pedal
Group:   Applications/Multimedia
%description -n lv2-TubeDistortion-plugin
Simulation of a Tube based Distortion Pedal from Guitarix

%package -n lv2-GxBoobTube-plugin
Summary: Little tube boost pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxBoobTube-plugin
The BoobTube is a little tube boost pedal simulation, it's a variation of the ValveCaster. 
It adds some overdrive and tube compression along with boosting the signal. From Guitarix

%package -n lv2-GxCreamMachine-plugin
Summary: Simulation, based on a tube power amp circuit
Group:   Applications/Multimedia
%description -n lv2-GxCreamMachine-plugin
Simulation, based on a tube power amp circuit.

%package -n lv2-GxValveCaster-plugin
Summary: Little tube boost pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxValveCaster-plugin
The ValveCaster is a little tube boost pedal simulation. 
It adds some overdrive and tube compression along with boosting the signal. From Guitarix

%package -n lv2-GxBaJaTubeDriver-plugin
Summary: Tube based overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxBaJaTubeDriver-plugin
Tube based overdrive pedal simulation from Guitarix

%package -n lv2-GxBlueAmp-plugin
Summary: Single-ended head amplifier simulation inspired by late 1950s Fender “Princeton” and “Champ” amplifier
Group:   Applications/Multimedia
%description -n lv2-GxBlueAmp-plugin
Single - ended head amplifier simulation inspired by late 1950s Fender “Princeton” and “Champ” amplifier designs, it delivers tight bass, clean mids and highs
From Guitarix

%package -n lv2-GxClubDrive-plugin
Summary: Overdrive Pedal Simulation based on a EF86 Pentode Valve Simulation
Group:   Applications/Multimedia
%description -n lv2-GxClubDrive-plugin
Overdrive Pedal Simulation based on a EF86 Pentode Valve Simulation from Guitarix

%package -n lv2-GxEpic-plugin
Summary: Simulation of a class A electric guitar valve amplifier
Group:   Applications/Multimedia
%description -n lv2-GxEpic-plugin
Simulation of a class A electric guitar valve amplifier from Guitarix

%package -n lv2-GxEternity-plugin
Summary: Low compression, natural sounding, overdrive pedal
Group:   Applications/Multimedia
%description -n lv2-GxEternity-plugin
This low compression overdrive pedal is perfect for any style of music that requires natural sounding overdrive. From Guitarix

%package -n lv2-GxLuna-plugin
Summary: Gnarly overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxLuna-plugin
Gnarly overdrive pedal simulation from Guitarix

%package -n lv2-GxPlexi-plugin
Summary: Power Amp simulation
Group:   Applications/Multimedia
%description -n lv2-GxPlexi-plugin
Power Amp simulation from Guitarix

%package -n lv2-GxShakaTube-plugin
Summary: Overdrive tube pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxShakaTube-plugin
A overdrive tube pedal simulation from Guitarix

%package -n lv2-GxSloopyBlue-plugin
Summary: Overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxSloopyBlue-plugin
Overdrive pedal simulation from Guitarix

%package -n lv2-GxSupersonic-plugin
Summary: Tube amp simulation
Group:   Applications/Multimedia
%description -n lv2-GxSupersonic-plugin
Tube amp simulation from Guitarix

%package -n lv2-GxTimRay-plugin
Summary: Overdrive pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxTimRay-plugin
Overdrive pedal simulation from Guitarix

%package -n lv2-GxUltraCab-plugin
Summary: Cabinet simulator stereo 
Group:   Applications/Multimedia
%description -n lv2-GxUltraCab-plugin
Cabinet simulator Lv2 stereo plugin from Guitarix

%package -n lv2-GxFz1b-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxFz1b-plugin
Vintage Fuzz Pedal simulation from Guitarix

%package -n lv2-GxFz1s-plugin
Summary: Vintage Fuzz Pedal simulation
Group:   Applications/Multimedia
%description -n lv2-GxFz1s-plugin
Vintage Fuzz Pedal simulation from Guitarix

%prep
%setup -qn GxPlugins.lv2

%build

%make_build INSTALL_DIR=%{buildroot}%{_libdir}/lv2 SSE_CFLAGS="%{optflags}" STRIP=true

%install 

make INSTALL_DIR=%{buildroot}%{_libdir}/lv2 SSE_CFLAGS="%{optflags}" STRIP=true install

%files -n lv2-AxisFace-plugin
%{_libdir}/lv2/gx_AxisFace.lv2/*

%files -n lv2-DOP250-plugin
%{_libdir}/lv2/gx_DOP250.lv2/*

%files -n lv2-Heathkit-plugin
%{_libdir}/lv2/gx_Heathkit.lv2/*

%files -n lv2-KnightFuzz-plugin
%{_libdir}/lv2/gx_KnightFuzz.lv2/*

%files -n lv2-liquiddrive-plugin
%{_libdir}/lv2/gx_liquiddrive.lv2/*

%files -n lv2-maestro_fz1b-plugin
%{_libdir}/lv2/gx_maestro_fz1b.lv2/*

%files -n lv2-maestro_fz1s-plugin
%{_libdir}/lv2/gx_maestro_fz1s.lv2/*

%files -n lv2-MicroAmp-plugin
%{_libdir}/lv2/gx_MicroAmp.lv2/*

%files -n lv2-quack-plugin
%{_libdir}/lv2/gx_quack.lv2/*

%files -n lv2-SunFace-plugin
%{_libdir}/lv2/gx_SunFace.lv2/*

%files -n lv2-TubeDistortion-plugin
%{_libdir}/lv2/gx_TubeDistortion.lv2/*

%files -n lv2-GxGuvnor-plugin
%{_libdir}/lv2/gx_guvnor.lv2/*

%files -n lv2-GxHotBox-plugin
%{_libdir}/lv2/gx_hotbox.lv2/*

%files -n lv2-GxHyperion-plugin
%{_libdir}/lv2/gx_hyperion.lv2/*

%files -n lv2-GxQuack-plugin
%{_libdir}/lv2/gx_quack.lv2/*

%files -n lv2-GxSaturator-plugin
%{_libdir}/lv2/gx_saturate.lv2/*

%files -n lv2-GxSD1-plugin
%{_libdir}/lv2/gx_sd1sim.lv2/*

%files -n lv2-GxSD2Lead-plugin
%{_libdir}/lv2/gx_sd2lead.lv2/*

%files -n lv2-GxSlowGear-plugin
%{_libdir}/lv2/gx_slowgear.lv2/*

%files -n lv2-GxSuperFuzz-plugin
%{_libdir}/lv2/gx_sfp.lv2/*

%files -n lv2-GxSuppaToneBender-plugin
%{_libdir}/lv2/gx_vstb.lv2/*

%files -n lv2-GxSVT-plugin
%{_libdir}/lv2/gx_ampegsvt.lv2/*

%files -n lv2-GxToneMachine-plugin
%{_libdir}/lv2/gx_tonemachine.lv2/*

%files -n lv2-GxUVox720k-plugin
%{_libdir}/lv2/gx_uvox.lv2/*

%files -n lv2-GxVBassPreAmp-plugin
%{_libdir}/lv2/gx_voxbass.lv2/*

%files -n lv2-GxVintageFuzzMaster-plugin
%{_libdir}/lv2/gx_vfm.lv2/*

%files -n lv2-GxVmk2-plugin
%{_libdir}/lv2/gx_vmk2d.lv2/*

%files -n lv2-GxVoodoFuzz-plugin
%{_libdir}/lv2/gx_voodoo.lv2/*

%files -n lv2-GxBoobTube-plugin
%{_libdir}/lv2/gx_boobtube.lv2/*

%files -n lv2-GxCreamMachine-plugin
%{_libdir}/lv2/gx_CreamMachine.lv2/*

%files -n lv2-GxValveCaster-plugin
%{_libdir}/lv2/gx_valvecaster.lv2/*

%files -n lv2-GxBottleRocket-plugin
%{_libdir}/lv2/gx_bottlerocket.lv2/*

%files -n lv2-GxBaJaTubeDriver-plugin
%{_libdir}/lv2/gx_bajatubedriver.lv2/*

%files -n lv2-GxBlueAmp-plugin
%{_libdir}/lv2/gx_blueamp.lv2/*

%files -n lv2-GxClubDrive-plugin
%{_libdir}/lv2/gx_clubdrive.lv2/*

%files -n lv2-GxEpic-plugin
%{_libdir}/lv2/gx_epic.lv2/*

%files -n lv2-GxEternity-plugin
%{_libdir}/lv2/gx_eternity.lv2/*

%files -n lv2-GxLuna-plugin
%{_libdir}/lv2/gx_luna.lv2/*

%files -n lv2-GxPlexi-plugin
%{_libdir}/lv2/gx_plexi.lv2/*

%files -n lv2-GxShakaTube-plugin
%{_libdir}/lv2/gx_shakatube.lv2/*

%files -n lv2-GxSloopyBlue-plugin
%{_libdir}/lv2/gx_sloopyblue.lv2/*

%files -n lv2-GxSupersonic-plugin
%{_libdir}/lv2/gx_supersonic.lv2/*

%files -n lv2-GxTimRay-plugin
%{_libdir}/lv2/gx_timray.lv2/*

%files -n lv2-GxUltraCab-plugin
%{_libdir}/lv2/gx_ultracab.lv2/*

%files -n lv2-GxFz1b-plugin
%{_libdir}/lv2/gx_maestro_fz1b.lv2/*

%files -n lv2-GxFz1s-plugin
%{_libdir}/lv2/gx_maestro_fz1s.lv2/*

%changelog
* Sat Apr 18 2021 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Update to v0.9

* Tue Jun 02 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8
- Update to v0.8

* Wed Jul 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7
- Update to v0.7

* Tue Jan 22 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6
- Update to v0.6

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4
- update for Fedora 29

* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4

* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.3
- Initial build
