# Tag: Editor, Audio, MIDI
# Type: Standalone, Plugin, LV2, VST3, CLAP
# Category: Audio, IDE, Language

Name: plugdata
Version: 0.9.1
Release: 2%{?dist}
Summary: Pure Data as a plugin, with a new GUI
URL: https://github.com/timothyschoen/PlugData
ExclusiveArch: x86_64 aarch64
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

# ./plugdata-source.sh <TAG>
# ./plugdata-source.sh v0.9.1

Source0: PlugData.tar.gz
Source1: plugdata-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gtk+-x11-3.0)
BuildRequires: libcurl-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: xsimd-devel
BuildRequires: lv2-devel
BuildRequires: mpg123-devel
BuildRequires: lame-devel
BuildRequires: flac-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: opus-devel
BuildRequires: fluidsynth-devel
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: desktop-file-utils

%description
Plugin wrapper around PureData to allow patching in a wide selection of DAWs.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%package -n clap-%{name}
Summary:  CLAP version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n PlugData

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DBUILD_SHARED_LIBS=OFF -DENABLE_GEM=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/
install -m 755 -d %{buildroot}%{_libdir}/clap/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_fontbasedir}/plugdata/

cp -ra Plugins/LV2/* %{buildroot}%{_libdir}/lv2/
cp -ra Plugins/VST3/* %{buildroot}%{_libdir}/vst3/
cp -ra Plugins/CLAP/* %{buildroot}%{_libdir}/clap/

cp Plugins/Standalone/* %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p Resources/Icons/plugdata_logo.png %{buildroot}/%{_datadir}/icons/%{name}/plugdata.png
install -m 644 -p Resources/Fonts/*.ttf %{buildroot}/%{_fontbasedir}/plugdata/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/plugdata.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=plugdata
Comment=Audio Plugin
Exec=plugdata
Icon=plugdata
Terminal=false
Type=Application
Categories=Audio;AudioVideo;
EOF

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/plugdata.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/plugdata.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_fontbasedir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Sat Aug 10 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.1-2
- update to 0.9.1-2

* Mon Jul 29 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-2
- update to 0.9.0-2 - activate GEM

* Sun Jul 21 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-1
- update to 0.9.0-1

* Wed Jan 17 2024 Yann Collette <ycollette.nospam@free.fr> - 0.8.3-1
- update to 0.8.3-1

* Tue Nov 21 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.2-1
- update to 0.8.2-1

* Fri Nov 17 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.1-1
- update to 0.8.1-1

* Wed Oct 04 2023 Yann Collette <ycollette.nospam@free.fr> - 0.8.0-1
- update to 0.8.0-1

* Tue May 09 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.1-1
- update to 0.7.1-1

* Tue Mar 07 2023 Yann Collette <ycollette.nospam@free.fr> - 0.7.0-1
- update to 0.7.0-1

* Mon Jan 16 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.4-1
- update to 0.6.4-1

* Tue Jan 10 2023 Yann Collette <ycollette.nospam@free.fr> - 0.6.3-1
- update to 0.6.3-1

* Thu Nov 03 2022 Yann Collette <ycollette.nospam@free.fr> - 0.6.2-1
- update to 0.6.2-1

* Wed Jun 29 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
