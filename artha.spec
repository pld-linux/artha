Summary:	An off-line English thesaurus based on WordNet
Summary(pl.UTF-8):	Angielski słownik synonimów oparty o WordNet
Name:		artha
Version:	0.9.1
Release:	1
License:	LGPL
Group:		Applications/Dictionaries
Source0:	http://dl.sourceforge.net/artha/%{name}-%{version}.tar.bz2
# Source0-md5:	6614a81980e7bccf55449ad6ab9ee080
URL:		http://artha.sourceforge.net
BuildRequires:	WordNet-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.14
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	pkgconfig
Requires:	WordNet
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
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/*
