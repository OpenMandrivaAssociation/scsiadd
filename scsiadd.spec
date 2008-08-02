%define	name	scsiadd
%define	version	1.95
%define	release	%mkrel 4

Summary:	Utility to add and remove SCSI devices on the fly
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		System/Configuration/Hardware
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.52-mdkconf.patch.bz2
URL:		http://llg.cubic.org/tools/
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

