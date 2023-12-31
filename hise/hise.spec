# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3, IDE, Devel
# Category: Audio, Programming, Tool

Name:    HISE
Version: 3.6.2
Release: 1%{?dist}
Summary: The open source framework for sample based instrument
License: GPL-3.0-or-later OR LicenseRef-www-hise-audio
URL:     https://github.com/christophhart/HISE

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/christophhart/HISE/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: JUCE
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
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: desktop-file-utils

%description
HISE is a cross-platform open source audio application for building virtual instruments.
It emphasizes on sampling, but includes some basic synthesis features for making hybrid
instruments as well as audio effects.

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n %{name}-%{version}

unzip %{SOURCE1}

%build

%set_build_flags
CWD=`pwd`
#export LDFLAGS="`pkg-config --libs glib-2.0 gtk+-3.0 webkit2gtk-4.0` $LDFLAGS"
export CPPFLAGS="-I$CWD/VST_SDK/VST2_SDK"

cd projects/standalone/
Projucer --resave HISE\ Standalone.jucer

cd Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true

cd ../../../..

cd projects/plugin/
Projucer --resave HISE.jucer

cd Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true

%install

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/demos/
install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/

cp projects/standalone/Builds/LinuxMakefile/build//HISE\ Standalone %{buildroot}/%{_bindir}/hise
cp -ra extras/* %{buildroot}/%{_datadir}/%{name}/demos/
install -m 644 -p ./hi_core/hi_images/logo_mini.png %{buildroot}/%{_datadir}/icons/%{name}/%{name}.png

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -p projects/plugin/Builds/LinuxMakefile/build/HISE.so %{buildroot}%{_libdir}/vst/

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=HISE
Exec=hise
Icon=hise
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

desktop-file-install                         \
  --add-category="Audio;AudioVideo"	     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license license.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/demos/*

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Sat Sep 23 2023 Yann Collette <ycollette.nospam@free.fr> - 3.6.2-1
- update to 3.6.2-1

* Wed Sep 13 2023 Yann Collette <ycollette.nospam@free.fr> - 3.6.1-1
- update to 3.6.1-1

* Sat Aug 12 2023 Yann Collette <ycollette.nospam@free.fr> - 3.6.0-1
- update to 3.6.0-1

* Mon Jul 17 2023 Yann Collette <ycollette.nospam@free.fr> - 3.5.0-1
- update to 3.5.0-1

* Sun Mar 26 2023 Yann Collette <ycollette.nospam@free.fr> - 3.0.3-1
- update to 3.0.3-1

* Tue Mar 21 2023 Yann Collette <ycollette.nospam@free.fr> - 3.0.2-1
- update to 3.0.2-1

* Mon Nov 21 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.1-1
- update to 3.0.1-1

* Wed Oct 26 2022 Yann Collette <ycollette.nospam@free.fr> - 3.0.0-1
- update to 3.0.0-1

* Tue Jul 05 2022 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- Initial spec file
