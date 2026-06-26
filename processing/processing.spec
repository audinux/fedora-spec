# Status: active
# Tag: Devel, Editor
# Type: Standalone, Language
# Category: Tool, Programming

%global debug_package %{nil}

# Build number embedded in the upstream release tag (processing-BUILDNUM-VERSION).
# Update this together with Version on each upstream release.
%global buildnum 1433

Name: processing
Version: 4.5.5
Release: 3%{?dist}
Summary: Processing Development Environment (PDE)
# Core is LGPL, others are GPL
License: GPL-2.0+ and LGPL-2.0+
URL: https://processing.org/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/processing/processing4/releases/download/processing-%{buildnum}-%{version}/processing-%{version}-linux-x64-portable.zip
Source1: https://github.com/processing/processing4/releases/download/processing-%{buildnum}-%{version}/processing-%{version}-linux-aarch64-portable.zip
Source2: %{name}.desktop

# Upstream ships self-contained portable zips with a bundled JRE and native
# OpenGL libraries (JOGL); automatic dependency detection is not useful here.
AutoReqProv: no

%description
Processing is a flexible software sketchbook and a language for learning
how to code within the context of the visual arts.
Since 2001, Processing has promoted software literacy within the visual
arts and visual literacy within technology. There are tens of thousands
of students, artists, designers, researchers, and hobbyists who use
Processing for learning and prototyping.

- Free to download and open source
- Interactive programs with 2D, 3D or PDF output
- OpenGL integration for accelerated 2D and 3D
- For GNU/Linux, Mac OS X, and Windows
- Over 100 libraries extend the core software
- Well documented, with many books available

%prep
%ifarch x86_64
%setup -q -n Processing
%endif
%ifarch aarch64
# -T disables Source0 extraction; -b 1 extracts the aarch64 zip before cd
%setup -q -n Processing -T -b 1
%endif

%build

%install
install -m 0755 -d %{buildroot}/opt/%{name}
cp -R * %{buildroot}/opt/%{name}/

install -dm 0755 %{buildroot}/%{_datadir}/pixmaps
install -m 0644 lib/app/resources/lib/icons/pde-256.png \
    %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -dm 0755 %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/

install -m 0755 -d %{buildroot}/%{_bindir}
ln -s /opt/processing/bin/processing %{buildroot}/%{_bindir}/processing

# Remove Windows cross-compilation tools present in both arch zips
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-windows.exe
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-windows.exe

%ifarch x86_64
# Remove non-x86_64 native libraries bundled in the x64 portable zip
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/libraries/io/library/linux-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/libraries/io/library/linux-arm64
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-linux-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-linux-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/mode/jogl-all-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/mode/gluegen-rt-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/lib/app/resources/core/library/jogl-all-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/lib/app/resources/core/library/gluegen-rt-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/lib/app/jogl-all-2.5.0-natives-linux-armv6hf-*.jar
rm -rf %{buildroot}/opt/processing/lib/app/gluegen-rt-2.5.0-natives-linux-armv6hf-*.jar
%endif

%ifarch aarch64
# Remove non-aarch64 native libraries bundled in the aarch64 portable zip
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/libraries/io/library/linux-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-linux-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-armv6hf
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-linux-armv6hf
%endif

%files
%{_bindir}/%{name}
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jun 25 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.5-3
- update to 4.5.5-3

* Thu Jun 25 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.4-3
- add aarch64 support: Source1 is the aarch64 portable zip; %prep selects
  the right zip per arch; %install removes arch-specific native files
- add %global buildnum for easier version bumps (update both together)
- cleanup: remove OpenSUSE copyright header, stray comments, redundant
  BuildArch line, and normalize rm -rf paths (removed spurious ./)

* Wed Jun 24 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.4-2
- update to 4.5.4-2

* Mon Mar 02 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.3-2
- update to 4.5.3-2

* Thu Jan 29 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.2-2
- update to 4.5.2-2

* Mon Jan 19 2026 Yann Collette <ycollette.nospam@free.fr> - 4.5.1-2
- update to 4.5.1-2

* Thu Dec 18 2025 Yann Collette <ycollette.nospam@free.fr> - 4.5.0-2
- update to 4.5.0-2

* Tue Oct 14 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.10-2
- update to 4.4.10-2

* Tue Oct 07 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.8-2
- update to 4.4.8-2

* Thu Sep 04 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.7-2
- update to 4.4.7-2

* Sun Aug 17 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.6-2
- update to 4.4.6-2

* Mon Jul 14 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.5-2
- update to 4.4.5-2

* Fri May 16 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.4-2
- update to 4.4.4-2

* Fri Apr 25 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.3-2
- update to 4.4.3-2

* Wed Apr 16 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.2-2
- update to 4.4.2-2

* Wed Apr 16 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.1-2
- update to 4.4.1-2

* Fri Mar 14 2025 Yann Collette <ycollette.nospam@free.fr> - 4.4.0-2
- update to 4.4.0-2

* Fri Feb 21 2025 Yann Collette <ycollette.nospam@free.fr> - 4.3.4-2
- update to 4.3.4-2

* Tue Jan 21 2025 Yann Collette <ycollette.nospam@free.fr> - 4.3.3-2
- update to 4.3.3-2

* Thu Dec 12 2024 Yann Collette <ycollette.nospam@free.fr> - 4.3.2-2
- update to 4.3.2-2

* Tue Nov 12 2024 Yann Collette <ycollette.nospam@free.fr> - 4.3.1-2
- update to 4.3.1-2

* Wed Jul 26 2023 Yann Collette <ycollette.nospam@free.fr> - 4.3-2
- update to 4.3-2

* Mon Feb 20 2023 Yann Collette <ycollette.nospam@free.fr> - 4.2-2
- update to 4.2-2

* Mon Feb 20 2023 Yann Collette <ycollette.nospam@free.fr> - 4.1.3-2
- update to 4.1.3-2

* Thu Dec 01 2022 Yann Collette <ycollette.nospam@free.fr> - 4.1.1-2
- update to 4.1.1-2

* Fri Oct 01 2021 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-2
- fix for Fedora 35 + update to 3.5.4-2

* Sat Mar 14 2020 Yann Collette <ycollette.nospam@free.fr> - 3.5.4-1
- adjustement for Fedora 29 / 30 + update to 3.5.4-1

* Wed Sep 28 2016 guoyunhebrave@gmail.com
- Add _service file. Download binary tarball from Github

* Sun Sep 18 2016 guoyunhebrave@gmail.com
- Update to 3.2.1

* Thu Nov 24 2011 lars@linux-schulserver.de
- update to 1.5.1
