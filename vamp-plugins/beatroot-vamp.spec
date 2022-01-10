# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: beatroot-vamp
Version: 1.0
Release: 1%{?dist}
Summary: A Vamp Plugin implementation of the BeatRoot beat tracking system
License: GLPv2	
URL: https://code.soundsoftware.ac.uk/projects/beatroot-vamp	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/885/beatroot-vamp-v%{version}.tar.gz

BuildRequires: gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
A Vamp Plugin implementation of the BeatRoot beat tracking system

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s|-Wl,-Bstatic -L../vamp-plugin-sdk||g" Makefile.linux

sed -i -e "s|CFLAGS := -fPIC -O3 -Wall|CFLAGS := -fPIC \$(CFLAGS)|g"  Makefile.linux
sed -i -e "s|CXXFLAGS := \$(CFLAGS)|CXXFLAGS := -fPIC \$(CXXFLAGS)|g" Makefile.linux

%build

%set_build_flags

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 beatroot-vamp.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 beatroot-vamp.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 beatroot-vamp.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/beatroot-vamp.*

%changelog
* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

