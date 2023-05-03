# Tag: Live
# Type: Standalone, IDE
# Category: Programming, Audio, Graphic

# Global variables for github repository
%global commit0 ba9aee218dd4a9cfab914ad78bdb6d59e9a37400
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    fluxus
Version: 0.17rc5.%{shortcommit0}
Release: 4%{?dist}
Summary: A 3D game engine for livecoding worlds into existence
URL:     https://pawfal.org/fluxus/
License: GPLv2+

Vendor:       Audinux
Distribution: Audinux

Source0: https://gitlab.com/nebogeo/%{name}/-/archive/%{commit0}/fluxus-%{commit0}.tar.gz
Source1: https://github.com/defaultxr/fluxus-mode/raw/master/fluxus-mode.el
Source2: fluxus-SConstruct

BuildRequires: gcc gcc-c++
BuildRequires: python3-scons
BuildRequires: ode-devel >= 0.9
BuildRequires: racket-devel >= 5.1.1
BuildRequires: racket >= 5.1.1
BuildRequires: fftw-devel >= 3.2.2
BuildRequires: jack-audio-connection-kit-devel >= 1.9.7
BuildRequires: libsndfile-devel >= 1.0.25
BuildRequires: liblo-devel >= 0.26
BuildRequires: glew-devel >= 1.5.8
BuildRequires: freetype-devel >= 2.2.4
BuildRequires: libjpeg-turbo-devel >= 1.1.1
BuildRequires: libpng-devel >= 1.2.46
BuildRequires: libtiff-devel >= 3.9.5
BuildRequires: zlib-devel >= 1.2.3
BuildRequires: freeglut-devel >= 2.6.0
BuildRequires: alsa-lib-devel >= 1.0.24
BuildRequires: openal-soft-devel >= 1.12.854
#BuildRequires: gstreamer-devel >= 0.10.25
#BuildRequires: gstreamer-plugins-base-devel >= 0.10.25
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: libunicap-devel >= 0.9.12
BuildRequires: ffmpeg-devel >= 0.7
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: emacs w3m

Requires: racket >= 5.1.1
Requires: fftw >= 3.2.2
Requires: libsndfile >= 1.0.25
Requires: liblo >= 0.26
Requires: glew >= 1.5.8
Requires: freetype >= 2.2.4
Requires: libjpeg-turbo >= 1.1.1
Requires: libpng >= 1.2.46
Requires: libtiff >= 3.9.5
Requires: zlib >= 1.2.3
Requires: freeglut >= 2.6.0
Requires: alsa-lib >= 1.0.24
Requires: openal-soft >= 1.12.854
Requires: gstreamer >= 0.10.25
Requires: gstreamer-plugins-base >= 0.10.25
Requires: gstreamer-plugins-good >= 0.10.17
Requires: gstreamer-plugins-bad-free >= 0.10.22
Requires: libunicap >= 0.9.12
Requires: ffmpeg >= 0.7
Requires: emacs w3m-el

%description
A rapid prototyping, livecoding and playing/learning environment for 3D
graphics, sound and games. Extends Racket with graphical commands
and can be used within it’s own livecoding environment or from within
the DrRacket IDE.

%package emacs
Summary:  Fluxus support for Emacs
Requires: fluxus = %{version}-%{release}

%description emacs
Fluxus support for the Emacs text editor.

%prep
%autosetup -n %{name}-%{commit0}

cp %{SOURCE2} SConstruct

sed -i -e "s/\/lib\/racket/\/%{_lib}\/racket/g" SConstruct
sed -i -e "s/FluxusCollectsLocation = Prefix + \"\/lib\"/FluxusCollectsLocation = Prefix + \"\/%{_lib}\"/g" SConstruct

%build

#cd docs
#./makehelpmap.scm

%install

%set_build_flags

export CXXFLAGS="-std=c++11 -fPIC $CXXFLAGS"
export CFLAGS="-std=c++11 -fPIC $CFLAGS"

scons -Q install DESTDIR="%{buildroot}" Prefix=/usr RacketPrefix=/usr

install -m 644 -D modules/material/textures/fluxus-icon.png %{buildroot}/usr/share/pixmaps/fluxus-icon.png
install -m 644 -D debian/fluxus.desktop %{buildroot}/usr/share/applications/fluxus.desktop

install -m 755 -d %{buildroot}/usr/share/fluxus-019/
cp -r examples %{buildroot}/usr/share/fluxus-019/

install -m 755 -d %{buildroot}/usr/share/emacs/site-lisp/fluxus
cp %{SOURCE1} %{buildroot}/usr/share/emacs/site-lisp/fluxus/

cp -r docs %{buildroot}/usr/share/doc/fluxus-019/

desktop-file-install --vendor '' \
        --add-category=X-Sound \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/fluxus.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fluxus.desktop

%files
%{_bindir}/fluxus
%{_bindir}/fluxa
%{_libdir}/fluxus-019/
%{_datadir}/fluxus-019/
%{_docdir}/fluxus-019/
%{_datadir}/pixmaps/fluxus-icon.png
%{_datadir}/applications/fluxus.desktop

%files emacs
%{_datadir}/emacs/site-lisp/fluxus

%changelog
* Mon May 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-4
- fix for pipewire

* Thu Apr 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-3
- fix for fedora 34

* Wed Oct 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-3
- fix debug build

* Sun Nov 24 2019 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-2
- install examples in share + fixes

* Tue Nov 19 2019 Yann Collette <ycollette.nospam@free.fr> - 0.17rc5-1
- Initial release of the spec file
