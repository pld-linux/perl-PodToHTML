%include	/usr/lib/rpm/macros.perl
Summary:	PodToHTML perl module
Summary(pl):	Modu� perla PodToHTML
Name:		perl-PodToHTML
Version:	0.04
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//PodToHTML-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-PodParser
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-URI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodToHTML - converts POD to HTML or PostScript.

%description -l pl
PodToHTML - konwertuje pliki POD do formatu HTML lub PostScript.

%prep
%setup -q -n PodToHTML-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/podtohtml

%{perl_sitelib}/Pod/*.pm
%{perl_sitearch}/auto/PodToHTML

%{_mandir}/man[13]/*
