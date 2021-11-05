# Tag: Tracker
# Type: Standalone
# Category: Audio, Sequencer

Name:    buzztrax
Version: 0.10.2
Release: 6%{?dist}
Summary: Music composer similar to tracker applications.
License: LGPL2.1
URL:     https://www.buzztrax.org 

Vendor:       Audinux
Distribution: Audinux

Source0: https://files.buzztrax.org/releases/%{name}-%{version}.tar.gz
Patch0:  buzztrax-0001-fix-build.patch
Patch1:  buzztrax-0002-support-fluidsynth-2.patch

BuildRequires: gcc gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: intltool
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: libxml2-devel
BuildRequires: clutter-gtk-devel
BuildRequires: gtk+-devel
BuildRequires: gettext-devel
BuildRequires: gtk-doc
BuildRequires: gstreamer1-plugins-good
BuildRequires: orc-compiler
BuildRequires: alsa-lib-devel
BuildRequires: libgudev-devel
BuildRequires: fluidsynth-devel
BuildRequires: goffice-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils

%description
A song consists of a sequence with tracks and in each track one uses patterns with events 
(musical notes and control changes). In contrast to other Tracker programs, 
tracks are not simply sample players: a user can make a song using an arrangment 
of virtual audio plugins that are linked together to create different effects. 
Each of these machines can be controlled realtime or via patterns in the sequencer.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for

%prep

%autosetup -p1 -n %{name}-%{version}

sed -i -e "71d" Makefile.am

%build

autoreconf

%configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-dllwrapper=no --disable-rpath

%make_build CFLAGS="%{optflags} -Wno-error"

%install

%make_install
%ifarch x86_64
mv $RPM_BUILD_ROOT/usr/lib/buzztrax-songio $RPM_BUILD_ROOT/usr/lib64/
%endif

chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libbuzztrax-core.so.1.1.0
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/buzztrax-songio/libbtbsl.so
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/buzztrax-cmd
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/buzztrax-edit
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libbuzztraxaudio.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstfluidsynth.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libbuzztraxdec.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstbml.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstsidsyn.so

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-edit.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-songio-buzz.desktop

%files
%doc README.md
%license COPYING
%{_datadir}/gtk-doc/html/buzztrax-*
%{_bindir}/buzztrax-cmd
%{_bindir}/buzztrax-edit
%{_libdir}/buzztrax-songio/*
%{_libdir}/buzztrax
%{_libdir}/gstreamer-1.0/libbuzztrax*
%{_libdir}/gstreamer-1.0/libgstbml.*
%{_libdir}/gstreamer-1.0/libgstsidsyn.*
%{_libdir}/gstreamer-1.0/libgstfluidsynth.*
%{_libdir}/libbml.*
%{_libdir}/libbuzztrax-core.*
%{_libdir}/libbuzztrax-gst.*
%{_libdir}/libbuzztrax-ic.*
%{_datadir}/buzztrax
%{_datadir}/icons/gnome/*/apps/%{name}*.png
%{_datadir}/icons/gnome/*/apps/%{name}*.svg
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.svg
%{_datadir}/locale/*/LC_MESSAGES/%{name}-%{version}.mo
%{_datadir}/mime/packages/%{name}*.xml
%{_datadir}/GConf/gsettings/buzztrax.convert
%{_datadir}/gstreamer-1.0/presets/GstBtEBeats.prs
%{_datadir}/gstreamer-1.0/presets/GstBtSimSyn.prs
%{_datadir}/applications/%{name}-edit.desktop
%{_datadir}/applications/%{name}-songio-buzz.desktop
%{_datadir}/appdata/buzztrax.appdata.xml
%{_datadir}/glib-2.0/schemas/org.buzztrax.gschema.xml

%files devel
%{_includedir}/libbml
%{_includedir}/libbuzztrax-core
%{_includedir}/libbuzztrax-gst
%{_includedir}/libbuzztrax-ic
%{_libdir}/pkgconfig/libbml.pc
%{_libdir}/pkgconfig/libbuzztrax-core.pc
%{_libdir}/pkgconfig/libbuzztrax-gst.pc
%{_libdir}/pkgconfig/libbuzztrax-ic.pc

%changelog
* Mon Oct 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.10.2-6
- Fix for Fedora 33 

* Thu Apr 30 2020 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-5
- Fix for Fedora 

* Sun Oct 23 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-4
- changed source

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-3
- added orc dep

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org> - 0.10.2-2
- update spec to update icons on install

* Fri Oct 14 2016 L.L.Robinson <baggypants@fedoraproject.org>
- 
