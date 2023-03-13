Name:    nki
Version: 0.0.1
Release: 1%{?dist}
Summary: A simple console application to convert NKI files
License: GPLv3+
URL:     http://www.linuxsampler.org/nkitool/

Vendor:       Audinux
Distribution: Audinux

Source0: http://download.linuxsampler.org/dev/nkitool/nki.c

BuildRequires: gcc
BuildRequires: zlib-devel

%description
nkitool is a simple console application which exports and imports the human
readable XML file from and to Native Instruments Kontakt .nki instrument
articulation files. So far, Kontakt v1 to v4 format versions are supported
by this tool. nkitool is released in binary and source code format in the
public domain. However in case you find mistakes or improvements,
we would appreciate if you share them with us!

%prep

mkdir -p %{name}
cd %{name}
cp %{SOURCE0} .

sed -i -e "s/zlib-1.2.5\///g" nki.c

%build

%set_build_flags

cd %{name}
gcc $CFLAGS nki.c -o nki -lz $LDFLAGS

%install

cd %{name}
install -m 755 -d %{buildroot}/%{_bindir}/
cp nki %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%changelog
* Sun Mar 12 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial spec file
