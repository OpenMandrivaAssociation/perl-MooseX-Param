%define upstream_name    MooseX-Param
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Simple role to provide a standard param method
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a very simple Moose role which provides a the CGI manpage like
'param' method.

I found that I had written this code over and over and over and over again,
and each time it was the same. So I thought, why not put it in a role?

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


