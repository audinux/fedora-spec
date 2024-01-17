# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

Name: lmms-mao
Version: 1.2.2
Release: 12%{?dist}
Summary: Linux MultiMedia Studio
URL: https://lmms.io

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
# ./lmms-source.sh v1.2.2

Source0: lmms.tar.gz
Source1: lmms-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(jack)
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
BuildRequires: fltk-devel
BuildRequires: fltk-devel
%ifarch aarch64
BuildRequires: Carla-devel
%else
BuildRequires: Carla-mao-devel
%endif
BuildRequires: bash-completion
BuildRequires: qt5-linguist
BuildRequires: fltk-fluid
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

Features

 * Song-Editor for arranging the song
 * creating beats and basslines using the Beat-/Bassline-Editor
 * easy-to-use piano-roll for editing patterns and melodies
 * instrument- and effect-plugins
 * automation-editor
 * MIDI-support

%package devel
Summary:  Development files for lmms
Requires: lmms-mao = %{version}-%{release}

%description devel
The lmms-devel package contains header files for
developing addons for lmms.

%prep
%autosetup -n lmms

sed -i -e "s/-std=c11/-std=c11 -fPIC -DPIC/g" src/3rdparty/rpmalloc/CMakeLists.txt
sed -i -e "s/CARLA_EXPORT/CARLA_API_EXPORT/g" plugins/carlabase/carla.h

%build

%cmake -DWANT_SDL:BOOL=OFF \
       -DWANT_PORTAUDIO:BOOL=OFF \
       -DWANT_CAPS:BOOL=ON \
       -DWANT_TAP:BOOL=ON \
       -DWANT_SWH:BOOL=ON \
       -DWANT_CALF:BOOL=ON \
       -DWANT_CARLA:BOOL=ON \
       -DWANT_QT5:BOOL=ON \
       -DWANT_VST:BOOL=OFF \
       -DWANT_VST_NOWINE:BOOL=ON \
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

%files devel
%{_includedir}/lmms

%changelog
* Thu Oct 20 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-12
- update to 1.2.2-12 - use carla-mao on intel platforms

* Wed Dec 30 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-11
- update to 1.2.2-11 - activate calf, tap, caps ladspa plugins ... Seems to be missing now

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-10
- update to 1.2.2-10 - add missing requires + rebuilt because of carla

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-9
- update to 1.2.2-9 - fix for fedora 33

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-8
- update to 1.2.2-8

* Thu Apr 23 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-9
- fix for Fedora 32

* Thu Nov 28 2019 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-8
- update to 1.2.1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-8
- update for Fedora 29

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-8
- add a jack transport patch

* Tue May 1 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-7
- Rename lmms -> lmms-mao to ease install
- Remove vst part (this package is only built on 64 bits arch)

* Sat May 30 2015 Yann Collette <ycollette.nospam@free.fr> - 1.1.3-6
- lmms-1.1.3-libexecdir.patch
- lmms-1.1.3-vst-nowine.patch
- update lmms.spec to support version 1.1.3
- enable samples + demos songs
- Remove README.fedora.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-5
- lmms-1.0.3-no_werror.patch

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-4
- rebuild (fltk)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-3
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-1
- Update to 1.0.3.
- Rebase patches, drop obsolete patches.
- Filter internal provides.
- Spec file cleanups.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jul 28 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.15-1
- Update to 0.4.15.
- Modernize spec file.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.13-4
- Rebuilt for new STK.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-2
- Rebuilt for c++ ABI breakage

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.13-1
- Update to 0.4.13.

* Sat Jan 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.12-1
- Update to 0.4.12.
- Add patch for gcc47 compatibility.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.11-1
- Update to 0.4.11.

* Sat May 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-3
- Rebuild for new fltk.

* Thu Feb 10 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-2
- The remote_vst_plugin has been renamed to RemoteVstPlugin, fix
  libexecdir patch and specfile.

* Wed Feb  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.10-1
- Update to 0.4.10, rebase patches.
- Add patch for bz 672918.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.9-2
- Add patch to use system's fltk.
- Add BR to fltk-devel.

* Sat Dec 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.9-1
- Update to 0.4.9, rebase patches.

* Sat Sep  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.8-1
- Update to 0.4.8, rebase patches.
- Remove comments about minixml, no longer bundled.

* Wed Aug 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.7-1
- Update to 0.4.7.
- Remove obsolete patch, rebase other patches.
- Specfile fixes.

* Tue Feb 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-4
- Rebuilt for stk update.

* Wed Feb 10 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-3
- Add patch to fix DSO issue.

* Fri Jan 15 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-2
- Let cmake create rpaths where needed. This should fix bz 555852
  (zynaddsubfx gui not showing up). In order to make that work
  properly, drop the libdir patch, and set CMAKE_INSTALL_LIBDIR
  instead. Thanks to Rex Dieter for helping with that issue.

* Wed Dec 30 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.6-1
- Update to 0.4.6.
- Rebase patches.
- Minor specfile fixes.

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.4.5-2
- Update desktop file according to F-12 FedoraStudio feature

* Fri Sep  4 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.5-1
- Udate to 0.4.5.
- Rebase patches, and drop fltk patches not needed anymore.
- Add a dependency on the Calf LADSPA plugins.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.4-1
- Update to 0.4.4.
- Need to borrow patches for embedded fltk from the fltk package.
- Update detailed license information in the spec file.
- Update patches.

* Mon Mar  9 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.3-1
- Update to 0.4.3.
- Remove lmms-0.4.2-gcc44.patch (fixed upstream).
- Add README.fedora.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-4
- Re-add drumsynth files and adjust License tag.

* Thu Feb 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-3
- Add patch for gcc44 issues.

* Wed Feb 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-2
- Strip files with unclear licensing from the tarfile.
- Regenerate patches.
- Add BR on libsamplerate-devel.

* Thu Jan 22 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.2-1
- Update to 0.4.2.

* Sun Nov  2 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-1
- Updated to 0.4.0 final.
- Removed patches already applied upstream, adjusted the remaining.

* Fri Oct 24 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.2.rc3
- Add patch to fix libdir on ppc64.

* Tue Oct 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc3
- Update to 0.4.0rc3.
- Don't build remote_vst_plugin.exe on x86_64, but do build all other
  parts of the VST host there.

* Fri Sep 26 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc2
- Update to 0.4.0rc2.
- Use oss, jack, alsa and pulseaudio backends and disable other
  backends.
- Depend on the system packages for all but one of the ladspa plugins
  instead of building our own versions.

* Thu Sep 18 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-0.1.rc1
- Update to 0.4.0rc1. Upstream uses cmake and qt4 now.
- Updated license tag.
- Drop festival dependency, and add fftw and fluidsynth.
- Remove patches no longer necessary.
- VST now also builds on x86_64.

* Wed Sep 17 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-3
- Add stk-devel BR.
- Use libdir patch from upstream bug tracker.
- Use xdg-open instead of x-www-browser.

* Wed Jun 25 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-2
- Update license tag.
- Add patch to fix plugin dir on 64bit archs.
- Add ladspa-caps-plugins dependency.
- Suggestions from the review:
  * Simplify configure step.
  * Fix sf.net download link.
  * Add patch to let configure find the qt translations.
  * Link icon to _datadir/pixmaps.

* Mon Apr 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.2-1
- New package.
