Name:    plugdata
Version: 0.5.3
Release: 1%{?dist}
Summary: Pure Data as a plugin, with a new GUI
URL:     https://github.com/timothyschoen/PlugData
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

# ./plugdata-source.sh <TAG>
# ./plugdata-source.sh v0.5.3

Source0: PlugData.tar.gz
Source1: plugdata-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
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
BuildRequires: JUCE
BuildRequires: desktop-file-utils

%description
Plugin wrapper around PureData to allow patching in a wide selection of DAWs.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n PlugData

%build

export HOME=`pwd`
mkdir -p .vst3
mkdir -p .lv2
mkdir -p .local/share/PlugData

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DCMAKE_CXX_FLAGS="-include utility -fPIC"
%cmake_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst3/PlugData.vst3/
install -m 755 -d %{buildroot}%{_libdir}/vst3/PlugDataFx.vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/PlugData.lv2/
install -m 755 -d %{buildroot}%{_libdir}/lv2/PlugDataFx.lv2/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_fontbasedir}/PlugData/

cp -ra Plugins/LV2/PlugData.lv2/* %{buildroot}%{_libdir}/lv2/PlugData.lv2/
cp -ra Plugins/LV2/PlugDataFx.lv2/* %{buildroot}%{_libdir}/lv2/PlugDataFx.lv2/

cp -ra Plugins/VST3/PlugData.vst3/* %{buildroot}%{_libdir}/vst3/PlugData.vst3/
cp -ra Plugins/VST3/PlugDataFx.vst3/* %{buildroot}%{_libdir}/vst3/PlugDataFx.vst3/

cp Plugins/Standalone/* %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 644 -p Resources/plugd_logo.png %{buildroot}/%{_datadir}/icons/%{name}/%{name}.png
install -m 644 -p Resources/PlugDataFont.ttf %{buildroot}/%{_fontbasedir}/PlugData/

install -m 755 -d %{buildroot}/%{_datadir}/applications/
cat > %{buildroot}/%{_datadir}/applications/PlugData.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=PlugData
Comment=Audio Plugin
Exec=PlugData
Icon=PlugData
Terminal=false
Type=Application
Categories=Audio;AudioVideo;
EOF

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/PlugData.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/PlugData.desktop

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

%changelog
* Wed Jun 29 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5.3-1
- update to 0.5.3-1

* Sun Apr 24 2022 Yann Collette <ycollette.nospam@free.fr> - 0.5-1
- Initial spec file
