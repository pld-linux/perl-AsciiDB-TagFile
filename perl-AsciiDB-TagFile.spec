%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	AsciiDB-TagFile perl module
Summary(pl):	Modu³ perla AsciiDB-TagFile
Name:		perl-AsciiDB-TagFile
Version:	1.05
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/AsciiDB/AsciiDB-TagFile-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
AsciiDB-TagFile allows to manage a simple ASCII database.

%description -l pl
AsciiDB-TagFile pozwala na korzystanie z prostej, tekstowej bazy danych.

%prep
%setup -q -n AsciiDB-TagFile-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/AsciiDB/TagFile
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%dir %{perl_sitelib}/AsciiDB
%{perl_sitelib}/AsciiDB/*.pm

%dir %{perl_sitearch}/auto/AsciiDB
%{perl_sitearch}/auto/AsciiDB/TagFile

%{_mandir}/man3/*
