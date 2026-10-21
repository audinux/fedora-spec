# Status: active
# Tag: Synthesizer
# Type: Standalone, Plugin, LV2, CLAP, VST3
# Category: Synthesizer

Name: fsvr
Version: 0.8.2
Release: 1%{?dist}
Summary: Software reconstruction of the 1998 Yamaha FS1R synthesizer
License: GPL-3.0-or-later
URL: https://github.com/musicastudio/FSVR/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/musicastudio/FSVR/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(jack)
BuildRequires: lv2-devel
BuildRequires: alsa-lib-devel
BuildRequires: libX11-devel
BuildRequires: libglvnd-devel
BuildRequires: desktop-file-utils

Requires: license-%{name}
Requires: common-%{name}

%description
FSVR, Formant Synthesizer Virtual Rack, is a software reconstruction of the Yamaha FS1R as a plugin
and a console synth: its firmware logic rewritten in C++ from the decompiled ROM, four parts,
32 channels, the filter, both LFOs, pan, the three effect blocks, performances and Fseq playback.
CLAP, VST3, VST2 and standalone, with an editor for every parameter the unit has, a bank manager
for your own .syx libraries and Import Audio for Fseqs.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n common-%{name}
Summary: Common data files for %{name}
License: GPL-3.0-or-later

%description -n common-%{name}
Common data files for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary: VST2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n clap-%{name}
Summary: CLAP version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n FSVR-%{version}

%build

%set_build_flags
export CXXFLAGS=`echo $CXXFLAGS | sed -e "s/-Werror=format-security//g"`
export CFLAGS=`echo $CFLAGS | sed -e "s/-Werror=format-security//g"`
export LDFLAGS="`pkg-config --libs-only-L jack` $LDFLAGS"

%cmake -DFSVR_BUILD_PLUGIN=ON
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 bin/Standalone/FSVR %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/%{name}/presets/
cp -ra presets/* %{buildroot}/%{_datadir}/%{name}/presets/

install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -ra bin/CLAP/* %{buildroot}/%{_libdir}/clap/

install -m 755 -d %{buildroot}/%{_libdir}/vst/
cp -ra bin/VST2/* %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -ra bin/VST3/* %{buildroot}/%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 icon.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Exec=FSVR
Icon=%{name}
Comment=Software reconstruction of the 1998 Yamaha FS1R synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*

%files -n license-%{name}
%doc README.md NOTICE.md STATUS.md docs/*
%license LICENSE
%{_datadir}/%{name}/presets/*

%files -n common-%{name}
%{_datadir}/%{name}/presets/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Wed Oct 21 2026 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- Initial spec
