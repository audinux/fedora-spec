# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: cqvamp
Version: 1.1
Release: 2%{?dist}
Summary: A Vamp plugin implementing the Constant-Q transform of a time-domain signal
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/constant-q-cpp
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/1598/cq-v%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel
BuildRequires: libsndfile-devel

%description
A Vamp plugin implementing the Constant-Q transform of a time-domain signal

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
A Vamp plugin implementing the Constant-Q transform of a time-domain signal

%prep
%autosetup -n cq-v%{version}

sed -i -e "s/CFLAGS := -Wall -O3 -ffast-math -msse -msse2 -mfpmath=sse -fPIC -I..\/vamp-plugin-sdk\//CFLAGS := \$(CFLAGS) -fPIC/g" Makefile.linux
sed -i -e "s/CXXFLAGS := \$(CFLAGS) -std=c++11/CXXFLAGS := \$(CFLAGS) -fPIC -std=c++11/g" Makefile.linux
sed -i -e "s/\$(VAMPSDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.inc

%build

%set_build_flags

%make_build -j1 -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 cqvamp.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 cqvamp.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 cqvamp.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/cqvamp.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Mon Jan 10 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

