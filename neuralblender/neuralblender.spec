# Status: active
# Tag: Tool, AI
# Type: Plugin, LV2, Standalone
# Category: Audio, Tool

Name: neuralblender
Version: 1.1.5
Release: 1%{?dist}
Summary:  Guitar amp modeling plugin based on RTNeural and NeuralAmp
License: GPL-3.0-or-later
URL: https://sourceforge.net/projects/neuralblender/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/neuralblender/files/source/neuralblender_%{version}_source.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libsndfile-devel
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw-static
BuildRequires: pkgconfig(jack)
BuildRequires: xxd
BuildRequires: desktop-file-utils

Requires: license-%{name}
Requires: common-%{name}

%description
A simple, efficient but feature-rich amp modeling app and LV2 plugin based on RTNeural and NeuralAmpModeler (NAM).

%package -n license-%{name}
Summary: License and documentation for %{name}
License: GPL-3.0-or-later

%description -n license-%{name}
License and documentation for %{name}

%package -n common-%{name}
Summary: Common files for %{name}
License: GPL-3.0-or-later

%description -n common-%{name}
Common files for %{name}

%package -n lv2-%{name}
Summary: LV2 version of %{name}
License: GPL-3.0-or-later
Requires: license-%{name}
Requires: common-%{name}

%description -n lv2-%{name}
LV2 version of %{name}

%prep
%autosetup -n %{name}

sed -i -e "s|DESTINATION lib/lv2/neuralblender.lv2|DESTINATION %{_lib}/lv2/neuralblender.lv2|g" CMakeLists.txt

%build

%cmake -DSTANDALONE=ON \
       -DLV2=ON \
       -DGUI=ON \
       -DUSE_NATIVE_ARCH=OFF

%cmake_build

%install

%cmake_install

desktop-file-install                         \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/neuralblender.desktop
%{_datadir}/icons/hicolor/256x256/apps/neuralblender.png

%files -n common-%{name}
%{_datadir}/neuralblender/ir/*
%{_datadir}/neuralblender/nam/*
%{_datadir}/neuralblender/presets/*

%files -n license-%{name}
%doc README.md
%license LICENSE

%files -n lv2-%{name}
%{_libdir}/lv2/*

%changelog
* Fri Aug 21 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.5-1
- update to 1.1.5-1

* Tue Aug 18 2026 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- Initial build
