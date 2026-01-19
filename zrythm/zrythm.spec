# Status: active
# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global commit0 9cca91d511a2fe00b3ce9a14bb25437ecf3b5eaa

Name: zrythm
Version: 1.9.9
Release: 3%{?dist}
Summary: Highly automated Digital Audio Workstation (DAW) featureful and intuitive to use
License: GPL-2.0-or-later
URL: https://github.com/zrythm/zrythm
ExclusiveArch: x86_64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/zrythm/zrythm/archive/%{commit0}.zip#/%{name}-%{version}.zip
Patch0: zrythm-0001-remove-cpack.patch

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: cmake
BuildRequires: flex
BuildRequires: xdg-utils
BuildRequires: help2man
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: python3-sphinx-intl
BuildRequires: rubygem-sass
BuildRequires: llvm
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: alsa-lib-devel
BuildRequires: boost-devel
BuildRequires: flac-devel
BuildRequires: fmt-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gettext-devel
BuildRequires: google-benchmark-devel
BuildRequires: gsl-lite-devel
BuildRequires: gtest-devel
BuildRequires: json-devel
BuildRequires: lame-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libchromaprint-devel
BuildRequires: libogg-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: libzstd-devel
BuildRequires: lilv-devel
BuildRequires: llvm-devel
BuildRequires: lv2-devel
BuildRequires: magic_enum-devel
BuildRequires: mbedtls-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mpg123-devel
BuildRequires: opus-devel
BuildRequires: pkgconfig(jack)
BuildRequires: qt6-linguist
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qttools-devel
BuildRequires: spdlog-devel
BuildRequires: speex-devel
BuildRequires: sqlite-devel
BuildRequires: suil-devel
BuildRequires: xxhash-devel
BuildRequires: desktop-file-utils

Requires: breeze-icon-theme

%description
Zrythm is a highly automated Digital Audio Workstation (DAW) designed to be featureful and intuitive to use.
Zrythm sets itself apart from other DAWs by allowing extensive automation via built-in LFOs and envelopes
and intuitive MIDI or audio editing and arranging via clips.
In the usual Composing -> Mixing -> Mastering workflow, Zrythm puts the most focus on the Composing part.
It allows musicians to quickly lay down and process their musical ideas without taking too much time for unnecessary work.
It is written in C and uses the GTK+3 toolkit, with bits and pieces taken from other programs like Ardour and Jalv.
More info at https://www.zrythm.org

%prep
%autosetup -p1 -n zrythm-%{commit0}

sed -i -e "s/Qt6 6.10/Qt6 6.8/g" CMakeLists.txt

%build

# CXXFLAGS='-O2 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer '

# LDFLAGS='-Wl,-z,relro -Wl,--as-needed  -Wl,-z,pack-relative-relocs -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -Wl,--build-id=sha1 -specs=/usr/lib/rpm/redhat/redhat-package-notes '

# removed: -fstack-protector-strong -fstack-clash-protection -fcf-protection -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1
#export CXXFLAGS='-O0 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3   -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer '

%define X_display ":98"
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%cmake -DZRYTHM_BUNDLED_PLUGINS_WITH_STATIC_LINKING=OFF \
       -DZRYTHM_BUNDLED_PLUGINS=ON \
       -DZRYTHM_USE_JACK=ON \
       -DZRYTHM_USER_MANUAL=OFF \
       -DENABLE_CPACK=OFF \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/org.zrythm.Zrythm.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zrythm.Zrythm.desktop

%files
%doc CHANGELOG.md CONTRIBUTING.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/mime/*
%{_datadir}/metainfo/*
%{_datadir}/zrythm/
%{_datadir}/bash-completion/completions/zrythm
%{_mandir}/*

%changelog
* Thu Jan 15 2026 Yann Collette <ycollette.nospam@free.fr> - 1.9.9-3
- update to 1.9.9-3 - update to 9cca91d511a2fe00b3ce9a14bb25437ecf3b5eaa

* Thu Nov 20 2025 Yann Collette <ycollette.nospam@free.fr> - 1.9.9-2
- update to 1.9.9-2

* Mon Sep 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.9.9-1
- Initial build
