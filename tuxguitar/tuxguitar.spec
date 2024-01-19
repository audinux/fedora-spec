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

Summary:          A multitrack tablature editor and player written in Java-SWT
Name:             tuxguitar
Version:          1.5.6
Release:          8%{?dist}
URL:              http://www.tuxguitar.com.ar
# Source file cleaned of potentially proprietary SF2, DLL, EXE files:
#   export VERSION=1.5.2
#   wget -N http://downloads.sourceforge.net/tuxguitar/tuxguitar-$VERSION-src.tar.gz
#   tar zxf tuxguitar-$VERSION-src.tar.gz
#   find tuxguitar-$VERSION-src -name "*.exe" -exec rm {} \;
#   find tuxguitar-$VERSION-src -name "*.dll" -exec rm {} \;
#   find tuxguitar-$VERSION-src -name "*.sf2" -exec rm {} \;
#   tar zcf tuxguitar-$VERSION-src-clean.tar.gz tuxguitar-$VERSION-src
Source0:          %{name}-%{version}-src-clean.tar.gz
# Usage: ./tuxguitar-source.sh 1.5.6
Source1:          tuxguitar-source.sh

# Fedora specific start script
Patch0:           tuxguitar-startscript.patch
# Fedora specific default soundfont path
Patch1:           tuxguitar-default-soundfont.patch
# Build scripts for Fedora's additional arches
Patch2:           tuxguitar-additional-arch.patch
Patch3:           tuxguitar-c99.patch
License:          LGPLv2+

Requires:         eclipse-swt
Requires:         hicolor-icon-theme
Requires:         soundfont2-default

BuildRequires:    alsa-lib-devel
BuildRequires:    desktop-file-utils
BuildRequires:    fluidsynth-devel
BuildRequires:    pkgconfig(jack)
BuildRequires:    lv2-devel
BuildRequires:    suil-devel
BuildRequires:    lilv-devel
BuildRequires:    qt5-qtbase-devel

BuildRequires:    eclipse-swt
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    libappstream-glib
BuildRequires:    maven-local
BuildRequires:    maven-antrun-plugin

# eclipse-swt upstream stopped supporting non-64bit arches at version 4.11
ExcludeArch: s390 %{arm} %{ix86}

%description
TuxGuitar is a guitar tablature editor with player support through midi. It can
display scores and multitrack tabs. Various features TuxGuitar provides include
autoscrolling while playing, note duration management, bend/slide/vibrato/
hammer-on/pull-off effects, support for tuplets, time signature management, 
tempo management, gp3/gp4/gp5 import and export.

%prep
%setup -q -n %{name}-%{version}-src
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

# Remove prebuilt jar, class files
find . -name "*.jar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Remove NON FREE deps
%pom_remove_dep -r com.itextpdf:itextpdf
%pom_remove_dep -r com.itextpdf.tool:xmlworker
%pom_remove_dep -r com.itextpdf:itextpdf build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r com.itextpdf.tool:xmlworker build-scripts/%{name}-linux-%{bit}
%pom_disable_module ../../TuxGuitar-pdf build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r :tuxguitar-pdf
%pom_disable_module ../../TuxGuitar-pdf-ui build-scripts/%{name}-linux-%{bit}
%pom_remove_dep -r :tuxguitar-pdf-ui

# Fails to collect eclipse swt artifact
%pom_remove_plugin :maven-dependency-plugin build-scripts/%{name}-linux-%{bit}
%pom_remove_plugin :maven-dependency-plugin build-scripts/native-modules/%{name}-alsa-linux-%{bit}
%pom_remove_plugin :maven-dependency-plugin build-scripts/native-modules/%{name}-fluidsynth-linux-%{bit}
%pom_remove_plugin :maven-dependency-plugin build-scripts/native-modules/%{name}-jack-linux-%{bit}
%pom_remove_plugin :maven-dependency-plugin build-scripts/native-modules/%{name}-oss-linux-%{bit}
%pom_remove_plugin :maven-dependency-plugin build-scripts/native-modules/%{name}-synth-lv2-linux-%{bit}

%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt
%pom_xpath_set -r pom:org.eclipse.swt.artifactId org.eclipse.swt build-scripts/%{name}-linux-%{bit}
%pom_remove_dep :org.eclipse.swt.gtk.linux.x86
%pom_remove_dep :org.eclipse.swt.gtk.linux.x86_64
%pom_remove_dep :org.eclipse.swt.gtk.linux.ppc
%pom_remove_dep :org.eclipse.swt.win32.win32.x86
%pom_remove_dep :org.eclipse.swt.cocoa.macosx
%pom_remove_dep :org.eclipse.swt.cocoa.macosx.x86_64
%pom_remove_dep :org.eclipse.swt.carbon.macosx

%pom_xpath_inject pom:modules "<module>../../TuxGuitar-alsa</module>
 <module>../../TuxGuitar-fluidsynth</module>
 <module>../../TuxGuitar-jack-ui</module>
 <module>../../TuxGuitar-jack</module>
 <module>../../TuxGuitar-oss</module>
 <module>../../TuxGuitar-tray</module>
 <module>../../TuxGuitar-synth-lv2</module>
 <module>../../TuxGuitar-viewer</module>"  build-scripts/%{name}-linux-%{bit}

# Fix parent pom for jni modules
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-alsa-linux-%{bit} TuxGuitar-alsa
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-alsa-linux-%{bit}</relativePath>" TuxGuitar-alsa
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-fluidsynth-linux-%{bit} TuxGuitar-fluidsynth
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-fluidsynth-linux-%{bit}</relativePath>" TuxGuitar-fluidsynth
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-jack-linux-%{bit} TuxGuitar-jack
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-jack-linux-%{bit}</relativePath>" TuxGuitar-jack-ui
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-jack-linux-%{bit} TuxGuitar-jack-ui
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-jack-linux-%{bit}</relativePath>" TuxGuitar-jack
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-oss-linux-%{bit} TuxGuitar-oss
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-oss-linux-%{bit}</relativePath>" TuxGuitar-oss
%pom_xpath_set pom:parent/pom:artifactId tuxguitar-synth-lv2-linux-%{bit} TuxGuitar-synth-lv2
%pom_xpath_inject pom:parent "<relativePath>../build-scripts/native-modules/tuxguitar-synth-lv2-linux-%{bit}</relativePath>" TuxGuitar-synth-lv2

# fix tuxguitar-*.jni.path property
sed -i "s|\${parent.relativePath}|$PWD|" \
    build-scripts/native-modules/tuxguitar-alsa-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-fluidsynth-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-jack-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-oss-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-synth-lv2-linux-%{bit}/pom.xml
#fix libdir
sed -i 's|-L/usr/lib|-L%{_libdir}|' \
    build-scripts/native-modules/tuxguitar-alsa-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-fluidsynth-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-jack-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-oss-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-synth-lv2-linux-%{bit}/pom.xml
# Disable gcj support and add default compiler flags
sed -i -e "s|\$(shell gcj -print-file-name=include/)|%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux $RPM_OPT_FLAGS|" \
    -e "s|\(</tuxguitar-.*.jni.ldflags>\)| $RPM_LD_FLAGS\1|" \
    -e "s|\(</tuxguitar-.*.jni.cflags>\)| -I/usr/lib/jvm/java/include/ -I/usr/lib/jvm/java/include/linux/ $RPM_OPT_FLAGS\1|" \
    build-scripts/native-modules/tuxguitar-alsa-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-fluidsynth-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-jack-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-oss-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-synth-lv2-linux-%{bit}/pom.xml
#for i in TuxGuitar-*; do echo "   " \[ -r \"\$t\" \] \&\& CLASSPATH=\${CLASSPATH}:\$t;echo "   " t="\${PACKAGE_HOME}/$i.jar"; done |sed 's|TuxGuitar|${PACKAGE}|'
# Fix version tags
sed -i -e "s|\(<version>\).*\(</version>\)|\1%{version}\2|"\
    build-scripts/native-modules/tuxguitar-alsa-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-fluidsynth-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-jack-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-oss-linux-%{bit}/pom.xml \
    build-scripts/native-modules/tuxguitar-synth-lv2-linux-%{bit}/pom.xml \
    build-scripts/tuxguitar-linux-%{bit}/pom.xml

# Fedora 36+ changed their java compiler capabilities 
%pom_xpath_set pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:source 1.7 TuxGuitar-lib
%pom_xpath_set pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target 1.7 TuxGuitar-lib
%pom_xpath_set pom:build/pom:plugins/pom:plugin/pom:configuration/pom:source 1.7
%pom_xpath_set pom:build/pom:plugins/pom:plugin/pom:configuration/pom:target 1.7

%build

# -j for excluding the javadoc, since this is an application
%mvn_build -j -- -e -f build-scripts/%{name}-linux-%{bit}/pom.xml -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
# install jnis we built
mkdir -p %{buildroot}/%{_libdir}/%{name}
cp -a TuxGuitar-*/jni/*.so %{buildroot}/%{_libdir}/%{name}/

# Launch script
mkdir -p %{buildroot}//%{_bindir}
cp -a misc/tuxguitar.sh %{buildroot}//%{_bindir}/%{name}

# Fix permissions
chmod 755 %{buildroot}//%{_bindir}/%{name}
chmod 755 %{buildroot}/%{_libdir}/%{name}/*.so

# mime types
mkdir -p %{buildroot}//%{_datadir}/mime/packages/
cp -a misc/tuxguitar.xml %{buildroot}//%{_datadir}/mime/packages/

# data files
mkdir -p %{buildroot}//%{_datadir}/%{name}
cp -a TuxGuitar/share/* %{buildroot}//%{_datadir}/%{name}
# This file doesn't launch at this point. Might work when we can get the plugins working
cp -a misc/tuxguitar.tg %{buildroot}//%{_datadir}/%{name}
cp -a build-scripts/%{name}-linux-%{bit}/target/%{name}-%{version}-linux-%{bit}/dist/* %{buildroot}//%{_datadir}/%{name}

# jars connected to the jnis
cp -a TuxGuitar-alsa/target/%{name}-alsa-%{version}.jar %{buildroot}//%{_javadir}/%{name}/%{name}-alsa.jar
cp -a TuxGuitar-fluidsynth/target/%{name}-fluidsynth-%{version}.jar %{buildroot}//%{_javadir}/%{name}/%{name}-fluidsynth.jar
cp -a TuxGuitar-jack/target/%{name}-jack-%{version}.jar %{buildroot}//%{_javadir}/%{name}/%{name}-jack.jar
cp -a TuxGuitar-oss/target/%{name}-oss-%{version}.jar %{buildroot}//%{_javadir}/%{name}/%{name}-oss.jar

# These didn't work
#jpackage_script org.herac.tuxguitar.app.TGMain "" "" tuxguitar tuxguitar true
#jpackage_script org.herac.tuxguitar.app.TGMain "-Xmx512m" "" swt:tuxguitar tuxguitar true

# Lavender ersplus blue_serious
STYLE=Oxygen

for dim in 16 24 32 48 64 96; do
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/apps/
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/apps/%{name}.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-%{name}.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-gtp.png
    cp -a TuxGuitar/share/skins/${STYLE}/icon-${dim}x${dim}.png %{buildroot}/%{_datadir}/icons/hicolor/${dim}x${dim}/mimetypes/audio-x-ptb.png
done

# man page
mkdir -p %{buildroot}//%{_mandir}/man1
cp -a misc/%{name}.1 %{buildroot}//%{_mandir}/man1/    
    
# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}/%{_datadir}/metainfo
cat > %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/tuxguitar/support-requests/8/
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">tuxguitar.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A multitrack tablature editor and player</summary>
  <description>
  <p>
    Tuxguitar is a multitrack tablature editor and player.
    It provides the following features:
  </p>
  <ul>
    <li>Tablature editor</li>
    <li>Score Viewer</li>
    <li>Multitrack display</li>
    <li>Autoscroll while playing</li>
    <li>Note duration management</li>
    <li>Various effects (bend, slide, vibrato, hammer-on/pull-off)</li>
    <li>Support for triplets (5,6,7,9,10,11,12)</li>
    <li>Repeat open and close</li>
    <li>Time signature management</li>
    <li>Tempo management</li>
    <li>Imports and exports gp3,gp4 and gp5 files</li>
  </ul>
  </description>
  <url type="homepage">http://www.tuxguitar.com.ar/</url>
  <screenshots>
    <screenshot type="default">http://www.tuxguitar.com.ar/rd.php/gallery/show_picture.do?galid=1&amp;picid=47</screenshot>
    <screenshot>http://www.tuxguitar.com.ar/rd.php/gallery/show_picture.do?galid=1&amp;picid=46</screenshot>
  </screenshots>
</application>
EOF

%check
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications misc/tuxguitar.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files -f .mfiles
%license LICENSE
%doc AUTHORS CHANGES README
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%{_javadir}/%{name}/tuxguitar-alsa.jar
%{_javadir}/%{name}/tuxguitar-fluidsynth.jar
%{_javadir}/%{name}/tuxguitar-jack.jar
%{_javadir}/%{name}/tuxguitar-oss.jar

%changelog
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
