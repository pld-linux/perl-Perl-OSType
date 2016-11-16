#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Perl
%define		pnam	OSType
%include	/usr/lib/rpm/macros.perl
Summary:	Perl::OSType - map Perl operating system names to generic types
Summary(pl.UTF-8):	Perl::OSType - odwzorowanie nazw systemów operacyjnych Perla na ogólne
Name:		perl-Perl-OSType
Version:	1.010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa723870bc664bc5476a92073dce194f
URL:		http://search.cpan.org/dist/Perl-OSType/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
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

%description -l pl.UTF-8
Moduły uzależniające zachowanie w zależności od systemu operacyjnego
zwykle potrzebują wiedzieć, czy bieżący system pasuje do bardziej
ogólnego typu. Na przykłąd "linux" jest typem systemu operacyjnego
"Unix", podobnie "freebsd".

Ten moduł udostępnia odwzorowanie miedzy nazwą systemu operacyjnego
w postaci podawanej przez $^O a bardziej ogólnym typem. Początkowa
wersja jest operta na odwzorowaniach typów systemu zawartych w
Module::Build i ExtUtils::CBuilder (czyli systemy operacyjne
Microsoftu mają typ "Windows", a nie "Win32").

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
%{perl_vendorlib}/Perl/OSType.pm
%{_mandir}/man3/Perl::OSType.3pm*
