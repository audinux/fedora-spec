# Status: active
# Tag: Synthesizer
# Type: Plugin, Standalone, VST, VST3, CLAP
# Category: Audio, Synthesizer

%global debug_package %{nil}
%global zig_version 0.14.0

Name: floe
Version: 1.1.1
Release: 1%{?dist}
Summary: Sample library platform with a simple, powerful interface
License: GPL-3.0-or-later
URL: https://github.com/floe-audio/Floe
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/floe-audio/Floe/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://ziglang.org/download/%{zig_version}/zig-linux-x86_64-%{zig_version}.tar.xz
Source2: https://ziglang.org/download/%{zig_version}/zig-linux-aarch64-%{zig_version}.tar.xz

BuildRequires: gcc gcc-c++
BuildRequires: wget
BuildRequires: git
BuildRequires: xcb-util-wm-devel
BuildRequires: libXcursor-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel

%description
Streamlined sample-based instrument platform
Floe is a CLAP, VST3 and AU plugin for Windows, macOS, and Linux.
It loads and plays sample libraries in the Floe format.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary:  VST3 version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%package -n clap-%{name}
Summary:  CALP version of %{name}
License:  GPL-3.0-or-later
Requires: license-%{name}

%description -n clap-%{name}
CLAP version of %{name}

%prep
%autosetup -n Floe-%{version}

%ifarch x86_64
tar xvfJ %{SOURCE1}
%endif
%ifarch aarch64
tar xvfJ %{SOURCE2}
%endif
mv zig-linux-%{_arch}-%{zig_version} zig-bin

git config --global user.email "yc@example.com"
git config --global user.name "Yann Collette"

git init .
git add .
git commit -m "init"

%build

%set_build_flags

zig-bin/zig build install -Dbuild-mode=production
# zig-bin/zig build release

%install

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
install -m 755 -d %{buildroot}/%{_libdir}/clap/
cp -vfr zig-out/.vst3/* %{buildroot}/%{_libdir}/vst3/
cp -vfr zig-out/.clap/* %{buildroot}/%{_libdir}/clap/


%files
%doc readme.md faq.md 
%license LICENSES/*

%files -n vst3-%{name}
%{_libdir}/vst3/*

%files -n clap-%{name}
%{_libdir}/clap/*

%changelog
* Mon Jan 12 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-1
- Initial spec file
