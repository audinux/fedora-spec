# Tag: Alsa, MIDI
# Type: Standalone, VST3, VST, LV2, Plugin
# Category: MIDI, Tool

Name: showdmidi
Version: 1.9.9
Release: 1%{?dist}
Summary: Multi-platform GUI application to effortlessly visualize MIDI activity
License: GPL-3.0-only
URL: https://github.com/gbevin/ShowMIDI
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# ./gbevin-source.sh <project> <tag>
# ./gbevin-source.sh ShowMIDI 1.0.0

Source0: ShowMIDI.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: gbevin-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: libatomic

%description
Multi-platform command-line tool making it very easy to quickly
send MIDI messages to MIDI devices from your computer.

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%package -n lv2-%{name}
Summary:  LV2 version of %{name}
License:  GPL-3.0-only
Requires: %{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n ShowMIDI

unzip %{SOURCE1}

%build

export CWD=`pwd`

cd Builds/LinuxMakefile
%make_build STRIP=true CPPFLAGS="%{optflags} -I$CWD/VST_SDK/VST2_SDK"

%install

cd Builds/LinuxMakefile

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -p build/ShowMIDI %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 -d %{buildroot}%{_libdir}/vst3/
install -m 755 -d %{buildroot}%{_libdir}/lv2/

cp -ra build/ShowMIDI.lv2 %{buildroot}%{_libdir}/lv2/
install -m 755 -p build/ShowMIDI.so %{buildroot}%{_libdir}/vst/
cp -ra build/ShowMIDI.vst3 %{buildroot}%{_libdir}/vst3/

%files
%doc README.md
%license COPYING.md
%{_bindir}/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n vst-%{name}
%{_libdir}/vst/*

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Mon Jul 08 2024 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-3
- update to 1.0.0-1

* Thu May 30 2024 Yann Collette <ycollette.nospam@free.fr> - 0.9.0-3
- update to 0.9.0-1

* Sun Nov 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.2.2-3
- Initial spec file
