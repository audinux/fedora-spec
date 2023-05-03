%global commit0 35bce4608d7b995d9edbf919124b794874d8710c

Name:    gammou
Version: 0.8.1
Release: 2%{?dist}
Summary: Modular Sound Synthesizer
URL:     https://github.com/aliefhooghe/Gammou
License: BSD3

Vendor:       Audinux
Distribution: Audinux

# Usage: ./gammou-source.sh <TAG>
# ./gammou-source.sh master

Source0: Gammou.tar.gz
Source1: gammou.jpg
Source2: gammou-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: clang
BuildRequires: python3
BuildRequires: catch-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
%if 0%{?fedora} >= 37
BuildRequires: llvm14-devel
%else
BuildRequires: llvm-devel
%endif
BuildRequires: freetype-devel
BuildRequires: cxxopts-devel
BuildRequires: rtmidi-devel
BuildRequires: rtaudio-devel
BuildRequires: json-devel
BuildRequires: cxxopts-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils

%description
Gammou is a polyphonic modular sound synthesizer that be run as VST or standalone.

%package -n vst-%{name}
Summary:  VST2 version of %{name}
License:  GPLv2+
Requires: %{name}

%description -n vst-%{name}
VST2 version of %{name}

%prep
%autosetup -n Gammou

%build

cd src
%cmake -DGAMMOU_ENABLE_DESKTOP_APP=ON \
       -DGAMMOU_PACKAGE_PATH=%{_datadir}/%{name}/packages/ \
%if 0%{?fedora} >= 37
       -DLLVM_DIR=%{_libdir}/llvm14/lib/cmake/llvm \
%endif
       -DGAMMOU_SAMPLE_PATH=%{_datadir}/%{name}/waves/
%cmake_build

%install

cd src

install -m 755 -d %{buildroot}/%{_libdir}/vst/
install -m 755 -d %{buildroot}/%{_libdir}/%{name}/
install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/packages/
install -m 755 -d %{buildroot}/%{_datadir}/%{name}/waves/

cp %{__cmake_builddir}/gammou_desktop_app %{buildroot}/%{_bindir}/gammou
cp %{__cmake_builddir}/libgammou_vst2_plugin.so %{buildroot}/%{_libdir}/vst/

cp -rav %{__cmake_builddir}/packages/out/* %{buildroot}/%{_datadir}/%{name}/packages/
touch %{buildroot}/%{_datadir}/%{name}/waves/.empty

# Install thirdparty libs
cp %{__cmake_builddir}/DSPJIT/libDSPJIT.so %{buildroot}/%{_libdir}/%{name}/
cp %{__cmake_builddir}/View/NanoVG/libnanovg.so %{buildroot}/%{_libdir}/%{name}/

# Install icon
install -m 755 -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
cp %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

# Write desktop files
install -m 755 -d %{buildroot}/%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%name
Exec=%{name}
Icon=gammou
Comment=Gammoun Modular Synthesizer
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;
EOF

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Remove RPATH
chrpath --delete %{buildroot}/%{_libdir}/%{name}/libDSPJIT.so
chrpath --delete %{buildroot}/%{_libdir}/%{name}/libnanovg.so
chrpath --replace %{_libdir}/%{name}/ %{buildroot}/%{_libdir}/vst/libgammou_vst2_plugin.so
chrpath --replace %{_libdir}/%{name}/ %{buildroot}/%{_bindir}/gammou

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/applications/*
%{_datadir}/%{name}/
%{_datadir}/%{name}/packages/*
%{_datadir}/%{name}/waves/.empty

%files -n vst-%{name}
%{_libdir}/vst/*

%changelog
* Fri Mar 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix spec file

* Wed Jul 20 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
