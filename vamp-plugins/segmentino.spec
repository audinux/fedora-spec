# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: segmentino
Version: 1.1	
Release: 1%{?dist}
Summary: Segmentino is a Vamp plugin for automatic music structural segmentation
License: GLPv2	
URL: https://code.soundsoftware.ac.uk/projects/segmenter-vamp-plugin	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/2458/segmentino-v%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: polyml
BuildRequires: mercurial
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
Segmentino is a Vamp plugin for automatic music structural segmentation.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s/-O3.*/\$(VAMPCFLAGS)/g" Makefile.linux
sed -i -e "s/\$(CFLAGS)/\$(VAMPCXXFLAGS)/g" Makefile.linux

%build

%set_build_flags
PWD=`pwd`
export VAMPCFLAGS="$CFLAGS -I$PWD -fPIC"
export VAMPCXXFLAGS="$CXXFLAGS -I$PWD -fPIC"

%make_build -j1 -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 segmentino.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 segmentino.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 segmentino.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/segmentino.*

%changelog
* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

