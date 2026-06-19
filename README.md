The repo related to these packages can be found here:

Before Fedora 35:
https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/

After (including) Fedora 35:
https://copr.fedorainfracloud.org/coprs/ycollet/audinux/

This repo has old packages for Fedora 25 to 40 and up to date packages for Fedora 43, 44 and rawhide.

To build the spec file:
- copy it into your rpmbuild/SPEC directory
- run:
```
$ spectool -g <package_name.spec> # to download the source file
```
- copy the source file into rpmbuild/SOURCE
- run:
```
$ rpmbuild -ba filename.spec
```
The result can be found in:
- RPMS/noarch
- RPMS/x86_64

The SRPMS file is located in:
- SRPMS

Install the rpm file using yum:
as a root user:
```
$ yum install filename.rpm
# or
$ dnf install filename.rpm
```

To mirror the COPR repository:
```
$ mkdir -p rpm-copr/44
$ cd rpm-copr/44
$ dnf reposync --release=44 --repoid=copr:copr.fedorainfracloud.org:ycollet:audinux --destdir . --downloadcomp
```

To test the rebuild of the package using mock:
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --rebuild polyphone-2.0.1-1.fc44.src.rpm
```

To enable a thirdparty repository, you must add it to /etc/mock/templates/fedora-44.tpl for example and then, enable it via the command line. For example:
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --enablerepo=ycollet-audinux --rebuild dgedit-0.1-2.fc44.src.rpm
```

The portion added to /etc/mock/templates/fedora-{43,44,rawhide}.tpl is:

```
[ycollet-audinux]
name=Copr repo for audinux owned by ycollet
baseurl=https://copr-be.cloud.fedoraproject.org/results/ycollet/audinux/fedora-$releasever-$basearch/
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/ycollet/audinux/pubkey.gpg
enabled=1
enabled_metadata=1

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=604800
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
skip_if_unavailable = 1
keepcache = 0
```

This is the content of the repo conf file found in /etc/yum.repo.d.

To create the LiveCD using livecd-creator-mao:

First: prepare the thirdparty files (GuitarPro files, soundfonts, images):
```
$ ./prepare.sh
```
This script will download a zip a put everything in /tmp/prepare/ directory.

As a root user:
```
$ livecd-creator --verbose --config=fedora-44-live-jam-xfce.ks --fslabel=Audinux --releasever 44
```

```
# To build using the EPEL 7 version of livecd-tools:

$ mock -r /etc/mock/epel-7-x86_64.cfg --isolation=simple --init --install wget unzip livecd-tools
$ mock -r /etc/mock/epel-7-x86_64.cfg --copyin fedora-44-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/epel-7-x86_64.cfg --enable-network --shell

# To build using the Fedora 44 version of livecd-tools:

$ mock -r /etc/mock/fedora-44-x86_64.cfg --isolation=simple --init --install wget unzip livecd-tools
$ mock -r /etc/mock/fedora-44-x86_64.cfg --copyin fedora-44-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/fedora-44-x86_64.cfg --enable-network --shell

# Then: preinstall the required files and start livecd-creator

$ cd /builddir
$ ./prepare.sh
$ livecd-creator --verbose --config=fedora-44-live-jam-xfce.ks --fslabel=Audinux --releasever 44
```

To create the Lice CD using livemedia-creator:

As a root user:
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --isolation=simple --init --install lorax-lmc-novirt wget unzip libblockdev-lvm libblockdev-btrfs libblockdev-swap libblockdev-loop libblockdev-crypto libblockdev-mpath libblockdev-dm libblockdev-mdraid libblockdev-nvdimm
$ mock -r /etc/mock/fedora-44-x86_64.cfg --copyin fedora-44-live-jam-xfce.ks --copyin prepare.sh /builddir
$ mock -r /etc/mock/fedora-44-x86_64.cfg --enable-network --shell
$ cd /builddir
$ ./prepare.sh
$ livemedia-creator --make-iso --ks fedora-44-live-jam-xfce.ks --project Audinux --iso-name livecd-fedora-44-mao.iso --iso-only --releasever 44 --volid Audinux --image-name Audinux --resultdir /var/lmc --no-virt --tmp /var/tmp
```

To check the potential changes from the kickstart file:
$ dnf install pykickstart.noarch rpmfusion-free-remix-kickstarts.noarch spin-kickstarts.noarch
$ ksflatten -c /usr/share/spin-kickstarts/fedora-live-xfce.ks -o xfce.ks
$ meld fedora-44-live-jam-xfce.ks xfce.ks &

To test the ISO file with a standard BIOS:

Install QEmu-KVM and the SDL interface.

```
$ dnf install qemu-system-x86-core qemu-kvm
$ dnf install qemu-ui-sdl qemu-audio-sdl
$ dnf install qemu-device-display-qxl
```

Without audio:
```
$ qemu-kvm -m 2048 -vga qxl -display sdl -cdrom fedora-44-Audinux.iso
```
With audio and usb:
```
$ qemu-kvm -m 2048 -vga qxl -usb -device intel-hda -device hda-duplex -display sdl -cdrom fedora-44-Audinux.iso
```
With audio, usb and with 2 cpus:
```
$ qemu-kvm -m 2048 -vga qxl -usb -device intel-hda -device hda-duplex -smp cpus=2 -display sdl -cdrom fedora-44-Audinux.iso
```

To test the USB bootable file:
```
$ qemu-kvm -m 2048 -vga qxl -display sdl -smp cpus=2 -usb -device intel-hda -device hda-duplex -drive file=fedora-44-Audinux.iso -boot menu=on
```

To mount a usb device:
```
# lsusb
...
Bus 002 Device 003: ID 18d1:4e11 Google Inc. Nexus One
```

(Note the Bus and device numbers).
Manually, using qemu-kvm command line

```
$ qemu-kvm -m 2048 -name Audinux -display sdl -cdrom fedora-44-Audinux.iso -usb -device usb-host,hostbus=2,hostaddr=3
```

To test the ISO file with a UEFI BIOS:

```
$ dnf install edk2-ovmf
```

```
$ qemu-kvm -m 2048 -vga qxl -display sdl -cdrom fedora-44-Audinux.iso -bios /usr/share/edk2/ovmf/OVMF_CODE.fd
```

Write ISO to USB:

You can use dd:
```
$ dd if=Audinux.iso of=/dev/sdc bs=1024
```
Or mediawriter:
```
$ dnf install mediawriter
$ mediawriter
```

Once the USB key is installed, you can add data persistency using livecd-iso-to-disk:
```
$ dnf install livecd-tools
```

Locate where is your usb disk:
```
$ dmesg | tail
or
$ lsblk
```

Then, reformat to ext4 the usb disk:
```
$ mkfs.ext4 /dev/sdb
```

To add a persistent home directory of size 2Go:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --home-size-mb 2048 Audinux.iso /dev/sdb
```

To add a data persistency on your USB key:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --unencrypted-home --overlay-size-mb 2048 Audinux.iso /dev/sdb
```

To add both data persistency add home persistency on your USB key:
```
$ livecd-iso-to-disk --reset-mbr --format --msdos --unencrypted-home --overlay-size-mb 2048 --home-size-mb 2048 Audinux.iso /dev/sdb
```

Depending on the size of the iso file, you may need to format the USB drive using a efi format:
```
$ livecd-iso-to-disk --reset-mbr --format --efi --unencrypted-home --overlay-size-mb 2048 --home-size-mb 2048 Audinux.iso /dev/sdb
```

You can find a lot of informations related to USB stick and tools to generate these sticks here:
https://docs.pagure.org/docs-fedora/create-and-use-live-image.html

How to use a spec file:

If you use a red hat derivative, you can rebuild the rpm packages from the spec file.
Most of the time, you can copy the .spec file in your rpmbuild/SPEC directory.
Some times, there are some sources package to copy in rpmbuild/SOURCE directory. You have to check is the spec file, there are some indications on how to get the source code.

After that, if there are no indications on how to get the source code:
```
$ spectool -g <package_name>.spec
```
in rpmbuild/SPEC.
This command will download the some required source files.
You must then move the downloaded files from rpmbuild/SPEC to rpmbuild/SOURCE.
Otherwise, have a look in the spec file for instructions on how to get the source code.

And now, it's time to build the package:
```
$ rpmbuild -ba .spec
```
The package to be manually installed via dnf / yum or rpm are located in rpmbuild/RPMS
The source package is located in rpmbuild/SRPMS.

You can also check the following link:
https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/

# To test a GUI packages:

Install the package to be tested + dnf (if you want to install something else) + libX11-xcb (some GUI requires this package to be able to start inside the chroot).
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --dnf --install linux-show-player-0.5.2-1.fc44.noarch.rpm dnf libX11-xcb
```

Now, enable X session connections to the host:
```
$ xhost +
```

Then, start a shell chroot (and enable network connection if you want to complete manually the installation):
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --enable-network --shell
```

Export the host display when you are in the chroot:
```
<mock-chroot> sh-5.0# export DISPLAY=:0.0
```

And now start the application you wanted to test:
```
<mock-chroot> sh-5.0# linux-show-player
```

After the tests, exit from the chroot:
```
<mock-chroot> sh-5.0# exit
```

And cleanup the chroot:
```
$ mock -r /etc/mock/fedora-44-x86_64.cfg --clean
```

# Caveats

Known issues encountered on real-time audio workstations and their solutions.

## Scheduled system tasks causing GPU freeze and Wayland hang

**Symptom:** The NVIDIA GPU freezes briefly, KWin/Wayland hangs, and the
journal shows:

```
kernel: nvidia-modeset: ERROR: GPU:0: Idling display engine timed out: 0x0000987d:0:0:1255
kwin_wayland: The main thread was hanging temporarily!
systemd[1]: Starting plocate-updatedb.service - Update the plocate database...
```

All three lines appear at exactly the same timestamp.

**Root cause:** Fedora installs several scheduled maintenance timers
(`plocate-updatedb`, `dnf-makecache`, `fwupd-refresh`, `man-db-cache-update`,
etc.) that run automatically in the background. These tasks perform heavy
filesystem or network I/O without any RT awareness. The resulting burst of I/O
saturates the memory bus and PCIe bandwidth, causing the NVIDIA driver's
internal DMA/command queue operations to stall past their timeout. The Wayland
compositor hangs because it cannot communicate with the GPU during that window.

This is not specific to NVIDIA — any GPU driver with internal timeouts can be
affected. It is also a common source of audio xruns even when no GPU freeze is
visible.

**Fix — disable the offending timer:**

```bash
sudo systemctl disable --now plocate-updatedb.timer
```

You can still rebuild the locate database manually when needed:

```bash
sudo updatedb
```

**Alternative — keep the timer but lower its priority:**

```bash
sudo systemctl edit plocate-updatedb.service
```

Add the following and save:

```ini
[Service]
Nice=19
IOSchedulingClass=idle
IOSchedulingPriority=7
CPUSchedulingPolicy=idle
```

This instructs the kernel to give `updatedb` the lowest possible CPU and I/O
priority so it yields immediately whenever anything else needs the bus.

**Check for other disruptive timers:**

```bash
systemctl list-timers --all
```

The table below lists the Fedora maintenance services most likely to cause
xruns or GPU freezes on an RT audio workstation, and the recommended action
for each.

| Service | Why it hurts | Recommendation |
|---|---|---|
| `plocate-updatedb` | Full filesystem scan — saturates I/O bus | Disable or idle-nice |
| `dnf-makecache` | DNF metadata refresh — network + disk bursts | Idle-nice or disable |
| `fwupd-refresh` | Firmware update DB sync — network + disk | Idle-nice or disable |
| `man-db-cache-update` | man page DB rebuild — filesystem scan | Idle-nice or disable |
| `logrotate` | Log compression — CPU + I/O spike | Idle-nice |
| `systemd-journal-flush` | Journal flush to disk — I/O spike on rotation | Idle-nice |

To lower priority for any of the above, run `sudo systemctl edit <name>.service`
and add:

```ini
[Service]
Nice=19
IOSchedulingClass=idle
IOSchedulingPriority=7
CPUSchedulingPolicy=idle
```

To disable a timer entirely (and run it manually when needed):

```bash
sudo systemctl disable --now <name>.timer
```

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=audinux/fedora-spec&type=Date)](https://star-history.com/#audinux/fedora-spec&Date)
