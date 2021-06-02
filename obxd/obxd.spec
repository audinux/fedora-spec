# Tag: Jack, Alsa
# Type: Plugin, Standalone, VST3
# Category: Audio, Synthesizer

Name:    obxd
Version: 2.4
Release: 1%{?dist}
Summary: A VST3 Synthesizer
License: GPLv3
URL:     https://github.com/reales/OB-Xd

Source0: https://github.com/reales/OB-Xd/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: obxd-makefiles.tar.gz
# Source2: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source2: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
# ./vst3-source.sh master
Source3: vst3sdk.tar.gz
Patch0:  obxd_file_install_resources.patch

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: JUCE
BuildRequires: libXrandr-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXinerama-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel

%description
Virtual Analog Oberheim VST / VST3 based synthesizer

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPLv3
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -p1 -n OB-Xd-%{version}

tar xvfz %{SOURCE1}
unzip %{SOURCE2}
tar xvfz %{SOURCE3}

sed -i -e "s|RPMVST2|`pwd`/VST_SDK/VST2_SDK|g" Builds/LinuxMakefile/Makefile
sed -i -e "s|RPMVST3|`pwd`/vst3sdk|g" Builds/LinuxMakefile/Makefile

%build

%set_build_flags

cd Builds/LinuxMakefile
# %make_build CONFIG=Release STRIP=true
%make_build

%install 

install -m 755 -d %{buildroot}%{_libdir}/vst3/OB-Xd.vst3/
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_datadir}/discoDSP/OB-Xd/

cp -r Documents/discoDSP/* %{buildroot}%{_datadir}/discoDSP/

install -m 755 -p Builds/LinuxMakefile/build/OB-Xd %{buildroot}/%{_bindir}/
cp -ra Builds/LinuxMakefile/build/OB-Xd.vst3/* %{buildroot}/%{_libdir}/vst3/OB-Xd.vst3/
chmod a+x %{buildroot}/%{_libdir}/vst3/OB-Xd.vst3/Contents/x86_64-linux/OB-Xd.so

%files
%doc README.md
%license license.txt
%{_bindir}/*
%{_datadir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Wed Jun 02 2021 Yann Collette <ycollette.nospam@free.fr> - 2.4-1
- Initial spec file
