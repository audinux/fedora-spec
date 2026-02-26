# Status: active
# Tag: Jack
# Type: Standalone
# Category: Audio, Tool

%global commit0 25b5412f6b531c557ff05dde5ae5b07b479dd5d4

Name: luma
Version: 0.0.1
Release: 1%{?dist}
Summary: a minimal LV2 host for Linux that runs LV2 plugins with X11 user interfaces using JACK for audio
License: GPL-2.0-or-later
URL: https://github.com/brummer10/luma
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/brummer10/Luma/archive/%{commit0}.zip#/%{name}-%{version}.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: libX11-devel
BuildRequires: gtk2-devel
BuildRequires: lilv-devel
BuildRequires: pkgconfig(jack)

%description
Luma is a lightweight, multi-instance LV2 host for Linux designed for clarity, correctness, and debugging.
It supports real-world LV2 plugins including X11 and GTK2 user interfaces, advanced LV2 extensions such
as data-access, and a fully functional terminal-based NO-GUI mode.
Luma is intentionally compact, readable, and suitable as both:
- a minimal plugin launcher
- a reference LV2 host implementation
- a development and debugging tool
- a headless LV2 runner
- a testbed for LV2 UI and Atom interaction
    
%prep
%autosetup -n Luma-%{commit0}

%build

%make_build STRIP=true

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 luma %{buildroot}%{_bindir}/

%files
%doc ReadMe.md
%{_bindir}/*

%changelog
* Wed Feb 25 2026 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial build
