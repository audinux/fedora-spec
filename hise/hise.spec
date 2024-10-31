# Status: active
# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3, IDE, Devel
# Category: Audio, Programming, Tool

Name: HISE
Version: 4.1.0
Release: 2%{?dist}
Summary: The open source framework for sample based instrument
License: GPL-3.0-or-later OR LicenseRef-www-hise-audio
URL: https://github.com/christophhart/HISE
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinu

Source0: https://github.com/christophhart/HISE/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: unzip
BuildRequires: make
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
HISE is a cross-platform open source audio application for building virtual instruments.
It emphasizes on sampling, but includes some basic synthesis features for making hybrid
instruments as well as audio effects.

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: GPL-3.0-or-later OR LicenseRef-www-hise-audio

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n %{name}-%{version}

# VST2 SDK still required for the build
unzip %{SOURCE1}

cd tools/SDK
unzip sdk.zip

%build

%set_build_flags

CWD=`pwd`
export CPPFLAGS="-I$CWD/VST_SDK/VST2_SDK"

cd projects/standalone/
$CWD/tools/projucer/Projucer --resave HISE\ Standalone.jucer

cd Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true V=1

cd ../../../..

cd projects/plugin/
$CWD/tools/projucer/Projucer --resave HISE.jucer

cd Builds/LinuxMakefile/
%make_build CONFIG=Release STRIP=true v=1

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/demos/
install -m 755 -d %{buildroot}/%{_datadir}/applications/
install -m 755 -d %{buildroot}/%{_datadir}/icons/%{name}/
install -m 755 -d %{buildroot}/%{_libdir}/vst3/

cp projects/standalone/Builds/LinuxMakefile/build//HISE\ Standalone %{buildroot}/%{_bindir}/hise
cp -ra extras/* %{buildroot}/%{_datadir}/%{name}/demos/
install -m 644 -p ./hi_core/hi_images/logo_mini.png %{buildroot}/%{_datadir}/icons/%{name}/%{name}.png

cp -ra projects/plugin/Builds/LinuxMakefile/build/HISE.vst3 %{buildroot}/%{_libdir}/vst3/

install -m 755 -d %{buildroot}/%{_usrsrc}/
mkdir tmp
cd tmp
tar xvfz %{SOURCE0}

rm -rf HISE-%{version}/.github/
rm -f HISE-%{version}/.gitignore
rm -f HISE-%{version}/.gitmodules

find tools/ -executable -type f -exec rm -rf {} \;

mv HISE-%{version} %{buildroot}/%{_usrsrc}/HISE
cd ..

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=HISE
Exec=env GDK_BACKEND=x11 hise
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
%{_usrsrc}/HISE/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Oct 30 2024 Yann Collette <ycollette.nospam@free.fr> - 4.1.0-2
- update to 4.1.0-2

* Sat Jun 22 2024 Yann Collette <ycollette.nospam@free.fr> - 3.6.2-2
- update to 3.6.2-2 - add HISE sources in /usr/src/HISE

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
