#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	PodToHTML Perl module - converts POD to HTML or PostScript
Summary(pl):	Modu� Perla PodToHTML - konwersja plik�w POD do formatu HTML lub PostScript
Name:		perl-PodToHTML
Version:	0.04
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/PodToHTML-%{version}.tar.gz
# Source0-md5:	b08e3351b171b719f40031a188fe5c26
Patch0:		%{name}-fix.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Stream
BuildRequires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodToHTML Perl module converts POD to HTML or PostScript.

%description -l pl
Modu� Perla PodToHTML konwertuje pliki POD do formatu HTML lub
PostScript.

%prep
%setup -q -n PodToHTML-%{version}
%patch0 -p1
%{__perl} -pi -e 's/^(use\s+Pod::Parser\s+1.06)1/$1_1/' Pod/HTML_Elements.pm

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
