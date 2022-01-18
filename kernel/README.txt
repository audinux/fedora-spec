Use build_config.sh from fedora kernel spec repo:

$ wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.10.8.tar.gz
$ wget https://cdn.kernel.org/pub/linux/kernel/projects/rt/5.6/older/patch-5.10.8-rt24.patch.gz
$ tar xvfz linux-5.10.8.tar.gz
$ gunzip patch-5.10.8-rt24.patch.gz
$ cd linux-5.10.8
$ patch -p1 < ../patch-5.10.8-rt24.patch

Since some kernel, I bypassed this step and just build vanilla RT kernels.

$ git clone https://src.fedoraproject.org/rpms/kernel.git
$ cd kernel
$ git switch f32
$ ./build_config.sh kernel-5.10.8

Copy kernel-5.10.8-x86_64.config as '.config' in the linux kernel source directory.

$ make xconfig

Since 5.6.*: check General setup -> Configure standard kernel features (expert users). This will toogle the "Fully preemptible kernel).

Enable CONFIG_PREEMPT_RT_FULL (menu General setup -> Preemption model -> Fully preemptible kernel).
Enable CONFIG_HZ_1000 (menu Processor type and features -> Timer frequency -> 1000 Hz).

Save the configuration file.

Copy back .config file into kernel-config-5.10.

To clean-up the boot menu:

$ grub2-mkconfig -o /boot/grub2/grub.cfg

Since 5.15.*:

Search for "CONFIG_HAVE_PREEMPT_DYNAMIC=y" in kernel-config* and replaces it by "CONFIG_HAVE_PREEMPT_DYNAMIC=n".
