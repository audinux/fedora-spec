# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: vamp-tempogram
Version: 1.0
Release: 2%{?dist}
Summary: A Vamp plugin implementation of the tempogram and cyclic tempogram features
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/vamp-tempogram

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/1206/vamp-tempogram-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: vamp-plugin-sdk-devel

%description
A Vamp plugin implementation of the tempogram and cyclic tempogram features
described in Grosche, Müller, and Kurth 2010, providing a robust mid-level
representation that encodes local tempo information.

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s/\$(VAMPSDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.linux
sed -i -e "s/-Wall -Wextra -O3.*/\$(VAMPCFLAGS)/g" Makefile.linux

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -fPIC"

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 tempogram.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 tempogram.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 tempogram.n3  %{buildroot}/%{_libdir}/vamp/

%files
%license COPYING
%doc README CITATION
%{_libdir}/vamp/tempogram.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

