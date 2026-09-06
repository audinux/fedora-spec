# Status: active
# Tag: Drum
# Type: Plugin, VST3, Standalone
# Category: Synthesizer

Name: simple606
Version: 1.1.0
Release: 1%{?dist}
Summary: Basic TR-606 VST
License: MIT
URL: https://github.com/Fadedlimes/Simple606
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/Fadedlimes/Simple606/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: git
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
BuildRequires: mesa-libGL-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: gtk3-devel

Requires: license-%{name}

%description
An intuitive, fully synthesized analog drum machine and groovebox plugin built with JUCE.
Available as a VST3 plugin and Standalone application.

%package -n license-%{name}
Summary: License and documentation for %{name}
License: MIT

%description -n license-%{name}
License and documentation for %{name}

%package -n vst3-%{name}
Summary: VST3 version of %{name}
License: MIT
Requires: license-%{name}

%description -n vst3-%{name}
VST3 version of %{name}

%prep
%autosetup -n Simple606-%{version}

sed -i -e "s|PRODUCT_NAME \"Simple 606\"|PRODUCT_NAME \"Simple_606\"|g" CMakeLists.txt

%build

%cmake
%cmake_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 %{__cmake_builddir}/Simple606_artefacts/Standalone/* %{buildroot}/%{_bindir}/

install -m 755 -d %{buildroot}/%{_libdir}/vst3/
cp -vfr %{__cmake_builddir}/Simple606_artefacts/VST3/* %{buildroot}/%{_libdir}/vst3/

%files
%{_bindir}/*

%files -n license-%{name}
%doc README.md
%license License.txt

%files -n vst3-%{name}
%{_libdir}/vst3/*

%changelog
* Sun Sep 06 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial spec file
