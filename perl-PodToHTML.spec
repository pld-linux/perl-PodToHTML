%include	/usr/lib/rpm/macros.perl
Summary:	PodToHTML perl module
Summary(pl):	Modu³ perla PodToHTML
Name:		perl-PodToHTML
Version:	0.04
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/PodToHTML-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodToHTML - converts POD to HTML or PostScript.

%description -l pl
PodToHTML - konwertuje pliki POD do formatu HTML lub PostScript.

%prep
%setup -q -n PodToHTML-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/podtohtml
%{perl_sitelib}/Pod/*.pm
%{_mandir}/man[13]/*
