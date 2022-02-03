%define build_session 0

Summary: Grant rt permissions to all users or to active sessions
Name:    planetccrma-rt-permissions
Version: 2012.09.19
Release: 1%{?dist}
License: GPL3
URL:     http://ccrma.stanford.edu/planetccrma/software/

Vendor:       Audinux
Distribution: Audinux

Source0: 99-rt-permissions-all.conf
Source1: 99-rt-permissions.conf
Source2: rt-permissions.ck

BuildRequires: perl

%if 0%{?fedora} >= 17
%define MAX_PRIORITY 99
%else
%define MAX_PRIORITY 70
%endif
%define MAX_MEMORY_LOCK unlimited

%description
This package contains two subpackages, installing %{name}-all will
grant rt permissions to all users, installing %{name}-session will
grant rt permissions only to active sessions in the workstsion. 

%package all
Summary: Grant rt permissions to all users

%description all
Grant all users permission to run processes with realtime scheduling (up to priority %{MAX_PRIORITY})
and to lock memory (up to %{MAX_MEMORY_LOCK} bytes). 

%package session
Summary: Grant rt permissions to active sessions

%description session
Grant active sessions to run processes with realtime scheduling (up to priority %{MAX_PRIORITY})
and to lock memory (up to %{MAX_MEMORY_LOCK} bytes).

%autosetup
%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
cp %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions-all.conf
perl -p -i -e "s|\@\@MAX_PRIORITY\@\@|%{MAX_PRIORITY}|g" $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions-all.conf
perl -p -i -e "s|\@\@MAX_MEMORY_LOCK\@\@|%{MAX_MEMORY_LOCK}|g" $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions-all.conf

cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions.conf
perl -p -i -e "s|\@\@MAX_PRIORITY\@\@|%{MAX_PRIORITY}|g" $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions.conf
perl -p -i -e "s|\@\@MAX_MEMORY_LOCK\@\@|%{MAX_MEMORY_LOCK}|g" $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/99-rt-permissions.conf

%if 0%{?build_session}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ConsoleKit/run-session.d
cp %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ConsoleKit/run-session.d/rt-permissions.ck
perl -p -i -e "s|\@\@MAX_PRIORITY\@\@|%{MAX_PRIORITY}|g" $RPM_BUILD_ROOT%{_sysconfdir}/ConsoleKit/run-session.d/rt-permissions.ck
perl -p -i -e "s|\@\@MAX_MEMORY_LOCK\@\@|%{MAX_MEMORY_LOCK}|g" $RPM_BUILD_ROOT%{_sysconfdir}/ConsoleKit/run-session.d/rt-permissions.ck
%endif

%files 
%defattr(-,root,root,-)
%{_sysconfdir}/security/limits.d/99-rt-permissions.conf

%files all
%defattr(-,root,root,-)
%{_sysconfdir}/security/limits.d/99-rt-permissions-all.conf

%if 0%{?build_session}
%files session
%defattr(-,root,root,-)
%{_sysconfdir}/ConsoleKit/run-session.d/rt-permissions.ck
%endif

%changelog
* Thu Sep 20 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2012.09.19-1
- change amount of lockable memory to "unlimited", ardour complains
  about anything less than that

* Wed May 30 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2012.05.29-1
- lower max allowed priority for Fedora >= 17 to 70 which is now the
  default for Fedora - rtirq and friends take that into account

* Tue Nov 15 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2011.11.15-1
- fixed jack user group (from "jack-user" to "jackuser"), thanks to
  John Dey for the report

* Mon Nov 14 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2011.11.14-1
- create another package with permissions just for the jack-rt group

* Mon Nov 14 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2011.11.13-1
- just build the base package (no session stuff, it does not yet work)

* Wed May 25 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 2011.05.24-1
- initial build.

