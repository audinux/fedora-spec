# Tag: Jack, Equalizer, Compressor, Convolution, Gate, Analyzer, Reverb, Delay, MIDI
# Type: Plugin, LV2
# Category: Audio, Effect

Name:    lsp-plugins
Summary: Linux Studio Plugins collection
Version: 1.1.30
Release: 1%{?dist}
License: GPL
URL:     https://github.com/sadko4u/lsp-plugins

Vendor:       Audinux
Distribution: Audinux

# ./lsp-sources.sh 1.1.30

Source0: lsp-plugins.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: cairo-devel
BuildRequires: ladspa-devel
BuildRequires: expat-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: mesa-libGL-devel
BuildRequires: php-cli
BuildRequires: chrpath

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%prep
%autosetup -n lsp-plugins

# Disable strip for debug package
sed -i -e "s/+= -s/+=/g" Makefile
sed -i -e "/MAKE_OPTS/d" scripts/make/tools.mk

%build

%make_build DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS="%{optflags} -DLSP_NO_EXPERIMENTAL" BIN_PATH=%{_bindir} LIB_PATH=%{_libdir} DOC_PATH=%{_docdir}

%install

%make_install DESTDIR=%{buildroot} PREFIX=/usr BUILD_PROFILE=%{_arch} CC_FLAGS="%{optflags} -DLSP_NO_EXPERIMENTAL" BIN_PATH=/usr/bin LIB_PATH=/usr/lib64 DOC_PATH=/usr/share/doc install

chrpath --delete $RPM_BUILD_ROOT/usr/bin/*
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/ladspa/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/lsp-plugins/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/lv2/lsp-plugins.lv2/*.so
chrpath --delete $RPM_BUILD_ROOT/usr/%{_lib}/vst/lsp-plugins-lxvst-%{version}/*.so

%files
%doc CHANGELOG.txt README.txt
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Thu Apr 01 2021 Yann Collette <ycollette dot nospam at free.fr> 1.1.30-1
- update to 1.1.30-1

* Tue Jan 19 2021 Yann Collette <ycollette dot nospam at free.fr> 1.1.29-1
- update to 1.1.29-1

* Mon Dec 21 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.28-1
- update to 1.1.28-1

* Wed Sep 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.26-1
- update to 1.1.26-1

* Thu Jul 16 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.24-1
- update to 1.1.24-1

* Sun May 31 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.22-1
- update to 1.1.22-1

* Sun May 17 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.21-1
- update to 1.1.21-1

* Sun Apr 19 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.19-1
- update to 1.1.19-1

* Sun Apr 5 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.17-1
- update to 1.1.17-1

* Sun Mar 29 2020 Yann Collette <ycollette dot nospam at free.fr> 1.1.15-1
- update to 1.1.15-1

* Tue Dec 24 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.13-1
- update to 1.1.13-1

* Sun Dec 22 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.11-1
- update to 1.1.11-1

* Tue Jul 23 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.10-1
- update to 1.1.10-1

* Mon Mar 18 2019 Yann Collette <ycollette dot nospam at free.fr> 1.1.7-1
- update to 1.1.7-1

* Fri Dec 21 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.5-1
- update to 1.1.5-1

* Mon Oct 15 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- update for Fedora 29

* Sun Sep 30 2018 Yann Collette <ycollette dot nospam at free.fr> 1.1.4-1
- Initial release of the spec file
