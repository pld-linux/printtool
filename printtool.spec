Summary:	A printer configuration tool with a graphical user interface.
Summary(pl):	Program konfiguracyjny drukarki z graficznym interfejsem
Summary(pt_BR):	Ferramenta de configuração de impressoras
Summary(es):	Herramienta de configuración de impresoras
Name:		printtool
Version:	3.48
Release: 	1
License:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Group(pt_BR):	Aplicações/Editoração
Group(es):	Aplicaciones/Editoración
Source:		%{name}-%{version}.tar.gz
Requires:	ghostscript
Requires:	tcl
Requires:	tk
Requires:	rhs-printfilters >= 1.73
Requires:	LPRng
Requires:	control-panel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The printtool is a printer configuration tool with a graphical user
interface.  Printtool can manage both local and remote printers,
including Windows (SMB) and NetWare (NCP) printers.

Printtool should be installed so that you can manage local and remote
printers.

%description -l pt_BR
O printtool oferece uma interface gráfica para configurar
impressora. Administra tanto impressoras locais quanto
remotas. Impressoras Windows (SMB) também podem ser configuradas.

%description -l es
printtool nos ofrece una interface gráfica para configurar
impresora. Administra tanto impresoras locales como remotas. También
pueden ser configuradas impresoras Windows (SMB).

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/System

install printtool.desktop $RPM_BUILD_ROOT%{_datadir}/applnk/System

%{__make} \
        PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLBIN="install -m0755" \
	INSTALLDATA="install -m0644" \
	install

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/printtool
%{_libdir}/rhs/control-panel/printtool.init
%{_libdir}/rhs/control-panel/printtool.xpm
%{_datadir}/applnk/System/printtool.desktop
