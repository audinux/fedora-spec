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

Name:    processing
Version: 4.2
Release: 2%{?dist}
Summary: Processing Development Environment (PDE)
# Core is LGPL, others are GPL
License: GPL-2.0+ and LGPL-2.0+
Url:     https://processing.org/

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/processing/processing4/releases/download/processing-1292-%{version}/processing-%{version}-linux-x64.tgz
Source1: %{name}.desktop

AutoReqProv: no
BuildArch:   x86_64

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
%autosetup -n processing-%{version}

%build

%install
install -dm 0755 %{buildroot}/opt/%{name}
cp -R * %{buildroot}/opt/%{name}/

install -dm 0755 %{buildroot}/%{_datadir}/pixmaps
install -m 0644 lib/icons/pde-256.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -dm 0755 %{buildroot}/%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/

# Create a symlink
install -dm 0755 %{buildroot}/%{_bindir}
ln -s /opt/processing/processing %{buildroot}/%{_bindir}/processing

# Remove some non x86_64-linux files
rm -rf %{buildroot}/opt/processing/modes/java/libraries/io/library/linux-arm64/
rm -rf %{buildroot}/opt/processing/modes/java/libraries/io/library/linux-armv6hf/
rm -rf %{buildroot}/opt/processing/modes/java/libraries/serial/library/linux-arm64/
rm -rf %{buildroot}/opt/processing/modes/java/libraries/serial/library/linux-armv6hf/

%files
%{_bindir}/%{name}
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
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
