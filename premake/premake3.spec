# Tag: Devel, Tool
# Type: Standalone
# Category: Tool, Programming

Summary: Tool for describing builds
Name: premake3
Version: 3.7
Release: 2%{?dist}
License: GPL-3.0-or-later
URL: http://sourceforge.net/projects/premake/

Vendor:       Audinux
Distribution: Audinux

Source0: http://downloads.sourceforge.net/premake/premake-src-3.7.zip

BuildRequires: gcc gcc-c++
BuildRequires: make

%description
Describe your software project with a full-featured scripting language and let Premake write the build scripts for you.
With one file your project can support both IDE-addicted Windows coders and Linux command-line junkies!

%prep
%autosetup -n Premake-3.7

%build

%make_build

%install

install -m 755 -d %{buildroot}/%{_bindir}/
cp bin/premake %{buildroot}/%{_bindir}/premake3

%files
%defattr(-,root,root,-)
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{_bindir}/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 3.7-2
- update for Fedora 29

* Sat May 12 2017 Yann Collette <ycollette.nospam@free.fr> - 3.7-2
- change package name

* Fri Jun 19 2015 Yann Collette <ycollette.nospam@free.fr> - 3.7-1
- initial release
