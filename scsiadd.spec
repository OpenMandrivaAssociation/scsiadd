%define	name	scsiadd
%define	version	1.95
%define release	6

Summary:	Utility to add and remove SCSI devices on the fly
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		System/Configuration/Hardware
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.52-mdkconf.patch.bz2
URL:		https://llg.cubic.org/tools/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
scsiadd lets you insert or remove SCSI devices from the linux SCSI 
subsystem on the fly. This is useful for external devices 
like scanners or tapes which can be powered on after system boot.
Devices can be added or removed at any time.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README NEWS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-5mdv2010.0
+ Revision: 433633
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-4mdv2009.0
+ Revision: 260573
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-3mdv2009.0
+ Revision: 252219
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-1mdv2008.1
+ Revision: 127101
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import scsiadd


* Mon Feb 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.95-1mdk
- 1.95

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6-1mdk
- 1.6
- add epoch tag to handle upgrade
- update %%docs

* Mon Dec 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.52-1mdk
- 1.52
- regenerate patch

* Sat Dec 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.51-1mdk
- 1.51
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- quiet setup
- use %%configure macro
- fix install (P0)

* Mon Jan 27 2003 Götz Waschk <waschk@linux-mandrake.com> 1.41-3mdk
- fix URL
- fix rpmlint warnings

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.41-2mdk
- rebuild

* Mon Nov 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.41-1mdk
- 1.41

* Mon Aug 29 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.4-2mdk
- added man page.

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4.

* Mon Jan 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- updated to 1.3.

* Fri Aug 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1-1mdk
- used srpm from John Johnson <jjohnson@linux-mandrake.com>
- Made mandrake rpm and changed compression to bz2 
- macros
- BM
