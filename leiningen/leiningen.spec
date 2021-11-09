# Tag: Editor
# Type: Standalone, Language
# Category: Audio, Programming

Name:    leiningen
Version: 2.9.7
Release: 1%{?dist}
Summary: Clojure project automation tool
License: EPL
URL:     https://github.com/technomancy/leiningen

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/technomancy/leiningen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/technomancy/leiningen/releases/download/%{version}/leiningen-%{version}-standalone.jar
Source2: https://github.com/technomancy/leiningen/raw/%{version}/bin/lein

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: java-devel
BuildRequires: maven
BuildRequires: clojure
BuildRequires: wget
BuildRequires: sed

Requires: clojure java

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, you describe your build with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging your projects and can be easily extended with a number of
plugins.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 %{SOURCE1} %{buildroot}/%{_javadir}/%{name}-%{version}-standalone.jar

install -d -m 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE2} %{buildroot}%{_bindir}/lein

install -d -m 755 %{buildroot}%{_datadir}/pixmaps/
install -pm 644 resources/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 bash_completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/lein

install -d -m 755 %{buildroot}%{_datadir}/zsh/site-functions
install -pm 644 zsh_completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_lein

sed -i -e "/export LEIN_VERSION/i LEIN_JAR=/usr/share/java/leiningen-%{version}-standalone.jar" %{buildroot}%{_bindir}/lein

%files
%doc README.md TUTORIAL.md NEWS.md CONTRIBUTING.md
%license COPYING
%{_javadir}/*
%{_bindir}/lein
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/lein
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_lein
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Nov 09 2021 Yann Collette <ycollette.nospam@free.fr> - 2.9.7-1
- update to 2.9.7-1

* Wed Oct 28 2020 Yann Collette <ycollette.nospam@free.fr> - 2.9.4-1
- update to 2.9.4-1

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 2.9.1-1
- update to 2.9.1-1

* Wed Feb 13 2019 Yann Collette <ycollette.nospam@free.fr> - 2.8.3-1
- Update to 2.8.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Oct 16 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-4
- Revert to packaging uncompiled Leiningen sources; need to find out why
  we can't compile against RPM-packaged JARs

* Sun Aug 19 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-3
- Use package's own launcher script to build the JAR (from Debian)

* Tue Jun 12 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-2
- Package launcher script
- Update dependencies

* Mon Jun 11 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.1-1
- Initial package

