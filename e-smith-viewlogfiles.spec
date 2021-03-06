# $Id: e-smith-viewlogfiles.spec,v 1.12 2008/10/07 19:25:24 slords Exp $

Summary: Web manager panel to provide view access to log files
%define name e-smith-viewlogfiles
Name: %{name}
%define version 2.2.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-lib >= 1.13.1-58
Requires: perl
Requires: perl(CGI::FormMagick)
Requires: e-smith-formmagick >= 1.4.0-12
Requires: perl(Time::TAI64)
AutoReqProv: no

%changelog
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.8.0-11
- Add common <base> tags to e-smith-formmagick's general [SME: 4281]

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> 1.8.0-10
- Remove tests for removed FORM_TITLE's [SME: 4050]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.8.0-9
- Remove <base> tags now in general [SME: 3916]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.8.0-8
- Remove duplicate <base> entries [SME: 3891]

* Wed Jan 09 2008 Stephen Noble <support@dungog.net> 1.8.0-7
- show log filename on panel [SME: 2770]

* Mon Dec 24 2007 Stephen Noble <support@dungog.net> 1.8.0-6
- remove viewlogfile.orig [SME: 3647]

* Wed Oct 31 2007 Charlie Brady <charlie_brady@mitel.com> 1.8.0-5
- Exclude svlogd config and btmp files. [SME: 3486]

* Mon Oct 01 2007 Charlie Brady <charlie_brady@mitel.com> 1.8.0-4
- Allow viewing of qpsmtpd/state. [SME: 3416]

* Sat Sep 29 2007 Charlie Brady <charlie_brady@mitel.com> 1.8.0-3
- Convert squid log timestamps to localtime. [SME: 3432]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.8.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.7.2-03
- Bump release number only

* Thu Oct 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-02]
- Avoid uninitialized variable warnings in logfile when highlistPattern is
  unset. [SF: 1227604]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.7.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.7.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-11]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.7.0-10]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Thu Aug 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-09]
- Take II at chomp fix. [SF: 1264596]

* Thu Aug 25 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.7.0-08]
- Fix call to chomp, and save a temporary assign [SF: 1264596]

* Mon Aug 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-07]
- Fix typo in last change, and double spacing problem. [SF: 1264596]

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-06]
- Use Time::TAI64 module to convert multilog timestamps, rather than
  external invocation of tia64nlocal.

* Thu Jul 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-05]
- Remove false "fix" from previous change. [SF: 1227604]
- Replace deprecated "Copyright" header with "License" header.

* Thu Jul 28 2005 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-04]
- Fix "uninitialized value" warnings from viewlogfiles CGI. [SF: 1227604]
- Replace all uses of the deprecated esmith::config and db_ APIs.

* Thu Sep 16 2004 Michael Soulier <msoulier@e-smith.com>
- [1.7.0-03]
- Updated requires with new perl dependencies. [msoulier MN00040240]
- Fixed Content disposition. [msoulier MN00049326]

* Fri Aug 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.7.0-02]
- Added resolution of multilog timestamps in logfile download.
  [msoulier MN00033909]

* Fri Aug 27 2004 Michael Soulier <msoulier@e-smith.com>
- [1.7.0-01]
- rolling to dev - 1.7.0

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.6.0-03]
- Fixed escaping of HTML entities via HTML::Entities::encode_entities().
  [msoulier 10418]

* Wed Jul  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.6.0-02]
- Fixed odd FormMagick caching WSOD by removing intermediate page in log
  download. [msoulier 9223]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to stable stream number - 1.6.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-17]
- Spanish nav bar entries [gordonr 9153]

* Thu Jun 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-16]
- Added recognition of Mac clients, and made the .log extension unconditional.
  [msoulier 8634]

* Thu Jun 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-15]
- Added handling of filenames with additional subdirectories. 
  [msoulier 8634] 

* Thu Jun 19 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-14]
- Added detection of windows client via the user-agent string, so .log
  extension is only added in that case. Additionally, in that case, CR/LF
  conversion is performed on the logfile. [msoulier 8634]

* Wed Jun 18 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-13]
- Added a .log extension to all logfiles to work around the fact that Windows
  ignores http response directives. [msoulier 8634]

* Wed May 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-12]
- Added French and Spanish lexicon. [msoulier 8634]

* Fri May  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-11]
- Minor Spanish update from Alejandro [gordonr 8634]

* Fri May  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-10]
- Minor French/Spanish lexicon updates [gordonr 8634]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.5.0-09]
- Add Spanish lexicon for viewlogfiles [lijied 3793]

* Tue May  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-08]
- Added the operation parameter to the refresh option to maintain the default
  in the configuration database. [msoulier 8634]

* Tue May  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-07]
- Changed the operation selection widget to being generated by the backend
  code, so we can control the default. [msoulier 8634]
- Now caching the default choice in the configuration database.
  [msoulier 8634]

* Tue May  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-06]
- Updated dependencies for the download logfile feature. [msoulier 8634]
- Added download logfile feature. [msoulier 8634]

* Tue May  6 2003 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-05]
- Added a "Refresh" log button. [msoulier 6935]
- Added lexicon changes for refresh feature. [msoulier 6935]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [1.5.0-04]
- Removed Mitel Networks branding [lijied 8016]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-03]
- Make use of esmith::Tai64n to display multilog filenames and contents
  in local time [gordonr 6930]
- Use a hash instead of an array for the filename list and let
  FM do the sorting for us, which allows the displayed name and the filename
  to differ [gordonr 6930]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-02]
- Split out en-us lexicon [gordonr 4030]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-01]
- dev stream to 1.5.0

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.4.0-05]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Tue Mar 25 2003 Mark Knox <markk@e-smith.com>
- [1.4.0-04]
- Use localised date in report header [markk 3599]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.4.0-03]
- Modified viewlogfiles panel order [lijied 7356]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.4.0-02]
- Added French lexicon for viewlogfiles [lijied 5003]

* Fri Jan 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.4.0-01]
- rolling to delivery stream to 1.4.0

* Thu Nov  7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Fix warning about @logfiles variable [charlieb 4613]
- Allow log files containing spaces in filename to be viewed [charlieb 5588]
- Filter all logfiles using tai64nlocal, so that dates are in
  human readable form. [charlieb 5334]

* Thu Nov  7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Roll development stream to 1.3.0

* Sat Oct 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- Roll to maintained version number to 1.2.0

* Wed Jul 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.1.2-01]
- Removed stray e-smith-viewlogfiles-0.0.1 directory [gordonr 4466]

* Wed Jul 24 2002 Mark Knox <markk@e-smith.com>
- [1.1.1-01]
- Escape HTML chars even when not highlighting [markk 4466]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-01]
- Changing version to maintained stream number to 1.1.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.0.5-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.0.4-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Tue Apr 16 2002 Adrian Chung <adrianc@e-smith.com>
- [1.0.3-01]
- Conversion of viewlogfiles panel to FormMagick. [mac #3175]

* Tue Apr 16 2002 Adrian Chung <adrianc@e-smith.com>
- [1.0.2-01]
- Initial CVS version.

* Tue Apr 16 2002 Adrian Chung <mac@e-smith.com>
- [1.0.1-01]
- rollRPM: Rolled version number to 1.0.1-01. Includes patches up to 1.0.0-03.

* Wed Nov 07 2001 Tony Clayton <tonyc@e-smith.com>
- [1.0.0-03]
- rebranding to Mitel Networks

* Tue Aug 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-02]
- Distinguish between empty file and no matching lines in output.

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-01]
- Rolled version number to 1.0.0-01. Includes patches upto 0.0.1-05.

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-05]
- Display name of logfile and patterns applied in output

* Mon Aug 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-04]
- Disabled custom sort order - I find it non-intuitive
- Display "No lines displayed" if this is true
- Expanded text, describing filters in more depth
- Display filename of viewed log file

* Sat Aug 18 2001 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-03]
- Introduce custom sort order, with messages at top and rotated logs at end.
- Add feature to display gzipped files.

* Fri Aug 17 2001 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-02]
- Replace fixed log file list with one generated at run time
- Filter out known non-log files from the generated list
- Clean more of the environment (although I don't think it matters)
- Add brief text to explain the entry boxes

* Fri Aug 17 2001 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-01]
- initial release

%description
Insert an e-smith-manager web panel to allow log files to be viewed.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
