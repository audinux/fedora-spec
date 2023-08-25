Name:    morgan
Version: 1.2.0
Release: 1%{?dist}
Summary: Organ-inspired VST3 plug-ins
License: GPL-3.0-only
URL:     https://github.com/getdunne/MOrgan

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/getdunne/MOrgan/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: build.tar.gz
Source2: morgan.png

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: JUCE61
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
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: lv2-devel
BuildRequires: openssl-devel
BuildRequires: hidapi-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel
BuildRequires: libglvnd-devel
BuildRequires: desktop-file-utils

%description
This is a small collection of open-source audio plug-ins
inspired by the basic design of Hammond tone-wheel organs.
These are NOT intended to serve as a "B-3 emulator"--if
that's what you're looking for, have a look at the excellent
(and free) CollaB3 by Sampleson, or any of the many B-3
and "clonewheel" organ plug-ins available commercially.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n MOrgan-%{version}

# The build uses JUCE61
tar xvfz %{SOURCE1}

%build

%set_build_flags

export CXXFLAGS="$CXXFLAGS -include cstring -include utility -I/usr/src/JUCE61/modules -I/usr/src/JUCE61/modules/juce_audio_processors/format_types/VST3_SDK/"

cd MOrgan\ Cab/Builds/LinuxMakefile
%make_build STRIP=true
cd ../../..

cd MOrgan\ Osc/Builds/LinuxMakefile
%make_build STRIP=true
cd ../../..

cd MOrgan\ Perc/Builds/LinuxMakefile/
%make_build STRIP=true
cd ../../..

%install 

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cd MOrgan\ Cab/Builds/LinuxMakefile/build/
cp -a 'MOrgan Cab' %{buildroot}/%{_bindir}/MOrgan_Cab
cp -rav 'MOrgan Cab.vst3' %{buildroot}/%{_libdir}/vst3/MOrgan_Cab.vst3
mv %{buildroot}/%{_libdir}/vst3/MOrgan_Cab.vst3/Contents/%{_target}/MOrgan\ Cab.so %{buildroot}/%{_libdir}/vst3/MOrgan_Cab.vst3/Contents/%{_target}/MOrgan_Cab.so
cd ../../../..

cd MOrgan\ Osc/Builds/LinuxMakefile/build/
cp -a 'MOrgan Osc' %{buildroot}/%{_bindir}/MOrgan_Osc
cp -rav 'MOrgan Osc.vst3' %{buildroot}/%{_libdir}/vst3/MOrgan_Osc.vst3
mv %{buildroot}/%{_libdir}/vst3/MOrgan_Osc.vst3/Contents/%{_target}/MOrgan\ Osc.so %{buildroot}/%{_libdir}/vst3/MOrgan_Cab.vst3/Contents/%{_target}/MOrgan_Osc.so
cd ../../../..

cd MOrgan\ Perc/Builds/LinuxMakefile/build/
cp -a 'MOrgan Perc' %{buildroot}/%{_bindir}/MOrgan_Perc
cp -rav 'MOrgan Perc.vst3' %{buildroot}/%{_libdir}/vst3/MOrgan_Perc.vst3
mv %{buildroot}/%{_libdir}/vst3/MOrgan_Perc.vst3/Contents/%{_target}/MOrgan\ Perc.so %{buildroot}/%{_libdir}/vst3/MOrgan_Cab.vst3/Contents/%{_target}/MOrgan_Perc.so
cd ../../../..

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/morgan_cab.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=MOrgan_Cab
Exec=MOrgan_Cab
Icon=morgan
Comment=MOrgan Cab
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/morgan_osc.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=MOrgan_Osc
Exec=MOrgan_Osc
Icon=morgan
Comment=MOrgan Osc
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

cat > %{buildroot}%{_datadir}/applications/morgan_perc.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=MOrgan_Perc
Exec=MOrgan_Perc
Icon=morgan
Comment=MOrgan Perc
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/morgan_cab.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/morgan_osc.desktop

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/morgan_perc.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/morgan_cab.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/morgan_osc.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/morgan_perc.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Thu Aug 24 2023 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-1
- Initial spec file
