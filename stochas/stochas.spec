# Status: active
# Tag: MIDI, Sequencer
# Type: Standalone, Plugin, VST3, CLAP
# Category: DAW, Sequencer

Name: stochas
Version: 1.3.12
Release: 4%{?dist}
Summary: A VST3 MIDI sequencer
License: GPL-3.0-only
URL: https://github.com/surge-synthesizer/stochas
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Use ./source-stochas.sh to get the sources (latest master for now)
#     ./source-stochas.sh v1.3.12

Source0: stochas.tar.gz
Source1: source-stochas.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: rsync
BuildRequires: alsa-lib-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: pkgconfig(jack)

Requires: license-%{name}

%description
A VST3 MIDI sequencer

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

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n %{name}

# Remove git detection
sed -i -e "s/find_package/#find_package/g" cmake/versiontools.cmake

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/stochas_artefacts/VST3/Stochas.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}%{_libdir}/clap/
cp -ra %{__cmake_builddir}/stochas_artefacts/CLAP/Stochas.clap %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 644 -p %{__cmake_builddir}/stochas_artefacts/Standalone/Stochas %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license COPYING

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Oct 30 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.12-4
- update to 1.3.12-4

* Tue Feb 20 2024 Yann Collette <ycollette.nospam@free.fr> - 1.3.10-4
- update to 1.3.10-4

* Mon Dec 05 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.9-4
- update to 1.3.9-4

* Mon Nov 21 2022 Yann Collette <ycollette.nospam@free.fr> - 1.3.8-4
- update to 1.3.8-4

* Mon Oct 25 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-4
- update to 1.3.5-4 - update for Fedora 35

* Sun Jun 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.3.5-3
- update to 1.3.5-3

* Sun Dec 13 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-3
- update to 1.3.4-3 - fix install

* Mon Nov 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.4-2
- update to 1.3.4

* Sat Oct 3 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.3-2
- fix for fedora 33

* Sun Sep 6 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.3-1
- update to 1.3.3

* Thu Aug 13 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
