%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	PodToHTML perl module
Summary(pl):	Modu� perla PodToHTML
Name:		perl-PodToHTML
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module//PodToHTML-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-PodParser
Requires:	perl-HTML-Tree
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PodToHTML - converts POD to HTML or PostScript.

%description -l pl
PodToHTML - konwertuje pliki POD do formatu HTML lub PostScript.

%prep
%setup -q -n PodToHTML-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PodToHTML
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/podtohtml

%{perl_sitelib}/Pod/*.pm
%{perl_sitearch}/auto/PodToHTML

%{_mandir}/man[13]/*