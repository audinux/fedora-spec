+ mkdir -p /home/collette/rpmbuild/BUILDROOT/kernel-lqx-mao-6.0.7.lqx1-11.fc36.x86_64/boot /home/collette/rpmbuild/BUILDROOT/kernel-lqx-mao-6.0.7.lqx1-11.fc36.x86_64/lib/modules
+ make -j4 INSTALL_MOD_PATH=/home/collette/rpmbuild/BUILDROOT/kernel-lqx-mao-6.0.7.lqx1-11.fc36.x86_64 KBUILD_SRC= mod-fw= INSTALL_MOD_STRIP=1 CONFIG_MODULE_COMPRESS=1 CONFIG_MODULE_COMPRESS_XZ=1 modules_install
rm: invalid option -- 'l'
Try 'rm --help' for more information.
make: *** [Makefile:1475: __modinst_pre] Error 1
erreur : Mauvais statut de sortie pour /var/tmp/rpm-tmp.mZuLAz (%install)

