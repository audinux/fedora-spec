# Status: active
# Tag: Tool, Generative, Visualization
# Type: Standalone
# Category: Tool

%global debug_package %{nil}

Name: nodebox
Version: 3.1.0
Release: 2%{?dist}
Summary: Node-based GUI for data visualizations and generative design
License: GPL-3.0-or-later
URL: https://nodebox.net
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# The source tarball is built by nodebox-source.sh which clones the
# repository, downloads all Maven dependencies, builds the fat jar and
# resources directory, then packages them offline-ready.

# Usage: ./nodebox-source.sh <TAG>
#        ./nodebox-source.sh v3.1.0

Source0: nodebox-%{version}.tar.gz
Source1: nodebox-source.sh
Source2: nodebox.sh
Source3: nodebox.desktop
Source4: nodebox-icon.svg

# Java 11+ is required (build.xml sets release="11")
BuildRequires: java-latest-openjdk-devel
BuildRequires: ant
BuildRequires: desktop-file-utils

Requires: java-latest-openjdk-headless
# ffmpeg is used for video export via FileUtils.getApplicationFile("bin/ffmpeg")
# which resolves to resources/bin/ffmpeg, symlinked to the system binary
Requires: (ffmpeg or ffmpeg-free)

# All Java dependencies are bundled in the fat jar:
#   clojure 1.12.4, guava 33.5.0, httpclient5 5.5.2, itextpdf 5.5.13.4,
#   jna 5.18.1, json-path 2.10.0, jython-standalone 2.7.4, opencsv 5.12.0,
#   org.processing.core 1.5.1, ddf.minim 2.2.0, oscp5 0.9.8
# Bundling is necessary because several of these are not packaged in Fedora
# (processing-core, minim, oscp5) or require specific versions (itextpdf).
Provides: bundled(clojure) = 1.12.4
Provides: bundled(guava) = 33.5.0
Provides: bundled(httpclient5) = 5.5.2
Provides: bundled(itextpdf) = 5.5.13.4
Provides: bundled(jna) = 5.18.1
Provides: bundled(jython) = 2.7.4
Provides: bundled(opencsv) = 5.12.0

%description
NodeBox is a cross-platform, node-based application for creating generative
graphics, data visualizations, and animations. It uses a visual node graph
where processing blocks are connected together — no code required.

Features:
  - Visual node graph editor
  - Built-in library of nodes for math, strings, lists, colors, geometry,
    network access, and data processing
  - Jython (Python 2.7) scripting for custom nodes
  - SVG, PDF, and video export (via ffmpeg)
  - Live preview with parametric animation support

The application's resource layout is fixed: the fat jar is installed under
lib/ and all runtime assets (libraries, examples, Python stdlib) live in a
sibling resources/ directory, as expected by FileUtils.getApplicationFile().

Note on ffmpeg: NodeBox resolves the ffmpeg binary via
FileUtils.getApplicationFile("bin/ffmpeg"), which navigates relative to the
jar location. A symlink is installed at resources/bin/ffmpeg pointing to the
system ffmpeg binary.

%prep
%autosetup -n %{name}-%{version}

%build

# All artifacts are pre-built by nodebox-source.sh.
# The fat jar (nodebox.jar) bundles all Maven runtime dependencies using
# Ant's zipgroupfileset, so no Maven download is needed at RPM build time.

%install

# Application data: jar + resources
install -d %{buildroot}%{_datadir}/%{name}/lib/
install -d %{buildroot}%{_datadir}/%{name}/resources/

cp -a dist/unpacked/lib/nodebox.jar %{buildroot}%{_datadir}/%{name}/lib/
cp -a dist/unpacked/resources/libraries \
    dist/unpacked/resources/examples \
    dist/unpacked/resources/res \
    dist/unpacked/resources/lib \
       %{buildroot}%{_datadir}/%{name}/resources/

# Symlink system ffmpeg so NodeBox can find it at its expected path
install -d %{buildroot}%{_datadir}/%{name}/resources/bin/
ln -s %{_bindir}/ffmpeg %{buildroot}%{_datadir}/%{name}/resources/bin/ffmpeg

# Launcher wrapper
install -D -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
# Expand the rpm macro in the wrapper now that we know the install path
sed -i 's|%%{_datadir}|%{_datadir}|g' %{buildroot}%{_bindir}/%{name}

# Icons
install -D -m 0644 %{SOURCE4}               %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m 0644 artwork/nodebox-icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Desktop entry
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE3}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license src/main/java/nodebox/client/Application.java
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Tue Jun 16 2026 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-2
- update to 3.1.0-2 - cleanup spec

* Mon Jun 15 2026 Yann Collette <ycollette.nospam@free.fr> - 3.1.0-1
- Initial packaging
