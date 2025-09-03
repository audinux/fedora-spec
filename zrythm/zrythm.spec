# Status: active
# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global commit0 c3baa11958a1e005396d4cb3f857b243f9cc090b

Name: zrythm
Version: 1.9.9
Release: 1%{?dist}
Summary: Highly automated Digital Audio Workstation (DAW) featureful and intuitive to use
License: GPL-2.0-or-later
URL: https://github.com/zrythm/zrythm
ExclusiveArch: x86_64 aarch64

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
BuildRequires: gettext-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: flac-devel
BuildRequires: opus-devel
BuildRequires: lame-devel
BuildRequires: mpg123-devel
BuildRequires: speex-devel
BuildRequires: sqlite-devel
BuildRequires: boost-devel
BuildRequires: libchromaprint-devel
BuildRequires: fmt-devel
BuildRequires: libzstd-devel
BuildRequires: spdlog-devel
BuildRequires: google-benchmark-devel
BuildRequires: json-devel
BuildRequires: mbedtls-devel
BuildRequires: gtest-devel
BuildRequires: gtest-devel
BuildRequires: xxhash-devel
BuildRequires: magic_enum-devel
BuildRequires: gsl-lite-devel
BuildRequires: llvm-devel
BuildRequires: llvm
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

%build

# CXXFLAGS='-O2 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer '

# LDFLAGS='-Wl,-z,relro -Wl,--as-needed  -Wl,-z,pack-relative-relocs -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -Wl,--build-id=sha1 -specs=/usr/lib/rpm/redhat/redhat-package-notes '

# removed: -fstack-protector-strong -fstack-clash-protection -fcf-protection -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1
export CXXFLAGS='-O0 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3   -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer '

%cmake -DZRYTHM_BUNDLED_PLUGINS_WITH_STATIC_LINKING=OFF \
       -DZRYTHM_BUNDLED_PLUGINS=OFF \
       -DZRYTHM_USE_JACK=ON \
       -DZRYTHM_USER_MANUAL=OFF \
       -DENABLE_CPACK=OFF
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
%doc AUTHORS THANKS CHANGELOG.md CONTRIBUTING.md
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
* Mon Sep 01 2025 Yann Collette <ycollette.nospam@free.fr> - 1.9.9-1
- Initial build
