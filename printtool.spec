Summary:	A printer configuration tool with a graphical user interface.
Summary(pl):	Program konfiguracyjny drukarki z graficznym interfejsem
Summary(pt_BR):	Ferramenta de configura��o de impressoras
Summary(es):	Herramienta de configuraci�n de impresoras
Summary(ja):	^[$B%0%i%U%#%+%k%f!<%6%$%s%?%U%'!<%9$rHw$($?%W%j%s%?@_Dj%D!<%k^[(B
Name:		printtool
Version:	3.53
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
Requires:	ghostscript
Requires:	tcl
Requires:	tk
Requires:	rhs-printfilters >= 1.73
Requires:	LPRng
Requires:	control-panel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The printtool is a printer configuration tool with a graphical user
interface. Printtool can manage both local and remote printers,
including Windows (SMB) and NetWare (NCP) printers.

Printtool should be installed so that you can manage local and remote
printers.

%description -l es
printtool nos ofrece una interface gr�fica para configurar impresora.
Administra tanto impresoras locales como remotas. Tambi�n pueden ser
configuradas impresoras Windows (SMB).

%description -l ja
printtool
^[$B$O%0%i%U%#%+%k%f!<%6%$%s%?!<%U%'!<%9$rMQ$$$F0u:~$N@_Dj$r$9$k^[(B
^[$B%D!<%k$G$9!#^[(Bprinttool ^[$B$G$O%m!<%+%k%W%j%s%?$H^[(B Windows
(SMB)^[$B!"^[(BNetware (NCP)
^[$B$r4^$`%j%b!<%H%W%j%s%?$r07$&$3$H$,$G$-$^$9!#^[(B

printtool
^[$B$O%m!<%+%k$H%j%b!<%H%W%j%s%?$r@)8f$G$-$k$h$&$K$9$k$?$a$K^[(B
^[$B%$%s%9%H!<%k$9$Y$-$G$9!#^[(B

%description -l pl
printtool to narz�dzie do konfiguracji drukarek z graficznym
interfejsem u�ytkownika. Mo�e obs�ugiwa� lokalne i zdalne drukarki, w
tym windowsowe (SMB) i NetWare (NCP).

%description -l pt_BR
O printtool oferece uma interface gr�fica para configurar impressora.
Administra tanto impressoras locais quanto remotas. Impressoras
Windows (SMB) tamb�m podem ser configuradas.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/System}

install printtool.desktop $RPM_BUILD_ROOT%{_applnkdir}/System

%{__make} \
        PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLBIN="install -m0755" \
	INSTALLDATA="install -m0644" \
	install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/printtool
/usr/lib/rhs/control-panel/printtool.init
/usr/lib/rhs/control-panel/printtool.xpm
%{_applnkdir}/System/printtool.desktop
