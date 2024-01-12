# Tag: Presets, Video
# Type: Presets
# Category: Tool

Summary: Additional presets for ProjectM
Name: projectM-extra-presets
Version: 1.0.0
Release: 3%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-OpenMusic-green
URL: http://projectm.sourceforge.net

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/projectm/files/presets-samples/presets-2.0.0-Source.tar.gz
Source1: https://sourceforge.net/projects/projectm/files/presets-samples/presets-projectm-2.0.0-Source.tar.gz
Source2: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_200-2.0.0-Source.tar.gz
Source3: https://sourceforge.net/projects/projectm/files/presets-samples/presets-milkdrop_104-2.0.0-Source.tar.gz
Source4: http://ycollette.free.fr/Milkdrop/milkdrop-md-presets.zip
Source5: http://ycollette.free.fr/Milkdrop/milkdrop-megapack.zip
Source6: http://ycollette.free.fr/Milkdrop/milkdrop-vlc-presets.zip
Source7: http://spiegelmc.com.s3.amazonaws.com/pub/projectm_presets.zip
Source8: http://ycollette.free.fr/Milkdrop/CreamOfTheCrop_20200216.zip

BuildArch: noarch

BuildRequires: p7zip
BuildReauires: tar

%description
A collection of additional preset for projectM.

%package md
Summary: Extra presets for projectM (md presets)

%description md
Extra presets for projectM (md presets)

%package megapack
Summary: Extra presets for projectM (megapack presets)

%description megapack
Extra presets for projectM (megapack presets)

%package bltc201
Summary: Extra presets for projectM (bltc201 presets)

%description bltc201
Extra presets for projectM (bltc201 presets)

%package tryptonaut
Summary: Extra presets for projectM (tryptonaut presets)

%description tryptonaut
Extra presets for projectM (tryptonaut presets)

%package yin
Summary: Extra presets for projectM (yin presets)

%description yin
Extra presets for projectM (yin presets)

%package creamofthecrop
Summary: Extra presets for projectM (Cream Of The Crop presets)

%description creamofthecrop
Extra presets for projectM (yin presets)

%prep

%build
echo "Nothing to build."

%install

install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets

tar xvfz %{SOURCE0} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
tar xvfz %{SOURCE1} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
tar xvfz %{SOURCE2} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
tar xvfz %{SOURCE3} --one-top-level=$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets

mv presets-2.0.0-Source              presets-2.0.0
mv presets-projectm-2.0.0-Source     projectm-2.0.0
mv presets_milkdrop_200-2.0.0-Source milkdrop-2.0.0
mv presets_milkdrop_104-2.0.0-Source milkdrop-1.0.4

popd

7za x %{SOURCE4} -o$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
7za x %{SOURCE5} -o$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
7za x %{SOURCE6} -o$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
7za x %{SOURCE7} -o$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/
7za x %{SOURCE8} -o$RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets/

pushd .

cd $RPM_BUILD_ROOT%{_datadir}/projectM-mao/presets
mkdir $RPM_BUILD_ROOT%{_datadir}/projectM-mao/textures

mv milkdrop-md-presets  md
mv milkdrop-megapack    megapack
mv milkdrop-vlc-presets vlc

mv presets/presets_bltc201    bltc201
mv presets/presets_tryptonaut tryptonaut
mv presets/presets_yin        yin

# Cream of the crop
mv Presets/Dancer    cotc-dancer
mv Presets/Drawing   cotc-drawing
mv Presets/Fractal   cotc-fractal
mv Presets/Geometric cotc-geometric
mv Presets/Hypnotic  cotc-hypnotic
mv Presets/Particles cotc-particles
mv Presets/Reaction  cotc-reaction
mv Presets/Sparkle   cotc-sparkle
mv Presets/Supernova cotc-supernova
mv 'Presets/! Transition' cotc-transition
mv Presets/Waveform  cotc-wavefrom

rm README.txt
rm -rf User\ Profile

mv Textures/* ../textures/

find . -name "..[a-zA-Z]*"   -exec rm {} \;
find . -name ".[a-zA-Z]*"    -exec rm {} \;
find . -name "...[a-zA-Z]*"  -exec rm {} \;
find . -name ".. [a-zA-Z]*"  -exec rm {} \;
find . -name "...@[a-zA-Z]*" -exec rm {} \;
find . -name "*.cmake"       -exec rm {} \;

# Cleanup
rm -rf presets

rm md/presets/*.jar
rm md/presets/*.bat

rm -rf milkdrop-2.0.0/CMakeFiles
rm -rf milkdrop-1.0.4/CMakeFiles
rm -rf projectm-2.0.0/CMakeFiles
rm -rf presets-2.0.0/CMakeFiles

find . -name "amandio c*" -exec rm {} \;
find . -name "*.bak" -exec rm {} \;

# Rename
find . -name "*.MILK" -exec mv {} `basename {} .MILK`.milk \;
find . -name "*.MILk" -exec mv {} `basename {} .MILk`.milk \;
find . -name "*.MIL"  -exec mv {} `basename {} .MIL`.milk \;
find . -name "*.mil"  -exec mv {} `basename {} .mil`.milk \;

# Manage permissions

find %{buildroot}%{_datadir}/projectM-mao -type d -exec chmod 755 {} \;

find . -name "*.milk" -exec chmod 644 {} \;

popd

%files
%{_datadir}/projectM-mao/presets/presets-2.0.0/*
%{_datadir}/projectM-mao/presets/projectm-2.0.0/*
%{_datadir}/projectM-mao/presets/milkdrop-2.0.0/*
%{_datadir}/projectM-mao/presets/milkdrop-1.0.4/*
%{_datadir}/projectM-mao/presets/vlc/*

%files md
%{_datadir}/projectM-mao/presets/md/*

%files megapack
%{_datadir}/projectM-mao/presets/megapack/*

%files bltc201
%{_datadir}/projectM-mao/presets/bltc201/*

%files tryptonaut
%{_datadir}/projectM-mao/presets/tryptonaut/*

%files yin
%{_datadir}/projectM-mao/presets/yin/*

%files creamofthecrop
%{_datadir}/projectM-mao/presets/cotc-*
%{_datadir}/projectM-mao/textures/*

%changelog
* Sun Mar 7 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-3
- fix permissions

* Sun Nov 24 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- don't remove prjm files

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- fix for Fedora 31

* Sun Sep 09 2018 Yann Collette <ycollette dot nospam at free.fr> 1.0.0-1
- Initial release
