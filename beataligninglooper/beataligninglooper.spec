# Tag: Jack
# Type: Standalone
# Category: Audio, Looper

%global commit0 da64bd13d0b5db400e7a0fabd3efe245979e6667

Name: beataligninglooper
Version: 0.0.1
Release: 1%{?dist}
Summary: A guitar looper 
License: GPL-3.0-or-later
URL: https://github.com/DanielRudrich/BeatAligningGuitarLooper
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/DanielRudrich/BeatAligningGuitarLooper/archive/refs/heads/master.zip#/%{name}-%{version}.zip
Source1: Build.zip

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: unzip
BuildRequires: JUCE60
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
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils

# The Makefileq are generated using JUCE60 / ProJucer60

%description
A guitar looper which detects the tempo and plays along
a rudimentary drumbeat.
It also aligns start and stop of the loop to the nearest beats. 

%prep
%autosetup -n BeatAligningGuitarLooper-master

unzip %{SOURCE1}

%build

cd Builds/LinuxMakefile/

%make_build CXXFLAGS="-include math.h" LDFLAGS="-lfftw3 -lfftw3f"

%install

cd Builds/LinuxMakefile/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 build/BaGLApp %{buildroot}/%{_bindir}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/pixmaps/
install -m 644 ../../appLogo.png %{buildroot}/%{_datadir}/pixmaps/beataligninglooper.png

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{name}
Icon=%{name}
Comment=Beat Aligning Guitar Looper
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
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Sun Jan 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.9.9-1
- Initial spec file
