%define _lto_cflags %{nil}

Name:    cardinal
Version: 23.02
Release: 2%{?dist}
Summary: Virtual modular synthesizer plugin
License: GPL-3.0-or-later
URL:     https://github.com/DISTRHO/Cardinal

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DISTRHO/Cardinal/releases/download/%{version}/cardinal-%{version}.tar.xz
Source1: Cardinal.png

BuildRequires: gcc gcc-c++ make
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
BuildRequires: jack-audio-connection-kit-devel
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
BuildRequires: wget
BuildRequires: desktop-file-utils
BuildRequires: findutils
BuildRequires: fdupes

Requires(pre): python3-qt5
Requires:      %{name}-common = %{version}-%{release}

%description
Cardinal, the Rack!

Cardinal is a free and open-source virtual modular synthesizer plugin,
available as JACK standalone and LV2, VST2 and VST3 audio plugin
for FreeBSD, Linux, macOS and Windows.
It is based on the popular VCV Rack but with a focus on being a fully
self-contained plugin version.

%package common
Summary:   Common files for Cardinal
BuildArch: noarch

%description common
Common data files for Cardinal standalone and plugin versions.

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
Requires: %{name}-common = %{version}-%{release}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
Requires: %{name}-common = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
Requires: %{name}-common = %{version}-%{release}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
Requires: %{name}-common = %{version}-%{release}

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
mv %buildroot/usr/lib %buildroot/usr/lib64
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

install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

# Remove empty file
rm %{buildroot}%{_datadir}/%{name}/surgext/patches/README.md
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
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files common
%license LICENSE
%{_datadir}/%{name}/
%{_datadir}/doc/%{name}/

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
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
