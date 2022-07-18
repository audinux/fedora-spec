# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Editor

Name:    HISE
Version: 2.0.0
Release: 1%{?dist}
Summary: The open source framework for sample based instrument
License: GPLv2+
URL:     https://github.com/christophhart/HISE

Vendor:       Audinux
Distribution: Audinux
Source0: https://github.com/christophhart/HISE/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: hise-0001-juce-patch.patch
Patch1: hise-0002-ceilf.patch

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE61
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

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%set_build_flags

export LDFLAGS="`pkg-config --libs glib-2.0 gtk+-3.0 webkit2gtk-4.0` $LDFLAGS"

cd projects/standalone/
Projucer61 --resave HISE\ Standalone.jucer

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
%{_datadir}/%{name}/demos/*

%changelog
* Tue Jul 05 2022 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- Initial spec file
