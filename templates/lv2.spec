# Tag: Effect
# Type: LV2
# Category: Effect

Name:    lv2-invada-plugins
Version: 1.2.0
Release: 29%{?dist}
Summary: A collection of LV2 plugins from Invada Records
License: GPL-2.0-or-later
URL:     http://www.invadarecords.com/Downloads.php?ID=00000264

Vendor:       Audinux
Distribution: Audinux

Source0: http://launchpad.net/invada-studio/lv2/1.2/+download/invada-studio-plugins-lv2_%{version}-nopkg.tgz

BuildRequires: gcc
BuildRequires: make
BuildRequires: lv2-devel

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%autosetup -n invada-studio-plugins-lv2-%{version}

%build

%make_build

%install

%make_install install-sys INSTALL_SYS_PLUGINS_DIR="%{_libdir}/lv2"

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Wed Oct 25 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-29
- update to 1.2.0-29 - move from fedora to audinux
