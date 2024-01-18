# Kernel major version
%define kmaj  6
# Kernel minor version
%define kmin  6
# Kernel patch version
%define kpat  12
# RT patch version
%define krt   20
# package version
%define krel  13

%define kver  %{kmaj}.%{kmin}.%{kpat}
%define fcver %{dist}.%{_arch}

Name:    kernel-rt-mao
Summary: The Linux Real Time Kernel
Version: %{kver}.rt%{krt}
Release: %{krel}%{?dist}
License: GPL
URL:     http://www.kernel.org

Vendor:       Audinux
Distribution: Audinux

Source0: https://cdn.kernel.org/pub/linux/kernel/v%{kmaj}.x/linux-%{kver}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}
Patch0: https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/%{kmaj}.%{kmin}/older/patch-%{kver}-rt%{krt}.patch.gz

BuildRequires: openssl-devel
BuildRequires: openssl
BuildRequires: kmod
BuildRequires: patch
BuildRequires: bash
BuildRequires: tar
BuildRequires: bzip2
BuildRequires: xz
BuildRequires: findutils
BuildRequires: gzip
BuildRequires: m4
BuildRequires: perl-interpreter
BuildRequires: perl-Carp
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: make
BuildRequires: diffutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: binutils
BuildRequires: redhat-rpm-config
BuildRequires: bison
BuildRequires: flex
BuildRequires: net-tools
BuildRequires: hostname
BuildRequires: bc
BuildRequires: elfutils-devel
BuildRequires: rpm-build
BuildRequires: rpm
BuildRequires: elfutils
BuildRequires: elfutils-libelf-devel
BuildRequires: grub2-tools
BuildRequires: sed
BuildRequires: rsync
BuildRequires: dwarves

Provides: kernel = %{version}
Provides: kernel-rt-mao = %{version}

%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
The Linux Real Time Kernel, the operating system core itself

%package headers
Summary: Header files for the Linux real time kernel for use by glibc

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
Summary: Development package for building real time kernel modules to match the %{version} kernel
AutoReqProv: no

%description devel
This package provides real time kernel headers and makefiles sufficient to build modules
against the %{version} kernel package.

%prep
%autosetup -p1 -n linux-%{kver}

cp %{SOURCE1} .config
sed -i -e "s/EXTRAVERSION =/EXTRAVERSION = -rt%{krt}%{fcver}/g" Makefile
echo "" > localversion-rt

make oldconfig

%build

make clean && make %{?_smp_mflags}

%install

KBUILD_IMAGE=$(make image_name)

%ifarch ia64
  mkdir -p %{buildroot}/boot/efi %{buildroot}/lib/modules
%else
  mkdir -p %{buildroot}/boot     %{buildroot}/lib/modules
%endif

make %{?_smp_mflags} INSTALL_MOD_PATH=%{buildroot} KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install

# We estimate the size of the initramfs because rpm needs to take this size
# into consideration when performing disk space calculations. (See bz #530778)
dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{kver}-rt%{krt}%{fcver}.img bs=1M count=20

%ifarch ia64
  cp $KBUILD_IMAGE %{buildroot}/boot/efi/vmlinuz-%{kver}-rt%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/efi/vmlinuz-%{kver}-rt%{krt}%{fcver}
  ln -s efi/vmlinuz-%{kver}-%{krt}%{fcver} %{buildroot}/boot/
%else
  cp $KBUILD_IMAGE %{buildroot}/boot/vmlinuz-%{kver}-rt%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/vmlinuz-%{kver}-rt%{krt}%{fcver}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=%{buildroot}/usr KBUILD_SRC= headers_install
cp System.map %{buildroot}/boot/System.map-%{kver}-rt%{krt}%{fcver}
cp .config    %{buildroot}/boot/config-%{kver}-rt%{krt}%{fcver}

cp %{buildroot}/boot/vmlinuz-%{kver}-rt%{krt}%{fcver} %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz

rm -f %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
rm -f %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/source

mkdir -p %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
(cd %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver} ; ln -s build source)

# dirs for additional modules per module-init-tools, kbuild/modules.txt
mkdir -p %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/extra
mkdir -p %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/internal
mkdir -p %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/updates

# CONFIG_KERNEL_HEADER_TEST generates some extra files in the process of
# testing so just delete
find . -name *.h.s -delete

# first copy everything
cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
cp Module.symvers %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
cp System.map %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
if [ -s Module.markers ]; then
  cp Module.markers %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build
fi

# Move the devel headers out of the root file system

DevelDir=/usr/src/kernels/%{kver}-rt%{krt}%{fcver}

mkdir -p %{buildroot}/usr/src/kernels/%{kver}-rt%{krt}%{fcver}
mv %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build %{buildroot}/$DevelDir

# This is going to create a broken link during the build, but we don't use
# it after this point.  We need the link to actually point to something
# when kernel-devel is installed, and a relative link doesn't work across
# the F17 UsrMove feature.

ln -sf $DevelDir %{buildroot}/lib/modules/%{kver}-rt%{krt}%{fcver}/build

# prune junk from kernel-devel

find %{buildroot}/usr/src/kernels -name ".*.cmd" -delete

EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd %{buildroot}/usr/src/kernels/%{kver}-rt%{krt}%{fcver}; tar xvf -)

%post
# Create the initramfs file
/bin/kernel-install add %{kver}-rt%{krt}%{fcver} /lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
/bin/kernel-install remove %{kver}-rt%{krt}%{fcver} /lib/modules/%{kver}-rt%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%files
%defattr (-, root, root)
/lib/modules/%{kver}-rt%{krt}%{fcver}
/boot/*
%ghost /boot/initramfs-%{kver}-rt%{krt}%{fcver}

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kver}-rt%{krt}%{fcver}

%changelog
* Thu Jan 18 2024 Yann Collette <ycollette.nospam@free.fr> - 6.6.12-rt20-13
- update to 6.6.12-rt20-13 - vanilla RT kernel

* Thu Jul 27 2023 Yann Collette <ycollette.nospam@free.fr> - 6.4.6-rt8-13
- update to 6.4.6-rt8-13 - vanilla RT kernel

* Mon Jun 19 2023 Yann Collette <ycollette.nospam@free.fr> - 6.1.33-rt11-13
- update to 6.1.33-rt11-13 - vanilla RT kernel

* Mon May 15 2023 Yann Collette <ycollette.nospam@free.fr> - 6.1.28-rt10-13
- update to 6.1.28-rt10-13 - vanilla RT kernel

* Mon May 01 2023 Yann Collette <ycollette.nospam@free.fr> - 6.1.26-rt8-13
- update to 6.1.26-rt8-13 - vanilla RT kernel

* Sun Dec 18 2022 Yann Collette <ycollette.nospam@free.fr> - 6.0.5-rt14-13
- update to 6.0.5-rt14-13 - vanilla RT kernel

* Mon Nov 21 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.79-rt54-13
- update to 5.15.79-rt54-13 - vanilla RT kernel

* Tue Nov 01 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.76-rt53-13
- update to 5.15.73-rt53-13 - vanilla RT kernel

* Sun Oct 16 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.73-rt52-13
- update to 5.15.73-rt52-13 - vanilla RT kernel

* Sun Oct 02 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.71-rt51-13
- update to 5.15.71-rt51-13 - vanilla RT kernel

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.70-rt50-13
- update to 5.15.70-rt50-13 - vanilla RT kernel

* Sun Jul 31 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.55-rt48-13
- update to 5.15.55-rt48-13 - vanilla RT kernel

* Wed Jul 06 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.49-rt47-13
- update to 5.15.49-rt47-13 - vanilla RT kernel

* Wed Jun 01 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.44-rt46-13
- update to 5.15.44-rt46-13 - vanilla RT kernel

* Fri May 27 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.43-rt45-13
- update to 5.15.43-rt45-13 - vanilla RT kernel

* Mon May 16 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.40-rt43-13
- update to 5.15.40-rt43-13 - vanilla RT kernel

* Mon May 16 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.39-rt42-13
- update to 5.15.39-rt42-13 - vanilla RT kernel

* Mon May 02 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.36-rt41-13
- update to 5.15.36-rt41-13 - vanilla RT kernel

* Tue Apr 26 2022 Yann Collette <ycollette.nospam@free.fr> - 5.17.1-rt17-13
- update to 5.17.1-rt17-13 - vanilla RT kernel

* Thu Apr 07 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.32-rt39-13
- update to 5.15.32-rt39-13 - vanilla RT kernel

* Sat Mar 26 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.31-rt38-13
- Fix kernel config

* Sat Mar 26 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.31-rt38-12
- update to 5.15.31-rt38-12 - vanilla RT kernel

* Thu Mar 24 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.29-rt37-12
- update to 5.15.29-rt37-12 - vanilla RT kernel

* Tue Mar 15 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.28-rt36-12
- update to 5.15.28-rt36-12 - vanilla RT kernel

* Thu Mar 10 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.27-rt35-12
- update to 5.15.27-rt35-12 - vanilla RT kernel

* Fri Mar 04 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.26-rt34-12
- update to 5.15.26-rt34-12 - vanilla RT kernel

* Thu Mar 03 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.25-rt33-12
- update to 5.15.25-rt33-12 - vanilla RT kernel

* Tue Mar 01 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.25-rt32-12
- update to 5.15.25-rt32-12 - vanilla RT kernel

* Tue Feb 22 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.24-rt31-12
- update to 5.15.24-rt31-12 - vanilla RT kernel

* Mon Feb 07 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.21-rt30-12
- update to 5.15.21-rt30-12 - vanilla RT kernel

* Fri Feb 04 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.19-rt29-12
- update to 5.15.19-rt29-12 - vanilla RT kernel

* Tue Feb 01 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.18-rt28-12
- update to 5.15.18-rt28-12 - vanilla RT kernel

* Fri Jan 21 2022 Yann Collette <ycollette.nospam@free.fr> - 5.16.2-rt19-12
- update to 5.16.2-rt19-12 - vanilla RT kernel

* Tue Jan 18 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.14-rt27-12
- disable CONFIG_HAVE_PREEMPT_DYNAMIC in config file.

* Thu Jan 13 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.14-rt27-11
- update to 5.15.14-rt27-11 - vanilla RT kernel

* Fri Jan 07 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.13-rt26-11
- update to 5.15.13-rt26-11 - vanilla RT kernel

* Tue Jan 04 2022 Yann Collette <ycollette.nospam@free.fr> - 5.15.12-rt25-11
- update to 5.15.12-rt25-11 - vanilla RT kernel

* Sat Dec 18 2021 Yann Collette <ycollette.nospam@free.fr> - 5.15.10-rt24-11
- update to 5.15.10-rt24-11 - vanilla RT kernel

* Fri Dec 10 2021 Yann Collette <ycollette.nospam@free.fr> - 5.15.7-rt23-11
- update to 5.15.7-rt23-11 - vanilla RT kernel

* Thu Nov 18 2021 Yann Collette <ycollette.nospam@free.fr> - 5.15.2-rt20-11
- update to 5.15.2-rt20-11 - vanilla RT kernel

* Sat Nov 13 2021 Yann Collette <ycollette.nospam@free.fr> - 5.15.2-rt19-11
- update to 5.15.2-rt19-11 - vanilla RT kernel

* Mon Oct 04 2021 Yann Collette <ycollette.nospam@free.fr> - 5.14.2-rt21-11
- update to 5.14.2-rt21-11 - vanilla RT kernel

* Wed Mar 24 2021 Yann Collette <ycollette.nospam@free.fr> - 5.11.4-rt11-11
- update to 5.11.4-rt11-11 - vanilla RT kernel

* Wed Mar 24 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.25-rt35-11
- update to 5.10.25-rt35-11 - vanilla RT kernel

* Tue Mar 09 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.21-rt34-11
- update to 5.10.21-rt34-11 - vanilla RT kernel

* Fri Feb 19 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.17-rt32-11
- update to 5.10.17-rt32-11 - vanilla RT kernel

* Tue Feb 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.16-rt30-11
- update to 5.10.16-rt30-11 - vanilla RT kernel

* Tue Feb 9 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.14-rt28-11
- update to 5.10.14-rt28-11 - vanilla RT kernel

* Tue Feb 2 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.12-rt26-11
- update to 5.10.12-rt26-11 - vanilla RT kernel

* Tue Jan 19 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.8-rt24-11
- update to 5.10.8-rt24-11 - vanilla RT kernel

* Sat Jan 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.4-rt22-11
- update to 5.10.4-rt22-11 - vanilla RT kernel

* Sun Aug 23 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.19-rt12-11
- update to 5.6.19-rt12-11 - vanilla RT kernel

* Sun Jul 26 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.19-rt11-11
- update to 5.6.19-rt11-11 - vanilla RT kernel

* Fri Jun 19 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt10-11
- update to 5.6.17-rt10-11 - fix preempt option ...

* Tue Jun 16 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt10-10
- update to 5.6.17-rt10-10

* Wed Jun 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.17-rt9-10
- update to 5.6.17-rt9-10

* Wed May 27 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.14-rt7-10
- update to 5.6.14-rt7-10

* Thu May 14 2020 Yann Collette <ycollette.nospam@free.fr> - 5.6.10-rt5-10
- update to 5.6.10-rt5-10

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.39-rt23-10
- update to 5.4.39-rt23-10

* Sun May 10 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.34-rt21-10
- update to 5.4.34-rt21-10

* Mon Mar 30 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.28-rt19-10
- update to 5.4.28-rt19-10

* Sat Mar 21 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.26-rt17-10
- update to 5.4.26-rt17-10

* Sun Mar 8 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.24-rt15-10
- update to 5.4.24-rt15-10

* Sat Feb 29 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.22-rt13-10
- update to 5.4.22-rt13-10

* Sat Feb 15 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.19-rt11-10
- update to 5.4.19-rt11-10

* Fri Feb 7 2020 Yann Collette <ycollette.nospam@free.fr> - 5.4.17-rt9-10
- update to 5.4.17-rt9-10

* Mon Dec 16 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt15-9
- update to 5.2.21-rt15-9

* Wed Dec 4 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt14-9
- update to 5.2.21-rt14-9

* Sat Oct 19 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.21-rt13-9
- update to 5.2.21-rt13-9

* Tue Oct 8 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.19-rt11-9
- update to 5.2.19-rt11-9

* Mon Sep 30 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.17-rt9-9
- update to 5.2.17-rt9-9

* Sat Sep 14 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.14-rt7-9
- update to 5.2.14-rt7-9

* Tue Aug 27 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.10-rt5-9
- update to 5.2.10-rt5-9

* Sun Aug 18 2019 Yann Collette <ycollette.nospam@free.fr> - 5.2.9-rt3-9
- update to 5.2.9-rt3-9

* Sat Aug 17 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt16-9
- update to 5.0.21-rt16-9 - fix a radeon / dma bug

* Thu Jul 4 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt15-8
- update to 5.0.21-rt15-8

* Wed Jun 26 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt14-8
- update to 5.0.21-rt14-8 - buggy - doesn't boot

* Wed Jun 19 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.21-rt12-8
- update to 5.0.21-rt12-8

* Sun Jun 9 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.19-rt11-8
- update to 5.0.19-rt11-8

* Sat May 11 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.14-rt9-8
- update to 5.0.14-rt9-8

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.37-rt19-8
- update to 4.19.37-rt19-8

* Thu Mar 28 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.31-rt18-8
- update to 4.19.31-rt18-8

* Thu Mar 28 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.25-rt16-8
- update to 4.19.25-rt16-8

* Fri Mar 1 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.25-rt16-7
- update to 4.19.25-rt16-7

* Tue Jan 15 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.15-rt12-7
- update to 4.19.15-rt12-7

* Tue Jan 15 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-7
- update to 4.19.13-rt10-7 - fix package version

* Thu Jan 10 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-6
- update to 4.19.13-rt10-6

* Wed Jan 9 2019 Yann Collette <ycollette.nospam@free.fr> - 4.19.13-rt10-5
- update to 4.19.13-rt10-5

* Sun Oct 28 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.16-rt8-5
- fix kernel install

* Sat Oct 27 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.16-rt8-4
- add 4.18.16-rt8 kernel

* Wed Oct 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.12-rt7-3
- add 4.18.12-rt7 kernel

* Tue Sep 18 2018 Yann Collette <ycollette.nospam@free.fr> - 4.18.7-rt5-3
- add 4.18.7-rt5 kernel

* Sat Sep 8 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt11-3
- add 4.16.18-rt11 kernel

* Sun Jul 22 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.18-rt10-3
- add 4.16.18-rt10 kernel

* Sat Jun 23 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.15-rt7-3
- add 4.16.15-rt7 kernel

* Wed Jun 13 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-3
- fix a huge config problem

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.14.40-2
- add 4.14.40-rt30 kernel (4.16 kernels are xrunning)

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.12-rt5-2
- add 4.16.12-rt5 kernel

* Sun Jun 10 2018 Yann Collette <ycollette.nospam@free.fr> - 4.16.8-rt2-2
- add 4.16.8-rt2 kernel
