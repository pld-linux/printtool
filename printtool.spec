Summary:	A printer configuration tool with a graphical user interface
Summary(es.UTF-8):   Herramienta de configuración de impresoras
Summary(ja.UTF-8):   グラフィカルユーザインタフェースを備えたプリンタ設定ツール
Summary(pl.UTF-8):   Program konfiguracyjny drukarki z graficznym interfejsem
Summary(pt_BR.UTF-8):   Ferramenta de configuração de impressoras
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

%description -l es.UTF-8
El printtool es una herramienta de configuración de impresoras con una
GUI. Printtool puede manejar ambas las impresoras locales y remotas,
incluyendo las de Windows (SMB) y NetWare (NCP).

Printtool debe instalarse para que pueda manejar sus impresoras
locales y remotas.

%description -l ja.UTF-8
printtool はグラフィカルユーザインターフェースを用いて印刷の設定をする
ツールです。printtool ではローカルプリンタと Windows (SMB) 、Netware
(NCP) を含むリモートプリンタを扱うことができます。

printtool はローカルとリモートプリンタを制御できるようにするために
インストールすべきです。

%description -l pl.UTF-8
printtool to narzędzie do konfiguracji drukarek z graficznym
interfejsem użytkownika. Może obsługiwać lokalne i zdalne drukarki, w
tym windowsowe (SMB) i NetWare (NCP).

%description -l pt_BR.UTF-8
O printtool oferece uma interface gráfica para configurar impressora.
Administra tanto impressoras locais quanto remotas. Impressoras
Windows (SMB) também podem ser configuradas.

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
