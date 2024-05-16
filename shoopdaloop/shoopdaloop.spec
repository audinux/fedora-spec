# Tag: Live, Sequencer, Editor
# Type: Standalone
# Category: Tool, Audio, DAW

%define commit0 acc140d1b08b0fe3088db5324a958caf8c0d4985

Name: shoopdaloop
Version: 0.1
Release: 1%{?dist}
Summary: A (live) looping application with DAW elements.
License: GPL
URL: https://github.com/SanderVocke/shoopdaloop
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

# Usage: ./shoopdaloop-source.sh <TAG>
#        ./shoopdaloop-source.sh acc140d1b08b0fe3088db5324a958caf8c0d4985

Source0: shoopdaloop.tar.gz
Source1: shoopdaloop-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: spdlog-devel
BuildRequires: boost-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libglvnd-devel
BuildRequires: fmt-devel
BuildRequires: lilv-devel
BuildRequires: serd
BuildRequires: sord
BuildRequires: lv2-devel
BuildRequires: python3
BuildRequires: python3-pyside2-devel

%description
ShoopDaLoop is a live looping application for Linux with a few DAW-like features.

%prep
%autosetup -n %{name}

%build

python3 -m venv sdl-build
source sdl-build/bin/activate
pip install py-build-cmake~=0.1.8
pip install ctypesgen
pip install pycparser
pip install build
pip install installer
pip install meson

%{__python3} -m build --no-isolation --wheel .

%install

source sdl-build/bin/activate
%{__python3} -m pip install dist/shoopdaloop-*.whl

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Oct 13 2023 Yann Collette <ycollette.nospam@free.fr> - 0.1-1
- initial version
