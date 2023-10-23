# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: match-vamp
Version: 1.0
Release: 2%{?dist}
Summary: A Vamp plugin implementation of the MATCH audio alignment algorithm
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/match-vamp

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/1615/match-vamp-%{version}.tar.bz2

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
A Vamp plugin implementation of the MATCH audio alignment algorithm.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
A Vamp plugin implementation of the MATCH audio alignment algorithm.

%prep
%autosetup

sed -i -e "s/-Wl,-Bstatic -lvamp-sdk/-lvamp-sdk/g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 match-vamp-plugin.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 match-vamp-plugin.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 match-vamp-plugin.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/match-vamp-plugin.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Tue Jan 11 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

