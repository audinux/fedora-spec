# Tag: Effect, Plugin, Audio
# Type: Standalone, Plugin, VST, VST3
# Category: Audio, Effect

%global commit0 371355b375d9

Name: paulstretch
Version: 1.2.4
Release: 3%{?dist}
Summary: A Paulstretch VST2/VST3/Standalone plugin
License: MIT
URL: https://bitbucket.org/xenakios/paulstretchplugin
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://bitbucket.org/xenakios/paulstretchplugin/get/%{commit0}.zip
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: unzip
BuildRequires: make
BuildRequires: JUCE60
BuildRequires: fftw-devel
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: webkit2gtk3-devel
BuildRequires: gtk3-devel

%description
A PaulStretch VST/VST3/Standalone plugin

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst2-%{name}
Summary:  VST2 version of %{name}
License:  GPL-2.0-or-later
Requires: %{name}

%description -n vst2-%{name}
VST2 version of %{name}

%prep
%autosetup -p1 -n xenakios-paulstretchplugin-%{commit0}

unzip %{SOURCE1}

Projucer60 --resave paulstretchplugin.jucer

CURRENTDIR=`pwd`
sed -i -e "s|-pthread|-pthread -I$CURRENTDIR/VST_SDK/VST2_SDK|g" Builds/LinuxMakefile/Makefile
sed -i -e "s|libcurl|libcurl fftw3 fftw3f|g" Builds/LinuxMakefile/Makefile

%build

cd Builds/LinuxMakefile

%make_build

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_bindir}/vst3/

install -m 755 Builds/LinuxMakefile/build/PaulXStretch %{buildroot}/%{_bindir}/
install -m 755  Builds/LinuxMakefile/build/PaulXStretch.so %{buildroot}/%{_libdir}/vst/
cp -ra  Builds/LinuxMakefile/build/PaulXStretch.vst3 %{buildroot}/%{_libdir}/vst3/

%files
%doc readme.txt
%{_bindir}/*

%files -n vst2-%{name}
%{_libdir}/vst/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Fri Oct 01 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.4-3
- fix for Fedora 35

* Sun May 16 2021 Yann Collette <ycollette.nospam@free.fr> - 1.2.4-2
- fix version

* Sun May 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix typos + create standalone / vst2 / vst3 packages

* Sun May 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
