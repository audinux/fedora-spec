# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Pau Aliagas <linuxnow@gmail.com>
#
# The RPM side of the records: one binary package per Fedora record set under records/<host class>/<set>/. The
# Debian sets are built from debian/; this spec installs only the sets named below. The version is the dated one
# the tag and debian/changelog carry (vYYYYMMDDXX).

%global host_class x86-64
%global set_name fedora44
%global set_dir %{_datadir}/omx/qualification/%{host_class}/%{set_name}

Name: omx-qualification-records
Version: 2026110101
Release: 1%{?dist}
Summary: Distributed qualification records of OpenMixer plugin sets
License: GPL-3.0-or-later
URL: https://github.com/FreeMixer/omx-qualification-records
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# the record check in %%check
BuildRequires: python3

%description
The plugin-qualify records of plugin sets measured on a reference machine of
a host class, packaged so that plugin-qualify-sync on a machine of the same
class takes a plugin from them instead of measuring it.

%package -n omx-qualification-%{host_class}-%{set_name}
Summary: Qualification records of the %{set_name} plugin set for %{host_class}
# the first plugin-qualify that reads distributed records, as plugin-qualify-records-package declares it
Requires: plugin-qualify >= 0.17.0

%description -n omx-qualification-%{host_class}-%{set_name}
The plugin-qualify records of the %{set_name} plugin set (the OpenMixer worker
image's plugins on Fedora 44), measured on a %{host_class} machine.
plugin-qualify-sync takes a plugin from them instead of measuring it, and only
when every file of the installed plugin hashes as the measured one did; any
other plugin is measured on the machine as before. An x86_64 machine has no
device tree to name its class: the sync reads these records once
/etc/omx/qualify.conf says "host_class %{host_class}", and finds the CLAP
plugins of /usr/lib64/clap once it says "clap_extra /usr/lib64/clap".

%prep
%autosetup

%build
# the records are data: nothing to build

%install
mkdir -p %{buildroot}%{set_dir}
cp -p records/%{host_class}/%{set_name}/* %{buildroot}%{set_dir}/

%check
python3 tools/check-records.py %{buildroot}%{set_dir}
# the package installs every file of the set, byte for byte
(cd records/%{host_class}/%{set_name} && sha256sum *) | sort -k2 > in-tree.sha256
(cd %{buildroot}%{set_dir} && sha256sum *) | sort -k2 > installed.sha256
cmp in-tree.sha256 installed.sha256

%files -n omx-qualification-%{host_class}-%{set_name}
%license LICENSE
%dir %{_datadir}/omx
%dir %{_datadir}/omx/qualification
%dir %{_datadir}/omx/qualification/%{host_class}
%{set_dir}/

%changelog
