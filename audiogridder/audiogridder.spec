# Tag: Effect, Tool
# Type: Plugin, Standalone, VST3
# Category: Effect, Tool

Name: audiogridder
Version: 1.2.0
Release: 1%{?dist}
Summary: DSP servers using general purpose computers and networks 
License: MIT
URL: https://github.com/apohl79/audiogridder
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./audiogridder-source.sh <TAG>
#        ./audiogridder-source.sh v1.2.0

Source0: audiogridder.tar.gz
Source1: audiogridder-source.sh
Patch0: audiogridder-0001-fix-ffmpeg-detection.patch

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: boost-devel
BuildRequires: libwebp-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: desktop-file-utils

%description
AudioGridder is a network bridge for audio and MIDI that allows for offloading
the DSP processing of audio plugins to remote computers running macOS or Windows.
This can come in handy when mixing complex projects or running CPU intensive
instruments for instance. AudioGridder comes with a plugin and a server and
supports VST2, VST3 and AudioUnit plugin formats. Plugins can be hosted and
accessed across the network: simply run the AudioGridder server on a remote
machine and connect your DAW using the AudioGridder plugin. This allows you to add
remote insert chains or instruments into your DAW's signal paths. The DSP code of
the loaded remote plugins will be executed on the remote machine and the remote
plugin UI's will be streamed over the wire. With AudioGridder you get an
experience very close to hosting the plugins directly in your DAW but not using
your local CPU.

For more information and intstallation instructions, please visit
https://audiogridder.com.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  MIT
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n audiogridder

sed -i -e "s/\/usr\/bin\/strip/true/g" CMakeLists.txt

%build

%cmake -DAG_ENABLE_DYNAMIC_LINKING=ON
%cmake_build

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_libdir}/vst3/

cp %{__cmake_builddir}/Server/AudioGridderServer_artefacts/AudioGridderServer %{buildroot}%{_bindir}/
cp %{__cmake_builddir}/PluginTray/AudioGridderPluginTray_artefacts/AudioGridderPluginTray %{buildroot}%{_bindir}/

cp -ra %{__cmake_builddir}/Plugin/AudioGridderInst_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Plugin/AudioGridderMidi_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/
cp -ra %{__cmake_builddir}/Plugin/AudioGridderFx_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/64x64/
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/16x16/

cp Server/Resources/icon64.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/audiogridder.png
cp Server/Resources/icon16.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/audiogridder.png
cp Server/Resources/icon.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/audiogridder.png

# Install desktop file
install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/audiogridderserver.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=AudioGridder ServerC
Exec=AudioGridderServer
Icon=audiogridder
Comment=AudioGridder Server Backend
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/audiogridderserver.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/audiogridderserver.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/AudioGridderServer
%{_datadir}/icons/hicolor/512x512/*
%{_datadir}/icons/hicolor/64x64/*
%{_datadir}/icons/hicolor/16x16/*
%{_datadir}/applications/audiogridderserver.desktop

%files -n vst3-%{name}
%{_bindir}/AudioGridderPluginTray
%{_libdir}/vst3/*

%changelog
* Wed Mar 20 2024 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
