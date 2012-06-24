#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	PodToHTML Perl module - converts POD to HTML or PostScript
Summary(pl.UTF-8):	Moduł Perla PodToHTML - konwersja plików POD do formatu HTML lub PostScript
Name:		perl-PodToHTML
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/PodToHTML-%{version}.tar.gz
# Source0-md5:	fec09c1e062ed4c670b6b982649e2f24
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-URI
Requires:	perl-Pod-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(Pod::Parser)

%description
PodToHTML Perl module converts POD to HTML or PostScript.

%description -l pl.UTF-8
Moduł Perla PodToHTML konwertuje pliki POD do formatu HTML lub
PostScript.

%prep
%setup -q -n PodToHTML-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/podtohtml
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man[13]/*
