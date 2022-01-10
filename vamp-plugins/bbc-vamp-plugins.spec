# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: bbc-vamp-plugins
Version: 1.1	
Release: 1%{?dist}
Summary: A BBC collection of audio feature extraction algorithms	
License: Apache-2.0	
URL: https://github.com/bbc/bbc-vamp-plugins	

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/bbc/bbc-vamp-plugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
This is a collection of audio feature extraction algorithms written
in the Vamp plugin format by BBC Research and Development.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/CXXFLAGS   := /CXXFLAGS   := \$(CXXFLAGS) /g" Makefile.linux
sed -i -e "s/\$(VAMP_SDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 bbc-vamp-plugins.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 bbc-vamp-plugins.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 bbc-vamp-plugins.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README.md AUTHORS
%{_libdir}/vamp/bbc-vamp-plugins.*

%changelog
* Mon Jan 10 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

