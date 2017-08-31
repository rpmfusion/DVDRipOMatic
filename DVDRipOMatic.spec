Name:           DVDRipOMatic
Version:        0.95
Release:        14%{?dist}
Summary:        Simple DVD to XviD ripping application
Group:          Applications/Multimedia
License:        GPL
URL:            http://dvdripomatic.sourceforge.net
Source0:        http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         DVDRipOMatic-0.95-newmplayerfix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  desktop-file-utils
Requires:       kdebase3, kdewebdev, bc, mencoder, mplayer, transcode

%description
DVD Rip-O-Matic is a simple DVD-to-XviD ripping application developed by Dik
Takken. The wizard was designed to be very easy to use; it automatically
detects the optimal settings for you. It should also produce very high quality
AVI files, even if you have no idea what the settings mean and just use it in
the next-next-next-finish way.


%prep
%setup -q
%patch0 -p1


%build
#nothing to build

#Create simple scripts for easy launching from the command line.
cat << EOF > dvdripomatic
#!/bin/sh
# Simple script for friendly command line lauching of dvdripomatic
exec %{_bindir}/kmdr-executor %{_datadir}/apps/%{name}/%{name}.kmdr
EOF


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/apps/%{name}
mkdir -p %{buildroot}%{_bindir}
install -pm0755 %{name}.kmdr %{buildroot}%{_datadir}/apps/%{name}
install -pm0644 banner.png %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 DVDScan %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 dvdripomatic %{buildroot}%{_bindir}

desktop-file-install --vendor "" \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{SOURCE1}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changelog README
%{_datadir}/apps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/dvdripomatic


%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.95-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.95-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 0.95-12
- Fix permissions of DVDRipOMatic.kmdr

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon May 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.95-10
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.95-9
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 23 2009 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 0.95-7
- Update desktop file according to F-12 FedoraStudio feature

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.95-6
- rebuild for new F11 features

* Tue Sep 09 2008 Xavier Lamien <lxtnow[at]gmail.com> - 0.95-5
- Update files and rebuild for rpmfusion inclusion.

* Mon Mar 12 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-4%{?dist}
- Added patch to support newer versions of mplayer

* Mon Jan 15 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-3%{?dist}
- Dropped version= from .desktop file.
- Included README_dvdripomatic.dribble

* Sun Jan 14 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-2%{?dist}
- Dropped --add-category=X-Fedora from .desktop file

* Sun Dec 03 2006 Ian Chapman <packages@amiga-hardware.com> 0.95-1%{?dist}
- Initial release
