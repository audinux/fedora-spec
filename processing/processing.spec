# Status: active
# Tag: Devel, Editor
# Type: Standalone, Language
# Category: Tool, Programming

#
# spec file for package processing
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# Disable production of debug package.
%global debug_package %{nil}

Name: processing
Version: 4.4.4
Release: 2%{?dist}
Summary: Processing Development Environment (PDE)
# Core is LGPL, others are GPL
License: GPL-2.0+ and LGPL-2.0+
URL: https://processing.org/
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/processing/processing4/releases/download/processing-1304-%{version}/processing-%{version}-linux-x64-portable.zip
Source1: %{name}.desktop

AutoReqProv: no
BuildArch: x86_64

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
%autosetup -n Processing

%build

%install
install -dm 0755 %{buildroot}/opt/%{name}
cp -R * %{buildroot}/opt/%{name}/

install -dm 0755 %{buildroot}/%{_datadir}/pixmaps
install -m 0644 lib/app/resources/lib/icons/pde-256.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -dm 0755 %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/

# Create a symlink
install -dm 0755 %{buildroot}/%{_bindir}
ln -s /opt/processing/bin/processing %{buildroot}/%{_bindir}/processing

# Remove some non x86_64-linux files
# find . -name "*arm*"
rm -rf %{buildroot}/opt/processing/./lib/app/jogl-all-2.5.0-natives-linux-armv6hf-9c936e2029c28b1788e972cee34b8d.jar
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/libraries/io/library/linux-armv6hf
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/libraries/io/library/linux-arm64
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/application/launch4j/bin/windres-armv6hf
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/application/launch4j/bin/ld-linux-armv6hf
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/application/launch4j/bin/ld-armv6hf
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/application/launch4j/bin/windres-linux-armv6hf
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/mode/gluegen-rt-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/./lib/app/resources/modes/java/mode/jogl-all-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/./lib/app/resources/core/library/gluegen-rt-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/./lib/app/resources/core/library/jogl-all-2.5.0-natives-linux-armv6hf.jar
rm -rf %{buildroot}/opt/processing/./lib/app/gluegen-rt-2.5.0-natives-linux-armv6hf-d04f255aa1f37c245b032c7eec9477c.jar
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/windres-windows.exe
rm -rf %{buildroot}/opt/processing/lib/app/resources/modes/java/application/launch4j/bin/ld-windows.exe

%files
%{_bindir}/%{name}
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
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
