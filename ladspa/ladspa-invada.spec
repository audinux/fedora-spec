# Tag: Effect
# Type: LADSPA
# Category: Audio, Effect

Name: ladspa-invada
Version: 0.3.1
Release: 1%{?dist}
Summary: A collection of LADSPA plugins from Invada Records
License: GPL-2.0+
URL: http://www.invadarecords.com/Downloads.php?ID=00000264
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://launchpad.net/invada-studio/ladspa/0.3/+download/invada-studio-plugins_%{version}-nopkg.tar.gz
Patch0: ladspa-invada-0001-makefile.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: ladspa-devel

%description
A collection of LV2 plugins including delay, tube distortion, compressor,
LPF, HPF, phaser, reverb, and utilities, all featuring GUIs.

%prep
%autosetup -p1 -n invada-studio-plugins-%{version}

%build
export LDFLAGS="-z relro --as-needed  -z now --build-id=sha1"
%make_build

%install

%make_install INSTALL_PLUGINS_DIR=%{buildroot}/%{_libdir}/ladspa/ INSTALL_LRDF_DIR=%{buildroot}/%{_datadir}/ladsp/rdf/

%files
%doc README CREDITS
%license COPYING
%{_libdir}/ladspa/
/%{_datadir}/ladsp/rdf/

%changelog
* Mon Nov 28 2022 Yann Collette <ycollette dot nospam at free.fr> 0.3.1-1
- initial spec
