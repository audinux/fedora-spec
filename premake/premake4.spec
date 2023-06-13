Summary: Tool for describing builds
Name:    premake4
Version: 4.4beta5
Release: 1%{?dist}
License: GPL-3.0-or-later
URL:     http://sourceforge.net/projects/premake/

Vendor:       Audinux
Distribution: Audinux

Source0: https://sourceforge.net/projects/premake/files/Premake/4.4/premake-4.4-beta5-src.zip

BuildRequires: gcc gcc-c++

%description
Describe your software project with a full-featured scripting language
and let Premake write the build scripts for you. With one file your project
can support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%autosetup -n premake-4.4-beta5

sed -i -e "s/ -s//g" build/gmake.unix/Premake4.make

%build

%set_build_flags

cd build/gmake.unix/
%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/release/premake4 %{buildroot}/%{_bindir}/premake4

%files
%doc BUILD.txt CHANGES.txt README.txt
%license LICENSE.txt
%{_bindir}/*

%changelog
* Fri Oct 23 2020 Yann Collette <ycollette.nospam@free.fr> - 4.4-beta5-1
- fix debug build

* Mon Mar 4 2019 Yann Collette <ycollette.nospam@free.fr> - 4.4-beta5-1
- update to 4.4-beta5

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 4.3-1
- initial release
