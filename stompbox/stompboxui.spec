# Status: active
# Tag: Guitar, Amp Simul
# Type: Standalone
# Category: Audio, Effect

Name: stompboxui
Version: 0.1.16
Release: 1%{?dist}
Summary: Remote GUI and VST3 plugin for Stompbox guitar simulation
License: GPL-3.0-or-later
URL: https://github.com/mikeoliphant/StompboxUI
ExclusiveArch: x86_64

%global debug_package %{nil}

# ./mikeoliphant-source.sh <project> <tag>
# ./mikeoliphant-source.sh StompboxUI v0.1.16
# ./mikeoliphant-source.sh StompboxUI master

Source0: StompboxUI.tar.gz
Source1: mikeoliphant-source.sh

BuildRequires: gcc-c++
BuildRequires: dotnet-host
BuildRequires: dotnet-sdk-8.0
BuildRequires: mono-devel
BuildRequires: libgdiplus
BuildRequires: cmake
BuildRequires: pkgconfig(jack)
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires: license-%{name}

%description
Stompbox is a guitar amplification and effects application, arranged as a digital version of a guitar pedalboard.
This github repository is the front-end for the software (the core codebase is stompbox), to be used either as a
remote interface to an actual pedalboard implementation, or as a standalone VST plugin.
This is what it looks like running a Windows/Linux remote or as a VST plugin:

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%prep
%autosetup -n StompboxUI

%build

# Build image processor

cd StompboxUI/StompboxImageProcessor/
dotnet build -c Release StompboxImageProcessor.csproj
dotnet run -c Release StompboxImageProcessor.csproj
cd ..

# Build remote GUI
cd StompboxRemoteGL
# --runtime linux-x64 -p:PublishSingleFile=true --self-contained true
dotnet build -c Release StompboxRemoteGL.csproj

%install

mkdir -p %{buildroot}/%{_bindir}/
cp StompboxUI/StompboxRemoteGL/bin/Release/net8.0/StompboxRemoteGL  %{buildroot}/%{_bindir}/

%files
%{_bindir}/StompboxRemoteGL

%files -n license-%{name}
%doc README.md CREDITS.md
%license LICENSE.md

%changelog
* Wed Feb 04 2026 Yann Collette <ycollette.nospam@free.fr> - 0.1.16-1
- update to 0.1.16-1

* Wed Aug 13 2025 Yann Collette <ycollette.nospam@free.fr> - 0.1.15-1
- Initial build
