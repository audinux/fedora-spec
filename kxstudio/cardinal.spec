# Status: active
# Tag: Modular
# Type: Standalone, Plugin, LV2, VST, VST3, CLAP
# Category: Audio, Synthesizer, Effect

%define _lto_cflags %{nil}
# On some platforms, the debug symbols extraction produces
# some timeout.
%global debug_package %{nil}

Name: cardinal
Version: 24.12
Release: 2%{?dist}
Summary: Virtual modular synthesizer plugin
License: GPL-3.0-or-later
URL: https://github.com/DISTRHO/Cardinal
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/Cardinal/releases/download/%{version}/cardinal-%{version}.tar.xz
Source1: Cardinal.png

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: findutils
BuildRequires: fdupes
BuildRequires: wget
BuildRequires: python-qt5-devel
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fluidsynth-devel
BuildRequires: fftw-devel
BuildRequires: mxml-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: non-ntk-fluid
BuildRequires: non-ntk-devel
BuildRequires: pkgconfig(jack)
BuildRequires: linuxsampler-devel
BuildRequires: jansson-devel
BuildRequires: libarchive-devel
BuildRequires: libsamplerate-devel
BuildRequires: libXrandr-devel
BuildRequires: libXext-devel
BuildRequires: libXcursor-devel
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
BuildRequires: speexdsp-devel
BuildRequires: desktop-file-utils

Requires(pre): python3-qt5
Requires:      %{name}-common = %{version}-%{release}

%description
Cardinal, the Rack!

Cardinal is a free and open-source virtual modular synthesizer plugin,
available as JACK standalone and LV2, VST2 and VST3 audio plugin
for FreeBSD, Linux, macOS and Windows.
It is based on the popular VCV Rack but with a focus on being a fully
self-contained plugin version.

%package -n license-%{name}
Summary: License and documentation for %{name}
BuildArch: noarch

%description -n license-%{name}
License and documentation for %{name}

%package common
Summary: Common files for Cardinal
BuildArch: noarch

%description common
Common data files for Cardinal standalone and plugin versions.

%package mini
Summary: Mini variant of Cardinal
Requires: %{name}-common = %{version}-%{release}
Requires: license-%{name} = %{version}-%{release}

%description mini
This is a special variant with a very small, hand-picked module selection
and limited IO (2 audio ports plus 5 CV).

%package -n lv2-%{name}
Summary: LV2 version of %{name}
Requires: %{name}-common = %{version}-%{release}
Requires: license-%{name} = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
Requires: %{name}-common = %{version}-%{release}
Requires: license-%{name} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
Requires: %{name}-common = %{version}-%{release}
Requires: license-%{name} = %{version}-%{release}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
Requires: %{name}-common = %{version}-%{release}
Requires: license-%{name} = %{version}-%{release}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n %{name}-%{version}

%build

%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=format-security"
export CXXFLAGS="$CXXFLAGS -include cstdint -Wno-error=format-security"

%make_build PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true SYSDEPS=true

%install
%make_install PREFIX=/usr LIBDIR=%{_libdir} SKIP_STRIPPING=true SYSDEPS=true
%ifarch x86_64 amd64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Cardinal
Exec=Cardinal
Icon=Cardinal
Comment=Cardinal Modular Synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/%{name}-mini.desktop <<EOF
[Desktop Entry]
Name=Cardinal Mini
Exec=CardinalMini
Icon=Cardinal
Comment=Cardinal Modular Synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/

# Fix perms
find %{buildroot}%{_datadir}/%{name} -type f -perm /a+x -exec chmod -x '{}' \+
# Fix line endings
sed -i -e 's/\r$//' %{buildroot}%{_datadir}/%{name}/ValleyAudio/res/Topograph.svg
# Deduplicate files by soft linking
%fdupes -s %{buildroot}%{_datadir}/%{name}
# Make sure binaries are executable for stripping by debuginfo
find %{buildroot}%{_libdir} \
	\( -name '*.so' -o -name '*.clap' \) \
	-type f \
	-exec chmod 0755 '{}' \+

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/Cardinal
%{_bindir}/CardinalNative
%{_datadir}/applications/%{name}.desktop

%files common
%{_datadir}/%{name}/
%{_datadir}/doc/%{name}/
%{_datadir}/icons/hicolor/512x512/apps/*

%files mini
%{_bindir}/CardinalMini
%{_libdir}/lv2/CardinalMini.lv2/
%{_datadir}/applications/%{name}-mini.desktop

%files -n license-%{name}
%license LICENSE
%doc README.md docs/*

%files -n lv2-%{name}
%{_libdir}/lv2/Cardinal.lv2/
%{_libdir}/lv2/CardinalFX.lv2/
%{_libdir}/lv2/CardinalSynth.lv2/

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Dec 16 2024 Yann Collette <ycollette.nospam@free.fr> - 24.12-2
- update to 24.12-2

* Tue Sep 24 2024 Yann Collette <ycollette.nospam@free.fr> - 24.09-2
- update to 24.09-2

* Sat May 25 2024 Yann Collette <ycollette.nospam@free.fr> - 24.05-2
- update to 24.05-2

* Thu Apr 11 2024 Yann Collette <ycollette.nospam@free.fr> - 24.04-2
- update to 24.04-2

* Tue Oct 24 2023 Yann Collette <ycollette.nospam@free.fr> - 23.10-2
- update to 23.10-2

* Sun Jul 16 2023 Justin Koh <j@ustink.org> - 23.07-2
- Update to 23.07-2

* Mon Feb 27 2023 Yann Collette <ycollette.nospam@free.fr> - 23.02-2
- update to 23.02-2

* Tue Dec 20 2022 Yann Collette <ycollette.nospam@free.fr> - 22.12-2
- update to 22.12-2

* Sun Nov 27 2022 Yann Collette <ycollette.nospam@free.fr> - 22.11-2
- update to 22.11-2

* Sat Oct 15 2022 Yann Collette <ycollette.nospam@free.fr> - 22.10-2
- update to 22.10-2

* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 22.07-2
- update to 22.07-2 - fix packaging

* Thu Jun 30 2022 Yann Collette <ycollette.nospam@free.fr> - 22.07-1
- update to 22.07-1

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 22.05-1
- update to 22.05-1

* Mon Apr 04 2022 Yann Collette <ycollette.nospam@free.fr> - 22.04-1
- update to 22.04-1

* Mon Mar 21 2022 Yann Collette <ycollette.nospam@free.fr> - 22.03-1
- update to 22.03-1

* Fri Feb 18 2022 Yann Collette <ycollette.nospam@free.fr> - 22.02-1
- Initial build
