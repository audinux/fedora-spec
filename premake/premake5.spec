# Status: active
# Tag: Devel, Tool
# Type: Standalone
# Category: Tool, Programming

Summary: Tool for describing builds
Name: premake5
Version: 5.0.0beta6
Release: 1%{?dist}
License: GPL-3.0-or-later
URL: https://github/premake/
ExclusiveArch: x86_64 aarch64

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/premake/premake-core/archive/v5.0.0-beta4.tar.gz#/premake5-5.0.0-beta6.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: libuuid-devel

%description
Describe your software project with a full-featured scripting language and
let Premake write the build scripts for you. With one file your project can
support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%autosetup -n premake-core-5.0.0-beta4

%build

%set_build_flags

export CFLAGS="-fPIC $CFLAGS" 

%make_build -f Bootstrap.mak linux

bin/release/premake5 gmake

# Inject optflags into CFLAGS
sed -i "s|^\s*ALL_CFLAGS\s*+=.*|ALL_CFLAGS += \$(ALL_CPPFLAGS) %{optflags}|" Premake5.make
sed -i "s|^\s*ALL_CXXFLAGS\s*+=.*|ALL_CXXFLAGS += \$(ALL_CPPFLAGS) %{optflags}|" Premake5.make
# Disable stripping the executable
sed -i "s|^\s*ALL_LDFLAGS\s*+= \$(LDFLAGS) -s|ALL_LDFLAGS += \$(LDFLAGS)|" Premake5.make

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
install -m 755 -d %{buildroot}/%{_mandir}/man1/

cp bin/release/premake5 %{buildroot}/%{_bindir}/premake5
cp packages/debian/premake.1 %{buildroot}/%{_mandir}/man1/premake5.1

%files
%doc BUILD.txt CHANGES.txt README.md
%license LICENSE.txt
%{_bindir}/premake5
%{_mandir}/man1/premake5.1*

%changelog
* Sun Mar 30 2025 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-beta6-1
- update to 5.0.0-beta6-1

* Mon Feb 17 2025 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-beta5-1
- update to 5.0.0-beta5-1

* Mon Dec 30 2024 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-beta4-1
- update to 5.0.0-beta4-1

* Mon Nov 11 2024 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-beta3-1
- update to 5.0.0-beta3-1

* Wed Jun 24 2020 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-alpha15-1
- update to 5.0.0-alpha15-1

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 5.0.0-alpha13-1
- initial release
