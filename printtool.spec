Summary:	A printer configuration tool with a graphical user interface.
Summary(pl):	Program konfiguracyjny drukarki z graficznym interfejsem
Name:		printtool
Version:	3.48
Release: 	1
Copyright:	GPL
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
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
