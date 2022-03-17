%define debug_package %{nil}

Summary: Tools for building live CDs
Name: livecd-tools-mao
Version: 28.3
Release: 3%{?dist}
License: GPLv2
URL: https://github.com/livecd-tools/livecd-tools

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/livecd-tools/livecd-tools/archive/refs/tags/livecd-tools-%{version}.tar.gz
Patch1: 0001-switch-from-authconfig-to-authselect.patch
Patch2: 0002-add-support-for-kernel-rt.patch

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: /usr/bin/pod2man

Requires: python3-imgcreate-mao = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: livecd-iso-to-mediums-mao = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%package -n python-imgcreate-sysdeps-mao
Summary: Common system dependencies for python-imgcreate
Requires: coreutils
Requires: xorriso >= 1.4.8
Requires: isomd5sum
Requires: parted
Requires: util-linux
Requires: dosfstools >= 2.11-8
Requires: e2fsprogs
Requires: lorax >= 18.3
Requires: rsync

# syslinux dependency
Requires: syslinux >= 6.02-4
Requires: syslinux-nonlinux >= 6.02-4

Requires: dumpet
Requires: sssd-client
Requires: cryptsetup
Requires: squashfs-tools
Requires: policycoreutils
Requires: selinux-policy-targeted
# dracut 045+ required for overlayfs live media support
Requires: dracut
Requires: dracut-live

%description -n python-imgcreate-sysdeps-mao
This package describes the common system dependencies for
python-imgcreate.

%package -n python3-imgcreate-mao
Summary: Python 3 modules for building system images
%{?python_provide:%python_provide python3-imgcreate}
Requires: python-imgcreate-sysdeps-mai%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: python3-pyparted
Requires: python3-dnf >= 1.1.0
Requires: python3-kickstart
Requires: python3-urlgrabber
Requires: libselinux-python3
Requires: python3-dbus

%description -n python3-imgcreate-mao
Python 3 modules that can be used for building images for things
like live image or appliances.

%package -n livecd-iso-to-mediums-mao
Summary: Tools for installing ISOs to different mediums
Requires: python-imgcreate-sysdeps-mao%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n livecd-iso-to-mediums-mao
Tools for installing Live CD ISOs to different mediums
(e.g. USB sticks, hard drives, PXE boot, etc.)

%prep
%autosetup -p1 -n livecd-tools-livecd-tools-%{version}

%build
# Nothing to do

%install

# Install Python 3 stuff
%make_install PYTHON=python3

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%ifnarch %{ix86} x86_64
# livecd-iso-to-mediums-mao doesn't work without syslinux
rm -rfv %{buildroot}%{_bindir}/livecd-iso-to-*
rm -rfv %{buildroot}%{_mandir}/man8/livecd-iso-to-*
%endif

%files
%license COPYING
%doc AUTHORS README HACKING
%doc config/livecd-fedora-minimal.ks
%doc config/livecd-mageia-minimal-*.ks
%{_mandir}/man*/*
%exclude %{_mandir}/man8/livecd-iso-to-disk.8*
%{_bindir}/livecd-creator
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/editliveos
%{_bindir}/mkbiarch
%{_datadir}/doc/livecd-tools/*

%files -n python-imgcreate-sysdeps-mao
# No files because empty metapackage

%files -n python3-imgcreate-mao
%license COPYING
%doc API
%{python3_sitelib}/imgcreate

%files -n livecd-iso-to-mediums-mao
%license COPYING
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_mandir}/man8/livecd-iso-to-disk.8*

%changelog
* Mon Aug 23 2021 Pavel Březina <pbrezina@redhat.com> - 1:28.3-3
- Switch from authconfig to authselect (rhbz#1982159)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Neal Gompa <ngompa13@gmail.com> - 1:28.3-1
- Release 28.3 (ngompa13)
- imgcreate/live: Make EFI packages optional for x86 (ngompa13)
- Fix missync of locations of efiboot.img (m.novosyolov)
- mkdir isolinux on aarch64 (m.novosyolov)
- Fix check if EFI bootloader exists (m.novosyolov)

* Sat Jun 26 2021 Neal Gompa <ngompa13@gmail.com> - 1:28.2-1
- Release 28.2 (ngompa13)
- rearrange xorrisofs options to make image efi bootable (sobjerke)
- place efiboot.img and macboot.img in /isolinux (sobjerke)
- Remove duplicate sentence (35056002+BessieTheCookie)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:28.1-2
- Rebuilt for Python 3.10

* Fri May 21 2021 Neal Gompa <ngompa13@gmail.com> - 1:28.1-1
- Release 28.1 (ngompa13)
- imgcreate/live: Add missing comma for xorrisofs options (ngompa13)
- prevent urlgrabber.urlgrab() from overwriting ks files in current directory (sobjerke)

* Sat May 08 2021 Neal Gompa <ngompa13@gmail.com> - 1:28.0-2
- Add missing dependencies (urlgrabber, dracut-live)
- Remove hfsplus-tools as a dependency for EL8+

* Sat May 08 2021 Neal Gompa <ngompa13@gmail.com> - 1:28.0-1
- Release 28.0 (ngompa13)
- HACKING: Fix URL for the Git repository (ngompa13)
- imgcreate/live: Add missing variable "_isDracut" (ngompa13)
- imgcreate/live: Use the right EFI binaries for x86 images (ngompa13)
- imgcreate/live: Add AArch64 support (ngompa13)
- imgcreate/live: Rework ISO creation to split x86 specific parts out (ngompa13)
- Add missing files to uninstall section of makefile (quanterium)
- Separate the errors for no ks specified and file not found (bcotton)
- Pass package_types to dnf base group_install as tuple, not set (awilliam)
- imgcreate: Allow more SquashFS compression options. (fgrose)
- BindChrootMount: Expand this class to include bind mounting of files. (fgrose)
- Obsolete osmin.img processing. (fgrose)
- live.py: harmonize xorrisofs arguments with lorax live/x86.tmpl (fgrose)
- imgcreate/kickstart: Use urlgrabber again instead of urllib (ngompa13)
- Make --livedir & --multi handling more robust. (fgrose)
- editliveos: Use USERNAME now instead of LOGNAME. (fgrose)
- livecd-iso-to-disk: Update test for 'gio' presence. (fgrose)
- live.py: Store EFI boot images in /images/. (fgrose)
- livecd-iso-to-disk: Use -E, --exit-if-exists option to udevadm settle. (fgrose)
- live.py: Update xorrisofs_options for x86 images. (fgrose)
- editliveos: Rework installing packages into image (khoidinhtrinh)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:27.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Adam Williamson <awilliam@redhat.com> - 1:27.1-8
- Backport PR #168 to fix a compatibility issue with DNF 4.4.0+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:27.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:27.1-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:27.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:27.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:27.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Neal Gompa <ngompa13@gmail.com> - 1:27.1-1
- Bump version to 27.1 (ngompa13)
- Fix Kernel version detection (pablo)

* Sun Apr 14 2019 Neal Gompa <ngompa13@gmail.com> - 1:27.0-1
- Bump version to 27.0 (ngompa13)
- imgcreate/creator: Change to text strings for reading file list from rpm
  (ngompa13)
- imgcreate/live: Check for dracut being installed to determine usability
  (ngompa13)
- imgcreate/live: Add squashfs as a mandatory extra filesystem (ngompa13)
- imgcreate/live: Rename dracut config file to 99-liveos.conf (ngompa13)
- 'udevadm settle' needs some time to settle (sbonds)
- README: Removed unnecessary 'the' (scwicker)
- imgcreate/kickstart: Use systemctl for enabling/disabling services (ngompa13)
- livecd-iso-to-disk: Simply mount read-only to test for flat_squashfs.
  (fgrose)
- editliveos: Accommodate netinstall in multi boot configuration files.
  (fgrose)
- livecd-iso-to-disk+pod: Support netinstall .isos and as multi install.
  (fgrose)

* Fri Apr 12 2019 Neal Gompa <ngompa13@gmail.com> - 1:26.1-4
- Add patch to adapt to rpm Python bindings changing from bytes to strings (RH#1699432)

* Thu Apr 04 2019 Neal Gompa <ngompa13@gmail.com> - 1:26.1-3
- Backport fix from upstream to use systemctl instead of chkconfig (RH#1696064)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Neal Gompa <ngompa13@gmail.com> - 1:26.1-1
- Bump version to 26.1 (ngompa13)
- Run setfiles after chroot (noto.kazufumi)
- imgcreate/dnfinst: Force latest packages from only specified repos (ngompa13)

* Sat Nov 24 2018 Neal Gompa <ngompa13@gmail.com> - 1:26.0-3
- Backport fix from upstream to ensure latest versions install
- Fix extlinux dependency for EL7

* Fri Nov 23 2018 Neal Gompa <ngompa13@gmail.com> - 1:26.0-2
- Fix Obsoletes of python2-imgcreate from <F29 for F30+

* Fri Nov 23 2018 Neal Gompa <ngompa13@gmail.com> - 1:26.0-1
- Bump version to 26.0 (ngompa13)
- imgcreate/kickstart: Exclude /sys from SELinux labeling (ngompa13)
- imgcreate/live: Switch to single-step ISO hybridization by xorrisofs
  (ngompa13)
- Use xorrisofs instead of genisoimage (ngompa13)
- imgcreate/live: Drop UDF support (ngompa13)
- Fix excludeWeakdeps for older pykickstart versions (pablo)
- README: Update to include --flat-squashfs option. (fgrose)
- editliveos: Fix inconsistent ops argument. (fgrose)
- livecd-iso-to-disk: Accept both dracut 045-8 and 049+ for OverlayFS. (fgrose)
- README: Update to include liveimage-mount & editliveos tools. (fgrose)
- config/livecd-fedora-minimal.ks:  Increase root partition size. (fgrose)
- Support a flattened squashfs.img & non-standard image & overlay paths.
  (fgrose)
- livecd-iso-to-disk: Support netinstall .iso (fgrose)
- edit-livecd: Delete unmaintained script superceded by editliveos. (fgrose)
- Handle dnf config option showing as tuple, not list, in DNF 3.6 (awilliam)
- live.py: Fix unreported logging.error (fgrose)
- livecd-iso-to-disk: Skip Multi Image query on --skipcopy condition. (fgrose)
- livecd-iso-to-disk: Tighten permissions on some files. (fgrose)
- DNF 3: workaround a bug with config values that are lists (awilliam)
- Add support for RISC-V (riscv64) (david.abdurachmanov)
- Revert "Use restorecon instead of setfiles for relabeling" (puiterwijk)
- imgcreate: Copy gcdia32.efi in __copy_efi_files if it exists (Kevin)
- Fix the io.open() and utf-8 problems in imgcreate/util.py (david.l.cantrell)
- Remove get_modules(). (david.l.cantrell)
- livecd-iso-to-disk: adjust efi boot configuration code. (fgrose)
- fs.py & editliveos: remove code glitches (fgrose)
- editliveos: Bind mount /etc/resolv.conf (fgrose)
- fs.py & editliveos: Fix overlay changing. (fgrose)
- util.py: Captured output from subprocesses should always be decoded. (scott)
- Update livecd-creator manpage with info about imcomplete options
  (zhang.xianwei8)
- livecd-iso-to-disk: Revert change that broke EFI/MBR hybrid booting (scott)
- livecd-iso-to-disk: Fix faulty --efi boot config code. (fgrose)
- livecd-iso-to-disk: Fix overlay size reporting & type testing. (fgrose)
- livecd-iso-to-disk: Accommodate multiple BOOT*.EFI files. (fgrose)

* Thu Nov 22 2018 Neal Gompa <ngompa13@gmail.com> - 1:25.0-14
- Backport workaround for lack of excludeWeakDeps with EL7 pykickstart

* Thu Nov 15 2018 Neal Gompa <ngompa13@gmail.com> - 1:25.0-13
- Fix when Python 2 subpackage is obsoleted
- Fix up EL7 support

* Tue Nov 13 2018 Neal Gompa <ngompa13@gmail.com> - 1:25.0-12
- Drop Python 2 subpackage for F30+/RHEL8+

* Wed Sep 26 2018 Adam Williamson <awilliam@redhat.com> - 1:25.0-11
- Backport further fix for #1595917

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:25.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1:25.0-9
- Rebuilt for Python 3.7

* Wed Jun 27 2018 Adam Williamson <awilliam@redhat.com> - 1:25.0-8
- Work around a DNF 3 bug that breaks repo setup (#1595917)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:25.0-7
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 1:25.0-6
- Revert patch to use restorecon due to unloaded selinux policy

* Thu Mar 22 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 1:25.0-5
- Require selinux-policy-targeted in imgcreate-sysdeps

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:25.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:25.0-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 1:25.0-2
- Backport patch to fix appliance-creator

* Sat Oct 21 2017 Neal Gompa <ngompa13@gmail.com> - 25.0-1
- Bump version to 25.0 (ngompa13)
- Set the correct partition size for minimal Mageia kickstarts (ngompa13)
- editliveos: A full featured replacement for tools/edit-livecd. (fgrose)
- fs.py: Add functions and classes to support Live Image Mounting. (fgrose)
- creator.py, live.py: Allow more options to be passed to functions. (fgrose)
- debug.py: Add support for argparse parser. (fgrose)
- fs.py: Allow more options to be passed to functions. (fgrose)
- util.py: Add a subprocess call that returns standard values. (fgrose)
- Remove absolute directories on external program call paths. (fgrose)
- livecd-iso-to-disk: Allow auto --multi install. (fgrose)
- Fix ARM architecture check (ngompa13)
- Declare the literal "kernel-" as a byte array to fix crash (ngompa13)
- livecd-iso-to-disk: Fix boot configuration for images lacking /EFI (fgrose)
- livecd-iso-to-disk: Fix space evaluation for images lacking /EFI (fgrose)
- Use restorecon instead of setfiles for relabeling (scott)
- liveimage-mount: Add support for OverlayFS overlays. (fgrose)
- livecd-iso-to-disk+pod:  Enable a --copy-overlay option. (fgrose)
- livecd-iso-to-disk+pod:  Enable a --copy-home option. (fgrose)
- livecd-iso-to-disk+pod: Add --overlayfs option for overlay. (fgrose)
- livecd-iso-to-disk+pod: Allow multi installs to live booted devices (fgrose)
- livecd-iso-to-disk: Fix sed for kernelargs. (fgrose)
- livecd-iso-to-disk: Adjust syslinux default menu style, as needed. (fgrose)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Neal Gompa <ngompa13@gmail.com> - 24.4-1
- Bump version to 24.4 (ngompa13)
- livecd-iso-to-disk: Fix freespace determination for DVD installer. (fgrose)
- livecd-iso-to-disk: Fix labeling of target device filesystem. (fgrose)
- Switch the default filesystem to ext4 (ngompa13)

* Wed Apr 12 2017 Neal Gompa <ngompa13@gmail.com> - 24.3-2
- Include missing sample kickstarts

* Wed Apr 12 2017 Neal Gompa <ngompa13@gmail.com> - 24.3-1
- Bump version to 24.3 (ngompa13)
- livecd-iso-to-disk: Fix --efi --format code sequence problems. (fgrose)
- livecd-iso-to-disk+pod: Add options for automatic boot. (fgrose)
- livecd-iso-to-disk+pod: Add --no-overlay & --reset-overlay options. (fgrose)
- livecd-iso-to-disk: Remove checkLVM() as it seems unnecessary now. (fgrose)
- livecd-iso-to-disk & liveimage-mount: Multi Live Image Boot fixes. (fgrose)
- Update minimal Fedora kickstart to use sha512 auth algorithm (ngompa13)
- Add minimal Mageia kickstarts to serve as examples (ngompa13)
- Use genisoimage instead of mkisofs (ngompa13)

* Tue Mar 07 2017 Neal Gompa <ngompa13@gmail.com> - 24.2-1
- Bump version to 24.2 (ngompa13)
- livecd-iso-to-disk+pod: Code cleanups & modernization. (fgrose)
- livecd-iso-to-disk: Update partition handling (fgrose)
- livecd-iso-to-disk: Replace unneeded uses of awk. (fgrose)
- livecd-iso-to-disk+pod: Multi Live Image boot configuration (fgrose)

* Tue Feb 28 2017 Neal Gompa <ngompa13@gmail.com> - 24.1-1
- Fix livecd-iso-to-disk pod text (ngompa13)
- Bump version to 24.1 (ngompa13)
- Add more primary authors (ngompa13)
- liveimage-mount: Add an exception class to allow standalone use. (fgrose)
- liveimage-mount: Support multiple concurrent invocations. (fgrose)
- liveimage-mount: Extend mount-hacks & overlay options. (fgrose)
- liveimage-mount: Support encrypted home filesystems. (fgrose)
- liveimage-mount: Add a read-only option for mounting. (fgrose)
- liveimage-mount: Add an unmount mode. (fgrose)
- liveimage-mount: Don't bypass udev in dmsetup. (fgrose)
- livecd-iso-to-disk: Restructure filesystem label handling (fgrose)
- livecd-iso-to-disk+pod: Fix missing/outdated boot configurations (fgrose)
- livecd-iso-to-disk: Cleanup sed statements (fgrose)
- Disable 64bit feature in mke2fs for syslinux>=6.03 (yturgema)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Neal Gompa <ngompa13@gmail.com> - 24.0-3
- Move system dependencies for livecd-tools to python-imgcreate-sysdeps (#1409536)
- Ensure pythonX-imgcreate depend on python-imgcreate-sysdeps (#1409536)

* Wed Dec 21 2016 Kevin Fenzi <kevin@scrye.com> - 24.0-2
- Rebuild for Python 3.6

* Tue Dec 06 2016 Brian C. Lane <bcl@redhat.com> - 24.0-1
- Remove unused tmpdir parameter in resize2fs(). (fgrose)
- HACKING: Fix mailing list address (ngompa13)
- README: Fix the mailing list reference (ngompa13)
- Check if FirewallD is installed before running ks firewall commands (ngompa13)
- Merge pull request #6 from Conan-Kudo/yumtodbo (kevin.kofler)
- Fixup and update the README (ngompa13)
- Yum -> DNF; ayum -> dbo (ngompa13)
- Properly exclude packages from the install set (ngompa13)
- Merge pull request #3 from Conan-Kudo/warningfix (kevin.kofler)
- logging.warn -> logging.warning (ngompa13)
- Delete any leftover (Kevin)
- Fix error handling in creator.py (Kevin)
- Merge pull request #2 from Conan-Kudo/fixmakefile (kevin.kofler)
- Fix command for creating symlink in Makefile (ngompa13)
- Fix command for getting Python directory in the Makefile (ngompa13)
- Merge pull request #1 from Conan-Kudo/futurize (kevin.kofler)
- Bump version to 24.0 (ngompa13)
- Fix up README (ngompa13)
- More conversion of strings to bytestrings (ngompa13)
- Convert bytestring to string (ngompa13)
- Replace deprecated string.join() with str.join (ngompa13)
- Fix division to be unambiguous (ngompa13)
- Purge all Python < 2.6 exception handling code (ngompa13)
- 'msg' should be 'message' for CreatorError exceptions (ngompa13)
- More string to bytestring conversions (ngompa13)
- Convert string to bytestring (ngompa13)
- Convert result sliced from bytestring into string (ngompa13)
- More declaring bytestrings as bytestrings (ngompa13)
- Replace file() with open() (ngompa13)
- use six module for urllib import (ngompa13)
- Mark byte being written as byte (ngompa13)
- Prepend file:// for local paths that don't have it already (ngompa13)
- Remove unused import for system-config-keyboard (ngompa13)
- Migrate from urlgrabber to urllib for Python 2/3 compatibility (ngompa13)
- Makefile fixes for setting which Python to use (ngompa13)
- Add support for setting Python interpreter to be used (ngompa13)
- Port to Python 2.6+, 3.3+ (ngompa13)
- Port from yum to dnf. (Kevin)
- Add imgcreate/.gitignore (Kevin)
- Disambiguation (PeteLawler)

* Fri Aug 26 2016 Brian C. Lane <bcl@redhat.com> - 23.4-1
- Version 23.4 (bcl)
- yuminst.LiveCDYum.runInstall: import yum.Errors (sandro.bonazzola)
- Wrap all parted calls in LC_ALL=C (#1350253) (bcl)
- Fix calling livecd-iso-to-pxeboot with a full path (cadegenn)
- Stop truncating /etc/resolv.conf in SELinux module -- fixes #31 (torrancew)
- litp: Copy ldlinux.c32 to tftpboot for PXE live setup. (bcl)
- Always use rsync to copy Packages (#1343645) (bcl)
- Fix extended regular expression [0-9] (fgrose)
- Enable loop device as installation target (fgrose)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:23.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 05 2016 Brian C. Lane <bcl@redhat.com> 23.3-1
- Version 23.3 (bcl)
- litd: add the "rw" argument even if there's no "ro" (#1318470) (lkundrak)
- Remove everything but LiveOS/ from appended ISO (lzap+git)
- support aarch64 (jef199006)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Brian C. Lane <bcl@redhat.com> 23.2-3
- Actually add the source file

* Thu Oct 15 2015 Brian C. Lane <bcl@redhat.com> 23.2-2
- Version 23.2 (bcl)
- Use add_drivers for dracut config (#1192030) (bcl)
- litd: Don't add inst.stage2 to cmdline (bcl)
- livecd-iso-to-disk: partnum should only be a digit (#1136586) (bcl)
- Handle devices ending in a digit (#1136586) (bcl)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Brian C. Lane <bcl@redhat.com> 23.1-1
- Version 23.1 (bcl)
- litd: All parted calls should use -s mode (#1195478) (bcl)
- litd: Make sure device nodes have time to appear (bcl)
- Sync usage documentation with livecd-iso-to-disk.pod (fgrose)
- Correct misinformation and cover new options (fgrose)
- Update repo urls to point to new github location (#1208825) (bcl)
- Explicitly add the uas driver to the initrd (#1201983) (bcl)
- Update repo urls to point to new github location.

* Mon Mar 02 2015 Brian C. Lane <bcl@redhat.com> 23.0-1
- Version 23.0 (bcl)
- kickstart: Handle resolv.conf being a nonexistent symlink (walters)
- Report Kickstart errors without traceback (#1168030) (bcl)
- Change console font to eurlatgr (myllynen)
- litd: Add missing syslinux modules (#1192137) (bcl)
- Note lz4 compression in help (bruno)

* Thu Feb 26 2015 Dennis Gilmore <dennis@ausil.us> - 21.4-2
- Require python-kickstart since it has teh python2 version of pykickstart

* Mon Oct 27 2014 Brian C. Lane <bcl@redhat.com> 21.4-1
- Version 21.4 (bcl)
- Ignore case when looking for UEFI boot*efi file (#1156380) (bcl)
- Preload the libnss_sss library (#1127103) (bcl)

* Mon Oct 20 2014 Brian C. Lane <bcl@redhat.com> 21.3-1
- Version 21.3 (bcl)
- mkefiboot now expects all upper case for BOOT*.EFI (#1154138) (bcl)
- Move __fstype into ImageCreator class (bcl)
- Catch Yum errors and print them (#1119906) (bcl)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Brian C. Lane <bcl@redhat.com> 21.2-1
- Version 21.2 (bcl)
- Abort livecd creation if selinux relabel fails (#1121301) (bcl)
- Add lorax ppc config files to search path (bcl)
- Use inst.repo and inst.stage2 (bcl)
- Use rd.live.overlay instead of overlay (bcl)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Brian C. Lane <bcl@redhat.com> 21.1-1
- Version 21.1 (bcl)
- Update live.py for syslinux 6.02-4 (bcl)

* Wed Mar 26 2014 Brian C. Lane <bcl@redhat.com> 21.0-1
- Version 21.0 (bcl)
- Update kickstart.py for new kickstart (bcl)
- Update yuminst for new pykickstart (bcl)
- Cleanup paths in README (bcl)
- livecd-creator: Make sure kickstart file exists (#1074295) (bcl)

* Fri Jan 31 2014 Brian C. Lane <bcl@redhat.com> 20.4-1
- Version 20.4 (bcl)
- Fix extlinux check (#1059278) (bcl)
- Check kickstart for repo line (#1005580) (bcl)
- Catch CreatorError during class init (#1005580) (bcl)
- Add docleanup to edit-livecd (#1000744) (bcl)
- utf8 decode unicode error strings (#1035248) (bcl)
- Remove switch to Permissive (#1051523) (bcl)

* Tue Jan 07 2014 Brian C. Lane <bcl@redhat.com> 20.3-1
- Version 20.3 (bcl)
- Add missing quote (#1044675) (bcl)

* Tue Jan 07 2014 Brian C. Lane <bcl@redhat.com> 20.2-1
- Version 20.2 (bcl)
- Use LC_ALL=C for parted calls (#1045854) (bcl)
- Fix to work with the changed yum.config._getsysver (bruno)
- Add check for extlinux tools (#881317) (bcl)
- Cleanup arg parsing a bit (#725047) (bcl)

* Mon Nov 18 2013 Brian C. Lane <bcl@redhat.com> 20.1-1
- add 'troubleshooting' submenu with 'basic graphics mode' to UEFI boot menu (awilliam)
- make UEFI boot menu resemble the BIOS and non-live boot menus more (awilliam)
- drop 'xdriver=vesa' from basic graphics mode parameters (per ajax) (awilliam)
- Ensure filesystem modules end up in the live image initramfs. (notting)
- Don't use mkfs.extN options for any filesystem types. (notting)
- litd: Add --label option to override LIVE label (helio)
- liveimage-mount: add missing import (bcl)
- Change vfat limit from 2047 to 4095 (#995552) (bcl)

* Wed Aug 07 2013 Brian C. Lane <bcl@redhat.com> 20.0-1
- Version 20.0 (bcl)
- Install docs in unversioned doc directory (#992144) (bochecha)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Brian C. Lane <bcl@redhat.com> 19.6-1
- Version 19.6 (bcl)
- litd: Add kickstart option (bcl)
- ts.check output is a list of tuples (#979759) (bcl)
- Add repo --noverifyssl support (#907707) (bcl)

* Mon Jun 17 2013 Brian C. Lane <bcl@redhat.com> 19.5-1
- Version 19.5 (bcl)
- Write vconsole.conf directly (bcl)
- litd: Add --updates option (bcl)

* Fri May 31 2013 Brian C. Lane <bcl@redhat.com> 19.4-1
- Version 19.4 (bcl)
- Replace bash string parsing with awk (#962039,#969521) (bcl)
- Fix default.target symlink (#968272) (bcl)

* Wed May 29 2013 Brian C. Lane <bcl@redhat.com> 19.3-2
- Add requirement on rsync (#967948)

* Thu May 23 2013 Brian C. Lane <bcl@redhat.com> 19.3-1
- Version 19.3 (bcl)
- Avoid setting empty root password (#964299) (thoger)
  CVE-2013-2069
- Handle urlgrabber callback changes (#963645) (bcl)

* Wed May 08 2013 Dennis Gilmore <dennis@ausil.us> 19.2-2
- only require hfsplus-tools on ppc and x86 arches

* Wed Apr 03 2013 Brian C. Lane <bcl@redhat.com> 19.2-1
- Version 19.2 (bcl)
- Use parted to check for GPT disklabel (#947653) (bcl)
- Output details of dep check failure (bcl)
- Properly generate kernel stanzas (#928093) (bcl)

* Sat Mar 16 2013 Brian C. Lane <bcl@redhat.com> 19.1-1
- Version 19.1 (bcl)
- iso9660 module is named isofs (bcl)
- disable dracut hostonly and rescue image (#921422) (bcl)

* Fri Mar 08 2013 Brian C. Lane <bcl@redhat.com> 19.0-1
- Version 19.0 (bcl)
- iso9660 is now a module, include it (bcl)
- correctly check for selinux state (#896610) (bcl)
- Simplify kickstart example (#903378) (bcl)
- default to symlink for /etc/localtime (#885246) (bcl)

* Sat Feb 23 2013 Bruno Wolff III <bruno@wolff.to> 18.14-2
- Get an up to date build in rawhide, since the mass 
- rebuild used a master branch that was behind the f18 
- branch and builds from f18 are no longer inherited.

- Version 18.14 (bcl)
- add --verifyudev to dmsetup (#885385) (bcl)

- Version 18.13 (bcl)
- silence the selinux umount error (bcl)
- use systemd instead of inittab for startx (bcl)
- set selinux permissive mode when building (bcl)
- fix kickstart logging entry (bcl)
- write hostname to /etc/hostname (#870805) (bcl)
- add nocontexts for selinux (#858373) (bcl)
- remove lokkit usage (bcl)
- use locale.conf not sysconfig/i18n (#870805) (bcl)
- don't write clock (#870805) (bcl)
- add remainder of virtio modules to initrd (#864012) (bcl)

- Require hfsplus-tools so that images will boot on Mac

- Version 18.12 (bcl)
- Remove grub 0.97 splash (bcl)

- Version 18.11 (bcl)
- not copying UEFI files shouldn't be fatal (#856893) (bcl)
- don't require shim and grub2-efi (#856893) (bcl)

- efi_requires.patch: don't force grub2-efi and shim into the package
  list, it breaks 32-bit compose and isn't needed, we have it in comps

- Version 18.10 (bcl)
- use cp -r instead of -a (bcl)

- Version 18.9 (bcl)
- fix extra-kernel-args (#853570) (bcl)
- New location for GRUB2 config on UEFI (#851220) (bcl)
- Add nocleanup option to retain temp files (bcl)
- Update imgcreate for UEFI Secure Boot (bcl)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:18.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Brian C. Lane <bcl@redhat.com> 18.8-1
- Version 18.8 (bcl)
- dracut needs to load vfat and msdos filesystems (bcl)

* Thu Aug 02 2012 Brian C. Lane <bcl@redhat.com> 18.7-1
- Version 18.7 (bcl)
- Recognize rd.live.image as well as liveimg in sed scripts of livecd-iso-to-
  disk & edit-livecd (fgrose)
- fix /etc/localtime file vs. symlink (#829032) (bcl)

* Tue Jul 31 2012 Brian C. Lane <bcl@redhat.com> 18.6-1
- Version 18.6 (bcl)
- switch to using rd.live.image instead of liveimg (bcl)
- dracut doesn't need explicit filesystems (bcl)
- livecd-creator: Add --cacheonly for offline use (martin)
- Implement cacheonly (offline) support in ImageCreator and LoopCreator (martin)
- if mounting squashfs add ro mount option (jboggs)
- imgcreate: Use copy2 for TimezoneConfig (#829032) (bcl)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:18.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Brian C. Lane <bcl@redhat.com> 18.5-1
- Version 18.5 (bcl)
- Include Mac volume name graphic (mjg)
- copy repo data to USB for F17 (#806166) (bcl)
- Version 18.4 (bcl)
- allow for use of yum plugins during livecd creation (notting)
- Capitalise EFI names (mjg)
- Add tighter Mac boot image integration (mjg)
- fix quoting with basename and SRC (#814174) (bcl)
- check for LIVE-REPO partition when writing DVD (#813905) (bcl)

* Mon Apr 16 2012 Brian C. Lane <bcl@redhat.com> 18.3-1
- Version 18.3 (bcl)
- add support for cost in kickstart repo line (#735079) (mads)
- skip copying DVD image file with skipcopy option (786037) (bcl)
- remove kernel and initrd from EFI/BOOT (#811438) (bcl)
- fix syntax problem in detectsrctype (bcl)

* Thu Mar 01 2012 Brian C. Lane <bcl@redhat.com> - 18.2-1
- Version 18.2 (bcl)
- livecd-iso-to-disk: Add 2MB slop to calculation (bcl)
- Change EFI/boot to EFI/BOOT (mjg)
- Add support for generating EFI-bootable hybrid images (mjg)

* Thu Feb 23 2012 Brian C. Lane <bcl@redhat.com> - 18.1-1
- Version 18.1 (bcl)
- livecd-iso-to-disk: create partition for iso (bcl)

* Wed Feb 15 2012 Brian C. Lane <bcl@redhat.com> - 18.0-1
- Version 18.0 (bcl)
- check for valid script path before editing livecd image and update usage
  options confusion (jboggs)
- imgcreate: fix typo in ResizeError (bcl)
- add missing selinux_mountpoint class object to edit-livecd (jboggs)

* Wed Jan 18 2012 Brian C. Lane <bcl@redhat.com> - 17.4-1
- Version 17.4 (bcl)
- selinux may be off on the host, skip mount (#737064) (bcl)
- Set base_persistdir (#741614) (bcl)
- Fix the fix for dracut modules (#766955) (bcl)
- Use dracut.conf.d instead fo dracut.conf (bcl)
- dracut needs dmsquash-live explicitly included (bcl)
- edit-livecd: -k --kickstart option (apevec)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Brian C. Lane <bcl@redhat.com> 17.3-1
- Version 17.3 (bcl)
- python-imgcreate: remove -f from second lokkit call (#769457) (bcl)
- Install edit-livecd to /usr/bin (bcl)

* Thu Nov 03 2011 Brian C. Lane <bcl@redhat.com> 17.2-1
- Version 17.2 (bcl)
- Fix indent and typo in liveimage-mount (#749643) (bcl)
- Make sure the target is labeled LIVE (#751213) (bcl)
- Only check first match for boot flag (#739411) (bcl)
- Stop creating backup image before resizing (#737243) (bcl)

* Thu Sep 01 2011 Brian C. Lane <bcl@redhat.com> 17.1-1
- Version 17.1 (bcl)
- Add title and product args (#669120) (bcl)
- Skip bind mounts when source isn't there (bcl)
- Add new syslinux.cfg template (#734173) (bcl)
- Use copyFile on the iso (bcl)
- Use rsync to copy if available (bcl)

* Thu Aug 11 2011 Brian C. Lane <bcl@redhat.com> 17.0-1
- Version 17.0
- Quote $SRC so iso's with spaces will work (#694915) (bruno)
- Handle move to /sys/fs/selinux (#728576) (dwalsh)
- master is now v17.X (bcl)
- Turn on the legacy_boot flag for EFI (#680563) (bcl)
- Don't ask about replacing MBR when formatting (bcl)
- Make MBR replacement message more clear (bcl)
- Ensure previous filesystems are wiped when formatting (#712553) (bcl)
- Modify pxeboot script to work with F16 (bcl)
- Add initial support for ARM architectures (martin.langhoff)
- Copy updates and product image files (bcl)

* Thu Mar 31 2011 Brian C. Lane <bcl@redhat.com> 16.3-1
- Version 16.3 (bcl)
- Copy old initrd/xen files to isolinux when using base-on (#690940) (bcl)
- Don't fail on missing splash image (bcl)
- Images go into $SYSLINUXPATH (bcl)
- fix typo (bcl)
- Check for spaces in fs label when using overlay (#597599) (bcl)
- Fix logic for syslinux check (bcl)
- Fix image-creator symlink so that it is relative (bcl)
- symlink /etc/mtab to /proc/self/mounts (#688277) (bcl)
- liveimage-mount installed LiveOS with overlay (fgrose)
- Fix overzealous boot->BOOT change (bcl)
- Fix return code failure (#689360) (fgrose)
- Fix pipefailure in checkSyslinuxVersion (#689329) (fgrose)
- Symlink image-creator instead of hardlink (#689167) (bcl)
- Add extracting BOOTX64.efi from iso (#688258) (bcl)
- Add repo to DVD EFI install config file (#688258) (bcl)
- Add EFI support to netboot (#688258) (bcl)
- Support /EFI/BOOT or /EFI/boot (#688258) (bcl)

* Mon Mar 14 2011 Brian C. Lane <bcl@redhat.com> 16.2-1
- Version 16.2 (bcl)
- livecd-iso-to-disk: Catch all failures (lkundrak)
- Mailing list address changed (lkundrak)
- Fall back to to msdos format if no extlinux (bcl)
- Create an ext4 filesystem by default for home.img (fgrose)
- Add error checks to home.img creation (bcl)
- livecd-iso-to-disk Detect more disk space issues (fgrose)
- gptmbr can be written directly to the mbr (bcl)
- Fixup livedir support (#679023) (jan.kratochvil)

* Fri Feb 18 2011 Brian C. Lane <bcl@redhat.com> 16.1-1
- Version 16.1 (bcl)
- Print reason for sudden exit (bcl)
- Fix skipcopy usage with DVD iso (#644194) (bmj001)
- Move selinux relabel to after %%post (#648591) (bcl)
- Add support for virtio disks to livecd (#672936) (bcl)
- Support attached LiveOS devices as well as image files for LiveOS editing.
  (fgrose)
- Check return value on udevadm (#637258) (bcl)

* Tue Feb 15 2011 Brian C. Lane <bcl@redhat.com> 16.0-1
- Version 16.0 (bcl)
- Add tmpdir to LiveImageCreator (bcl)
- Source may be a file or a block device, mount accordingly (bcl)
- Enable reading of SquashFS compression type. (fgrose)
- Enable cloning of a running LiveOS image into a fresh iso. (fgrose)
- Update usage documentation & add it to the script (fgrose)
- Support the propagation of an installed Live image (fgrose)
- Rename image source- and target-related variables (fgrose)
- Align start of partition at 1MiB (#668967) (bcl)
- Pass tmpdir to ImageCreator class initializer (#476676) (bcl)
- Add tmpdir to ImageCreator class initializer (#476676) (bcl)
- Enable an optional tmpdir for e2image in fs.resize2fs() (fgrose)
- Bad karma commit reverted; The option to boot from a local drive *MUST* exist
  as 99.9% of our consumers have default desktop hardware configurations.
  (jeroen.van.meeuwen)
- Really switch the default compression type, not just the default cli option
  value (jeroen.van.meeuwen)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Brian C. Lane <bcl@redhat.com> - 15.3-1
- Version 15.3 (bcl)
- Remove boot from local drive option (bcl)
- Check for one big initrd.img (#671900) (bcl)
- Make xz the default compression type for live images. (bruno)
- Update documentation for xz availability. (bruno)
- Change releasever to a command line option (#667474) (bcl)

* Tue Jan 04 2011 Dennis Gilmore <dennis@ausil.us> - 15.2-2
- patch to drop support of releasever in urls it destroys image creation in koji

* Wed Dec 22 2010 Brian C. Lane <bcl@redhat.com> - 15.2-1
- Version 5.2 (bcl)
- Assign a device-mapper UUID w/ subsystem prefix to the dm snapshot. (dlehman)
- Fix git URLs to match reality. (dlehman)
- Trap copyFile errors (#663849) (fgrose)
- Fix incomplete rename of freespace variable (#656154) (fgrose)

* Tue Nov 30 2010 Brian C. Lane <bcl@redhat.com> - 15.1-1
- Bump version to 15.1 (bcl)
- Wrap subprocess.call() so we can capture all command output for debugging.
  (jlaska)
- Work with the logging settings when emitting progress. (jlaska)
- Add a quiet option to surpress stdout. Adjust handle_logfile to not surpress
  stdout. (jlaska)
- Fix partition number selection for MMC bus devices (#587411) (fgrose)
- Fix disk space estimation errors (#656154) (fgrose)
- Tolerate empty transactions (lkundrak)
- Merge livecd-creator and image-creator (lkundrak)
- Cleanup if/then blocks (#652522) (fgrose)

* Mon Nov 15 2010 Brian C. Lane <bcl@redhat.com> - 15.0-1
- Each branch needs a different version number.

* Mon Nov 15 2010 Brian C. Lane <bcl@redhat.com> - 0.3.6-1
- Bump version to 0.3.6 (bcl)
- Misc. fixups (#652522) (fgrose)
- Set indentation to 4 spaces (#652522) (fgrose)
- Add a release target (bcl)
- Pass dracut args during check (#589778) (bcl)
- Update dracut args (#652484) (bcl)
- Cleanup tabs (#652522) (fgrose)
- Cleanup EOL spaces (#652522) (fgrose)
- Typo. Need space before ]. (bruno)
- Add support for timeout and totaltimeout to livecd-iso-to-disk (#531566)
  (bcl)
- Add proxy support to livecd-creator (#649546) (bcl)

* Mon Nov 01 2010 Brian C. Lane <bcl@redhat.com> - 0.3.5-1
- Converting version number to NVR
- Removed patches (now included in v0.3.5)

* Sun Sep 26 2010 Bruno Wolff III <bruno@wolff.to> - 034-11
- Fix live image relabel when compose host has selinux disabled.

* Tue Sep 21 2010 Bruno Wolff III <bruno@wolff.to> - 034-10
- Document the lzo compressor.

* Thu Sep 16 2010 Bruno Wolff III <bruno@wolff.to> - 034-9
- Change requires to /sbin/extlinux since that will work with old and new
  versions of syslinux.

* Thu Sep 16 2010 Bruno Wolff III <bruno@wolff.to> - 034-8
- extlinux is now in a subpackage that is required by livecd-iso-to-disk

* Tue Sep 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 034-7
- fix background image copying to use new-new logo path

* Tue Sep 14 2010 Bruno Wolff III <bruno@wolff.to> - 034-6
- One /dev/loop* change had been missed. Backport patch.

* Mon Sep 13 2010 Bruno Wolff III <bruno@wolff.to> - 034-5
- Backport basic video menu label fix

* Mon Sep 13 2010 Bruno Wolff III <bruno@wolff.to> - 034-4
- Backport missing parts of the regex fix patch

* Mon Sep 13 2010 Bruno Wolff III <bruno@wolff.to> - 034-3
- Backported fix for vesa boot menu item

* Sun Sep 12 2010 Bruno Wolff III <bruno@wolff.to> - 034-2
- mkbiarch needs pyparted

* Sat Sep 11 2010 Bruno Wolff III <bruno@wolff.to> - 034-1
- A new experimental script for creating live images.
- Handle partition devices that have a separator character in them.
- Initial checkin of a new expermiental tool for live backup images.
- Allow use of stage2 for repos to help with netinst ISOs.
- Fix issue with using netinst ISOs.
- Add support for ext4 now that syslinux supports it.
- Fix for enumerating loop devices using bash 4.1.7.
- Change --skipcopy to not overwrite other large areas.
- Add basic video driver option to syslinux/isolinux.
- Don't create sparse files one byte too large.
- Display progress information when copying image to USB devices.
- Set default boot language for USB images to the current locale.
- Use grep instead of depreceated egrep.
- Set up locale or there can be problems handling nonascii strings.
- Try normal umount before falling back to lazy umount.
- Allow creation of SELinux enabled LiveCD from an SELinux disabled system.

* Fri Jul 30 2010 Bruno Wolff III <bruno@wolff.to> - 033-3
- The previous update got replaced by the python update; another bump is needed.

* Tue Jul 27 2010 Bruno Wolff III <bruno@wolff.to> - 033-2
- Replace 'zlib' with 'gzip' to fix thinko about the compressor name.

* Tue Jul 27 2010 Bruno Wolff III <bruno@wolff.to> - 033-1
- Fix for vesa splash file change for bz 617115.
- Use lazy umounts as a work around for bz 617844.
- Better handling of Environment exceptions for bz 551932.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 032-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 19 2010 Bruno Wolff III <bruno@wolff.to> - 032-4
- liveimage-mount is new to 023

* Sat Jun 19 2010 Bruno Wolff III <bruno@wolff.to> - 032-3
- Change the version in the Makefile

* Sat Jun 19 2010 Bruno Wolff III <bruno@wolff.to> - 032-2
- Fix tar prefix and document how to make it

* Sat Jun 19 2010 Bruno Wolff III <bruno@wolff.to> - 032-1
- Added support for specifying compressors
- Add Requires for parted - Bug 605639
- Add rd_NO_DM dracut cmdline options - Bug 589783
- See http://git.fedorahosted.org/git/?p=livecd;a=shortlog for a list of
  upstream commits since 031 was tagged.

* Tue Nov 03 2009 Warren Togami <wtogami@redhat.com> - 031-1
- livecd-iso-to-disk capable of installing installer DVD to USB

* Mon Oct 19 2009 Warren Togami <wtogami@redhat.com> - 030-1
- Tell dracut not to ask for LUKS passwords or activate mdraid sets
- Silence the /etc/modprobe.conf deprecation warning

* Wed Sep 16 2009 Warren Togami <wtogami@redhat.com> - 028-1
- Fix LiveUSB with live images
- Fix display of free space during livecd-iso-to-disk error (farrell)

* Tue Sep 15 2009 Warren Togami <wtogami@redhat.com> - 027-2
- test patch to make LiveUSB work again, need to be sure it doesn't
  break LiveCD before committing in the next version

* Thu Sep 10 2009 Warren Togami <wtogami@redhat.com> - 027-1
- Support new dracut output filename /boot/initramfs-*
- Fix cleanup of fake /selinux directory during teardown Bug #522224

* Mon Aug 24 2009 Jeremy Katz <katzj@redhat.com> - 026-1
- More resize2fs -M usage
- Work with dracut-based initramfs
- Some error handling updates

* Thu Jul 30 2009 Jeremy Katz <katzj@redhat.com> - 025-1
- Bind mount /dev/shm also (#502921)
- Update man pages (Michel Duquaine, #505742)
- Use blkid instead of vol_id (mclasen, #506360)
- A few livecd-iso-to-disk tweaks (Martin Dengler, Jason Farrell)
- Another fix for SELinux being disabled (#508402)
- Use resize2fs -M and handle resize errors better
- Use isohybrid on the live image 
- Use system-config-keyboard instead of rhpl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May  6 2009 Jeremy Katz <katzj@redhat.com> - 024-1
- Fix ppc image creation (#497193, help from jwboyer)
- Fixes for using ext[23] usb stick (wtogami)
- Check filesystem after resizing and raise an error if there are 
  problems (#497377)

* Tue Apr 14 2009 Jeremy Katz <katzj@redhat.com> - 023-1
- Don't prompt about overwriting when making usb stick (#491234)
- Fix up livecd-iso-to-pxeboot for new syslinux paths
- Fix --xo variable expansion (Alexander Boström)
- Name of EFI partitions doesn't matter for mactel mode (Jim Radford)
- Fix unterminated sed command (#492376)
- Handle kernel/squashfs mismatch when making usb stick in
  --xo mode (Alexander Boström)
- Support all of the options for the 'firewall' kickstart directive
- Deal with syslinux com32 api incompat when making usb sticks (#492370)
- Add options to force fetching of repomd.xml every run (jkeating)
- Quiet restorecon (Marc Herbert)
- Fix traceback with syslinux disabled (#495269)
- Split python-imgcreate module into a subpackage

* Mon Mar  9 2009 Jeremy Katz <katzj@redhat.com> - 022-1
- Fixes for hybird GPT/MBR usb sticks (Stewart Adam)
- Support setting SELinux booleans (Dan Walsh)
- Fix unicode error messages (Felix Schwarz)
- Update man pages (Chris Curran, #484627)
- Support syslinux under /usr/share
- Remove some legacy support from livecd-iso-to-disk
- Basic support for multi-image usb sticks

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Jeremy Katz <katzj@redhat.com> - 021-1
- Start of support for hybrid GPT/MBR usb sticks (Stewart Adam)
- Fix for udev deprecated syntax (#480109)
- Keep cache with --cache (Jan Kratochvil, #479716)
- Use absolute path to cachedir (#479716)
- Support UDF for large ISO spins (Bruno Wolf, #476696)
- Improvements for encrypted /home setup (mdomsch, #475399)
- Don't allow spaces in labels (#475834)
- Fix --tmpdir relative path (dhuff)
- Support ext4 rootfs
- Fix device command version check (apevec)
- Allow URLs for specifying the kickstart config (bkearney)
- Fix macro name for excludedocs (bkearney)
- Fix up --base-on (#471656)

* Wed Nov 12 2008 Jeremy Katz <katzj@redhat.com> - 020-1
- Support setting up a swap file
- Verify integer args in livecd-iso-to-disk (#467257)
- Set up persistent /home on internal mtd0 for XO
- Default to resetting the overlay on XO
- Support copying the raw ext3fs to the usb stick instead of the squash
- Mactel fixes
- Align initrd properly on XO (#467093)
- Make initrd load addr work on newer XO firmwares
- Fix up Xen paths for Xen live images (Michael Ansel)
- Support --defaultdesktop (Orion Poplawski)

* Fri Oct 10 2008 Jeremy Katz <katzj@redhat.com> - 019-1
- livecd-iso-to-disk: Various other XO fixes
- Cleanup rpmdb locks after package installation
- Fix traceback due to lazy rhpl.keyboard import
- Fix using groups with options (jkeating)
- Support persistent /home on XO's internal flash
- Fix ramdisk load addr in boot/olpc.fth for XO
- Fix up boot from SD
- Fix extracting boot parameters for pxe (apevec)
- Make rpm macro information persist into the image (bkearney)
- Support %%packages --instLangs (bkearney)

* Thu Aug 28 2008 Jeremy Katz <katzj@redhat.com> - 018-1
- Use logging API for debugging messages (dhuff)
- Some initial support for booting live images on an XO
- Refactoring of mount code for appliance-creator (danpb, dhuff)
- Make --base-on actually work again
- Drop the image configs; these are now in the spin-kickstarts repo
- plymouth support
- Listen to bootloader --append in config
- Add man pages (Pedro Silva)
- Support booting from Intel based Macs via EFI on USB (#450193)
- Fixes for SELinux enforcing (eparis)
- Eject the CD on shutdown (#239928)
- Allow adding extra kernel args with livecd-iso-to-disk
- Support for persistent /home (#445218)
- Copy timezone to /etc/localtime (#445624)
- Ensure that commands run by livecd-creator exist
- Mount a tmpfs for some dirs (#447127)

* Tue May  6 2008 Bill Nottingham <notting@redhat.com> - 017-1
- fix F9 final configs

* Thu May  1 2008 Jeremy Katz <katzj@redhat.com> - 016-1
- Config changes all around, including F9 final configs
- Fix up the minimal image creation
- Fix odd traceback error on __del__ (#442443)
- Add late initscript and split things in half
- livecd-iso-to-disk: Check the available space on the stick (#443046)
- Fix partition size overriding (kanarip)

* Thu Mar  6 2008 Jeremy Katz <katzj@redhat.com> - 015-1
- Support for using live isos with pxe booting (Richard W.M. Jones and 
  Chris Lalancette)
- Fixes for SELinux being disabled (Warren Togami)
- Stop using mayflower for building the initrd; mkinitrd can do it now
- Create a minimal /dev rather than using the host /dev (Warren Togami)
- Support for persistent overlays when using a USB stick (based on support 
  by Douglas McClendon)

* Tue Feb 12 2008 Jeremy Katz <katzj@redhat.com> - 014-1
- Rework to provide a python API for use by other tools (thanks to 
  markmc for a lot of the legwork here)
- Fix creation of images with ext2 filesystems and no SELinux
- Don't require a yum-cache directory inside of the cachedir (#430066)
- Many config updates for rawhide
- Allow running live images from MMC/SD (#430444)
- Don't let a non-standard TMPDIR break things (Jim Meyering)

* Mon Oct 29 2007 Jeremy Katz <katzj@redhat.com> - 013-1
- Lots of config updates
- Support 'device foo' to say what modules go in the initramfs
- Support multiple kernels being installed
- Allow blacklisting kernel modules on boot with blacklist=foo
- Improve bootloader configs
- Split configs off for f8

* Tue Sep 25 2007 Jeremy Katz <katzj@redhat.com> - 012-1
- Allow %%post --nochroot to work for putting files in the root of the iso
- Set environment variables for when %%post is run
- Add progress for downloads (Colin Walters)
- Add cachedir option (Colin Walters)
- Fixes for ppc/ppc64 to work again
- Clean up bootloader config a little
- Enable swaps in the default desktop config
- Ensure all configs are installed (#281911)
- Convert method line to a repo for easier config reuse (jkeating)
- Kill the modprobe FATAL warnings (#240585)
- Verify isos with iso-to-disk script
- Allow passing xdriver for setting the xdriver (#291281)
- Add turboliveinst patch (Douglas McClendon)
- Make iso-to-disk support --resetmbr (#294041)
- Clean up filesystem layout (Douglas McClendon)
- Manifest tweaks for most configs

* Tue Aug 28 2007 Jeremy Katz <katzj@redhat.com> - 011-1
- Many config updates for Fedora 8
- Support $basearch in repo line of configs; use it
- Support setting up Xen kernels and memtest86+ in the bootloader config
- Handle rhgb setup
- Improved default fs label (Colin Walters)
- Support localboot from the bootloader (#252192)
- Use hidden menu support in syslinux
- Have a base desktop config included by the other configs (Colin Walters)
- Use optparse for optino parsing
- Remove a lot of command line options; things should be specified via the
  kickstart config instead
- Beginnings of PPC support (David Woodhouse)
- Clean up kernel module inclusion to take advantage of files in Fedora
  kernels listing storage drivers

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 010-1
- Separate out configs used for Fedora 7
- Add patch from Douglas McClendon to make images smaller
- Add patch from Matt Domsch to work with older syslinux without vesamenu
- Add support for using mirrorlists; use them
- Let livecd-iso-to-disk work with uncompressed images (#248081)
- Raise error if SELinux requested without being enabled (#248080)
- Set service defaults on level 2 also (#246350)
- Catch some failure cases
- Allow specifying tmpdir
- Add patch from nameserver specification from Elias Hunt

* Wed May 30 2007 Jeremy Katz <katzj@redhat.com> - 009-1
- miscellaneous live config changes
- fix isomd5 checking syntax error

* Fri May  4 2007 Jeremy Katz <katzj@redhat.com> - 008-1
- disable screensaver with default config
- add aic7xxx and sym53c8xx drivers to default initramfs
- fixes from johnp for FC6 support in the creator
- fix iso-to-stick to work on FC6

* Tue Apr 24 2007 Jeremy Katz <katzj@redhat.com> - 007-1
- Disable prelinking by default
- Disable some things that slow down the live boot substantially
- Lots of tweaks to the default package manifests
- Allow setting the root password (Jeroen van Meeuwen)
- Allow more specific network line setting (Mark McLoughlin)
- Don't pollute the host yum cache (Mark McLoughlin)
- Add support for mediachecking

* Wed Apr  4 2007 Jeremy Katz <katzj@redhat.com> - 006-1
- Many fixes to error handling from Mark McLoughlin
- Add the KDE config
- Add support for prelinking
- Fixes for installing when running from RAM or usb stick
- Add sanity checking to better ensure that USB stick is bootable

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-3
- have to use excludearch, not exclusivearch

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-2
- exclusivearch since it only works on x86 and x86_64 for now

* Wed Mar 28 2007 Jeremy Katz <katzj@redhat.com> - 005-1
- some shell quoting fixes
- allow using UUID or LABEL for the fs label of a usb stick
- work with ext2 formated usb stick

* Mon Mar 26 2007 Jeremy Katz <katzj@redhat.com> - 004-1
- add livecd-iso-to-disk for setting up the live CD iso image onto a usb 
  stick or similar

* Fri Mar 23 2007 Jeremy Katz <katzj@redhat.com> - 003-1
- fix remaining reference to run-init

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 002-1
- update for new version

* Fri Dec 22 2006 David Zeuthen <davidz@redhat.com> - 001-1%{?dist}
- Initial build.

