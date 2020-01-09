Name:		cloud-utils-growpart
Version:	0.29
Release:	5%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	https://launchpad.net/cloud-utils/trunk/%{version}/+download/cloud-utils-%{version}.tar.gz
Patch0001:	0001-growpart-fix-bug-occurring-if-start-sector-and-size-.patch
Patch2:		0002-growpart-fix-bug-when-resizing-a-middle-partition-wi.patch
URL:		https://launchpad.net/cloud-utils
Source1:	LICENSE

BuildArch:	noarch

Summary:	Script for growing a partition

Requires:	gawk
Requires:	util-linux
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk

%description
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%prep
%autosetup -n cloud-utils-%{version} -p1

%build

%install
cp %{SOURCE1} LICENSE

# Create the target directories
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

# Install the growpart binary and man page
cp bin/growpart $RPM_BUILD_ROOT/%{_bindir}/
cp man/growpart.* $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%doc ChangeLog LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*

%changelog
* Mon Jun 03 2019 Miroslav Rezanina <mrezanin@redhat.com> - 0.29-5
- Fix bug when resizing a middle partition with sgdisk
- Resolves: rhbz#1695091

* Mon Dec 10 2018 Lars Kellogg-Stedman <lars@redhat.com> - 0.29-3
- Fix growpart error when partition size matches partition offset
- Resolves: rhbz#1593451

* Wed Apr 19 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.29-2
- Import to RHEL 7
Resolves: rhbz#1308711

* Mon Dec 05 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.29-1
- update to 0.29
- resolves rhbz#1321373

* Tue May 10 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.28-1
- fix locale related problems in growpart script (rhbz#1327620)
  w/ rebase to 0.28

* Tue May 10 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-14

* Tue Mar 18 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-13
- suppress partx usage error

* Tue Jan 14 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-11
- import into RHEL

