Summary:	An off-line English thesaurus based on WordNet
Summary(pl.UTF-8):	Angielski słownik synonimów oparty o WordNet
Name:		artha
Version:	1.0.5
Release:	1
License:	GPL v2+
Group:		Applications/Dictionaries
Source0:	https://downloads.sourceforge.net/artha/%{name}-%{version}.tar.bz2
# Source0-md5:	a916a7a943ac676a60f03cc839b04f37
URL:		https://artha.sourceforge.net/
BuildRequires:	WordNet-devel >= 3.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gtk+2-devel >= 2:2.24
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	WordNet
Requires:	dbus-libs >= 0.60
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.22
Requires:	gtk+2 >= 2:2.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artha is a free cross-platform English thesaurus that works completely
off-line and is based on WordNet. Artha focuses on high usability,
without trading off simplicity and ease of use.

%description -l pl.UTF-8
Artha to angielski słownik wyrazów bliskoznacznych oparty o WordNet i
działajacy całkowicie off-line. Artha została stworzona z myślą o
dużej funkcjonalnosci, ale bez rezygnowania z prostoty i łatwości
używania.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/artha
%{_datadir}/%{name}
%{_desktopdir}/artha.desktop
%{_pixmapsdir}/artha.png
%{_mandir}/man1/artha.1*
