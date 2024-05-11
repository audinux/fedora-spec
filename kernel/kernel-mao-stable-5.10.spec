# Kernel major version
%define kmaj  5
# Kernel minor version
%define kmin  10
# Kernel patch version
%define kpat  216
# RT patch version
%define krt   108
# package version
%define krel  12

%define kver  %{kmaj}.%{kmin}.%{kpat}
%define fcver %{dist}.%{_arch}

Name:    kernel-rt-stable-mao
Summary: The Linux Real Time Kernel
Version: %{kver}.rt%{krt}
Release: %{krel}%{?dist}
License: GPL
URL:     http://www.kernel.org

Vendor:       Audinux
Distribution: Audinux

Source0: https://cdn.kernel.org/pub/linux/kernel/v%{kmaj}.x/linux-%{kver}.tar.gz
Source1: kernel-config-%{kmaj}.%{kmin}
Patch0:  https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/%{kmaj}.%{kmin}/older/patch-%{kver}-rt%{krt}.patch.gz
Patch1:  kernel-5.10-remove-bpf-feature-detect.patch

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
BuildRequires: zlib-devel
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
sed -i -e "s/EXTRAVERSION =/EXTRAVERSION = -rt-stable%{krt}%{fcver}/g" Makefile
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
dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{kver}-rt-stable%{krt}%{fcver}.img bs=1M count=20

%ifarch ia64
  cp $KBUILD_IMAGE %{buildroot}/boot/efi/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/efi/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  ln -s efi/vmlinuz-%{kver}-stable-%{krt}%{fcver} %{buildroot}/boot/
%else
  cp $KBUILD_IMAGE %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
  chmod a+x %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver}
%endif

make %{?_smp_mflags} INSTALL_HDR_PATH=%{buildroot}/usr KBUILD_SRC= headers_install
cp System.map %{buildroot}/boot/System.map-%{kver}-rt-stable%{krt}%{fcver}
cp .config    %{buildroot}/boot/config-%{kver}-rt-stable%{krt}%{fcver}

cp %{buildroot}/boot/vmlinuz-%{kver}-rt-stable%{krt}%{fcver} %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz

rm -f %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
rm -f %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/source

mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
(cd %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver} ; ln -s build source)

# dirs for additional modules per module-init-tools, kbuild/modules.txt
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/extra
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/internal
mkdir -p %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/updates

# CONFIG_KERNEL_HEADER_TEST generates some extra files in the process of
# testing so just delete
find . -name *.h.s -delete

# first copy everything
cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
cp Module.symvers %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
cp System.map %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
if [ -s Module.markers ]; then
  cp Module.markers %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build
fi

# Move the devel headers out of the root file system

DevelDir=/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}

mkdir -p %{buildroot}/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}
mv %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build %{buildroot}/$DevelDir

# This is going to create a broken link during the build, but we don't use
# it after this point.  We need the link to actually point to something
# when kernel-devel is installed, and a relative link doesn't work across
# the F17 UsrMove feature.

ln -sf $DevelDir %{buildroot}/lib/modules/%{kver}-rt-stable%{krt}%{fcver}/build

# prune junk from kernel-devel

find %{buildroot}/usr/src/kernels -name ".*.cmd" -delete

EXCLUDES="--exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude .tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.ko.xz --exclude=*.cmd --exclude=Documentation --exclude=firmware --exclude .config.old --exclude .missing-syscalls.d"
tar $EXCLUDES -cf- . | (cd %{buildroot}/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}; tar xvf -)

%post
# Create the initramfs file
/bin/kernel-install add %{kver}-rt-stable%{krt}%{fcver} /lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%postun
/bin/kernel-install remove %{kver}-rt-stable%{krt}%{fcver} /lib/modules/%{kver}-rt-stable%{krt}%{fcver}/vmlinuz
grub2-mkconfig -o /boot/grub2/grub.cfg

%files
%defattr (-, root, root)
/lib/modules/%{kver}-rt-stable%{krt}%{fcver}
/boot/*
%ghost /boot/initramfs-%{kver}-rt-stable%{krt}%{fcver}

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{kver}-rt-stable%{krt}%{fcver}

%changelog
* Sat May 11 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.216-rt108-12
- update to 5.10.216-rt108-12 - vanilla RT kernel

* Fri Apr 19 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.215-rt107-12
- update to 5.10.215-rt107-12 - vanilla RT kernel

* Fri Mar 22 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.212-rt104-12
- update to 5.10.212-rt104-12 - vanilla RT kernel

* Mon Mar 11 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.211-rt103-12
- update to 5.10.211-rt103-12 - vanilla RT kernel

* Mon Mar 04 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.210-rt102-12
- update to 5.10.210-rt102-12 - vanilla RT kernel

* Fri Feb 23 2024 Yann Collette <ycollette.nospam@free.fr> - 5.10.209-rt101-12
- update to 5.10.209-rt101-12 - vanilla RT kernel - add ldconfig in post

* Fri Dec 22 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.204-rt100-11
- update to 5.10.204-rt100-11 - vanilla RT kernel

* Wed Nov 22 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.201-rt98-11
- update to 5.10.201-rt98-11 - vanilla RT kernel

* Sat Nov 11 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.199-rt97-11
- update to 5.10.199-rt97-11 - vanilla RT kernel

* Tue Oct 10 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.197-rt96-11
- update to 5.10.197-rt96-11 - vanilla RT kernel

* Wed Oct 04 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.194-rt95-11
- update to 5.10.194-rt95-11 - vanilla RT kernel

* Sun Sep 03 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.192-rt92-11
- update to 5.10.192-rt92-11 - vanilla RT kernel

* Thu Jul 06 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.186-rt91-11
- update to 5.10.186-rt91-11 - vanilla RT kernel

* Mon Jun 19 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.184-rt90-11
- update to 5.10.184-rt90-11 - vanilla RT kernel

* Mon Jun 19 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.180-rt89-11
- update to 5.10.180-rt89-11 - vanilla RT kernel

* Wed May 31 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.180-rt88-11
- update to 5.10.180-rt88-11 - vanilla RT kernel

* Sun Mar 26 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.176-rt86-11
- update to 5.10.176-rt86-11 - vanilla RT kernel

* Thu Mar 23 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.175-rt84-11
- update to 5.10.175-rt84-11 - vanilla RT kernel

* Sun Feb 19 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.168-rt83-11
- update to 5.10.168-rt83-11 - vanilla RT kernel

* Tue Jan 31 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.165-rt81-11
- update to 5.10.165-rt81-11 - vanilla RT kernel

* Thu Jan 26 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.162-rt79-11
- update to 5.10.162-rt79-11 - vanilla RT kernel

* Mon Jan 16 2023 Yann Collette <ycollette.nospam@free.fr> - 5.10.162-rt78-11
- update to 5.10.162-rt78-11 - vanilla RT kernel

* Fri Dec 09 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.158-rt77-11
- update to 5.10.158-rt77-11 - vanilla RT kernel

* Fri Nov 04 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.153-rt76-11
- update to 5.10.153-rt76-11 - vanilla RT kernel

* Mon Oct 31 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.152-rt75-11
- update to 5.10.152-rt75-11 - vanilla RT kernel

* Mon Sep 26 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.145-rt74-11
- update to 5.10.145-rt74-11 - vanilla RT kernel

* Sun Sep 04 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.140-rt73-11
- update to 5.10.140-rt73-11 - vanilla RT kernel

* Sat Jun 11 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.131-rt72-11
- update to 5.10.131-rt72-11 - vanilla RT kernel

* Sat Jun 11 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.120-rt70-11
- update to 5.10.120-rt70-11 - vanilla RT kernel

* Sun May 15 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.115-rt67-11
- update to 5.10.115-rt67-11 - vanilla RT kernel

* Thu Apr 07 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.109-rt65-11
- update to 5.10.109-rt65-11 - vanilla RT kernel

* Wed Mar 16 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.106-rt64-11
- update to 5.10.106-rt64-11 - vanilla RT kernel

* Fri Mar 11 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.104-rt63-11
- update to 5.10.104-rt63-11 - vanilla RT kernel

* Fri Feb 11 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.100-rt62-11
- update to 5.10.100-rt62-11 - vanilla RT kernel

* Thu Jan 06 2022 Yann Collette <ycollette.nospam@free.fr> - 5.10.90-rt60-11
- update to 5.10.90-rt60-11 - vanilla RT kernel

* Sun Dec 19 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.87-rt59-11
- update to 5.10.87-rt59-11 - vanilla RT kernel

* Thu Dec 02 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.83-rt58-11
- update to 5.10.83-rt58-11 - vanilla RT kernel

* Mon Nov 29 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.78-rt56-11
- update to 5.10.78-rt56-11 - vanilla RT kernel

* Sat Oct 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.73-rt54-11
- update to 5.10.73-rt54-11 - vanilla RT kernel

* Fri Sep 17 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.65-rt53-11
- update to 5.10.65-rt53-11 - vanilla RT kernel

* Fri Aug 27 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.59-rt52-11
- update to 5.10.59-rt52-11 - vanilla RT kernel

* Sat Aug 21 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.59-rt51-11
- update to 5.10.59-rt51-11 - vanilla RT kernel

* Mon Aug 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.56-rt49-11
- update to 5.10.56-rt49-11 - vanilla RT kernel

* Sat Aug 07 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.56-rt48-11
- update to 5.10.56-rt48-11 - vanilla RT kernel

* Fri Jul 23 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.52-rt47-11
- update to 5.10.52-rt47-11 - vanilla RT kernel

* Fri Jul 16 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.47-rt46-11
- update to 5.10.47-rt46-11 - vanilla RT kernel

* Sat Jul 03 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.47-rt45-11
- update to 5.10.47-rt45-11 - vanilla RT kernel

* Sat Jun 05 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.41-rt42-11
- update to 5.10.41-rt42-11 - vanilla RT kernel

* Wed May 12 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.35-rt39-11
- update to 5.10.35-rt39-11 - vanilla RT kernel

* Sat May 08 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.30-rt38-11
- update to 5.10.30-rt38-11 - vanilla RT kernel

* Tue Apr 20 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.30-rt37-11
- update to 5.10.30-rt37-11 - vanilla RT kernel

* Thu Apr 08 2021 Yann Collette <ycollette.nospam@free.fr> - 5.10.27-rt36-11
- update to 5.10.27-rt36-11 - vanilla RT kernel

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
