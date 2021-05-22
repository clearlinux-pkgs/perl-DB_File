#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DB_File
Version  : 1.855
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/P/PM/PMQS/DB_File-1.855.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PM/PMQS/DB_File-1.855.tar.gz
Summary  : 'Perl5 access to Berkeley DB version 1.x'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-DB_File-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : db-dev

%description
DB_File
Version 1.855
13 October 2020
program is free software; you can redistribute it and/or modify
it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-DB_File package.
Group: Development
Provides: perl-DB_File-devel = %{version}-%{release}
Requires: perl-DB_File = %{version}-%{release}

%description dev
dev components for the perl-DB_File package.


%package perl
Summary: perl components for the perl-DB_File package.
Group: Default
Requires: perl-DB_File = %{version}-%{release}

%description perl
perl components for the perl-DB_File package.


%prep
%setup -q -n DB_File-1.855
cd %{_builddir}/DB_File-1.855

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DB_File.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DB_File.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/DB_File/DB_File.so
