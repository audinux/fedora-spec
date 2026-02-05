# Status: active
# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%define commit0 c62b42a7c9cbcc1eb61da00808968d6dbabe2ed9

Name: lmms-mao-weekly
Version: 1.2.99
Release: 31%{?dist}
Summary: Linux MultiMedia Studio - Weekly version
URL: https://lmms.io
ExclusiveArch: x86_64 aarch64

# Because dnf does not find a carla so file
AutoReqProv: no

# - lmms itself is GPLv2+
# - included third-party code
#   - libsamplerate: GPLv2+ (but we use the system one)
# - third party code used by plugins:
#   - drumsynth files: GPLv2+ or MIT
#   - for ladspa-effecs (note that we only include cmt in the binary
#     rpm (see below):
#     - caps: GPLv2
#     - cmt: GPLv2(+?)
#     - swh: GPLv2+
#     - tap: GPLv2+
#     - calf: GPLv2+ and LGPLv2+
#   - GNU UnRTF (flp_import plugin): GPLv3+
#   - Portsmf (midi_import plugin): MIT
#   - Blip_Buffer and Gb_Snd_Emu (papu plugin): LGPLv2.1+
#   - reSID (sid plugin): GPLv2+
#   - basename.c (vst_base): Copyright only
#   - embedded zynaddsubfx plugin: GPLv2+
#     - fltk (zynaddsubfx): LGPLv2+, with exceptions (but we use
#       system's fltk)
License: GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

Vendor:       Audinux
Distribution: Audinux

# ./lmms-source.sh <tag>
# ./lmms-source.sh master

Source0: lmms.tar.gz
Source1: lmms-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: perl-List-MoreUtils
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: suil-devel
BuildRequires: lilv-devel
BuildRequires: lame-devel
BuildRequires: stk-devel
BuildRequires: SDL2-devel
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: fftw3-devel
BuildRequires: fluidsynth-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: libgig-devel
BuildRequires: ladspa-devel
BuildRequires: stk-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-linguist
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
%ifarch aarch64
BuildRequires: Carla-devel
%else
BuildRequires: Carla-mao-devel
%endif
BuildRequires: bash-completion
BuildRequires: desktop-file-utils

%ifarch aarch64
Requires: Carla
%else
Requires: Carla-mao
%endif
Requires: stk
Requires: libgig

%global __provides_exclude_from ^%{_libdir}/lmms/.*$
%global __requires_exclude ^libvstbase\\.so.*$|^libZynAddSubFxCore\\.so.*$

%description
LMMS aims to be a free alternative to popular (but commercial and
closed- source) programs like FruityLoops/FL Studio, Cubase and Logic
allowing you to produce music with your computer. This includes
creation of loops, synthesizing and mixing sounds, arranging samples,
having fun with your MIDI-keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program and those
of powerful synthesizers, samplers, effects etc. in a modern,
user-friendly and easy to use graphical user-interface.

Features:
 * Song-Editor for arranging the song
 * creating beats and basslines using the Beat-/Bassline-Editor
 * easy-to-use piano-roll for editing patterns and melodies
 * instrument- and effect-plugins
 * automation-editor
 * MIDI-support

%prep
%autosetup -n lmms

%build

%cmake -DWANT_SDL:BOOL=ON \
       -DWANT_PORTAUDIO:BOOL=ON \
       -DWANT_ALSA:BOOL=ON \
       -DWANT_JACK:BOOL=ON \
       -DWANT_WEAKJACK:BOOL=ON \
       -DWANT_PULSEAUDIO:BOOL=ON \
       -DWANT_MP3LAME:BOOL=ON \
       -DWANT_OGGVORBIS:BOOL=ON \
       -DWANT_LV2:BOOL=ON \
       -DWANT_SUIL:BOOL=ON \
       -DWANT_CAPS:BOOL=ON \
       -DWANT_SF2:BOOL=ON \
       -DWANT_STK:BOOL=ON \
       -DWANT_TAP:BOOL=ON \
       -DWANT_SWH:BOOL=ON \
       -DWANT_CMT:BOOL=ON \
       -DWANT_CALF:BOOL=ON \
       -DWANT_CARLA:BOOL=ON \
       -DWANT_LIBGIG:BOOL=ON \
       -DWANT_QT5:BOOL=ON \
       -DWANT_VST:BOOL=OFF \
       -DWANT_VST_64:BOOL=ON \
       -DCMAKE_C_FLAGS="-fPIC -DPIC" \
       -DCMAKE_EXE_LINKER_FLAGS:STRING="$LDFLAGS -pie" \
       -DCMAKE_SKIP_RPATH=OFF \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

# workaround: copy bash completion manually into install dir because it fails during cmake install
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions
cp %{_builddir}/lmms*/doc/bash-completion/lmms %{buildroot}/%{_datadir}/bash-completion/completions/lmms

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/lmms.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/lmms.desktop

%files
%doc doc/AUTHORS README.md INSTALL.txt
%license LICENSE.txt
%{_bindir}/lmms
%{_mandir}/man1/*
%{_libdir}/lmms/
%{_datadir}/lmms/
%{_datadir}/applications/lmms.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/lmms.xml
%{_datadir}/bash-completion/completions/lmms
%exclude %{_includedir}/lmms

%changelog
* Tue Feb 03 2026 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-31
- update to c62b42a7c9cbcc1eb61da00808968d6dbabe2ed9

* Fri Jan 02 2026 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-30
- update to 2db75bd5d97d4a5433865a710e06da8242a96422

* Thu Dec 25 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-29
- update to 5e8f220b9c9801029465d7579c039c15cce28266

* Wed Dec 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-28
- update to f0cb32ff088c604cb77a2cc4b35a53db761bcd65

* Fri Oct 03 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-27
- update to db6fc2948cc57482c48ae20d1cf4f770943851b1

* Sat Aug 30 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-26
- update to fbac56fdccc615b4efbd43dcb0a45a748e588838

* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-25
- update to 0d6cbbdf5ea35b3adaed6bf6e8c10e14c728eb02

* Tue Jul 22 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-24
- update to 71ce49d7ba02d5435454e56c9024e3278dbea20c

* Wed Jul 09 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-23
- update to 4c3f8191af2c35ae40d5b15d8aeedb68d43f1c54

* Sun Jun 15 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-22
- update to 76dddd8c66b103723940bf5f9326e6b8934e3d5c

* Mon May 26 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-21
- update to cb84fce599dfb657cdc9070216e36b2d30dbbb5e

* Mon Apr 28 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-20
- update to c91c81eee7b3cddf750a686930b58c3540689fc6

* Mon Mar 10 2025 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-19
- update to 8821d88c098ce886ed82df048c89c0106482a702

* Sun Dec 01 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-18
- update to f579750608da6448283942f557f82714dd840d0a

* Thu Nov 28 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-17
- update to 5acc7965c28ea6685de4f6ae13f9dfd9020c9310

* Fri Oct 11 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-16
- update to 378ff8bab02edb67110dc8b68694e6bce008fdfe

* Fri Aug 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-15
- update to bda1a9c37ed29cd7c80f08d7405dd4dbfad8947d

* Tue Jul 23 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-14
- update to 851c884f58155275e6adbde40f2611d076edd345

* Sun May 05 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-13
- update to 20102c4ae47afa3aee8f92b1728c559ef7c455d3

* Tue Apr 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-12
- update to d2c2a805064e504edd06841609be28e0ac38a26e

* Fri Mar 22 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-11
- update to 3e19d1335f478504c22ed68af9c96fccd6a6774b

* Sat Mar 16 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-10
- update to 4120a04d0be6c7c00dd9610da7a2ec9d023c55ce

* Wed Feb 21 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-9
- update to 360254fd81cda14cbcec3fff3dff5456005ebfc8

* Mon Dec 18 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-8
- update to f3d3a1421e2f4eb7d8dd8b35fdef1e8df2cd2cf8

* Sun Nov 12 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-7
- update to ecc5ff8ca7b826ab22e4b68c456129782ef0eee2

* Fri Nov 03 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-6
- update to fccbe5d517539f1c45bb54c04646569d0d3c00ec

* Mon Oct 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-5
- update to 63d03fa3a70ce538ecb8417a9c55d95ee17c5648

* Fri Oct 13 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-4
- update to 21dc88c37a6d4dbefa056ab29aba73388d34a7bd

* Sat Sep 23 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-3
- update to f0aa2862d7efe06a483f6056ba20de315d065597

* Sat Aug 26 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-2
- update to fc2f6a0b31bdd10c47cc0c6c2c18723d208eaae0

* Thu Aug 10 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.99-1
- New package.
