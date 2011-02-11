#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Perl
%define		pnam	OSType
%include	/usr/lib/rpm/macros.perl
Summary:	Perl::OSType - Map Perl operating system names to generic types
Name:		perl-Perl-OSType
Version:	1.002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	73be06de32cd51cf5e6de37b5725e0ac
URL:		http://search.cpan.org/dist/Perl-OSType/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules that provide OS-specific behaviors often need to know if the
current operating system matches a more generic type of operating
systems. For example, 'linux' is a type of 'Unix' operating system and
so is 'freebsd'.

This module provides a mapping between an operating system name as
given by $^O and a more generic type. The initial version is based on
the OS type mappings provided in Module::Build and ExtUtils::CBuilder.
(Thus, Microsoft operating systems are given the type 'Windows' rather
than 'Win32'.)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Perl
%{perl_vendorlib}/Perl/*.pm
%{_mandir}/man3/Perl::OSType.3pm*
