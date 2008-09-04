Name:           DVDRipOMatic
Version:        0.95
Release:        4%{?dist}
Summary:        Simple DVD to XviD ripping application
Group:          Applications/Multimedia
License:        GPL
URL:            http://dvdripomatic.sourceforge.net
Source0:        http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:         DVDRipOMatic-0.95-newmplayerfix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       bc
Requires:       kdewebdev
Requires:       kdebase
Requires:       mencoder
Requires:       mplayer
Requires:       transcode

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
# Build desktop icons
cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
GenericName=: DVD Ripping Tool
Comment=%{summary}
Exec=dvdripomatic
Icon=dvd_unmount
Terminal=false
Type=Application
Categories=Qt;KDE;AudioVideo;
EOF

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
install -pm0644 %{name}.kmdr %{buildroot}%{_datadir}/apps/%{name}
install -pm0644 banner.png %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 DVDScan %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 dvdripomatic %{buildroot}%{_bindir}

desktop-file-install --vendor dribble \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/apps/%{name}
%{_datadir}/applications/dribble-%{name}.desktop
%{_bindir}/dvdripomatic
%doc Changelog README


%changelog
* Mon Mar 12 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-4%{?dist}
- Added patch to support newer versions of mplayer

* Mon Jan 15 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-3%{?dist}
- Dropped version= from .desktop file.
- Included README_dvdripomatic.dribble

* Sun Jan 14 2007 Ian Chapman <packages@amiga-hardware.com> 0.95-2%{?dist}
- Dropped --add-category=X-Fedora from .desktop file

* Sun Dec 03 2006 Ian Chapman <packages@amiga-hardware.com> 0.95-1%{?dist}
- Initial release