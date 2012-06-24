Summary:	A printer configuration tool with a graphical user interface
Summary(es):	Herramienta de configuraci�n de impresoras
Summary(ja):	����ե�����桼�����󥿥ե��������������ץ������ġ���
Summary(pl):	Program konfiguracyjny drukarki z graficznym interfejsem
Summary(pt_BR):	Ferramenta de configura��o de impressoras
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
El printtool es una herramienta de configuraci�n de impresoras con una
GUI. Printtool puede manejar ambas las impresoras locales y remotas,
incluyendo las de Windows (SMB) y NetWare (NCP).

Printtool debe instalarse para que pueda manejar sus impresoras
locales y remotas.

%description -l ja
printtool �ϥ���ե�����桼�����󥿡��ե��������Ѥ��ư���������򤹤�
�ġ���Ǥ���printtool �Ǥϥ�����ץ�󥿤� Windows (SMB) ��Netware
(NCP) ��ޤ��⡼�ȥץ�󥿤򰷤����Ȥ��Ǥ��ޤ���

printtool �ϥ�����ȥ�⡼�ȥץ�󥿤�����Ǥ���褦�ˤ��뤿���
���󥹥ȡ��뤹�٤��Ǥ���

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install printtool.desktop $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/printtool.desktop
