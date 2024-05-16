# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: qm-vamp-plugins
Version: 1.8.0
Release: 2%{?dist}
Summary: A set of Vamp audio analysis plugins developed at the Centre for Digital Music.
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/qm-vamp-plugins/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/2624/qm-vamp-plugins-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: vamp-plugin-sdk-devel

%description
A set of Vamp audio analysis plugins developed at the Centre for Digital Music.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
A set of Vamp audio analysis plugins developed at the Centre for Digital Music.

%prep
%autosetup

sed -i -e "s/-DNDEBUG.*/\$(VAMPCFLAGS)/g" build/linux/Makefile.linux64
sed -i -e "s/\$(CFLAGS)/\$(VAMPCXXFLAGS)/g" build/linux/Makefile.linux64

sed -i -e "s/-DNDEBUG.*/\$(VAMPCFLAGS)/g" lib/qm-dsp/build/linux/Makefile.linux64
sed -i -e "s/\$(CFLAGS)/\$(VAMPCXXFLAGS)/g" lib/qm-dsp/build/linux/Makefile.linux64

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -DUSE_PTHREADS -fPIC"
export VAMPCXXFLAGS="$CXXFLAGS -DUSE_PTHREADS -fPIC"

%make_build -j1 -f build/linux/Makefile.linux64

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 qm-vamp-plugins.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 qm-vamp-plugins.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 qm-vamp-plugins.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README.md CHANGELOG.md
%{_libdir}/vamp/qm-vamp-plugins.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-2
- update to 1.0.0-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-1
- Initial spec file

