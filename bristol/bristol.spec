Name:       bristol
Version:    0.60.11
Release:    20%{dist}
Summary:    Synthesizer emulator

License:    GPLv2+
URL:        http://bristol.sourceforge.net
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:    %{name}.desktop
Patch0:     bristol-0.60.9-CVE-2010-3351.patch
Patch1:     bristol-0.60.11-fix-build-with-alsa.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libX11-devel
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils

%description
Bristol is an emulation package for a number of different 'classic'
synthesizers including additive and subtractive and a few organs.
The application consists of the engine, which is called bristol,
and its own GUI library called brighton that represents all the emulations.

%package devel
Summary:    %{summary}
Requires:   %{name} = %{version}

%description devel
This package contains the development libraries for Bristol.

%prep
%autosetup -p1

find ./bitmaps/ -name '*.gz' | xargs chmod -x
chmod -x ./memory/profiles/*
find . -name '*.c' | xargs chmod -x
find . -name '*.h' | xargs chmod -x
find . -name '*.xbm' | xargs chmod -x
find . -name '*.svg' | xargs chmod -x
chmod -x NEWS COPYING* README AUTHORS ChangeLog
chmod -x memory/mixer/default/memory memory/mini/readme.txt

# Only x86_64 is optimised for SSE, non x86 platforms don't have SSE
%ifnarch x86_64
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.am
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.in
%endif

%build

autoreconf -if
CFLAGS="-fPIC -fcommon" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static=no --disable-version-check
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install

make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm INSTALL
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 0644 bitmaps/bicon.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/bristol.svg

desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    %{SOURCE1}

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/bristol
%{_datadir}/pixmaps/*
%{_datadir}/applications/bristol.desktop
%{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%{_libdir}/lib*.so

%changelog
* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.60.11-16
- Fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.60.11-7
- Add patch to fix rawhide build.
- Minor spec cleanup; fix whitespace and rpmlint complaints.
- Use %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.60.11-1
- New upstream.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.60.10-2
- Fix compilation on platforms where we don't support SSE

* Tue Jun 05 2012 Jon Ciesla <limburgher@gmail.com> - 0.60.10-1
- New upstream.

* Fri Jan 20 2012 Dan Horák <dan[at]danny.cz> - 0.60.9-2
- fix build on secondary arches

* Wed Jan 11 2012 Jon Ciesla <limburgher@gmail.com> - 0.60.9-1
- New upstream.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jon Ciesla <limb@jcomserv.net> - 0.60.8-1
- New upstream.

* Wed Sep 29 2010 Jon Ciesla <limb@jcomserv.net> - 0.60.6-1
- New upstream, fix for CVE-2010-3351, BZ 638376.

* Tue Jan 26 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-6
- Removed INSTALL.

* Mon Jan 25 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-5
- Switched to svg icon, preserved timestamps.

* Fri Jan 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-4
- Dropped Encoding from desktop.
- Fixed lib ownership.

* Fri Jan 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-3
- Drop -libs subpackage, create -devel.
- Re-dropped mistakenly added static libs.
- Add .desktop file for -b3.

* Thu Jan 21 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-2
- Configure macro, parallel make, fixed rpath.

* Tue Jan 19 2010 Jon Ciesla <limb@jcomserv.net> - 0.40.7-1
- Initial creation.
