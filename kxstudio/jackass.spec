# Tag: Tool
# Type: Plugin, VST
# Category: MIDI, Tool

%global debug_package %{nil}

Name: jackass
Version: 1.1
Release: 1%{?dist}
Summary: JACK-MIDI support for VST hosts, including Wine apps
License: MIT
URL: https://github.com/falkTX/JackAss
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/falkTX/JackAss/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: mingw32-winpthreads-static
BuildRequires: mingw64-winpthreads-static
BuildRequires: pkgconfig(jack)
BuildRequires: wine-devel
BuildRequires: glibc-devel(x86-32)
BuildRequires: wine-devel(x86-32)
BuildRequires: libstdc++-devel(x86-32)

%description
JackAss is a VST plugin that provides JACK-MIDI support for VST hosts.
Simply load the plugin in your favourite host to get a JACK-MIDI port.
Each new plugin instance creates a new MIDI port.

%prep
%autosetup -n JackAss-%{version}

unzip %{SOURCE1}
cp -r VST_SDK/VST2_SDK/* vstsdk2.4/

sed -i -e "s/VST_EXPORT AEffect\*/VST_EXPORT VSTCALLBACK AEffect\*/g" vstsdk2.4/public.sdk/source/vst2.x/vstplugmain.cpp

%build
%set_build_flags

%make_build SKIP_STRIPPING=true NOOPT=true V=1

%install

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 *.so %{buildroot}/%{_libdir}/vst/

%files
%doc README.md
%license LICENSE
%{_libdir}/vst/*

%changelog
* Tue Jan 09 2024 Yann Collette <ycollette.nospam@free.fr> - 1.1-3
- initial version of the spec
