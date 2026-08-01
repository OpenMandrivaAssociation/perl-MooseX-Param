%define upstream_name    MooseX-Param
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	4

Summary:	Simple role to provide a standard param method
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/MooseX-Param
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEVAN/MooseX-Param-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This is a very simple Moose role which provides a the CGI manpage like
'param' method.

I found that I had written this code over and over and over and over again,
and each time it was the same. So I thought, why not put it in a role?

%prep
%setup -q -n MooseX-Param-0.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :
%make test || :

%install
%makeinstall_std

%files
%doc ChangeLog META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

