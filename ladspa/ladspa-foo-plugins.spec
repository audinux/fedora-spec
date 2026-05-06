# Status: active
# Tag: Effect
# Type: LADSPA
# Category: Audio, Effect

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to toni@links2linux.de

Name: ladspa-foo-plugins
Summary: Foo plugins - a limiter and a special dynamics processor
Version: 1.2.1
Release: 1%{?dist}
License: GPL-2.0
URL: http://www.studionumbersix.com/foo/
ExclusiveArch: x86_64 aarch64

Source: https://github.com/ycollet/ladspa-foo/archive/refs/tags/v%{version}.tar.gz#/ladspa-foo-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: ladspa-devel
BuildRequires: perl-XML-Parser

%description
foo-plugins is a ladspa plugin package currently consisting of
two plugins, a limiter and a special dynamics processor.

The plugins are released under the General Public License which
means they are free to use and their source code is available.

foo-plugins ladspa identifier range: 3181-3220

3181: Foo Lookahead Limiter
3182: Foo Transient Architect
3183: Foo Transient Architect (mono)
3184: Foo Driver

%prep
%autosetup -n ladspa-foo-%{version}

%build

%make_build

%install

%__install -dm 755 %{buildroot}/%{_libdir}/ladspa

%make_install

%files
%doc README LICENSE
%{_libdir}/ladspa/*.so

%changelog
* Wed May 06 2026 Yann Collette <ycollette dot nospam at free.fr> 1.2.1-1
- initial spec for Fedora - update to 1.2.1

* Wed Aug 14 2013 - guillaume@opensuse.org
- Add ExclusiveArch:  %{ix86} x86_64 since it uses SSE/SSE2 flags

* Sat Dec 26 2009 Toni Graffy <toni@links2linux.de> - 1.2-0.pm.1
- update to 1.2
- Version 1.2 released. This release contains a lot of stuff I don't
  even remember if they are finished or not. Let's hope they don't screw up your system
  New plugins: Foo Chop Liver, Foo Limiter 2, Foo Saturator and t00b Limiter
  Use at your own caution. Chop Liver should work fine as it's so simple, but I'm not
  100% about where I left the others when I stopped working on them. The docs are not
  up yet, but writing them requires me to actually remember exactly what they do.

  * Sat Oct 13 2007 Toni Graffy <toni@links2linux.de> - 1.0-0.pm.1
- initial package 1.0
