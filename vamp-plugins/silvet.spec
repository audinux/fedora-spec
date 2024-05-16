# Tag: Effect, Analyzer
# Type: Plugin, VAMP
# Category: Audio, Effect

Name: silvet
Version: 1.1
Release: 2%{?dist}
Summary: Silvet, or Shift-Invariant Latent Variable Transcription, is a Vamp plugin for polyphonic music transcription
License: GLPv2
URL: https://code.soundsoftware.ac.uk/projects/silvet
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://code.soundsoftware.ac.uk/attachments/download/1594/silvet-v%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: vamp-plugin-sdk-devel
BuildRequires: boost-devel

%description
Silvet, or Shift-Invariant Latent Variable Transcription,
is a Vamp plugin for polyphonic music transcription (from
audio to note times and pitches).

%package -n vamp-%{name}
Summary: %{name} VAMP plugin

%description -n vamp-%{name}
Silvet, or Shift-Invariant Latent Variable Transcription,
is a Vamp plugin for polyphonic music transcription (from
audio to note times and pitches).

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s/\$(VAMPSDK_DIR)\/libvamp-sdk.a/-lvamp-sdk/g" Makefile.inc
sed -i -e "s/.*-Wall -O3.*/CFLAGS=\$(VAMPCFLAGS)/g" Makefile.linux
sed -i -e "s/.*-Wall -O3.*/CFLAGS=\$(VAMPCFLAGS)/g" constant-q-cpp/Makefile.linux

%build

%set_build_flags

export VAMPCFLAGS="$CFLAGS -fPIC"

%make_build -j1 -f Makefile.linux

%install

install -m 755 -d %{buildroot}/%{_libdir}/vamp/
install -m 755 silvet.so  %{buildroot}/%{_libdir}/vamp/
install -m 644 silvet.cat %{buildroot}/%{_libdir}/vamp/
install -m 644 silvet.n3  %{buildroot}/%{_libdir}/vamp/

%files -n vamp-%{name}
%license COPYING
%doc README
%{_libdir}/vamp/silvet.*

%changelog
* Fri Jul 22 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-2
- update to 1.1-2

* Sat Jan 08 2022 Yann Collette <ycollette.nospam@free.fr> - 1.1-1
- Initial spec file

