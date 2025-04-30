# Status: active
# Tag: Effect, Tool
# Type: Plugin, LV2
# Category: Effect, Tool

Name: lv2-gtk-ui-bridge
Version: 0.1
Release: 1%{?dist}
Summary: LV2 Gtk2/3 UIs as LV2 X11 UIs
License: MIT
URL: https://github.com/falkTX/lv2-gtk-ui-bridge
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/falkTX/lv2-gtk-ui-bridge/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: sratom-devel
BuildRequires: sord-devel
BuildRequires: libX11-devel

%description
lv2-gtk-ui-bridge is a special LV2 bundle that allows to use legacy LV2 Gtk2/3 UIs as LV2 X11 UIs.
This increases the compatibility of such UIs to hosts that do not support the legacy UI types.

Because Gtk2/3 can often conflict with host function symbols
(e.g. a Gtk4 host can't load Gtk3 libraries) the UI is loaded in a separate process.
This means the UI can load without crashing the host if usually there would be function symbol
conflicts, but in return it is not possible to support LV2 instance access nor LV2 data access
(which some UIs use for fancy fast graphs).
Parameter changes and LV2 atom messages still work as normal though, passing through an IPC layer.

The list of supported plugins is hardcoded in lv2-gtk-ui-bridge.lv2/manifest.ttl.
This file needs to be updated in order to support more plugins with a Gtk2/3-based UI.
Just create a ticket or a pull request in case I missed any.

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags

%make_build

%install

install -m 755 -d %{buildroot}%{_libdir}/lv2/
cp -rav lv2-gtk-ui-bridge.lv2 %{buildroot}/%{_libdir}/lv2/

%files
%doc README.md
%license COPYING
%{_libdir}/lv2/*

%changelog
* Mon Apr 28 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version of the spec
