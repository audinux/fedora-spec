# Tag: Editor
# Type: Standalone
# Category: Audio, Sampler

Summary: Instrument editor for gig files
Name:    gigedit
Version: 1.1.1
Release: 2%{?dist}
License: GPL2
URL:     http://www.linuxsampler.org/

Distribution: Planet CCRMA
Vendor:       Planet CCRMA

Source0: http://download.linuxsampler.org/packages/gigedit-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: intltool
BuildRequires: gtkmm30-devel
BuildRequires: libgig-devel
BuildRequires: libsndfile-devel
BuildRequires: linuxsampler-devel
BuildRequires: libxslt-devel
BuildRequires: docbook-style-xsl
BuildRequires: jack-audio-connection-kit-devel

Requires: hicolor-icon-theme

%description
Gigedit is an instrument editor for gig files. Gig files are
used by software samplers such as LinuxSampler and GigaStudio.

With gigedit it is possible to modify existing gig files and also to
create completely new instruments from scratch. Gigedit can be run as
a stand-alone application, or as a plugin to LinuxSampler.

Please note that this is an early version that only includes the most
basic features needed to create and edit gig files. There is still a
lot to do, fix and improve. Be sure to backup your original gig files
before editing them in gigedit.

%prep
%autosetup

%build

%set_build_flags
%configure CXXFLAGS="-std=c++11 -DHAS_PANGOMM_CPP11_ENUMS=0 $CXXFLAGS"
%make_build LIBTOOLFLAGS="--tag=CXX"

%install

%make_install

rm -f %{buildroot}/%{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.la
rm -f %{buildroot}/%{_libdir}/gigedit/libgigedit.la

%files
%doc doc/quickstart/*html doc/quickstart/*png doc/quickstart/*css
%{_bindir}/gigedit
%exclude %{_libdir}/gigedit/libgigedit.a
%{_libdir}/gigedit/libgigedit.so*
%exclude %{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.a
%{_libdir}/linuxsampler/plugins/libgigeditlinuxsamplerplugin.so
%exclude %{_datadir}/doc/gigedit
%{_datadir}/gigedit
%{_datadir}/locale/de/LC_MESSAGES/gigedit.mo
%{_datadir}/locale/sv/LC_MESSAGES/gigedit.mo

%changelog
* Sun Oct 09 2022 Yann Collette <ycollette.nospam@free.fr> - 1.2.0-2
- update to 1.2.0-2

* Thu Nov 05 2020 Yann Collette <ycollette.nospam@free.fr> - 1.1.1-2
- update to 1.1.1-2

* Mon Jun 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-2
- fix build on fedora 30

* Mon Nov 5 2018 Yann Collette <ycollette.nospam@free.fr> - 1.1.0-1
- update to 1.1.0

* Sun Aug 28 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.0-1
- update to 1.0.0
- add libxslt-devel build requirement

* Sat Jul 10 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> -
- remove and relink libtool with proper binary

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- add check for libsigc++ so that proper link libraries are used for
  fc13/gcc4.4.4

* Sat Nov  7 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- updated to 0.2.0

* Sat Oct 18 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.1
- initial build.
