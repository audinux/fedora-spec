# Tag: Effect
# Type: Plugin, LV2
# Category: Audio, Effect

Name: ensemble-chorus
Version: 0.0.1
Release: 2%{?dist}
Summary: Effect plugin for ensemble-chorus (VST/LV2)
URL: https://github.com/jpcima/ensemble-chorus
ExclusiveArch: x86_64 aarch64
License: BSL-1.0

Vendor:       Audinux
Distribution: Audinux

# ./ensemble-chorus-source.sh master

Source0: ensemble-chorus.tar.gz
Patch0: ensemble-chorus-0001-fix-JUCE-compilation.patch

BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(jack)
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: freetype-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: fltk-devel
BuildRequires: fltk-fluid
BuildRequires: desktop-file-utils

%description
Effect plugin for ensemble-chorus (VST/LV2)

%prep

%autosetup -p1 -n ensemble-chorus

%ifarch x86_64
  sed -i -e "s/lib\/lv2/lib64\/lv2/g" CMakeLists.txt
  sed -i -e "s/lib\/vst/lib64\/vst/g" CMakeLists.txt
%endif

sed -i -e "s/AudioMidi;//g" resources/desktop/ensemble_chorus.desktop

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/ensemble_chorus.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ensemble_chorus.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lv2/*
%{_libdir}/vst/*
%{_datadir}/applications/ensemble_chorus.desktop
%{_datadir}/pixmaps/ensemble_chorus.png
%{_datadir}/pixmaps/ensemble_chorus.xpm

%changelog
* Mon Oct 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- fix for Fedora 33

* Thu May 30 2019 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
