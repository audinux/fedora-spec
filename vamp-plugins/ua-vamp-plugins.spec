# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: ua-vamp-plugins
Version: 2.0
Release: 1%{?dist}
Summary: UAPlugins are a set of VAMP plugins developed by the Computer Music Laboratory team
License: GLPv2	
URL: https://github.com/pertusa/UAVampPlugins	

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/pertusa/UAVampPlugins/archive/refs/heads/master.zip#/ua-vamp-plugins.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel
BuildRequires: fftw-devel

%description
UAPlugins are a set of VAMP plugins developed by the Computer Music
Laboratory team from the GRFIA group at the University of Alicante.

The methods used in this library were developed by Antonio Pertusa
and José Manuel Iñesta, supported by the project DRIMS
(code TIN2009-14247-C02), the Consolider Ingenio 2010 research
program (project MIPRCV, CSD2007-00018), and the PASCAL2 Network
of Excellence, IST-2007-216886.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n UAVampPlugins-master

sed -i -e "/^PLUGIN_LIBS/d" Makefile.linux
sed -i -e "s/#PLUGIN_LIBS/PLUGIN_LIBS/g" Makefile.linux
sed -i -e "s/-O3/\$(CXXFLAGS)/g" Makefile.linux
sed -i -e "s/\$(VAMP_SDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 ua-vamp-plugins.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 ua-vamp-plugins.cat %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license LICENSE
%doc readme.md
%{_libdir}/vamp/ua-vamp-plugins.*

%changelog
* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 2.0-1
- Initial spec file

