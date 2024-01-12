# Tag: Effect, Equalizer
# Type: LADSPA
# Category: Audio, Effect

# spec file for package ladspa-vocoder
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name: ladspa-vocoder
Version: 0.4
Release: 1%{?dist}
Summary: LADSPA vocoder plugin
License: GPL-2.0+
Url: https://www.sirlab.de/linux/download

Vendor:       Audinux
Distribution: Audinux

Source0: https://www.sirlab.de/linux/download/vocoder-ladspa-%{version}.tgz
Patch1: ladspa-vocoder-0001-add-attributes.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: ladspa-devel

%description
This package provides a LADSPA (Linux Audio Developer's Simple Plug-in API)
vocoder plugin.

%prep
%autosetup -n vocoder-%{version}

sed -i -e "/\-msse2/d" Makefile
sed -i -e "s/\$(LD)/\$(CC)/g" Makefile

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
%set_build_flags
%make_build CFLAGS="%{optflags} -fPIC -ggdb"

%install
%make_install INSTALL_PLUGINS_DIR=%{buildroot}/%{_libdir}/ladspa/

%files
%doc README
%license COPYRIGHT
%{_libdir}/ladspa

%changelog
* Tue Dec 29 2020 Yann Collette <ycollette dot nospam at free.fr> 0.4-1
- update to 0.4-1

* Mon Mar  3 2014 tiwai@suse.de
- Run spec-cleaner
- Remove obsoleted autoreq/autoprov tags
- Patch carried from the original ladspa package:
  vocoder-0.1.dif
* Mon Dec 16 2013 tiwai@suse.de
- Initial version 0.3: split from ladspa package
