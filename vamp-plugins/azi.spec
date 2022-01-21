# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: azi
Version: 1.0
Release: 1%{?dist}
Summary: Experimental azimuth-based stereo plan plugin
License: GLPv2	
URL: https://code.soundsoftware.ac.uk/projects/azi	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/hg/azi/archive/tip.zip#/%{name}.zip

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel

%description
Experimental azimuth-based stereo plan plugin

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
%{description}

%prep
%autosetup -n %{name}-299df1b44eff

sed -i -e "s/-Wall -O3.*/\$(VAMPCFLAGS)/g" Makefile.linux
sed -i -e "s/\$(VAMPSDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.inc

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -fPIC -DUSE_PTHREADS"

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 azi.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 azi.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 azi.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/azi.*

%changelog
* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

