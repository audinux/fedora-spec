# Status: active
# Tag: Effect, Amp Simul
# Type: Standalone, Plugin, LV2, CLAP, VST3
# Category: Effect

Name: ampforge
Version: 0.4.0
Release: 1%{?dist}
Summary: Open-source guitar amp simulator plugin — VST3/LV2/CLAP, with a reorderable pedalboard chain (amp, cab IR, drive, mod, delay/reverb)
License: GPL-3.0-or-later
URL: https://github.com/Loursy/AmpForge
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Loursy/AmpForge/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: mesa-libGL-devel
BuildRequires: pkgconfig(jack)
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: dbus-devel

%description
A free, open-source guitar amp simulator plugin for Linux — with a couple of vocal effects built in too.
AmpForge is a single plugin — not a chain of separate plugins bolted together in a DAW — that hosts a
full, reorderable pedalboard-and-amp chain internally, in the spirit of Guitar Rig / BIAS FX.
It ships as VST3, LV2, CLAP, and a JACK/PipeWire standalone app, all built from one codebase.
Linux has never really had a good, free, actively-developed answer to Guitar Rig or BIAS FX. AmpForge
is an attempt at exactly that.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n AmpForge-%{version}

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/bin/ampforge_amp %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/bin/ampforge_screamer %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/bin/ampforge_gain %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/bin/ampforge_main %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/ampforge_amp.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/ampforge_screamer.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/ampforge_gain.lv2 %{buildroot}/%{_libdir}/lv2/
cp -ra %{__cmake_builddir}/bin/ampforge_main.lv2 %{buildroot}/%{_libdir}/lv2/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/ampforge_amp.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/ampforge_screamer.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/ampforge_gain.vst3 %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/bin/ampforge_main.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
install -m 755 %{__cmake_builddir}/bin/ampforge_main.clap %{buildroot}/%{_libdir}/clap/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md THIRD-PARTY-NOTICES.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Thu Aug 27 2026 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-1
- update to 0.4.0-1

* Wed Aug 19 2026 Yann Collette <ycollette.nospam@free.fr> - 0.3.0-1
- Initial build
