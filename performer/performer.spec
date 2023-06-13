%global debug_package %{nil}

# Tag: Session, Jack, Live
# Type: Standalone
# Category: Session Mngmt
# GUIToolkit: Qt5

Name:    performer
Version: 1.0.2
Release: 3%{?dist}
Summary: Live performance audio session manager using Carla
URL:     https://github.com/progwolff/performer
License: GPL-2.0-or-later

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/progwolff/performer/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtwebengine-devel
BuildRequires: qt5-qtwebview-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: sed

%description
Live performance audio session manager using Carla

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/AudioVideo/X-AudioVideo/g" performer.desktop

%build

%cmake -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake -DWITH_KF5=0 \
       -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

make -C %{__cmake_builddir} performer_autogen

%cmake -DWITH_KF5=1 \
       -DCMAKE_C_FLAGS:STRING=-fPIC \
       -DCMAKE_CXX_FLAGS:STRING=-fPIC \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fPIC \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

make -C %{__cmake_builddir} performer_autogen

%cmake_build

%install

%cmake_install

# install hydrogen.desktop properly.
desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc CONTRIBUTORS README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-3
- update for Fedora 33

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-2
- update for Fedora 29
- update to 59ce476dc03d494bf6aa33f6443f625e7be098c3

* Mon May 14 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.2-1
- update to latest version

* Tue Nov 28 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.1-1
- Initial version of spec file
