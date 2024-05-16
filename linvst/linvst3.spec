# Tag: Rack, Tool
# Type: Standalone
# Category: Tool, Audio

%global debug_package %{nil}

Name: LinVst3
Version: 4.9
Release: 1%{?dist}
Summary: Linux Windows vst3 wrapper/bridge
License: GPL-3.0-only
URL: https://github.com/osxmidi/linvst3
ExclusiveArch: x86_64 aarch64

Source0: https://download.steinberg.net/sdk_downloads/vst-sdk_3.7.0_build-116_2020-07-31.zip
Source1: %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: glibc-devel(x86-32)
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libX11-devel(x86-32)
BuildRequires: libstdc++-devel(x86-32)
BuildRequires: wine-devel
BuildRequires: wine-devel(x86-32)

Requires: wine
Requires: python3

%description
LinVst3 adds support for Windows vst3's to be used in Linux3 vst3 capable DAW's.

%prep
%autosetup -n VST_SDK

cd VST3_SDK
tar xvfz %{SOURCE1}
cd %{name}-%{version}

sed -i "s/LINK_WINE = .* -l/LINK_WINE = -L\/usr\/lib64\/wine -l/g" Makefile
sed -i "s/LINK_WINE32 = .* -l/LINK_WINE32 = -L\/usr\/lib\/wine -l/g" Makefile

%build

cd VST3_SDK/%{name}-%{version}

# export LDFLAGS="-lX11 -lrt"

#make -f Makefile-convert
make

%install

cd VST3_SDK/%{name}-%{version}

%make_install
%make_install -f Makefile-convert

mkdir -p %{buildroot}/%{_datadir}/%{name}/64bit-32bit
install -m 755 linvst3.so %{buildroot}/%{_datadir}/%{name}/64bit-32bit

mkdir -p %{buildroot}/%{_datadir}/%{name}/doc
cp -ra Detailed-Guide %{buildroot}/%{_datadir}/%{name}/doc
cp -ra Realtime-Audio-Config %{buildroot}/%{_datadir}/%{name}/doc

mkdir -p %{buildroot}/%{_datadir}/%{name}/manage/
cp manage/linvst3manage-cli %{buildroot}/%{_bindir}/
cp manage/linvst3manage.ini %{buildroot}/%{_datadir}/%{name}/manage/
cp manage/README.md %{buildroot}/%{_datadir}/%{name}/manage/

%files
%license COPYING
%doc README.md
%{_bindir}/linvstmanage-cli
%{_bindir}/lin-vst3-servertrack.exe
%{_bindir}/lin-vst3-servertrack.exe.so
%{_bindir}/lin-vst3-servertrack32.exe
%{_bindir}/lin-vst3-servertrack32.exe.so
%{_bindir}/linvst3convert
%{_datadir}/%{name}/
%{_datadir}/%{name}/64bit-32bit/linvst3.so
%{_datadir}/%{name}/doc/*
%{_datadir}/%{name}/manage/*

%changelog
* Tue Aug 22 2023 Yann Collette <ycollette.nospam@free.fr> - 4.9-1
- Initial build
