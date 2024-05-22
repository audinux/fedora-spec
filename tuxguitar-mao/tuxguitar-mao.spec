# Tag: Audio, Sequencer, Editor, MIDI
# Type: Standalone
# Category: Audio, Sequencer, MIDI, DAW

%ifarch x86_64
%global bit x86_64
%else
%ifarch armv7hl
%global bit armv7hl
%else
%ifarch ppc64
%global bit ppc64
%else
%ifarch ppc64le
%global bit ppc64le
%else
%ifarch s390x
%global bit s390x
%else
%ifarch aarch64
%global bit aarch64
%else
%global bit x86
%endif
%endif
%endif
%endif
%endif
%endif

%define debug_package %{nil}

Name: tuxguitar
Version: 1.6.2
Release: 10%{?dist}
Summary: A multitrack tablature editor and player written in Java-SWT
License: LGPL-2.1-or-later
URL: https://github.com/helge17/tuxguitar
ExclusiveArch: x86_64 

Source0: https://github.com/helge17/tuxguitar/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: tuxguitar.sh
# Source2: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
# Source2: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
# 4.13:
# wget https://archive.eclipse.org/eclipse/downloads/drops4/R-4.13-201909161045/swt-4.13-gtk-linux-x86_64.zip
# 4.21:
# wget https://archive.eclipse.org/eclipse/downloads/drops4/R-4.21-202109060500/swt-4.21-gtk-linux-x86_64.zip
# wget https://archive.eclipse.org/eclipse/downloads/drops4/R-4.21-202109060500/swt-4.21-gtk-linux-aarch64.zip
# 4.27:
# wget https://archive.eclipse.org/eclipse/downloads/drops4/R-4.27-202303020300/swt-4.27-gtk-linux-x86_64.zip
# wget https://archive.eclipse.org/eclipse/downloads/drops4/R-4.27-202303020300/swt-4.27-gtk-linux-aarch64.zip
%define swt_version 4.27
Source3: swt-%{swt_version}-gtk-linux-aarch64.zip
Source4: swt-%{swt_version}-gtk-linux-x86_64.zip

# Fedora specific default soundfont path
Patch0: 0014-desktop.patch
Patch1: tuxguitar-default-soundfont.patch
Patch2: 0015-fix-prototype.patch

Requires: eclipse-swt
Requires: hicolor-icon-theme
Requires: soundfont2-default

BuildRequires: gcc
BuildRequires: make
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-verifier-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: alsa-lib-devel
BuildRequires: fluidsynth-devel
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: suil-devel
BuildRequires: lilv-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: eclipse-swt
BuildRequires: mojo-executor-maven-plugin
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

# eclipse-swt upstream stopped supporting non-64bit arches at version 4.11
ExcludeArch: s390 %{arm} %{ix86}

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management, 
tempo management, gp3/gp4/gp5 import and export.

%prep
%setup -q -n %{name}-%{version}

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

# In source archive, all modules have an attribute "VERSION" set to "SNAPSHOT"
# this attribute is set during build/delivery
# Refer to application delivery process :
#   https://github.com/helge17/tuxguitar/blob/9d40a35ffc906fd0479b4c47aff00e048daac220/misc/build_tuxguitar_from_source.sh#L118
find . \( -name "*.xml" -or -name "*.gradle" -or -name "*.properties" -or -name control -or -name Info.plist \) \
     -and -type f -exec sed -i "s/SNAPSHOT/%{version}/" '{}' \;

sed -i "s/static final String RELEASE_NAME =.*/static final String RELEASE_NAME = (TGApplication.NAME + \" %{version}\");/" desktop/TuxGuitar/src/org/herac/tuxguitar/app/view/dialog/about/TGAboutDialog.java

# Installing missing VST2 files
#unzip %{SOURCE2}
#mkdir -p desktop/build-scripts/native-modules/tuxguitar-synth-vst-linux-%{bit}/include/
#cp VST_SDK/VST2_SDK/pluginterfaces/vst2.x/* desktop/build-scripts/native-modules/tuxguitar-synth-vst-linux-%{bit}/include/

# Replace swt version
sed -i -e "s/4.13/%{swt_version}/g" desktop/pom.xml
%ifarch aarch64
sed -i -e "s/x86_64/aarch64/g" desktop/pom.xml
%endif

%build

cd desktop/build-scripts/tuxguitar-linux-swt-%{bit}

# Installation of swt
mkdir swt-%{swt_version}-gtk-linux-%{bit}
cd swt-%{swt_version}-gtk-linux-%{bit}
%ifarch aarch64
unzip %{SOURCE3}
%else
unzip %{SOURCE4}
%endif
mvn install:install-file -Dfile=swt.jar -DgroupId=org.eclipse.swt -DartifactId=org.eclipse.swt.gtk.linux.%{bit} -Dpackaging=jar -Dversion=%{swt_version}
cd ..

# Building tuxguitar
mvn -X -e clean verify -P native-modules

%install

#mvn_install

# install jnis we built
mkdir -p %{buildroot}/%{_jnidir}/%{name}/
cp -a desktop/TuxGuitar-*/jni/*.so %{buildroot}/%{_jnidir}/%{name}/

# Launch script
mkdir -p %{buildroot}/%{_bindir}
cp -a %{SOURCE1} %{buildroot}/%{_bindir}/%{name}

# This file doesn't launch at this point. Might work when we can get the plugins working
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -a desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/dist/* %{buildroot}/%{_datadir}/%{name}/

# Fix permissions
chmod 755 %{buildroot}/%{_bindir}/%{name}
chmod 755 %{buildroot}%{_jnidir}/%{name}/*.so

# mime types
mkdir -p %{buildroot}/%{_datadir}/mime/packages/
cp -a desktop/build-scripts/common-resources/common-linux/share/mime/packages/tuxguitar.xml %{buildroot}/%{_datadir}/mime/packages/

# data files
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a desktop/TuxGuitar/share/* %{buildroot}/%{_datadir}/%{name}
cp -a misc/tuxguitar.tg %{buildroot}/%{_datadir}/%{name}
cp -a desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/dist/* %{buildroot}/%{_datadir}/%{name}

# icon
install -D -m 644 desktop/build-scripts/common-resources/common-linux/share/pixmaps/tuxguitar.xpm %{buildroot}%{_datadir}/pixmaps/tuxguitar.xpm

# man page
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a desktop/build-scripts/common-resources/common-linux/share/man/man1/%{name}.1 %{buildroot}/%{_mandir}/man1/    
    
# desktop files
mkdir -p %{buildroot}/%{_datadir}/applications/
install -pm 644 desktop/build-scripts/common-resources/common-linux/share/applications/%{name}.desktop %{buildroot}/%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications/ desktop/build-scripts/common-resources/common-linux/share/applications/%{name}.desktop

# jar files
mkdir -p %{buildroot}/%{_javadir}/%{name}/
cp desktop/build-scripts/native-modules/%{name}-alsa-linux-%{bit}/target/build/share/plugins/%{name}-alsa.jar %{buildroot}%{_javadir}/%{name}/
cp desktop/build-scripts/native-modules/%{name}-jack-linux-%{bit}/target/build/share/plugins/%{name}-jack-ui.jar %{buildroot}%{_javadir}/%{name}/
cp desktop/build-scripts/native-modules/%{name}-jack-linux-%{bit}/target/build/share/plugins/%{name}-jack.jar %{buildroot}%{_javadir}/%{name}/

cp desktop/build-scripts/native-modules/%{name}-synth-lv2-linux-%{bit}/target/build/share/plugins/%{name}-synth-lv2.jar %{buildroot}%{_javadir}/%{name}/
cp desktop/build-scripts/native-modules/%{name}-fluidsynth-linux-%{bit}/target/build/share/plugins/%{name}-fluidsynth.jar %{buildroot}%{_javadir}/%{name}/
#cp desktop/build-scripts/native-modules/%{name}-synth-vst-linux-%{bit}/target/build/share/plugins/%{name}-synth-vst.jar %{buildroot}%{_javadir}/%{name}/

cp desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/lib/*.jar %{buildroot}%{_javadir}/%{name}/
cp desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/lib/*.so %{buildroot}%{_jnidir}/%{name}/
cp desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/share/plugins/* %{buildroot}%{_javadir}/%{name}/

# clients
mkdir -p %{buildroot}%{_libexecdir}/%{name}/
#cp desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/vst-client/tuxguitar-synth-vst.bin %{buildroot}%{_libexecdir}/%{name}/
cp desktop/build-scripts/%{name}-linux-swt-%{bit}/target/%{name}-%{version}-linux-swt-%{bit}/lv2-client/tuxguitar-synth-lv2.bin %{buildroot}%{_libexecdir}/%{name}/

# Install vst-client and lv2-client and set the path in these conf files

## /usr/share/tuxguitar/tuxguitar-synth-lv2.cfg
cat > %{buildroot}/%{_datadir}/%{name}/%{name}-synth-lv2.cfg <<EOF
lv2.client.command=/usr/libexec/tuxguitar/tuxguitar-synth-lv2.bin,\${lv2.sessionId},\${lv2.serverPort},\${lv2.bufferSize},\${lv2.pluginUri}
lv2.client.working.dir=/tmp/tuxguitar-lv2-client
EOF

## /usr/share/tuxguitar/tuxguitar-synth-vst.cfg
#cat > %{buildroot}/%{_datadir}/%{name}/%{name}-synth-vst.cfg <<EOF
#vst.plugin.extensions=so;dll
#vst.plugin.client.command.so=/usr/libexec/tuxguitar/tuxguitar-synth-vst.bin,\${vst.sessionId},\${vst.serverPort},\${vst.fileName}
#vst.plugin.client.command.dll=wine,/usr/libexec/tuxguitar/vst-client.exe,\${vst.sessionId},\${vst.serverPort},\${vst.fileName}
#vst.plugin.client.working.dir=/tmp/tuxguitar-vst-client
#EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_javadir}/%{name}/*.jar
%{_jnidir}/%{name}/*.so
%{_libexecdir}/%{name}/*
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Apr 03 2024 Yann Collette <ycollette.nospam@free.fr> - 1.6.2-10
- update to 1.6.2-10

* Fri Feb 02 2024 Yann Collette <ycollette.nospam@free.fr> - 1.6.1-10
- update to 1.6.1-10

* Thu Nov 23 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- update to 1.6.0-10 - enable aarch64 build - update to swt-4.27

* Wed Nov 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- update to 1.6.0-9 - fix LV2 / VST management

* Wed Nov 15 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- update to 1.6.0-8

* Thu Nov 02 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-8
- update to 1.5.6-8

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Florian Weimer <fweimer@redhat.com> - 1.5.4-7
- Fix C99 compatibility issue

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.4-4
- Fedora 36+ does not support compiling Java version 6. RHBZ#2051214

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5.4-3
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.4-1
- Version update

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.3-7
- Rebuild against fluidsynth-2.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.5.3-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.3-3
- Rebuild against fluidsynth2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.3-1
- Version update

* Sat Aug 03 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.2-4
- Don't build on 32bit arches as eclipse-swt is no longer available
  starting at version 4.11

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.2-1
- Version update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5.1-1
- Version update

* Thu Mar 01 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.5-1
- Version update

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-6
- Remove obsolete scriptlets

* Sun Aug 6 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4-5
- s390x patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4-1
- Version update

* Fri Mar 25 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.2-1
- Version update

* Mon Feb 08 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1-1
- Version update
- Drop upstreamed patches

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.0-1
- Version update

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2-20
- Add an AppData file for the software center

* Mon Feb 02 2015 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-19
- Set SWT_GTK3=0 workaround for blank setting dialogs. RHBZ#1187848

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2-18
- update mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-15
- Unversioned docdir https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sun Aug 04 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2-14
- Removed the BuildRequires: ant-nodeps as the virtual provides was removed from
  ant >= 1.9.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-12
- Changed swt.jar location specification RHBZ#923597

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-10
- Enabled the tuner plugin

* Sun Sep 23 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-9
- Disable cairo graphics to prevent garbled output on "Score Edition Mode" 
  RHBZ#827746,859734.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-7
- Require itext-core instead of itext to drop gcj dependency

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-5
- Remove gcj bits as per the new guidelines.
- Change Requires: libswt3-gtk2 to eclipse-swt

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-3
- Fix CVE-2010-3385 insecure library loading vulnerability - RHBZ#638396

* Sat Nov 28 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-2
- Change build system (we'll use our build-fedora.xml rather than patching Debian's
  Makefile). 
- Disable system tray and oss plugins by default.
- Make fluidsynth/alsa/fluid soundfont combination the default output so that the
  software works out of the box.

* Sat Nov 14 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.2-1
- New upstream version

* Wed Aug 05 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.1-3
- Update the .desktop file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.1-1
- New upstream version
- Clean-up the SPEC file
- Include GCJ-AOT-bits

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 15 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-8
- Enabled the PDF plugin since all the dependencies are now provided in repos

* Thu Oct 02 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-7
- Added "exec" to replace the called shell to java process in the launching script

* Wed Oct 01 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-6
- Required libswt3-gtk2 since rpmbuild doesn't pick it up.
- Some more cleanup in the spec file
- Fixed a typo regarding installation of icons
- Called update-desktop-database in %%post and %%postun
- jni files put in %%_libdir_/%%name.

* Mon Sep 29 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-5
- Compiled the package with openjdk instead of gcj.
- ExcludeArch'ed ppc/ppc64 on F-8.

* Sun Sep 28 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-4
- Added the comment about %%{?_smp_mflags}
- Used macros more extensively.
- Changed the license to LGPLv2+
- Fixed java requirement issue by requiring java >= 1.7
- Required jpackage-utils
- Removed pre-shipped binaries
- Fixed %%defattr

* Sun Sep 28 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-3
- Fixed java requirement issue by requiring icedtea for F-8 and openjdk for F-9+
- Patched the source to enable the fluidsynth plugin
- Added DistTag
- Patched the source in order to pass RPM_OPT_FLAGS to gcc
- Removed ExclusiveArch

* Thu Sep 25 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-2
- Added desktop-file-utils to BuildRequires.
- Replaced java-1.7.0-icedtea with java-1.6.0-openjdk in Requires.

* Wed Sep 24 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com>> - 1.0-1
- Initial build.
