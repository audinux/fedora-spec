# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: ofa-vamp-plugin
Version: 1.0
Release: 1%{?dist}
Summary: Plugin that performed audio fingerprinting and track identification using the MusicIP OFA library
License: GLPv2	
URL: http://code.soundsoftware.ac.uk/projects/ofa-vamp-plugin	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/hg/ofa-vamp-plugin/archive/tip.zip#/ofa-masteR.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: libofa-devel
BuildRequires: expat-devel
BuildRequires: libcurl-devel

%description
Plugin that performed audio fingerprinting and track identification using the MusicIP OFA library

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n ofa-vamp-plugin-1aa804db4773

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-fPIC -O2 -Wall/-fPIC -O2 -Wall \$(CXXFLAGS)/g" Makefile

%build

%set_build_flags

%make_build -f Makefile

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 ofa-vamp-plugin.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 ofa-vamp-plugin.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 ofa-vamp-plugin.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%doc README
%{_libdir}/vamp/ofa-vamp-plugin.*

%changelog
* Wed Jan 12 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

