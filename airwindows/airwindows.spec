# Tag: Effect
# Type: Plugin, VST
# Category: Audio, Effect

%global commit0 a6dba1efc8bf7581e6f8c93d680f0e5c88432e5f

Name:    airwindows
Version: 0.0.1
Release: 81%{?dist}
Summary: A huge set of VST2 plugins
License: MIT
URL:     https://github.com/airwindows/airwindows

Vendor:       Audinux
Distribution: Audinux

# Usage: ./airwindows-source.sh <TAG>
#        ./airwindows-source.sh master

Source0: airwindows.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip
Source2: airwindows-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: wget
BuildRequires: unzip
BuildRequires: cmake

%description
Airwindows plugins are modular, graphic-less, stripped-down, VST plugins

%prep
%autosetup -n %{name}

unzip %{SOURCE1}

# Build a shared lib instead of a module to be able to get debug symnols
sed -i -e "s/MODULE/SHARED/g" plugins/LinuxVST/Helpers.cmake

mkdir -p plugins/LinuxVST/include/vstsdk/
mkdir -p plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/

cp VST_SDK/VST2_SDK/pluginterfaces/vst2.x/*    plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/
cp VST_SDK/VST2_SDK/public.sdk/source/vst2.x/* plugins/LinuxVST/include/vstsdk/

sed -i -e "s/add_subdirectory/include_directories/g"     plugins/LinuxVST/CMakeLists.txt
sed -i -e "s/add_compile_options/#add_compile_options/g" plugins/LinuxVST/CMakeLists.txt

sed -i -e "/include_directories/a file(GLOB VSTSDK_SOURCES include/vstsdk/*.h include/vstsdk/*.cpp)" plugins/LinuxVST/CMakeLists.txt

%build

cd plugins/LinuxVST

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build

%install

cd plugins/LinuxVST/

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 %{__cmake_builddir}/*.so %{buildroot}/%{_libdir}/vst/

%files
%doc plugins/LinuxVST/README.md Airwindopedia.txt
%license plugins/LinuxVST/LICENSE
%{_libdir}/*

%changelog
* Tue Mar 05 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-81
- update to a6dba1efc8bf7581e6f8c93d680f0e5c88432e5f

* Tue Jan 16 2024 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-80
- update to 2aa1a11d3441930fa95fda13f681f652b7ecbe87

* Mon Dec 18 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-79
- update to 1644e7457bcc7ff038c41ba6eda7b04865d2c373

* Thu Nov 23 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-78
- update to b884ce1ab00763dba2cf10be692bf24d4aa3271d

* Tue Oct 03 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-77
- update to 6115627993f4a7a6d1d219ac92d70e52af39b77b

* Sat Jul 22 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-76
- update to 393c76b1430aed163d8bf12e6fd444a3694d163d

* Wed Feb 01 2023 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-75
- update to 4dbf9414ec5e67a563be605e37ced4206c5747d8

* Mon Nov 21 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-74
- update to f06250c08225d4040af3addab2026e99779ef42e

* Thu Sep 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-73
- update to dfb1b1f4fe31a943409fd20d79e14e1315abd3c8

* Mon Sep 12 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-72
- update to 7b8647e22b1f865c4a31c606a8c0d3e438efd48b

* Mon Aug 22 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-71
- update to 75b61509ffc3e8cb1c5355a1a72fe7eb2f661a08

* Mon Jun 27 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-70
- update to 4f1ee147a1a86a4cb98644381a37570e28569277

* Sun Jun 12 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-69
- update to 12df780f8b29d45bb16bf195b4daa3bca513bff9

* Fri Apr 15 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-68
- update to 339fe09e9c0d044e3db45505f1fd1a25ad72530b

* Tue Mar 22 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-67
- update to 36cf488ba7e1c61fa708cac54cd091c3fd649d81

* Mon Mar 14 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-66
- update to fea197a674777e06e7abe7c119a9526d2f031792

* Mon Feb 28 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-65
- update to 43799635b47db58d4a4a4c041ff601566ba85723

* Tue Feb 22 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-64
- update to 47e16fec36b86140cee81f79cfa81cc30de250f4

* Mon Feb 21 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-63
- update to a0c7153bacbaec6abc19d8a8ef20909c36f9d35a

* Sat Feb 19 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-62
- update to 320a0f71cbfc06c5893c064171216ff823c49640

* Sun Jan 30 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-61
- update to f1e7313c284110347f2907ebe47ad1c03a9b2e9e

* Wed Jan 05 2022 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-60
- fix linking

* Tue Dec 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-59
- update to 9c5182552324c56cfe04883a8e791f601d08de0e

* Thu Dec 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-58
- update to 9f87b74834a9e624478fa2680518581373b8b4d8

* Wed Dec 08 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-57
- update to a6a7406df9b99878ad51708e8da0e0246f727858

* Sun Nov 28 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-56
- update to 1ba0dd4fdc6968da360ee3c2926cd4464584bb54

* Wed Nov 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-55
- update to 4b804bcd7ff94524fd109c55d2f784123ef7436c

* Mon Nov 08 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-54
- update to 352db649a87753d95d1969ecd6599f607dacc84b

* Sat Oct 23 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-53
- update to 1dfd32ed468f55134a36f8ec0fe4f53f4a40c192

* Mon Oct 11 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-52
- update to afa1a703f4514aee68c14774cf5d55aa8aced5cd

* Sun Oct 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-51
- update to 75d842e477913162850453ae67ee4d838b16854f

* Sun Oct 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-50
- update to b07ff60adba1e71b2248db65406d5ce6c14f4bc8

* Wed Sep 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-49
- update to 4a426a85bc1eecf6645d71ff9e3142d135bc29be

* Wed Sep 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-48
- update to 9887068f3bf9607a61e97c93aed34b8ece47e457

* Thu Sep 16 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-47
- update to 485b49497abcc0255df1c9f7b84d8fd4a1429e83

* Wed Sep 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-46
- update to 881ce22b2dced6abdcca6e0b1e93ad8c53db798b

* Fri Sep 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-45
- update to 2cf9a6b6a38b931d0e9cefe919babf5d035b4b0b

* Fri Sep 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-44
- update to ed55e46d3df1ffda9f45795fe2f00201421c5fdd

* Tue Aug 24 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-43
- update to c657f1262b16bf9ee1961a6a0daa2210e2bc55ea

* Sat Aug 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-42
- update to 34e5786c00ed4be313d0b3a17bc48c1ef6f40ca3

* Wed Aug 18 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-41
- update to df6249fa1d83d04f5969ccd86471a2f8d1b33d9a

* Sat Aug 14 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-40
- update to 785689e3ad41aa58dc78043e75e230224f532221

* Tue Aug 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-39
- update to 875b05321408ed8f772f80f54feddc9e89aef5fd

* Fri Jul 30 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-38
- update to 6aa15eefabcfa0b636175b6dd25f399e13dc49a4

* Sat Jul 24 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-37
- update to eb454669efc84f54334c9f53edcd2c28b9001673

* Sat Jul 17 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-36
- update to d0b9afa50e20a73b0be72bf8e3da27e01d9cf798

* Sat Jul 10 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-35
- update to 50c47b0b78bff037161e8578048d26f10198f092

* Sat Jul 03 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-34
- update to 96869f28a1bddea6521a5bdad24b597af3aa109f

* Sat Jun 26 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-33
- update to f673fe3da38623640ebe02bd36995c0e01bef62c

* Tue Jun 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-32
- update to 3aac179465a5dc5585c4925fc16399865ac47ffa

* Sun Jun 13 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-31
- update to 08af05d938414f220b684230523a70174a5161a2

* Tue Jun 01 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-30
- update to 2a7d6fa1c8813b7d6f7daed1ed685d68142bb616

* Tue May 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-29
- update to 9da0890fa3a7ee521e17197cc2ece276fba8396b

* Mon May 24 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-28
- update to 50e813d894dd4426b204b2a112fc89a5420430e6

* Fri May 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-27
- update to 12785bb45db400eeddd79c11d830320a070bb4ca

* Sat Apr 24 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-26
- update to 7337eb6c32be3f00f1f79332e7f3e11434ad1cd6

* Mon Apr 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-25
- update to 4f0f40165314f5f0281209eb3f18bd7016b42d75

* Mon Apr 05 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-24
- update to b6d655bad82b89bef1b5c0570e23a96dd443cb29

* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-23
- update to a3569b22e96a8c458f5fed129e611b80793fbe92

* Sun Mar 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-22
- update to 450b0c513d9743be4ef9aeed39d01e67111b5a44

* Mon Mar 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-21
- update to e4e38318a41f15515c32ba0c41cda0d824f5580f

* Mon Mar 8 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-20
- update to 7bb7fde13a9c94af242835823b813e6bcd0f20c8

* Mon Mar 1 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-19
- update to 68d733204a1d12a2d05045ed57d973b4a386bc30

* Mon Feb 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-18
- update to 3980dcb3d19bb2e2645d1c825fcea1bad3ee7adc

* Mon Feb 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-17
- update to 690897408f7ada94fdae90f3cf2a41ce8c9e1080

* Mon Feb 8 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-16
- update to f885ba303eaab68a8de079400c37c9cbf82b37c9

* Mon Feb 1 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-15
- update to 125b760f469e532f701e43602b01dc49c043d72a

* Mon Jan 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-14
- update to d8884ef296bc7073e10d19fc6611de6d1ad1b976

* Mon Jan 11 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-13
- update to e36d8abd86ed7fbf6507eff0a1b52fef7db1d5dc

* Wed Jan 6 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-12
- update to 3d92bfb6ea84f32c7d059d77aa83d263293a52b1

* Mon Jan 4 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-11
- update to 57dea44c96ec17445b06d3c45d05fd9af42528bc

* Mon Dec 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-10
- update to b155145346207aca5febd9c8820e5c25d41a53b2

* Mon Dec 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-9
- update to cfd9507cae7ff327c36ae36d602487aa6e0857cc

* Mon Dec 14 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-8
- update to 6ed6016b79e43b3c3183d95ed6f4a2de890c284e

* Mon Dec 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-7
- update to 5b6c3dbce336f714b885d5b72ddd478f823d0bb8

* Mon Nov 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6
- update to 2a06dc45b2b19fcce91e9abfeaa7124791868498

* Mon Nov 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 8e70eedbaeb7998a276331eb5eeb1015b1bc8807

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to bda54733c70a8857bea04a3511e0c247acee79e1

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 6eb63993bc6b04b7000846fb9b122e2b6469bddd

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to fa61072ea31a876ab28d80bf5edcae717ab6ddf3 - fix for fedora 33

* Wed Jul 29 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
