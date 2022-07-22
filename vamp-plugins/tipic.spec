# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: tipic
Version: 1.0
Release: 2%{?dist}
Summary: Tipic - Tibre-Invariant Pitch Chroma
License: GLPv2	
URL: https://code.soundsoftware.ac.uk/projects/tipic	

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/2272/tipic-src-v%{version}.tar.gz

BuildRequires: gcc gcc-c++ make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
A C++ Vamp plugin providing an efficient causal implementation of
pitch-chroma audio features approaching timbre invariance, after
the paper "Towards timbre-invariant audio features for harmony-based music"
by Meinard Müller and Sebastian Ewert.

This plugin is intended to provide features extracted from a music audio
signal, containing a reduction of the pitch and harmonic content of the
audio which is relatively stable in the presence of timbral differences
and local variations such as vibrato.

Provided under the GNU General Public License. Uses the QM DSP library.

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
A C++ Vamp plugin providing an efficient causal implementation of
pitch-chroma audio features approaching timbre invariance, after
the paper "Towards timbre-invariant audio features for harmony-based music"
by Meinard Müller and Sebastian Ewert.

This plugin is intended to provide features extracted from a music audio
signal, containing a reduction of the pitch and harmonic content of the
audio which is relatively stable in the presence of timbral differences
and local variations such as vibrato.

Provided under the GNU General Public License. Uses the QM DSP library.

%prep
%autosetup -n %{name}-src-v%{version}

sed -i -e "s/-Wall -Werror -O3.*/\$(VAMPCFLAGS)/g" Makefile.linux
sed -i -e "s/\$(CFLAGS)/\$(VAMPCXXFLAGS)/g" Makefile.linux
sed -i -e "s/\$(VAMPSDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.inc

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -fPIC"
export VAMPCFLAGS="$CXXFLAGS -fPIC"

%make_build -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 tipic.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 tipic.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 tipic.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README.txt CITATION
%{_libdir}/vamp/tipic.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-2
- update to 1.0-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.0-1
- Initial spec file

