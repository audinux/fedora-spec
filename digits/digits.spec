# Tag: Synthesizer
# Type: Plugin, VST
# Category: Audio, Synth

%global commit0 f5ee4aa74e40b118bddcb3ef18d44b734e6fbef8

Name: digitsvst
Version: 0.0.1
Release: 1%{?dist}
Summary: An advanced phase distortion synthesizer
License: GPL-3.0-or-later
URL: https://github.com/LouisGorenfeld/DigitsVst
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/LouisGorenfeld/DigitsVst/archive/%{commit0}.zip#/%{name}-%{commit0}.zip
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: make

%description
Digits is an advanced phase distortion synthesizer

%prep
%autosetup -n DigitsVst-%{commit0}

# Install VST2 sdk
mkdir -p sdks/vstsdk2.4
unzip %{SOURCE1}
mv VST_SDK/VST2_SDK/* sdks/vstsdk2.4

# For the GUI
cp -r VST_SDK/VST3_SDK/vstgui4/* src/

sed -i -e "/strip/d" linux/Digits.make
sed -i -e "s/-Wall /\$(DEPFLAGS) /g" linux/Digits.make

# Deactivate GUI for now
sed -i -e "s/-DNO_EDITOR/-DNO_EDITOR -DDIGITS_MULTICORE/g" linux/Digits.make

mv Digits\ Manual.pdf Digits_Manual.pdf

%build

%set_build_flags
export DEPFLAGS="$CXXFLAGS"

cd linux
%make_build -f Digits.make

%install

cd linux

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 DigitsVST.so %{buildroot}/%{_libdir}/vst/

install -m 755 -d %{buildroot}%{_datadir}/digits/patches/
cp -rav ../patches %{buildroot}%{_datadir}/digits/patches/

%files
%doc README Design.txt Digits_Manual.pdf
%license License.txt
%{_libdir}/vst/*
%{_datadir}/digits/*

%changelog
* Fri May 03 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
