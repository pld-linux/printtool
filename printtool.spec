Summary:	A printer configuration tool with a graphical user interface
Summary(es):	Herramienta de configuración de impresoras
Summary(pl):	Program konfiguracyjny drukarki z graficznym interfejsem
Summary(pt_BR):	Ferramenta de configuração de impressoras
Name:		printtool
Version:	3.53
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	2817f2229147b99c826b0c8a5ed7a878
Requires:	LPRng
Requires:	control-panel
Requires:	ghostscript
Requires:	rhs-printfilters >= 1.73
Requires:	tcl
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The printtool is a printer configuration tool with a graphical user
interface. Printtool can manage both local and remote printers,
including Windows (SMB) and NetWare (NCP) printers.

Printtool should be installed so that you can manage local and remote
printers.

%description -l es
El printtool es una herramienta de configuración de impresoras con una
GUI. Printtool puede manejar ambas las impresoras locales y remotas,
incluyendo las de Windows (SMB) y NetWare (NCP).

Printtool debe instalarse para que pueda manejar sus impresoras
locales y remotas.

%description -l pl
printtool to narzêdzie do konfiguracji drukarek z graficznym
interfejsem u¿ytkownika. Mo¿e obs³ugiwaæ lokalne i zdalne drukarki, w
tym windowsowe (SMB) i NetWare (NCP).

%description -l pt_BR
O printtool oferece uma interface gráfica para configurar impressora.
Administra tanto impressoras locais quanto remotas. Impressoras
Windows (SMB) também podem ser configuradas.

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
