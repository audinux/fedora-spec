# Tag: Jack, MIDI
# Type: Standalone
# Category: Audio, DAW

%global zrythm_version 1.1.11
Name:    zrythm
Version: 1.0.0.b%{zrythm_version}
Release: 5%{?dist}
Summary: Highly automated Digital Audio Workstation (DAW) featureful and intuitive to use
License: GPL-2.0-or-later
URL:     https://git.zrythm.org/zrythm/zrythm

Vendor:       Audinux
Distribution: Audinux

Source0: https://git.zrythm.org/zrythm/zrythm/archive/v1.0.0-beta.%{zrythm_version}.tar.gz#/zrythm-v1.0.0-beta.%{zrythm_version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: flex
BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: suil-devel
BuildRequires: libyaml-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: rubberband-devel
BuildRequires: libsndfile-devel
BuildRequires: libaudec-devel
BuildRequires: libcyaml-devel
BuildRequires: gtk3-devel
BuildRequires: portaudio-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fftw-devel
BuildRequires: libgtop2-devel
BuildRequires: guile22-devel
BuildRequires: gtksourceview3-devel
BuildRequires: graphviz-devel
BuildRequires: libzstd-devel
BuildRequires: libchromaprint-devel
BuildRequires: libreproc-devel
BuildRequires: libbacktrace-devel
BuildRequires: xxhash-devel
BuildRequires: rtmidi-devel
BuildRequires: rtaudio-devel
BuildRequires: libadwaita-devel
BuildRequires: meson
BuildRequires: help2man
BuildRequires: pandoc
BuildRequires: texi2html
BuildRequires: python3-pip
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-intl
BuildRequires: python3-sphinx-copybutton
BuildRequires: python3-sphinxcontrib-rsvgconverter
BuildRequires: desktop-file-utils
BuildRequires: gtk-update-icon-cache
BuildRequires: xdg-utils
BuildRequires: rubygem-sass
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: json-glib-devel
BuildRequires: libcurl-devel
%if 0%{?fedora} < 34
BuildRequires: coreutils
BuildRequires: libtool
BuildRequires: make
BuildRequires: elfutils-libelf-devel
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: perl-interpreter
# for sys/inotify.h
BuildRequires: glibc-devel
BuildRequires: libattr-devel
BuildRequires: libselinux-devel
# for sys/sdt.h
BuildRequires: systemtap-sdt-devel
%if 0%{?rhel}
# For gnutls-hmac.patch
BuildRequires: pkgconfig(gnutls)
%endif
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel
%endif
BuildRequires: sassc
BuildRequires: appstream-devel
BuildRequires: libpanel-devel
BuildRequires: gtksourceview5-devel

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
%autosetup -n zrythm

# Compile using -O0 because of jack xruns
sed -i -e "/cc = meson.get_compiler ('c')/a add_global_arguments('-O0'\, language : 'c')" meson.build
sed -i -e "s/-O3/-O0/g" src/utils/meson.build
sed -i -e "s/-O3/-O0/g" src/audio/meson.build

# Search for libpulse.pc instead of pulseaudio.pc
sed -i -e "s/'pulseaudio'/'libpulse'/g" meson.build

# Disable warning treated as errors with sphinx
sed -i -e "s/ sphinx_build_opts = \[ / #sphinx_build_opts = \[ /g" doc/user/meson.build

# Fix version of cyaml
sed -i -e "s/99.1.0/1.1.0/g" meson.build

# disable linkcheck
sed -i -e "149,168d" doc/user/meson.build

%build

# Install sphinx-furo theme
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
pip install --user furo

mkdir build
%meson \
       --wrap-mode=nofallback \
       --force-fallback-for "gtk4, wayland-protocols" \
       --default-library static \
       -Dmanpage=true \
       -Duser_manual=true \
       -Dlsp_dsp=disabled \
       -Dcheck_updates=false \
       -Dportaudio=enabled \
       -Drtmidi=enabled \
       -Drtaudio=enabled \
       -Dsdl=enabled \
       -Doptimization=3 \
       -Ddebug=true \
       -Dbuild_plugins_with_static_libs=false \
       --buildtype release \
       --prefix=/usr

%meson_build

%install

%meson_install

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
%{_datadir}/doc/%{name}/*
%{_datadir}/fonts/*
%{_datadir}/glib-2.0/*
%{_datadir}/icons/*
%{_datadir}/locale/*
%{_datadir}/mime/*
%{_datadir}/zrythm/
%{_datadir}/bash-completion/completions/zrythm
%{_mandir}/*
%exclude %{_libdir}/*.a
%exclude %{_datadir}/fish/vendor_completions.d/zrythm.fish
%if 0%{?fedora} < 34
%exclude %{_bindir}/gapplication
%exclude %{_bindir}/gdbus
%exclude %{_bindir}/gio
%exclude %{_bindir}/glib-compile-schemas
%exclude %{_bindir}/gsettings
%exclude %{_bindir}/glib-compile-resources
%exclude %{_bindir}/glib-genmarshal
%exclude %{_bindir}/glib-gettextize
%exclude %{_bindir}/glib-mkenums
%exclude %{_bindir}/gobject-query
%exclude %{_bindir}/gresource
%exclude %{_bindir}/gtester
%exclude %{_bindir}/gtester-report
%exclude %{_includedir}/glib-2.0/*
%exclude %{_includedir}/gio-unix-2.0/*
%exclude %{_datadir}/aclocal/*
%exclude %{_datadir}/bash-completion/completions/gio
%exclude %{_datadir}/bash-completion/completions/gapplication
%exclude %{_datadir}/bash-completion/completions/gdbus
%exclude %{_datadir}/bash-completion/completions/gresource
%exclude %{_datadir}/bash-completion/completions/gsettings
%exclude %{_datadir}/gdb/auto-load/usr/lib64/*
%exclude %{_datadir}/gettext/*
%exclude %{_datadir}/glib-2.0/*
%exclude %{_datadir}/locale/*/LC_MESSAGES/glib20.mo
%exclude %{_libdir}/glib-2.0/include/*
%exclude %{_libdir}/pkgconfig/*
%exclude %{_libdir}/libgio-2.0.so*
%exclude %{_libdir}/libglib-2.0.so*
%exclude %{_libdir}/libgmodule-2.0.so*
%exclude %{_libdir}/libgobject-2.0.so*
%exclude %{_libdir}/libgthread-2.0.so*
%endif

%changelog
* Fri Mar 25 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-beta.1.1.11-5
- update to 1.0.0-beta.1.1.11-5

* Sat Sep 11 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.25.1.22-5
- update to 1.0.0-alpha.25.1.22-5

* Sat Sep 11 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.25.1.11-5
- update to 1.0.0-alpha.25.1.11-5

* Mon Sep 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.25.1.1-5
- update to 1.0.0-alpha.25.1.1-5

* Sat Sep 04 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.25.0.1-5
- update to 1.0.0-alpha.25.0.1-5

* Sat Aug 28 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.24.0.1-5
- update to 1.0.0-alpha.24.0.1-5

* Thu Aug 26 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.23.0.1-5
- update to 1.0.0-alpha.23.0.1-5

* Sat Aug 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.22.1.11-5
- update to 1.0.0-alpha.22.1.11-5

* Tue Aug 03 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.22.0.1-5
- update to 1.0.0-alpha.22.0.1-5

* Thu Jul 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.21.0.13-5
- update to 1.0.0-alpha.21.0.13-5

* Thu Jul 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.20.0.1-5
- update to 1.0.0-alpha.20.0.1-5

* Wed Jul 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.19.0.1-5
- update to 1.0.0-alpha.19.0.1-5

* Thu Jun 10 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.18.2.1-5
- update to 1.0.0-alpha.18.2.1-5

* Sun Jun 06 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.18.1.1-5
- update to 1.0.0-alpha.18.1.1-5

* Fri Jun 04 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.17.1.22-5
- update to 1.0.0-alpha.17.1.22-5

* Wed Jun 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.17.1.3-5
- update to 1.0.0-alpha.17.1.3-5

* Sat May 22 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.16.1.1-5
- update to 1.0.0-alpha.16.1.1-5 - fix exclude of glib files for Fedora 32 and 33

* Sat May 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.16.1.1-4
- update to 1.0.0-alpha.16.1.1-4

* Fri May 07 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.16.0.37-4
- update to 1.0.0-alpha.16.0.37-4

* Sun May 02 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.16.0.12-4
- update to 1.0.0-alpha.16.0.12-4

* Sat May 01 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.16.0.1-4
- update to 1.0.0-alpha.16.0.1-4

* Sun Apr 04 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.15.0.1-4
- update to 1.0.0-alpha.15.0.1-4

* Mon Mar 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.14.1.2-4
- update to 1.0.0-alpha.14.1.2-4

* Sun Mar 14 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.14.1.1-4
- update to 1.0.0-alpha.14.1.1-4

* Sat Mar 13 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.14.0.1-4
- update to 1.0.0-alpha.14.0.1-4

* Mon Mar 8 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.13.1.1-4
- update to 1.0.0-alpha.13.1.1-4

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.13.0.4-4
- update to 1.0.0-alpha.13.0.4-4

* Sun Feb 28 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.13.0.1-4
- update to 1.0.0-alpha.13.0.1-4

* Sat Feb 20 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.12.0.1-4
- update to 1.0.0-alpha.12.0.1-4

* Mon Feb 15 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.11.1.1-4
- update to 1.0.0-alpha.11.1.1-4

* Fri Feb 12 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.11.0.2-4
- update to 1.0.0-alpha.11.0.2-4

* Tue Feb 2 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.10.0.1-4
- update to 1.0.0-alpha.10.0.1-4

* Sun Jan 24 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.9.0.1-4
- update to 1.0.0-alpha.9.0.1-4

* Mon Jan 18 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.8.0.1-4
- update to 1.0.0-alpha.8.0.1-4

* Sun Jan 3 2021 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.7.1.1-4
- update to 1.0.0-alpha.7.1.1-4

* Thu Dec 31 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.7.0.1-4
- update to 1.0.0-alpha.7.0.1-4

* Sat Dec 12 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.6.0.1-4
- update to 1.0.0-alpha.6.0.1-4

* Tue Nov 17 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.5.0.1-4
- update to 1.0.0-alpha.5.0.1-4

* Wed Oct 28 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.4.0.1-4
- fix requires breeze

* Sun Oct 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.4.0.1-2
- update to 1.0.0-alpha.4.0.1-2

* Tue Sep 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.3.0.1-2
- update to 1.0.0-alpha.3.0.1-2

* Sat Sep 26 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-alpha.2.0.1-2
- update to 1.0.0-alpha.2.0.1-2

* Tue Sep 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.982-2
- update to 0.8.982-2

* Tue Sep 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.911-2
- update to 0.8.911-2

* Mon Aug 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.868-2
- update to 0.8.868-2

* Wed Aug 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.797-2
- update to 0.8.797-2

* Thu Jul 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.757-2
- update to 0.8.757-2

* Sat Jul 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.694-2
- update to 0.8.694-2

* Sat Jun 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.604-2
- update to 0.8.604-2

* Sun Jun 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.535-2
- update to 0.8.535-2

* Sat May 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.459-2
- update to 0.8.459-2

* Wed May 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.397-2
- update to 0.8.397-2

* Sun May 3 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.378-2
- update to 0.8.378-2

* Thu Apr 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.333-2
- update to 0.8.333-2

* Sun Apr 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.298-2
- update to 0.8.298-2

* Sat Apr 11 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.252-2
- update to 0.8.252-2

* Tue Mar 31 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.200-2
- update to 0.8.200-2

* Fri Mar 20 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.156-2
- update to 0.8.156-2

* Thu Mar 12 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.113-2
- update to 0.8.113

* Thu Mar 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.038-2
- update to 0.8.038

* Mon Mar 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.8.001-2
- update to 0.8.001

* Sun Feb 23 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.573-2
- update to 0.7.573

* Mon Jan 27 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.474-2
- update to 0.7.474

* Fri Jan 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.425-2
- update to 0.7.425

* Sat Jan 18 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.383-2
- update to 0.7.383

* Thu Jan 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.367-2
- update to 0.7.367

* Tue Jan 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.7.345-2
- update to 0.7.345

* Thu Dec 26 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.295-2
- update to 0.7.295

* Mon Dec 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.270-2
- update to 0.7.270

* Thu Dec 12 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.186-2
- update to 0.7.186

* Sun Nov 3 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.093-2
- update to 0.7.093

* Thu Oct 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.7.002-2
- update to 0.7.002

* Sun Oct 13 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.502-2
- update to 0.6.502

* Wed Oct 2 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.479-2
- update to 0.6.479

* Fri Sep 20 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.422-2
- update to 0.6.422

* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.384-2
- update to 0.6.384

* Sun Sep 8 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.323-1
- update to 0.6.323

* Wed Aug 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.6.039-1
- update to 0.6.039

* Sun Jul 21 2019 Yann Collette <ycollette.nospam@free.fr> - 0.5.162-1
- Initial build
